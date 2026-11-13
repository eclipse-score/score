..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

.. _collecting_logs:

Collecting logs
===============

S-CORE applications log via **mw::log** from the `logging <https://github.com/eclipse-score/logging>`_ module
(``score_logging``). This chapter shows how the platform info service and its consumer log, how the logging is
configured and how the logs are collected: on the console and as **DLT** (Diagnostic Log and Trace), the log format
which is used in the automotive domain.

Logging in the code
-------------------
The service creates a logger for its context and writes log messages with a log level:

.. code-block:: cpp
    :linenos:

    #include "score/mw/log/logger.h"

    auto& logger = score::mw::log::CreateLogger("PINF", "platform info");
    logger.LogInfo() << "platform_info_service: offering " + std::string{kInstanceSpecifier} + " for S-CORE " +
                            ToString(platform_info);
    logger.LogError() << "platform_info_service: cannot offer service: " << std::string{offered.error().Message()};

``PINF`` is the *context id* of the messages. Together with the *application id* from the configuration below,
it identifies the source of each message. The Bazel target needs the dependency ``@score_logging//score/mw/log``.

Logging configuration
---------------------
Which messages are written where is configured per process in a JSON file. The service uses
`deploy/platform_info/etc/logging.json <https://github.com/eclipse-score/reference_integration/blob/main/deploy/platform_info/etc/logging.json>`_:

.. code-block:: json
    :linenos:

    {
        "appId": "PINS",
        "appDesc": "Platform info service",
        "logLevel": "kInfo",
        "logLevelThresholdConsole": "kInfo",
        "logMode": "kConsole|kRemote"
    }

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Entry
     - Meaning
   * - ``appId``
     - Application id of the process in the logs (up to four characters), ``PINS`` for the service and ``PINC`` for the consumer
   * - ``logLevel``
     - Lowest log level that is logged, e.g. ``kInfo``; ``kDebug`` and ``kVerbose`` add more details
   * - ``logLevelThresholdConsole``
     - Lowest log level that is written to the console
   * - ``logMode``
     - Where the logs go: ``kConsole`` to the console, ``kRemote`` as DLT via the datarouter, ``kFile`` to a file

mw::log uses the file given in the environment variable ``MW_LOG_CONFIG_FILE``. If it is not set, mw::log takes the first
existing file of ``../etc/logging.json`` relative to the directory of the executable, ``etc/logging.json`` and
``logging.json`` in the working directory. In addition, an optional ECU-wide file ``/etc/ecu_logging_config.json``
is read. The service is started in ``/usr/bin/platform_info`` on the target and finds ``etc/logging.json`` there;
the consumer gets its configuration via ``MW_LOG_CONFIG_FILE``. Without it, the consumer would pick up the
``etc/logging.json`` of the service when started in the same directory, and log with the application id ``PINS``.

Console logs
------------
With ``kConsole``, the messages are printed to the console of the process, e.g. when the service is started
as described in the :doc:`building source code <building_source_code>` chapter:

.. code-block:: text

    2026/11/13 13:22:11.6131644 818992094 000 ECU1 PINS PINF log info verbose 1 platform_info_service: offering score/platform/info for S-CORE known_good 2026-08-28T09:19:12Z

Each line contains the time stamp, the ECU id (``ECU1``), the application id (``PINS``), the context id (``PINF``)
and the log level (``info``), followed by the message. Messages of the S-CORE modules used by the application appear
with their own context ids, e.g. ``lola`` for mw::com.

DLT logs and the datarouter
---------------------------
With ``kRemote``, the processes hand their messages to the **datarouter**, the logging daemon of ``score_logging``.
The datarouter collects the messages of all processes on the target and sends them as DLT messages via UDP multicast
to ``239.255.42.99``, port ``3490``. The channels are configured in its
`log-channels.json <https://github.com/eclipse-score/reference_integration/blob/main/deploy/logging/etc/log-channels.json>`_.
On the reference images, the datarouter is deployed under ``/usr/bin/datarouter``, next to the platform info service.
If no datarouter runs, the DLT output is dropped; the console output remains.

To collect the DLT logs of the platform info service on your Linux machine, run the following commands in the
reference integration:

1. Build the datarouter and ``dlt-receive``. ``dlt-receive`` from the
   `COVESA dlt-daemon <https://github.com/COVESA/dlt-daemon>`_ project is provided by the Integration Testing Framework,
   with an extension for UDP multicast:

   .. code-block:: bash

      bazel build --config=linux-x86_64 @score_logging//score/datarouter @score_itf//third_party/dlt:dlt-receive

2. Start ``dlt-receive`` and store the received messages in a file. ``--net-if`` is the IP address of the network
   interface of your machine, e.g. as shown by ``hostname -I``:

   .. code-block:: bash

      bazel-bin/external/score_itf++_repo_rules+dlt_daemon/dlt-receive -o /tmp/platform_info.dlt \
        --udp --net-if <your IP address> --port 3490 --mcast-ip 239.255.42.99 &

3. Start the datarouter in the directory that contains its configuration:

   .. code-block:: bash

      (cd deploy/logging && ../../bazel-bin/external/score_logging+/score/datarouter/datarouter --no_adaptive_runtime &)

4. Start the service and the consumer as described in the :doc:`building source code <building_source_code>` chapter.
   Then stop the datarouter and ``dlt-receive``, e.g. with ``pkill datarouter`` and ``pkill dlt-receive``.

5. Open ``/tmp/platform_info.dlt`` in a DLT viewer, e.g. `dlt-viewer <https://github.com/COVESA/dlt-viewer>`_,
   and filter for the application ids ``PINS`` and ``PINC``. Besides the messages of the datarouter itself
   (application id ``DR``), the recording contains, for example:

   .. code-block:: text

      SCPP PINS PINF platform_info_service: offering score/platform/info for S-CORE known_good 2026-08-28T09:19:12Z ...
      SCPP PINC PINF platform_info_consumer: found the platform info service
      SCPP PINC PINF platform_info_consumer: S-CORE version check passed (8 modules match)
      SCPP PINS PINF platform_info_service: stopped

   ``SCPP`` is the ECU id which the datarouter sets for its DLT channels in ``log-channels.json``.

Other tools, e.g. Wireshark or Chipmunk, and the setup of the network interfaces are described in the
`DLT capture guide <https://github.com/eclipse-score/logging/blob/main/score/datarouter/doc/guideline/dlt_capture_demo.md>`_
of the logging module.

Logs collected by the platform integration test
-----------------------------------------------
In the reference integration, the logs are also collected automatically. The platform integration test
`test_platform_run.py <https://github.com/eclipse-score/reference_integration/blob/main/platform_integration_tests/platform_run/test_platform_run.py>`_
runs the showcase *S-CORE Platform Run* on the Linux image, in which the launch manager starts the datarouter,
the platform info service and then the consumer. While the showcase runs, the test records all DLT messages on the host
and checks, for example, that the consumer reported the successful version check:

.. code-block:: python

    ("PINC", "PINF", r"platform_info_consumer: S-CORE version check passed"),

The recording is stored as ``platform_run.dlt`` in the undeclared test outputs
(``bazel-testlogs/platform_integration_tests/platform_run/platform_run/test.outputs/``, packed into
``outputs.zip`` unless Bazel runs with ``--nozip_undeclared_test_outputs``). In CI, it is uploaded as
artifact ``platform-run-dlt-<commit>`` of the workflow
`test_and_docs.yml <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/test_and_docs.yml>`_,
so you can download and open the logs of every pull request in a DLT viewer.

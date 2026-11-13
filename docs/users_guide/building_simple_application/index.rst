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

.. _contribute_own_module:

Contribute own module
=====================

This guide walks you through contributing a new platform module to Eclipse S-CORE end-to-end.
As a running example it uses the **platform info service** and its client, the **platform info consumer**,
from the `reference integration <https://github.com/eclipse-score/reference_integration>`_.
The example shows how to compose existing S-CORE platform modules into new functionality:

- The `platform info service <https://github.com/eclipse-score/reference_integration/tree/main/deploy/platform_info>`_
  offers the mw::com service ``score/platform/info``. Its field ``platform_info`` reports the S-CORE version the
  platform was built from, i.e. the version or commit of every ``target_sw`` module in ``known_good.json``,
  sealed with a CRC32 checksum from ``baselibs``.
- The `platform info consumer <https://github.com/eclipse-score/reference_integration/blob/main/showcases/standalone/platform_info_consumer.cpp>`_
  finds the service via mw::com service discovery, checks the CRC32 and compares the reported version with the
  version it was built for. It runs as the showcase *Platform Version Check* and is verified by a platform integration test.
- In the showcase *S-CORE Platform Run*, the launch manager of ``score_lifecycle`` starts the service as a platform
  daemon and the consumer as one of the test applications. All of them log via mw::log, and the logs are collected
  as DLT and analyzed by a platform integration test.

Service and consumer use three S-CORE modules: ``score_communication`` (mw::com), ``score_baselibs``
(CRC32, argument handling) and ``score_logging`` (mw::log). This makes the example small enough to follow, but complete:
it covers the build, the documentation, the CI/CD workflows, the deployment onto the reference images,
automated tests and the collection of logs.

.. note::

   The example lives inside the reference integration (``deploy/platform_info``, ``showcases/standalone`` and
   ``showcases/platform_run``), whereas your own module lives in its own repository. The steps are the same;
   where they differ, this guide shows both. The example replaces the former ``scrample`` demo application.

By the end of this section you will have:

- Created a properly structured S-CORE module from scratch.
- Generated documentation from source and integrated it into the platform docs.
- Built the module with Bazel and verified it compiles cleanly.
- Wired up CI/CD workflows so every change is automatically validated.
- Plugged the module into the reference integration so it becomes part of the platform.
- Collected and analyzed the logs of your application, on the console and as DLT.

.. toctree::
   :maxdepth: 1

   first_score_module.rst
   doc_generation.rst
   building_source_code.rst
   cicd_workflows.rst
   reference_integration.rst
   collecting_logs.rst

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

.. _learn_from_examples:

Learn from examples
===================

Your module will use the interfaces of other S-CORE modules. The best way to learn how they are used is to look at
their example applications. Most modules provide them in their repository:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Module
     - Examples
   * - baselibs
     - `examples <https://github.com/eclipse-score/baselibs/tree/main/examples>`_, e.g. the logging frontends
       ``log_builtin``, ``log_custom`` and ``log_cpp_init``, ``result`` and ``flatbuffers``
   * - communication
     - `mw::com tutorial <https://github.com/eclipse-score/communication/tree/main/score/mw/com/doc/tutorial>`_
       with producer and consumer applications
   * - config_management
     - `examples <https://github.com/eclipse-score/config_management/tree/main/examples>`_
   * - kyron
     - `examples <https://github.com/eclipse-score/kyron/tree/main/examples>`_, e.g. ``main_macro``,
       ``safety_task`` and ``select``
   * - lifecycle
     - `examples <https://github.com/eclipse-score/lifecycle/tree/main/examples>`_: supervised applications in C, C++
       and Rust and a control application for the launch manager
   * - logging
     - `examples <https://github.com/eclipse-score/logging/tree/main/examples>`_ and the
       `custom recorder example <https://github.com/eclipse-score/logging/tree/main/score/mw/log/custom_recorder_example>`_
   * - persistency
     - `examples <https://github.com/eclipse-score/persistency/tree/main/examples>`_ and the
       `Rust KVS examples <https://github.com/eclipse-score/persistency/tree/main/score/kvs/rust_kvs/examples>`_
   * - time
     - `examples/time <https://github.com/eclipse-score/time/tree/main/examples/time>`_: ``steady_time``,
       ``high_res_steady_time``, ``system_time`` and ``vehicle_time``

Examples in the reference integration
-------------------------------------
The `reference integration <https://github.com/eclipse-score/reference_integration>`_ shows how these
examples run on the integrated platform. Its
`showcases <https://github.com/eclipse-score/reference_integration/tree/main/showcases>`_ build the example
applications directly from the module repositories, e.g. ``@score_kyron//examples:safety_task`` or
``@score_time//examples/time/steady_time``, and combine modules, e.g. lifecycle with communication.
The `platform integration tests <https://github.com/eclipse-score/reference_integration/tree/main/platform_integration_tests>`_
(PIT) start these showcases on the reference images and check their results.

A larger end-to-end example is the
`Drive Replay Demo <https://github.com/eclipse-score/reference_integration/tree/main/showcases/drive_replay>`_:
a scripted highway drive is replayed into a forward collision warning, all processes are started and supervised by
the launch manager (lifecycle), and communication, persistency and logging work together; if the warning hangs or
crashes, the system falls back to a degraded mode and recovers. The README contains a video of a real run.

Integrating your module
-----------------------
Once your module is released, it can be integrated into the S-CORE platform. Follow the
`integration process <https://eclipse-score.github.io/reference_integration/main/integration_process/integration_process.html>`_
of the reference integration. It describes step by step how a module is registered in ``known_good.json``, built for
all target platforms, deployed onto the images as showcase, tested and included in the reports. If you integrate
S-CORE modules into your own distribution, use the reference integration and this guide as a blueprint.
How module versions get into an S-CORE release is described in the :ref:`integration process <integration_process>`
of this user guide.

..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
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

S-Core v0.5-alpha release notes
===============================

.. document:: S-Core v0.5-alpha release note
   :id: doc__score_v05_alpha_release_note
   :status: draft
   :safety: ASIL_B
   :realizes: wp__platform_sw_release_note

| **Platform Name**: S-CORE
| **Release Tag**: v0.5.0-alpha
| **Origin Release Tag**: none - first published release
| **Release Date**: 2025-11-17

Overview
^^^^^^^^^

This document provides an overview of the changes, improvements, and bug fixes included in the software platform release version v0.5.0-alpha.
This is the very first release of the **Eclipse S-Core platform**. The software architectue and implemented modules are presented at the image below.

.. image:: ../_assets/architecture.drawio.svg
   :width: 1000
   :alt: Architecture overview
   :align: center

|

Timeline
---------
The current timeline for Eclipse S-Core releases is shown below.

.. image:: ../_assets/score_release_plan.drawio.svg
   :width: 800
   :alt: Architecture overview
   :align: center

|

For more detailed planning overview please check our `GitHub project <https://github.com/orgs/eclipse-score/projects/17/views/26>`_.

S-Core book
------------
First version of **Eclipse S-CORE book**, that can be used as "how-to" for all who wants to start with S-Core project, can be found here: TODO Link.
This book provides explanation of general concepts of **Eclipse S-Core project** and contains a "step-by-step" guide for building a first application
based on Eclipse S-Core platform modules.

Improvements
^^^^^^^^^^^^^

- please consider release notes of every module

Bug Fixes
^^^^^^^^^^^^

- please consider release notes of every module

Integrated Software Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Communication**: zero-copy, shared-memory based inter-process communication for minimal latency intra-ECU messaging

  - **Link to release**: `communication v0.1.1 <https://github.com/eclipse-score/communication/releases/tag/v0.1.1>`_
  - **Release notes**:

    - Find the full release note at: :need:`doc__communication_release_note`

- **Baselibs**: provides a selection of basic C++ utility libraries for common use in the S-CORE project

  - **Link to release**: `baselibs v0.1.3 <https://github.com/eclipse-score/baselibs/releases/tag/v0.1.3>`_
  - **Release notes**:

    - Check the full `baselibs release notes <https://github.com/eclipse-score/baselibs/releases/tag/v0.1.3>`_ for more information

- **Persistency**: ensures the long-term storage and retrieval of data, provides a reliable mechanism for preserving information,
  allowing the application to maintain its state and data integrity over time

  - **Link to release**: `persistency v0.2.0 <https://github.com/eclipse-score/persistency/releases/tag/v0.2.0>`_
  - **Release notes**:

    - **Please note**: `definition of feature requirements and architecture <https://eclipse-score.github.io/score/main/features/persistency/index.html>`_  and
      `component requirements and architecture <https://eclipse-score.github.io/score/main/modules/persistency/index.html>`_ is partially out of date.
      This will be fixed with next release.
    - Check the full `persistency release notes <https://github.com/eclipse-score/persistency/releases/tag/v0.2.0>`_ for more information

- **Orchestrator**: orchestration framework and safe async runtime called kyron for Rust

  - **Link to release**: `orchestrator v0.0.3 <https://github.com/eclipse-score/orchestrator/releases/tag/v0.0.3>`_
  - **Release notes**:

    - Provides Kyron - async runtime for Rust. Kyron is a customizable, high-performance async/await runtime designed for advanced concurrent programming with focus on funcional safety.
      It allows fine-grained control over scheduling, thread management, and workload isolation through configurable execution engines.

      - `Read more on scope. <https://github.com/eclipse-score/orchestrator/blob/main/src/kyron/doc/features.md>`__
      - `Check out the examples. <https://github.com/eclipse-score/orchestrator/tree/main/src/kyron/examples>`__

    - Provides Orchestration - framework to build Task Chains with deterministic execution flow.
      The Orchestrator framework provides a structured, declarative way to define cause-effect chains and timing requirements within software applications.
      It enables developers to specify control flow, timing constraints, and error handling in a platform-independent manner.
      The Orchestrator integrates seamlessly with the kyron, clearly separating application logic from deployment and resource management.

      - `Read more on scope. <https://github.com/eclipse-score/orchestrator/blob/main/src/orchestration/doc/features.md>`__
      - `Check out the examples. <https://github.com/eclipse-score/orchestrator/tree/main/src/orchestration/examples>`__


- **Reference integration**: central place for integration of Eclipse S-Core modules

  - **Link to release**: `reference integration v0.5.0-alpha <https://github.com/eclipse-score/reference_integration/releases/tag/v0.5.0-alpha>`_
  - **Release notes**

    - **common**

      - Provides integration of all 0.5 modules including `scrample demo application <https://github.com/eclipse-score/scrample>`_
      - Provides CI/CD workflows to ensure stability of the reference integration:

        - `build and test on every pr <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/build_and_test_on_every_pr.yml>`_ and
          `test integration <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/test_integration.yml>`_
          build all functional modules of Eclipse S-Core v0.5 and execute multiple tests to ensure stability of the reference integration for every pr and on every release creation
      - Provides `complete documentation <https://eclipse-score.github.io/reference_integration/main/>`_ of all modules
  
    - **reference qnx image**

      - Provides reference QNX x86_64 qemu image, for usage see `reference integration README <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/README.md>`_
      - `release verification <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/release_verification.yml>`_ executes multiple integration tests
        in reference qnx image during creation of releases to ensure that the reference qnx image is fully functional
      - Provides `basic itf tests <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu/test/itf>`_.
        Check following `build commands <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu#build-commands>`_ for running itf tests locally and for other important commands.

    - **reference autosd linux image** (Experimental)

      - Provides reference linux based autosd image, for usage see `autosd README <https://github.com/eclipse-score/reference_integration/tree/main/autosd/build>`_
      - Integrates ipc tests (same functionality as scrample example) and executes them on top of autosd image in a separate
        `build_and_test_autosd <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/build_and_test_autosd.yml>`_ workflow
      - **Please note**: the integration of autosd linux image is experimental and do not follow S-CORE process, e.g. integration into bazel is missing. This will be
        fixed in the upcoming releases.

    - **reference ebclfsa linux image** (Experimental)

      - Shows the integration of Eclipse S-CORE on Elektrobit corbos Linux for Safety Applications.
        It integrates *scrample* application based on the Eclipse S-CORE communication framework as demo/test application.
        This application is then integrated into the so-called "fast-dev" variant of EB corbos Linux for Safety Applications (EBcLfSA).
        This is an `aarch64`-based, pre-built image, capable of demonstraing the execution of high integrity applications in regular Linux user-space.
        The example can be executed using QEMU.
        In the `related CI workflow <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/build_and_test_ebclfsa.yml>`_,
        all these steps are performed, and the resulting log files are stored and made available for download.
        See `ebclfsa README <https://github.com/eclipse-score/reference_integration/blob/main/ebclfsa/README.md>`_ for details.

      - **Please note**: the integration of ebclfsa linux image is experimental. It already provides integration into bazel build system
        however some of the integration code needs rework in the future releases.



Associated Infrastructure Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **process_description**: provides a process model establishing organization rules for developing open source software
  in the automotive industry, which can be used in safety and security context

  - **Link to release**: `process_description v0.1.3 <https://github.com/eclipse-score/process_description/releases/tag/v1.3.0>`_
  - **Release notes**

    - The process model provides processes, which conform to state-of the art standards

      - ASPICE 4.0
      - ISO 26262
      - ISO 21434
      - ISO PAS 8926

    - Check the full `process_description release notes <https://github.com/eclipse-score/process_description/releases/tag/v1.3.0>`_ for more information

- **docs-as-code**: tooling for linking and generation of documentation
  
  - **Link to release**: `docs-as-code v2.0.1 <https://github.com/eclipse-score/docs-as-code/releases/tag/v2.0.1>`_

- **tooling**: tooling for S-CORE development

  - **Link to release**: `tooling v1.0.2 <https://github.com/eclipse-score/tooling/releases/tag/v1.0.2>`_

- **ITF**: integration Testing Framework for execution of feature integration tests on the reference image

  - **Link to release**: `itf v0.1.0  <https://github.com/eclipse-score/itf/releases/tag/0.1.0>`_
  - **Release notes**

    - Bazel setup for macro *py_itf_test*
    - Pinging target
    - SSH and SPTP module
    - DLT module
    - Starting Qemu from `reference_integration <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu>`_ repository
    - `ITF readme <https://github.com/eclipse-score/itf/blob/main/README.md>`_
    - `reference_integration readme <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/README.md#build-commands>`_

- **Test Scenarios**: testing framework providing a backend for testers to create parametrizable scenarios in Rust and C++ which can be used in common test case implementation validating parallel implementations.


  - **Link to release**: `Test Scenarios v0.3.0  <https://github.com/eclipse-score/testing_tools/releases/tag/v0.3.0>`_
  - **Release notes**

    - Provides test_scenarios_cpp - C++ framework for defining, running, and managing test scenarios in a structured and extensible way.
    - Provides test_scenarios_rust - equivalent implemented in Rust.
    - Both frameworks share the same concepts and allow to define parametrizable test scenarios that can be used in common test case implementations.
      They are designed to support automated testing, scenario grouping, and integration with CLI tools.

Performed Verification
^^^^^^^^^^^^^^^^^^^^^^^^
Following tests were executed:

- every C++ module was successfully built with gcc and qcc toolchain
- every RUST module was successfully built with rust toolchain
- every module has executed its unit-tests
- few basic integration tests were executed with reference integration qnx image in QEMU as it can be seen in the
  `release verification workflow <https://github.com/eclipse-score/reference_integration/blob/37aa2fc1409f6907bf5d9f3c2643489bb937f90e/.github/workflows/release_verification.yml#L56>`_
  CI/CD workflow
- for *persistency* and *orchestration* modules, component and feature integration tests with *score-test-scenarios* framework were executed, see
  `feature_showcase <https://github.com/eclipse-score/reference_integration/tree/main/feature_showcase>`_ and
  `feature_integration_tests <https://github.com/eclipse-score/reference_integration/tree/main/feature_integration_tests>`_ for more details.

Known Issues
^^^^^^^^^^^^^^^^
- see release notes of every module seperately

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^^^^^
- none, first published release.

Contact Information
^^^^^^^^^^^^^^^^^^^^
For any questions or support, please contact the *Project lead* or raise an issue/discussion.

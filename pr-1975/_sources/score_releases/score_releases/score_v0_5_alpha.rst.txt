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
   :realizes: PROCESS_wp__platform_sw_release_note

| **Platform Name**: S-CORE
| **Release Tag**: v0.5.0-alpha
| **Origin Release Tag**: none - first published release
| **Release Commit Hash**: <add hash>
| **Release Date**: 2025-11-11

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
First version of **Eclipse S-Core book**, that can be used as "how-to" for all who wants to start with S-Core project, can be found here: TODO Link.
This book provides explanation of general concepts of **Eclipse S-Core project** and contains a "step-by-step" guide for building a first application
based on Eclipse S-Core platform modules.

New Features
^^^^^^^^^^^^^

- **Inter-process Communication**
- **Base libs**
- **Fixed execution order framework**
- **Logging**
- **Persistency Key-Value-Storage**
- **Reference integration**
- **Orchestration and Kyron async runtime for Rust**

Improvements
^^^^^^^^^^^^^

- please consider release notes of every module

Bug Fixes
^^^^^^^^^^^^

- please consider release notes of every module

Integrated Software Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Communication**: (Version). Link to Software module release note.
- **FEO**: (Version). Link to Software module release note.
- **Logging**: (Version). Link to Software module release note.
- **Tracing**: (Version). Link to Software module release note.
- **Baselibs**: (Version). Link to Software module release note.
- **OS**: (Version). Link to Software module release note (external module).
- **Orchestrator**: Orchestration framework and safe async runtime called kyron for Rust

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

  - **Link to release**: tbd
  - **Release notes**

    - Provides reference QNX x86_64 qemu image, for usage see `reference integration README <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/README.md>`_
    - Provides integration of all 0.5 modules including `scrample demo application <https://github.com/eclipse-score/scrample>`_
    - Provides `basic itf tests <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu/test/itf>`_.
      Check following `build commands <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu#build-commands>`_ for running itf tests locally and for other important commands.
    - Provide CI/CD workflows to ensure stability of the reference integration:

      - `build and test on every pr <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/build_and_test_on_every_pr.yml>`_ executes all itf tests in reference qnx image on every pr
        to ensure that the image is still functional
      - `release verification <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/release_verification.yml>`_ does the same on every release
      - `test integration <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/test_integration.yml>`_ for every pr and on every release builds all functional modules of Eclipse S-Core v0.5
        release and additionally executes component tests with `<score-test-scenarios https://github.com/eclipse-score/testing_tools>`_ framework for some of components.


Associated Infrastructure Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **process_description**: (Version). Process description of S-CORE. Link to release note?
- **docs-as-code**: (Version). Tooling for linking and generation of documentation. Link to release note?
- **tooling**: (Version). Provided tooling for S-CORE development. Link to release note?
- **ITF**: Integration Testing Framework for execution of feature integration tests on the reference image

  - **Link to release**: `itf v0.1.0  <https://github.com/eclipse-score/itf/releases/tag/0.1.0>`_
  - **Release notes**

    - Bazel setup for macro *py_itf_test*
    - Pinging target
    - SSH and SPTP module
    - DLT module
    - Starting Qemu from `reference_integration <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu>`_ repository
    - `ITF readme <https://github.com/eclipse-score/itf/blob/main/README.md>`_
    - `reference_integration readme <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/README.md#build-commands>`_

- **Test Scenarios**: Testing framework providing a backend for testers to create parametrizable scenarios in Rust and C++ which can be used in common test case implementation validating parallel implementations.


  - **Link to release**: `Test Scenarios v0.3.0  <https://github.com/eclipse-score/testing_tools/releases/tag/v0.3.0>`_
  - **Release notes**

    - Provides test_scenarios_cpp - C++ framework for defining, running, and managing test scenarios in a structured and extensible way.
    - Provides test_scenarios_rust - equivalent implemented in Rust.
    - Both frameworks share the same concepts and allow to define parametrizable test scenarios that can be used in common test case implementations.
      They are designed to support automated testing, scenario grouping, and integration with CLI tools.

Performed Verification
^^^^^^^^^^^^^^^^^^^^^^^^
Following tests were executed:

- every module has executed its unit-tests
- few basic integration tests were executed with reference integration qnx image in Qemu as can be seen e.g. in the following `Action Run <https://github.com/eclipse-score/reference_integration/actions/runs/19128779084/job/54664320615#step:7:689>`_.
- for some of the modules (**TODO**), component tests with score-test-scenarios framework were executed

Known Issues
^^^^^^^^^^^^^^^^
- see release notes of every module seperately

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^^^^^
- none, first published release.

Contact Information
^^^^^^^^^^^^^^^^^^^^
For any questions or support, please contact the *Project lead* or raise an issue/discussion.

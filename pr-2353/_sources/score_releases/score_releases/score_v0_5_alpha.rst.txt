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
This is the first published release of the **Eclipse S-CORE platform** (v0.5.0-alpha). It brings
together the initial set of core modules, reference integrations, and supporting infrastructure needed to
build and run example applications such as the `scrample <https://github.com/eclipse-score/scrample>`_
demo on multiple target images. The software architecture and implemented modules are illustrated in the diagram below.

This release of Eclipse S-CORE is an early alpha version intended solely for experimentation, test driving project processes, gaining experience in release creation and soliciting feedback.
Please be aware, that features may be incomplete, the software may exhibit instability or unexpected behavior, and breaking changes and alterations in scope are likely as development progresses.


.. image:: ../_assets/architecture.drawio.svg
   :width: 1000
   :alt: Architecture overview
   :align: center

|

Highlights
-----------
- First public alpha of the Eclipse S-CORE platform.
- Reference integration including the *scrample* demo application.
- Initial set of communication, persistency, orchestration, and base utility modules.
- Experimental reference images for QNX, Red Hat AutoSD Linux, and EB corbos Linux for Safety Applications.

Timeline
---------
The current timeline for Eclipse S-CORE releases is shown below.

.. image:: ../_assets/score_release_plan.drawio.svg
   :width: 800
   :alt: Architecture overview
   :align: center

|

For a detailed and always up-to-date planning view, see the `GitHub project <https://github.com/orgs/eclipse-score/projects/17/views/26>`_.

Eclipse S-CORE book
-------------------
The first version of the `Eclipse S-CORE book <https://eclipse-score.github.io/score/main/handbook/index.html>`_
is a “how-to” guide for users getting started with the project.
It introduces the core concepts of Eclipse S-CORE and walks through building
the ``scrample`` application step by step on top of the platform modules.

Improvements
^^^^^^^^^^^^^
This release introduces the initial integrated platform with the modules listed below.
For module-specific improvements, refer to the release notes in each module repository.

Bug Fixes
^^^^^^^^^^^^
Bug fixes are tracked and documented per module. Please see the corresponding module
release notes for details on fixed issues in this release.

Integrated Software Modules
-----------------------------

Communication
~~~~~~~~~~~~~
Zero-copy, shared-memory based inter-process communication for minimal-latency intra-ECU messaging.

- **Version:** ``communication v0.1.1``
- **Source / tag:** `Communication GitHub release <https://github.com/eclipse-score/communication/archive/refs/tags/v0.1.1.tar.gz>`_
- **Release notes:** :need:`doc__communication_release_note`

Fixed Execution Order Framework(FEO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Application Framework which is intended to support data-driven or time-driven applications.

- **Link to release**: ``feo v1.0.2``
- **Source / tag:** `FEO GitHub release <https://github.com/eclipse-score/feo/releases/tag/v1.0.2>`_
- **Release notes**:
    - A framework for applications (not for platform services)
    - For data-driven and time-driven applications (mainly in the ADAS domain)
    - Support fixed execution order
    - Supporting reprocessing

    - `Read more on scope. <https://eclipse-score.github.io/score/main/features/frameworks/feo/index.html>`__
    - `Check out the examples. <https://github.com/eclipse-score/feo/tree/main/examples>`__

Baselibs
~~~~~~~~~~~~~
Selection of basic C++ utility libraries for common use in the S-CORE project

- **Version:** ``baselibs v0.1.3``
- **Source / tag:** `Baselibs GitHub release <https://github.com/eclipse-score/baselibs/archive/refs/tags/v0.1.3.tar.gz>`_
- **Release notes**: `Baselibs release notes <https://github.com/eclipse-score/baselibs/releases/tag/v0.1.3>`_


Persistency
~~~~~~~~~~~~~
Ensures long-term storage and retrieval of data and provides a reliable mechanism for
preserving application state and data integrity over time.

- **Version:** ``persistency v0.2.1``
- **Source / tag:** `Persistency GitHub release <https://github.com/eclipse-score/persistency/archive/refs/tags/v0.2.1.tar.gz>`_
- **Notes**:

  - `The feature requirements and architecture <https://eclipse-score.github.io/score/main/features/persistency/index.html>`_  and
    `component requirements and architecture <https://eclipse-score.github.io/score/main/modules/persistency/index.html>`_ documents are partially out of date
    and will be updated in the next release.
  - See the full `persistency release notes <https://github.com/eclipse-score/persistency/releases/tag/v0.2.1>`_ for details


Orchestrator (Kyron and orchestration framework)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Provides:

- **Kyron** – an async runtime for Rust, designed for high-performance async/await execution
  with functional safety in mind. It offers fine-grained control over scheduling, thread management,
  and workload isolation via configurable execution engines.
- **Orchestrator** – a framework to build task chains with deterministic execution flow.
  It lets developers describe cause–effect chains, timing constraints, and error handling in a
  platform-independent way while keeping application logic separate from deployment and
  resource management.

- **Version:** ``orchestrator v0.0.3``
- **Source / tag:** `Orchestrator GitHub release <https://github.com/eclipse-score/orchestrator/archive/refs/tags/v0.0.3.tar.gz>`_
- **Further reading**:

  - `Kyron scope and design <https://github.com/eclipse-score/orchestrator/blob/main/src/kyron/doc/features.md>`__
  - `Kyron examples <https://github.com/eclipse-score/orchestrator/tree/main/src/kyron/examples>`__
  - `Orchestrator scope and design <https://github.com/eclipse-score/orchestrator/blob/main/src/kyron/doc/features.md>`__
  - `Orchestrator examples <https://github.com/eclipse-score/orchestrator/tree/main/src/kyron/examples>`__


Reference integration
~~~~~~~~~~~~~~~~~~~~~~
Central integration of Eclipse S-CORE modules

- **Version:** ``reference integration v0.5.0-alpha``
- **Source / tag:** `Reference Integration GitHub release <https://github.com/eclipse-score/reference_integration/releases/tag/v0.5.0-alpha>`_

Common
+++++++
- Integrates all v0.5 modules, including the ``scrample`` demo application.
- Provides CI/CD workflows to ensure stability of the reference integration:

  - `Build and test on every PR <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/build_and_test_on_every_pr.yml>`_
  - `Test integration <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/test_integration.yml>`_
    build all functional modules of Eclipse S-Core v0.5 and execute multiple tests to ensure stability of the reference integration for every pr and on every release creation.
  - Offers `complete documentation <https://eclipse-score.github.io/reference_integration/main/>`_ of all modules.

Reference QNX image
+++++++++++++++++++++
- Provides a QNX `x86_64` QEMU image; see `reference integration README <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/README.md>`_
  for usage instructions.
- `Release verification workflow <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/release_verification.yml>`_ runs multiple integration tests
  on the QNX image during release creation.
- Provides `basic ITF tests <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu/test/itf>`_.
  see the documented `build commands <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu#build-commands>`_ for running ITF tests locally.

Reference Red Hat AutoSD Linux image (Experimental)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
- Provides a Linux-based AutoSD image usable with QEMU for both `x86_64` and `aarch64`; for usage see `AutoSD README <https://github.com/eclipse-score/reference_integration/tree/main/autosd/build>`_
- Integrates IPC tests (equivalent functionality to the ``scrample`` example) using the QM environment.
- A dedicated `build_and_test_autosd <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/build_and_test_autosd.yml>`_ execute these tests.
- **Note**: The AutoSD Linux integration is experimental and does not yet follow the full S-CORE process. Bazel integration is still missing and will be
  addressed in upcoming releases.

Reference Elektrobit corbos Linux for Safety Applications Linux image (Experimental)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
- Demonstrates Eclipse S-CORE running on Elektrobit corbos Linux for Safety Applications (EBcLfSA).
- Integrates the ``scrample`` demo application into the "fast-dev" EBcLfSA image (aarch64).
- In the `related CI workflow <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/build_and_test_ebclfsa.yml>`_,
  all these steps are performed, and the resulting log files are stored and made available for download.
- Integration can be executed via QEMU; see the `EBcLfSA README <https://github.com/eclipse-score/reference_integration/blob/main/ebclfsa/README.md>`_ for details.
- **Note**: The EBcLfSA integration is experimental. Bazel integration exists, but parts of the integration code will be reworked in future releases.

Associated Infrastructure Modules
-----------------------------------

process_description
~~~~~~~~~~~~~~~~~~~~~~~
Provides a process model establishing organisational rules for developing open source software
in the automotive domain, suitable for safety and security contexts.

- **Version:** ``process description v0.1.3``
- **Standards alignment:**

    - ASPICE 4.0
    - ISO 26262
    - ISO 21434
    - ISO PAS 8926

- **Release notes**: `process_description release notes <https://github.com/eclipse-score/process_description/releases/tag/v1.3.0>`_

docs-as-code
~~~~~~~~~~~~~~
Tooling for linking and generation of documentation.

- **Version:** ``docs-as-code v2.0.2``
- **Source / tag:** `docs-as-code GitHub release <https://github.com/eclipse-score/docs-as-code/releases/tag/v2.0.1>`_

tooling
~~~~~~~~~~~~~~
Tooling for S-CORE development.

- **Version:** ``tooling v1.0.2``
- **Source / tag:** `tooling GitHub release <https://github.com/eclipse-score/tooling/releases/tag/v1.0.2>`_

ITF (Integration Testing Framework)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Framework for executing feature integration tests on the reference image.

- **Version:** ``itf v0.1.0``
- **Source / tag:** `ITF GitHub release <https://github.com/eclipse-score/itf/archive/refs/tags/0.1.0.tar.gz>`_
- **Capabilities:**
    - Bazel macro *py_itf_test*
    - Pinging target
    - SSH and SPTP module
    - DLT module
    - Starting Qemu from the `reference_integration <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu>`_ repository
    - **Documentation:**
        - `ITF README <https://github.com/eclipse-score/itf/blob/main/README.md>`_
        - `reference_integration README <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/README.md#build-commands>`_

Test Scenarios
~~~~~~~~~~~~~~~
Testing framework providing a backend for parametrizable scenarios in Rust and C++, usable in
common test case implementations and parallel implementations.

- **Version:** ``test_scenarios v0.3.0``
- **Source / tag:** `Test Scenarios <https://github.com/eclipse-score/testing_tools/archive/refs/tags/v0.3.0.tar.gz>`_
- **Components:**
  - ``test_scenarios_cpp`` – C++ framework for defining, running, and managing test scenarios.
  - ``test_scenarios_rust``– equivalent implementation in Rust.
- Both frameworks share the same concepts and support automated testing, scenario grouping,
  and integration with CLI tools.

Performed Verification
----------------------
The following tests were executed as part of this release:

- All C++ modules built successfully with GCC and QCC toolchains.
- All Rust modules built successfully with the Rust toolchain.
- Each module executed its unit tests.
- Basic integration tests were executed on the reference QNX image in QEMU via the
  `release verification <https://github.com/eclipse-score/reference_integration/blob/37aa2fc1409f6907bf5d9f3c2643489bb937f90e/.github/workflows/release_verification.yml#L56>`_ workflow
- for **persistency** and **orchestration** modules, component and feature integration tests were executed using the ``score-test-scenarios`` framework; see
  `feature_showcase <https://github.com/eclipse-score/reference_integration/tree/main/feature_showcase>`_ and
  `feature_integration_tests <https://github.com/eclipse-score/reference_integration/tree/main/feature_integration_tests>`_ for more details.

Known Issues
----------------------
- see release notes of every module seperately

Upgrade Instructions
----------------------
- none, first published release.

Contact Information
----------------------
For any questions or support, please contact the *Project lead* or raise an issue/discussion.

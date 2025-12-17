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

S-Core v0.5-beta release notes
===============================

.. document:: S-Core v0.5-beta release note
   :id: doc__score_v05_beta_release_note
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__platform_sw_release_note

| **Platform Name**: S-CORE
| **Release Tag**: v0.5.0-beta
| **Origin Release Tag**: none - first published release
| **Release Date**: 2025-12-18

Overview
^^^^^^^^^
This is the second milestone build of the **Eclipse S-CORE platform** (v0.5.0-beta). It brings
together the initial set of core modules, reference integrations, and supporting infrastructure needed to
build and run example applications such as the `scrample <https://github.com/eclipse-score/scrample>`_
demo on multiple target images. The software architecture and implemented modules are illustrated in the diagram below.

This release of Eclipse S-CORE is an early beta version intended solely for experimentation, test driving project processes, gaining experience in release creation and soliciting feedback.
Please be aware, that features may be incomplete, the software may exhibit instability or unexpected behavior, and breaking changes and alterations in scope are likely as development progresses.


.. image:: ../_assets/architecture.drawio.svg
   :width: 1000
   :alt: Architecture overview
   :align: center


|

Highlights
-----------


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
The `Eclipse S-CORE book <https://eclipse-score.github.io/score/main/handbook/index.html>`_
is a “how-to” guide for users getting started with the project or who want to contribute new modules.
It introduces the core concepts of Eclipse S-CORE and walks through building
the ``scrample`` application step by step on top of the platform modules.
It also includes a tutorial for the first application on top of the existing modules.

Improvements
^^^^^^^^^^^^^
Main focus of this release is to improve the overall stability and performance of the platform, as well as to enhance the usability.
This does include

- Static code analysis with CodeQL and Execution of Unit testing  as part of the `Reference Integration https://github.com/eclipse-score/reference_integration`_.
- A new combined build toolchain of qcc and gcc `bazel cpp toolchain https://github.com/eclipse-score/bazel_cpp_toolchains`_.
- Improved doc-as-code and process description
-

Bug Fixes Platform
^^^^^^^^^^^^^^^^^^

https://github.com/eclipse-score/score/issues?q=is%3Aissue%20state%3Aclosed%20type%3ABug

Integrated Software Modules
-----------------------------

Communication
~~~~~~~~~~~~~
Zero-copy, shared-memory based inter-process communication for minimal-latency intra-ECU messaging.

- **Version:** ``communication v0.1.2``
- **Source / tag:** `Communication GitHub release <https://github.com/eclipse-score/communication/archive/refs/tags/v0.1.2.tar.gz>`_
- **Release notes:** :need:`doc__communication_release_note`

Fixed Execution Order Framework(FEO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Version:** ``feo v0.1.2``
- **Source / tag:** `Communication GitHub release <https://github.com/eclipse-score/communication/archive/refs/tags/v0.1.2.tar.gz>`_
- **Stays at v0.5-alpha**

Baselibs
~~~~~~~~~~~~~
TBD


Persistency
~~~~~~~~~~~~~
Ensures long-term storage and retrieval of data and provides a reliable mechanism for
preserving application state and data integrity over time.

- **Version:** ``persistency v0.2.1``
- **Source / tag:** `Persistency GitHub release <https://github.com/eclipse-score/persistency/archive/refs/tags/v0.2.1.tar.gz>`_

Orchestrator
~~~~~~~~~~~~~

**Improvements**

- Support `log` frontend exchange  to: `log`, `tracing` or `score-log` (not yet implemented in this release)
- Increased CIT coverage and stability improvements
- Split of kyron into separate repositories: `orchestrator` and `kyron`

:Version: ``orchestrator v0.0.4``
:Source / tag: `Orchestrator GitHub release <https://github.com/eclipse-score/orchestrator/releases/tag/v0.0.4>`__
:Further reading: See below

  - `Orchestrator scope and design <https://github.com/eclipse-score/orchestrator/blob/main/src/orchestration/doc/features.md>`__
  - `Orchestrator examples <https://github.com/eclipse-score/orchestrator/tree/main/src/orchestration/examples>`__

Kyron
~~~~~~

**Improvements**

- Support `log` frontend exchange  to: `log`, `tracing` or `score-log` (not yet implemented in this release)
- Increased CIT coverage and stability improvements
- Split of kyron into separate repositories: `orchestrator` and `kyron`

:Version: ``kyron v0.0.3``
:Source / tag: `Kyron GitHub release <https://github.com/eclipse-score/kyron/releases/tag/v0.0.3>`__
:Further reading: See below

  - `Kyron scope and design <https://github.com/eclipse-score/kyron/blob/main/src/kyron/doc/features.md>`__
  - `Kyron examples <https://github.com/eclipse-score/kyron/tree/main/src/kyron/examples>`__


Reference integration
~~~~~~~~~~~~~~~~~~~~~~
Central integration of Eclipse S-CORE modules

- **Version:** ``reference integration v0.5.0-beta``
- **Source / tag:** `Reference Integration GitHub release <https://github.com/eclipse-score/reference_integration/releases/tag/v0.5.0-beta>`_


Reference QNX image
+++++++++++++++++++++
TBD

Reference Red Hat AutoSD Linux image (Experimental)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
TBD

Reference Elektrobit corbos Linux for Safety Applications Linux image (Experimental)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Improvements**

- New ``fastdev`` base image snapshot and corresponding toolchain which include latest security patches and updates.
- Updated packages avoid misleading errors during image start and shutdown, which could be confusing for users.

Associated Infrastructure Modules
-----------------------------------

process_description
~~~~~~~~~~~~~~~~~~~
Provides a process model establishing organizational rules for developing open source software
in the automotive domain, suitable for safety and security contexts.

- **Version:** ``process description v1.4.0``
- **Standards alignment:**

    - ASPICE 4.0
    - ISO 26262
    - ISO 21434
    - ISO PAS 8926

- **Release notes**: `process_description release notes <https://github.com/eclipse-score/process_description/releases/tag/v1.4.0>`_
- **Process maturity**: `process_description maturity levels <https://eclipse-score.github.io/process_description/main/>`_

docs-as-code
~~~~~~~~~~~~~~
Tooling for linking and generation of documentation.

- **Version:** ``docs-as-code v2.2.1``
- **Source / tag:** `docs-as-code GitHub release <https://github.com/eclipse-score/docs-as-code/releases/tag/v2.2.1>`_

tooling
~~~~~~~~~~~~~~
Tooling for S-CORE development.

- **Version:** ``tooling v1.0.4``
- **Source / tag:** `tooling GitHub release <https://github.com/eclipse-score/tooling/releases/tag/v1.0.4>`_


ITF (Integration Testing Framework)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Framework for executing feature integration tests on the reference image.

- **Version:** ``itf v0.1.0``
- **Source / tag:** `ITF GitHub release <https://github.com/eclipse-score/itf/archive/refs/tags/0.1.0.tar.gz>`_

Test Scenarios
~~~~~~~~~~~~~~~

**Improvements**
- Refactor tracing subscriber by externalizing it's initialization
- Remove baselibs dependency from C++ scenarios in JSON parsing

:Version: ``Test Scenarios v0.3.1``
:Source / tag: `Test Scenarios GitHub release <https://github.com/eclipse-score/testing_tools/releases/tag/v0.3.1>`__

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
- Static code analysis of all dependencies with CodeQL MISRA C++2023 package. The results you can find here: https://github.com/eclipse-score/reference_integration/actions/workflows/codeql-multiple-repo-scan.yml

Known Issues
----------------------
- see release notes of every module separately

Upgrade Instructions
----------------------
- Increase to newest bazel registry versions: https://github.com/eclipse-score/bazel_registry/tree/main/modules


Contact Information
----------------------
For any questions or support, please contact the *Project lead* or raise an issue/discussion.

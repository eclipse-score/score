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

S-CORE v0.6-release notes
===============================

.. document:: S-CORE v0.6 release note
   :id: doc__score_v06_release_note
   :status: draft
   :safety: QM
   :security: YES
   :realizes: wp__platform_sw_release_note

| **Platform Name**: S-CORE
| **Release Tag**: v0.6.0-beta
| **Origin Release Tag**: v0.5.0-beta
| **Release Date**: 2026-02-22

Overview
^^^^^^^^^
This is the third milestone build of the **Eclipse S-CORE platform** (v0.6.0). It brings
together the initial set of core modules, reference integrations, and supporting infrastructure needed to
build and run example applications such as the `scrample <https://github.com/eclipse-score/scrample>`_
demo on multiple target images. The software architecture and implemented modules are illustrated in the diagram below.

This release of Eclipse S-CORE is an early beta version intended solely for experimentation, test driving project processes, gaining experience in release creation and soliciting feedback.
Please be aware, that features may be incomplete, the software may exhibit instability or unexpected behavior, and breaking changes and alterations in scope are likely as development progresses.


.. image:: ../_assets/architecture.drawio_0_6.svg
   :width: 1000
   :alt: Architecture overview
   :align: center


|

Highlights
-----------

Eclipse S-CORE book
-------------------
The `Eclipse S-CORE book <https://eclipse-score.github.io/score/main/handbook/index.html>`_
is a “how-to” guide for users getting started with the project or who want to contribute new modules.


Improvements
^^^^^^^^^^^^^


S-CORE Platform
^^^^^^^^^^^^^^^^^^

- **Version:** ``score v0.5.5``
- **Release notes**: `S-CORE Platform release notes <https://github.com/eclipse-score/score/releases/tag/v0.5.5>`_



Integrated Software Modules
-----------------------------

Baselibs
~~~~~~~~~~~~~
Selection of basic C++ utility libraries for common use in the S-CORE project

- **Version:** ``baselibs v0.2.4``
- **Release notes**: `Baselibs release notes <https://github.com/eclipse-score/baselibs/releases/tag/v0.2.4>`_

Baselibs Rust
~~~~~~~~~~~~~

Selection of basic Rust utility libraries for common use in the S-CORE project

- **Version:** ``baselibs_rust v0.1.0``
- **Release notes**: `Baselibs Rust release notes <https://github.com/eclipse-score/baselibs_rust/releases/tag/v0.1.0>`_


**Improvements**

- `score_log` - logging frontend for S-CORE
- `containers`- common containers with different allocation and layout techniques including ABI compatible versions for inter-process communication
- `sync` - `std::sync` extensions utilities

Communication
~~~~~~~~~~~~~
Zero-copy, shared-memory based inter-process communication for minimal-latency intra-ECU messaging.

- **Version:** ``communication v0.1.3``
- **Release notes**: `Communication release notes <https://github.com/eclipse-score/baselibs_rust/releases/tag/v0.1.3>`_

**Improvements**

- Enabled various code quality tools
- Extension of the Rust API (expect further extensive work on this API)
- Support explicit setting of application id in configuration (with fallback to PID)

Fixed Execution Order Framework(FEO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A framework for data-driven and time-driven applications (mainly in the ADAS domain)

- **Version:** ``feo v1.0.5``
- **Release notes**: `FEO  release notes 1.0.x <https://github.com/eclipse-score/feo/releases/tag/v1.0.5>`_

**Improvements**

- Update GCC & Rust toolchains
- Update Error propagation and handling
- Update handling startup timeout
- Update handling of spurious interrupts, shutdown and termination signals
- Updates to CI and testing


Persistency
~~~~~~~~~~~
Ensures long-term storage and retrieval of data and provides a reliable mechanism for
preserving application state and data integrity over time.

- **Version:** ``persistency v0.3.0``
- **Release notes**: `Persistency release notes <https://github.com/eclipse-score/persistency/releases/tag/v0.3.0>`_

**Improvements**

- New backend API for Rust
- Testing improvements, including:
  - Additional C++ CIT tests, code quality improvements, tests logging.
- Tooling improvements, including:
  - Improved formatting, Rust linting.
- Aligned snapshot count behavior between C++ and Rust implementations.
- Adapted Ferrocene toolchain for Rust.
- Updated utilized toolchains, updated S-CORE dependencies.

Logging
~~~~~~~

**Improvements**

The Eclipse S-CORE Logging module provides a logging framework for automotive embedded systems,
featuring remote DLT (Diagnostic Log and Trace) capabilities with
lock-free communication between applications and the datarouter daemon.

- **Version:** ``logging v0.1.0``
- **Release notes**: `Logging release notes <https://github.com/eclipse-score/logging/releases/tag/v0.1.0>`_

Orchestrator
~~~~~~~~~~~~~
Orchestrator module provides a framework for defining and executing complex workflows and task sequences in a coordinated manner.

- **Version:** ``orchestrator v0.1.0``
- **Release notes**: `Orchestrator release notes <https://github.com/eclipse-score/orchestrator/releases/tag/v0.1.0>`_

**Improvements**

- Adapted toolchain to ferrocene for Rust
- Support qnx-x86_64
- Examples now run in reference integration repository images

:Further reading: See below

  - `Orchestrator scope and design <https://github.com/eclipse-score/orchestrator/blob/main/src/orchestration/doc/features.md>`__
  - `Orchestrator examples <https://github.com/eclipse-score/orchestrator/tree/main/src/orchestration/examples>`__


Kyron
~~~~~~~~~~~~~~
Kyron is a customizable, high-performance async/await runtime designed for advanced concurrent programming with focus on functional safety.
It allows fine-grained control over scheduling, thread management, and workload isolation through configurable execution engines.

- **Version:** ``kyron v0.1.1``
- **Release notes**: `Kyron release notes <https://github.com/eclipse-score/kyron/releases/tag/v0.1.1>`_

**Improvements**

- Adapted toolchain to ferrocene for Rust
- Support qnx-x86_64
- Integrated rust coverage reporting
- Improved up to 8% runtime time with task scheduler fixes
- Examples now run in reference integration repository images

**Bugfix**

- Minor bugfixes listed in github

**Known issues**

- Ongoing fixing of safety wakes `here <https://github.com/eclipse-score/kyron/pull/32>`_

:Further reading: See below

  - `Kyron scope and design <https://github.com/eclipse-score/kyron/blob/main/src/kyron/doc/features.md>`__
  - `Kyron examples <https://github.com/eclipse-score/kyron/tree/main/src/kyron/examples>`__


Lifecycle & Health Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Lifecycle module provides a Launch Manager for process lifecycle management as well as a Health Monitoring library to support supervision of process behavior.

- **Version:** ``lifecycle v0.1.0``
- **Release notes**: `Lifecycle release notes <https://github.com/eclipse-score/lifecycle/releases/tag/v0.1.0>`_

**Improvements**

- Health Monitoring library for applications with Rust and C++ API
  - Deadline Monitoring support
- Initial version of Launch Manager with mw::lifecycle API
  - The previously separate daemon processes launch_manager and health_monitor are now merged into a single launch_manager daemon process
- Working integration of Launch Manager and Health Monitoring library


Reference integration
~~~~~~~~~~~~~~~~~~~~~~
Central integration of Eclipse S-CORE modules

- **Version:** ``reference integration v0.6.0``
- **Source / tag:** `Reference Integration GitHub release <https://github.com/eclipse-score/reference_integration/releases/tag/v0.6.0>`_

**Improvements**
- Unify handling of images in repository
- Execute all images build and tests in CI
- Execute UT, Coverage in CI and produce documentation with results
- Provide `./score_starter` helper program to allow easily run given image without hassle
- Provide interactive example selection menu on target image so user can choose examples to run and see the results
- Remove separate bazel modules and use single bazel module with always aligned dependencies

Reference QNX image
+++++++++++++++++++++
- No changes compared to the previous software version.

Reference Red Hat AutoSD Linux image (Experimental)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Improvements**

- Remove unused packages to reduce image size
- Move AutoSD images to use Bootc (image mode)
- Integrate AutoSD's Bazel toolchain to build reference integration showcases


Reference Elektrobit corbos Linux for Safety Applications Linux image (Experimental)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- Updates to follow the latest integration structure and dependencies.
- No functional changes compared to the previous software version.

Associated Infrastructure Modules
-----------------------------------

process_description
~~~~~~~~~~~~~~~~~~~
Provides a process model establishing organizational rules for developing open source software
in the automotive domain, suitable for safety and security contexts.

- **Standards alignment:**

  - ASPICE 4.0
  - ISO 26262
  - ISO 21434
  - ISO PAS 8926

- **Version:** ``process description v1.4.3``
- **Release notes**: `process_description release notes v1.4.x <https://github.com/eclipse-score/process_description/releases/tag/v1.4.3>`_
- **Process maturity overview**:

.. figure:: ../_assets/score_process_area_overview.drawio.svg
  :width: 100%
  :align: center
  :alt: Process area overview for the **Project**

For more details please refer to
`Documentation Management Plan <https://eclipse-score.github.io/score/main/platform_management_plan/documentation_management.html>`_, that
provides process workproduct level overview for every software module and process area.


docs-as-code
~~~~~~~~~~~~~~
Tooling for linking and generation of documentation.

- **Version:** ``docs-as-code v3.0.1``
- **Source / tag:** `docs-as-code GitHub release <https://github.com/eclipse-score/docs-as-code/releases/tag/v3.0.1>`_

tooling
~~~~~~~~~~~~~~
Tooling for S-CORE development.

- **Version:** ``tooling v1.1.2``
- **Source / tag:** `tooling GitHub release <https://github.com/eclipse-score/tooling/releases/tag/v1.1.2>`_


ITF (Integration Testing Framework)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Improvements**

  - Improved ITF `user documentation <https://github.com/eclipse-score/itf/blob/main/README.md>`_

- **Version:** ``itf v0.1.1``
- **Source / tag:** `ITF GitHub release <https://github.com/eclipse-score/itf/releases/tag/v0.1.1>`_

Test Scenarios
~~~~~~~~~~~~~~~
Test scenarios provide a backend for defining C++ and Rust implemented test scenarios that allow parametrized execution of built scenario applications which are the input for test cases.

- **Improvements**
  - Adapted new toolchains for C++ and Rust

- **Version:** ``Test Scenarios v0.4.0``
- **Source / tag:** `Test Scenarios GitHub release <https://github.com/eclipse-score/testing_tools/releases/tag/v0.4.0>`_



Bazel CPP Toolchain
~~~~~~~~~~~~~~~~~~~~
- **What is in**

  - tbd

- **Version:** ``bazel_cpp_toolchains v0.3.0``
- **Release notes**: `Bazel CPP Toolchain release notes <https://github.com/eclipse-score/bazel_cpp_toolchains/releases/tag/v0.3.0>`_



Known Issues
----------------------
- see release notes of every module separately

Upgrade Instructions
----------------------
- Increase to newest bazel registry versions: https://eclipse-score.github.io/bazel_registry_ui
- Versions can be found under: https://github.com/eclipse-score/reference_integration/blob/main/known_good.json

Contact Information
----------------------
For any questions or support, please contact the *Project leads* or raise an issue/discussion.
https://projects.eclipse.org/projects/automotive.score

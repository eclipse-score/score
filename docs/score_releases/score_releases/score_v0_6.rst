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

S-Core v0.6-release notes
===============================

.. document:: S-Core v0.6 release note
   :id: doc__score_v06_release_note
   :status: draft
   :safety: ASIL_B
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


.. image:: ../_assets/architecture.drawio.svg
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
It introduces the core concepts of Eclipse S-CORE and walks through building
the ``scrample`` application step by step on top of the platform modules.
It also includes a tutorial for the first application on top of the existing modules.


Improvements
^^^^^^^^^^^^^


S-CORE Platform
^^^^^^^^^^^^^^^^^^

- **Version:** ``score v0.``
- **Source / tag:** `S-CORE Platform GitHub release <>`_
- **Release notes**: `S-CORE Platform release notes <>`_



Integrated Software Modules
-----------------------------

Baselibs
~~~~~~~~~~~~~
Selection of basic C++ utility libraries for common use in the S-CORE project

- **Version:** ``baselibs v0.``
- **Source / tag:** `Baselibs GitHub release <>`_
- **Release notes**: `Baselibs release notes <>`_

Baselibs Rust
~~~~~~~~~~~~~

Selection of basic Rust utility libraries for common use in the S-CORE project

- **Version:** ``baselibs_rust v0.1.0``
- **Source / tag:** `Baselibs Rust GitHub release <https://github.com/eclipse-score/baselibs_rust/releases/tag/v0.1.0>`_
- **Release notes**: `Baselibs Rust release notes <https://github.com/eclipse-score/baselibs_rust/releases/tag/v0.1.0>`_


**Improvements**

- `score_log` - logging frontend for S-CORE
- `containers`- common containers with different allocation and layout techniques including ABI compatible versions for inter-process communication
- `sync` - `std::sync` extensions utilities

Communication
~~~~~~~~~~~~~
Zero-copy, shared-memory based inter-process communication for minimal-latency intra-ECU messaging.

- **Version:** ``communication v0.``
- **Source / tag:** `Communication GitHub release <>`_
- **Release notes:** :need:`doc__communication_release_note`

**Improvements**

- Enabled various code quality tools
- Extension of the Rust API (expect further extensive work on this API)
- Support explicit setting of application id in configuration (with fallback to PID)

Fixed Execution Order Framework(FEO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Version:** ``feo v0.``
- **Source / tag:** `Communication GitHub release <>`_
- **Stays at v0.5-alpha**


Persistency
~~~~~~~~~~~~~
Ensures long-term storage and retrieval of data and provides a reliable mechanism for
preserving application state and data integrity over time.

- **Version:** ``persistency v0``
- **Source / tag:** `Persistency GitHub release <>`_


Logging
~~~~~~~~~~~~~~~~~~

**Improvements**

The Eclipse SCORE Logging module provides a comprehensive logging framework for automotive embedded systems,
featuring remote DLT (Diagnostic Log and Trace) capabilities with
lock-free communication between applications and the datarouter daemon.

This is the initial open-source release of the logging framework,
consolidating the complete project structure with build system, dependencies,
and tooling for integration into Eclipse SCORE projects.

The module is designed for Bazel-based builds and provides both the middleware logging
library (score/mw/log) that includes all supported recorders with respective backends and
the datarouter daemon (score/datarouter). The shared memory implementation between the middleware
library and datarouter daemon guarantees Freedom From Interference (FFI),
enabling safe logging from real-time and safety-critical contexts.

- **Version:** ``logging v0.``
- **VSource / tag:**  `logging release <>`__
- **Further reading:**: See below

  - `Logging release notes <>`__
  - `Logging ReadMe <https://github.com/eclipse-score/logging/tree/main/score/datarouter>`__

**Improvements**
 - `score_log_bridge` - connecting Rust `score_log` frontend to C++ logging backend


Orchestrator
~~~~~~~~~~~~~
Orchestrator module provides a framework for defining and executing complex workflows and task sequences in a coordinated manner.

- **Version:** ``orchestrator v0.1.0``
- **Source / tag:** `Orchestrator GitHub release <https://github.com/eclipse-score/orchestrator/releases/tag/v0.1.0>`_
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
- **Source / tag:** `Kyron GitHub release <https://github.com/eclipse-score/kyron/releases/tag/v0.1.1>`_
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
TBD

- **Version:** ``lifecycle v0.1.0``
- **Source / tag:** `Lifecycle GitHub release <https://github.com/eclipse-score/lifecycle/releases/tag/v0.1.0>`_
- **Release notes**: `Lifecycle release notes <https://github.com/eclipse-score/lifecycle/releases/tag/v0.1.0>`_

**Improvements**

 - Health Monitoring library for applications with Rust and C++ API
  - Deadline Monitoring support


Reference integration
~~~~~~~~~~~~~~~~~~~~~~
Central integration of Eclipse S-CORE modules

- **Version:** ``reference integration v0.6.0``
- **Source / tag:** `Reference Integration GitHub release <>`_

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
- Uses AutoSD's toolchain to build and generate Lola RPMs
- Deploy RPMs into an AutoSD Image

Pull requests:

tbd


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

- **Version:** ``process description v``
- **Standards alignment:**

  - ASPICE 4.0
  - ISO 26262
  - ISO 21434
  - ISO PAS 8926

- **Release notes**: `process_description release notes <>`_
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

- **Version:** ``docs-as-code v``
- **Source / tag:** `docs-as-code GitHub release <>`_

tooling
~~~~~~~~~~~~~~
Tooling for S-CORE development.

- **Version:** ``tooling v``
- **Source / tag:** `tooling GitHub release <>`_


ITF (Integration Testing Framework)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Improvements**

  - Improved ITF `user documentation <https://github.com/eclipse-score/itf/blob/main/README.md>`_

- **Version:** ``itf v0``
- **Source / tag:** `ITF GitHub release <>`_

Test Scenarios
~~~~~~~~~~~~~~~
- **Improvements**

  - Refactor tracing subscriber by externalizing it's initialization
  - Remove baselibs dependency from C++ scenarios in JSON parsing

- **Version:** ``Test Scenarios v0``
- **Source / tag:** `Test Scenarios GitHub release <>`_

.. _bazel_cpp_toolchain:

Bazel CPP Toolchain
~~~~~~~~~~~~~~~~~~~~
- **What is in**

  - tbd

- **Version:** ``bazel_cpp_toolchains v``
- **Source / tag:** `Bazel CPP Toolchain release <>`_
- **Release notes**: `Bazel CPP Toolchain release notes <>`_

Performed Verification
----------------------
tbd

Known Issues
----------------------
- see release notes of every module separately

Upgrade Instructions
----------------------
- Increase to newest bazel registry versions: https://github.com/eclipse-score/bazel_registry/tree/main/modules


Contact Information
----------------------
For any questions or support, please contact the *Project lead* or raise an issue/discussion.

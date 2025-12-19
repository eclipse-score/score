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

Release Note
============

.. document:: Communication Release Note
   :id: doc__communication_release_note
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__module_sw_release_note
   :tags: communication


Module Name: Communication

Release Tag: v0.1.1

Origin Release Tag: none

Release Commit Hash: 24d6e8916b89dbb405eae0b082348645d190dc18

Release Date: 2025-11-11

Overview
--------

This document provides an overview of the changes, improvements, and bug fixes included in the software module release version v0.5
as compared to the module's origin release (which is usually the previous release).

Disclaimer
----------
This release note does not "release for production", as it does not come with a safety argumentation and a performed safety assessment.
The work products compiled in the safety package are created with care according to a process satisfying standards, but the as the project,
being a non-profit and open source organization, can not take over any liability for its content.

New Features
------------

* **Feature 1**: Zero-copy, shared-memory based inter-process communication for minimal latency intra-ECU messaging.
* **Feature 2**: Support for mixed-criticality configurations to match different functional safety requirements.
* **Feature 3**: Service-oriented architecture with skeleton/proxy framework.
* **Feature 4**: Automatic service registration and lookup mechanism for dynamic service discovery at runtime.
* **Feature 5**: Event-driven publish-subscribe messaging pattern for data availability notifications.
* **Feature 6**: Field-based communication with initial-value support (currently no getters or setters).
* **Feature 7**: Zero-copy, binding-agnostic communication tracing support for observability and debugging.

Improvements
------------

This is the first release of the Communication module in Eclipse S-CORE, therefore there are no improvements to report.

Bug Fixes
---------

This is the first release of the Communication module in Eclipse S-CORE, therefore there are no bug fixes to report.

Compatibility
-------------

* **Dependencies**:

  * Bazel Platforms: version 0.0.11 - Platform abstraction for cross-platform builds
  * GoogleTest: version 1.15.0 - Unit testing framework for C++
  * Google Benchmark: version 1.9.1 - Performance benchmarking library
  * Rules Rust: version 0.61.0 - Bazel rules for Rust language support
  * Score Crates: version 0.0.2 - Rust crate dependencies repository
  * Boost Program Options: version 1.87.0 - Command-line argument parsing library
  * Download Utils: version 1.0.1 - Utility for downloading build artifacts
  * JSON Schema Validator: version 2.1.0 - JSON schema validation library (downloaded from GitHub)
  * Jsonschema: version 4.23.0 - Python JSON schema validation (downloaded from GitHub)
  * nlohmann_json: version 3.11.3 - C++ JSON library
  * Bazel Skylib: version 1.7.1 - Bazel standard library utilities
  * Rules Doxygen: version 2.5.0 - Bazel rules for Doxygen documentation generation
  * Score Baselibs: version 0.2.0 (commit de5bb27) - Core libraries with wait-free stack fix patch applied
  * Rules Python: version 0.32.0 - Bazel Python toolchain rules
  * Python: version 3.12 - Runtime for build tooling and traceability tools
  * TRLC: version 0.0.0 (trlc-2.0.2 release, commit 650b51a) - Requirements traceability language and compiler
  * LOBSTER: Requirements traceability and documentation tool (via custom extension)

* **Optional Dependencies (Platform-Specific)**:

  * score_toolchains_gcc: version 0.4 - Toolchain for builds with GCC on various targets
  * score_toolchains_qnx: version 0.0.2 - Toolchain for builds on QNX targets

Performed Verification
----------------------

This release note is based on the verification as documented in module verification report
:need:`doc__communication_verification_report`.


Known Issues
------------

* **Issue 1**: Limited test coverage due to restrictions in S-CORE testing infrastructure
* **Issue 2**: Incomplete Rust frontend with limited functionality compared to C++ frontend
* **Issue 3**: Incomplete PMR Integration - PMR support not fully implemented
* **Issue 4**: Incomplete Error Handling in Rust Bridge - Error propagation incomplete. May cause unwanted behavior in error paths.
* **Issue 5**: Runtime JSON Configuration Validation - Invalid configurations may lead to an abort during configuration parsing at application startup.

Upgrade Instructions
--------------------

This is the first release of the Communication module in Eclipse S-CORE, therefore there are no upgrade instructions.

Contact Information
-------------------

For any questions or support, please contact the *Project lead* or raise an issue/discussion.

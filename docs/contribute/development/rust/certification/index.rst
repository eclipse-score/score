..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

Certification
##############


Rust Certification Guidance
===========================

This section summarizes certification-relevant guidance for Rust and its
tooling, especially in the context of ISO 26262 and RTCA DO-178C/DO-332.

Key points for practice:

* Tool confidence and qualification must be explicitly defined for compiler and
   crates.
* Depending on project context and integrity level, three paths are considered:
   qualified tools, strong downstream verification that detects tool faults, or
   comprehensive confidence evidence for tool usage.
* Qualification evidence is tied to the exact tool version, target
   architecture, and relevant compiler configuration.
* Stable toolchains are expected for certification contexts; nightly features
   are not recommended for safety-related projects.
* Configuration management must include Rust toolchain components (e.g.,
   compiler, rustup/cargo, clippy/rustdoc), runtime libraries, and external
   crates.
* "Proven in use" arguments alone are considered difficult to justify for
   safety cases and should not replace structured qualification or verification
   arguments.

For SCORE, this baseline guidance should be used for certification
strategy, while project-specific safety case evidence is documented in the
corresponding plans and work products.

.. toctree::
   :maxdepth: 1

   toolchain/index
   tools/index

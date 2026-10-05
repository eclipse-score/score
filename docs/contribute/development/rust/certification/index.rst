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

* Determine tool confidence per S-CORE Tool Management process (TI/TD -> TCL).
  TCL is HIGH unless TI=YES and TD=NO; in that case TCL is LOW.
* If TCL is LOW, tool qualification is required. Apply the "validation of
  software tool" method with requirements, tests, and report updates in the
  Tool Verification Report workflow.
* Confidence/qualification evidence is valid only for the exact tool version,
  target architecture, and relevant tool configuration; changes require impact
  analysis and re-validation as needed.
* Proven-in-use is not used as a safety argument in S-CORE (tailored out in
  platform safety management).
* Use stable toolchains for safety-related development; nightly features are
  not recommended.
* Configuration management must include compiler, as well as tools like rustup/cargo, clippy/rustdoc,
  CodeQL, runtime libraries, and external crates.

For S-CORE, this baseline guidance should be used for certification
strategy, while project-specific safety case evidence is documented in the
corresponding plans and work products.

.. toctree::
   :maxdepth: 1

   toolchain/index
   tools/index

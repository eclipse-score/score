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

.. document:: Tool Evaluation List
   :id: doc__tool_evaluation_list
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__tool_verification_report
   :tags: tool_management


.. contents:: Table of Contents
   :depth: 3
   :local:


S-CORE - Complete Tool List for Tool Evaluation
===============================================

Overview
--------

This document provides a comprehensive initial inventory of all tools used across the Eclipse
S-CORE project.

The list is categorized by tool type, e.g. documentation tools, static analysis tools, testing
frameworks, build tools, etc.

The list is intended to be used for the evaluation of tools for safety and security impact, as part
of the tool management process defined in the S-CORE Tool Management Plan.

In future iterations, the list will be completed and updated, and delivered with every platform
release, as part of the Tool Verification Report.


1 Documentation Tools
---------------------

.. list-table:: Documentation Tools
   :header-rows: 1
   :widths: 5 15 15 10 10 10 40 40

   * - ID
     - Tool Name
     - Description
     - Version
     - Relevant [YES|NO]
     - Tool ownership
     - Link to Verification Report (if relevant)
     - Confirmation of Use [YES|NO] (if relevant)
   * - 1-1
     - Doc-as-Code
     - Documentation generation tool
     - 3.0.0 (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - :need:`doc_tool__doc_as_code`
     - YES
   * - 1-2
     - Sphinx
     - Python documentation generator (underlying Doc-as-Code)
     - Latest (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 1-3
     - sphinx-needs
     - Requirements tracking extension for Sphinx
     - T.B.D. (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 1-4
     - PlantUML
     - UML diagram generation
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 1-5
     - Graphviz
     - Graph visualization software
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 1-6
     - sphinxcontrib.plantuml
     - PlantUML integration for Sphinx
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 1-7
     - TRLC
     - BMW Requirements Traceability Language and Compiler
     - 2.0.2 (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 1-8
     - LOBSTER
     - BMW Requirements traceability and documentation tool
     - T.B.D. (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES


2 Static Analysis & Code Quality
--------------------------------


2a C++
++++++

.. list-table:: C++ Static Analysis & Code Quality
   :header-rows: 1
   :widths: 5 15 15 10 10 10 40 40

   * - ID
     - Tool Name
     - Description
     - Version
     - Relevant [YES|NO]
     - Tool ownership
     - Link to Verification Report (if relevant)
     - Confirmation of Use [YES|NO] (if relevant)
   * - 2a-1
     - clang-tidy
     - Static analysis for C++, used with Clang compiler
     - 19.x (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2a-2
     - clang-analyzer
     - Static analyzer from LLVM project
     - 19.x (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2a-3
     - clang-format
     - Code formatter (linter) from LLVM project
     - 19.x (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2a-4
     - CodeQL
     - CodeQL is a semantic code analysis engine used for security and code quality analysis.
     - T.B.D. (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2a-5
     - gcovr
     - Code coverage tool (uses gcov from GCC), part of GNU compiler collection
     - T.B.D. (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES


2b Rust
+++++++

.. list-table:: Rust Static Analysis & Code Quality
   :header-rows: 1
   :widths: 5 15 15 10 10 10 40 40

   * - ID
     - Tool Name
     - Description
     - Version
     - Relevant [YES|NO]
     - Tool ownership
     - Link to Verification Report (if relevant)
     - Confirmation of Use [YES|NO] (if relevant)
   * - 2b-1
     - clippy
     - Rust linter for static code analysis
     - 1.90.0 (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - :need:`doc_tool__clippy`
     - YES
   * - 2b-2
     - rustfmt
     - Rust code formatter
     - 1.8.0 (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - :need:`doc_tool__rustfmt`
     - YES
   * - 2b-3
     - rust-analyzer
     - Rust language server for IDE support
     - 1.8.0 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES


2c Python
+++++++++

.. list-table:: Python Static Analysis & Code Quality
   :header-rows: 1
   :widths: 5 15 15 10 10 10 40 40

   * - ID
     - Tool Name
     - Description
     - Version
     - Relevant [YES|NO]
     - Tool ownership
     - Link to Verification Report (if relevant)
     - Confirmation of Use [YES|NO] (if relevant)
   * - 2c-1
     - ruff
     - Fast Python formatter and linter, replaces multiple tools
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2c-2
     - pyright
     - Python static type checker
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2c-3
     - pylint
     - Python code quality analysis
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2c-4
     - pytest-cov
     - Python test coverage reporting
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2c-5
     - basedpyright
     - Alternative Python type checker
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES


2d Other
++++++++

.. list-table:: Other Static Analysis & Code Quality
   :header-rows: 1
   :widths: 5 15 15 10 10 10 40 40

   * - ID
     - Tool Name
     - Description
     - Version
     - Relevant [YES|NO]
     - Tool ownership
     - Link to Verification Report (if relevant)
     - Confirmation of Use [YES|NO] (if relevant)
   * - 2d-1
     - yamlfmt
     - YAML file formatter
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2d-2
     - actionlint
     - GitHub Actions workflow linter
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2d-3
     - starpls
     - Starlark (Bazel) language server
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2d-4
     - score_tooling
     - Copyright checker, CLI helper, license checker
     - 1.0.4 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2d-5
     - bazel-tools-cc
     - Clang-tidy based static code checker for Bazel
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 2d-6
     - gitlint
     - Commit message linting
     - 0.19.1 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES


3 Testing Frameworks
--------------------

.. list-table:: Testing Frameworks
   :header-rows: 1
   :widths: 5 15 15 10 10 10 40 40

   * - ID
     - Tool Name
     - Description
     - Version
     - Relevant [YES|NO]
     - Tool ownership
     - Link to Verification Report (if relevant)
     - Confirmation of Use [YES|NO] (if relevant)
   * - 3-1
     - gtest (GoogleTest)
     - C++ testing framework
     - 1.15.0 (see [1]_)
     - YES
     - :need:`rl__testing_community`
     - :need:`doc_tool__gtest`
     - YES
   * - 3-2
     - ITF
     - Integration Testing Framework, pytest-based
     - 0.1.0 (see [1]_)
     - YES
     - :need:`rl__testing_community`
     - :need:`doc_tool__itf`
     - YES
   * - 3-3
     - pytest
     - Python testing framework
     - T.B.D. (see [1]_)
     - YES
     - :need:`rl__testing_community`
     - :need:`doc_tool__pytest`
     - YES



4 Build & Development Tools
---------------------------

.. list-table:: Build & Development Tools
   :header-rows: 1
   :widths: 5 15 15 10 10 10 40 40

   * - ID
     - Tool Name
     - Description
     - Version
     - Relevant [YES|NO]
     - Tool ownership
     - Link to Verification Report (if relevant)
     - Confirmation of Use [YES|NO] (if relevant)
   * - 4-1
     - Bazel
     - Main build system
     - 8.3.0 (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - :need:`doc_tool__bazel`
     - YES
   * - 4-2
     - buildifier
     - Bazel file formatter and linter
     - 8.2.0.2 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 4-3
     - rules_python
     - Bazel Python build rules
     - 1.4.1 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 4-4
     - aspect_rules_py
     - Enhanced Python rules (provides py_venv)
     - 1.6.3 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 4-5
     - aspect_rules_lint
     - Generic linting and formatting rules
     - 1.5.3 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 4-6
     - rules_pkg
     - Packaging dependencies
     - 1.1.0 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 4-7
     - rules_java
     - Java build rules
     - 8.15.1 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 4-8
     - rules_cc
     - C/C++ build rules
     - 0.2.1 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 4-9
     - rules_rust
     - Rust build rules for Bazel
     - 0.63.0 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 4-10
     - score_toolchains_qnx
     - QNX SDP toolchain including compiler, linker, image creation tools
     - 0.5 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 4-11
     - score_toolchains_gcc
     - GCC toolchain packages for various targets
     - 0.5 (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 4-12
     - toolchains_llvm
     - LLVM toolchain rules for Bazel (host configuration, C++17 standard)
     - 1.4.0 (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - N/A
   * - 4-13
     - score_toolchains_rust
     - Rust toolchains for SCORE project
     - T.B.D. (see [1]_)
     - NO
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES

5 Compiler
----------

5a C++ Compiler
+++++++++++++++

.. list-table:: C++ Compiler
   :header-rows: 1
   :widths: 5 15 15 10 10 10 40 40

   * - ID
     - Tool Name
     - Description
     - Version
     - Relevant [YES|NO]
     - Tool ownership
     - Link to Verification Report (if relevant)
     - Confirmation of Use [YES|NO] (if relevant)
   * - 5a-1
     - GCC
     - Host C++ compiler with linker, generates compiler warnings, builds unit tests and binaries for SW integration testing
     - 12+ (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - :need:`doc_tool__gcc`
     - YES
   * - 5a-2
     - QNX 8.x SDP
     - Qualified compiler/linker from BlackBerry for QNX, used for target compilation
     - 12+ (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - :need:`doc_tool__qcc`
     - N/A


5b Rust Compiler
++++++++++++++++

.. list-table:: Rust Compiler
   :header-rows: 1
   :widths: 5 15 15 10 10 10 40 40

   * - ID
     - Tool Name
     - Description
     - Version
     - Relevant [YES|NO]
     - Tool ownership
     - Link to Verification Report (if relevant)
     - Confirmation of Use [YES|NO] (if relevant)
   * - 5b-1
     - Ferrocene
     - Qualified Rust compiler (planned for target, safety-critical use), see https://github.com/ferrocene
     - 1.90.0 (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 5b-2
     - Rust (standard)
     - For host development, no current selection for S-CORE host compiler
     - 1.90.0 (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - NO


6 Version Control & CI/CD
-------------------------

.. list-table:: Version Control and CI/CD Tools
   :header-rows: 1
   :widths: 5 15 15 10 10 10 40 40

   * - ID
     - Tool Name
     - Description
     - Version
     - Relevant [YES|NO]
     - Tool ownership
     - Link to Verification Report (if relevant)
     - Confirmation of Use [YES|NO] (if relevant)
   * - 6-1
     - Git
     - Version control system
     - 2.x (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES
   * - 6-2
     - GitHub
     - Code hosting and collaboration platform
     - cloud
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - :need:`doc_tool__github`
     - YES
   * - 6-3
     - GitHub Actions
     - CI/CD automation platform
     - T.B.D. (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES


7 License & Security
--------------------

.. list-table:: License & Security
   :header-rows: 1
   :widths: 5 15 15 10 10 10 40 40

   * - ID
     - Tool Name
     - Description
     - Version
     - Relevant [YES|NO]
     - Tool ownership
     - Link to Verification Report (if relevant)
     - Confirmation of Use [YES|NO] (if relevant)
   * - 7-1
     - Eclipse Dash
     - License analysis tool
     - T.B.D. (see [1]_)
     - YES
     - :need:`rl__infrastructure_tooling_community`
     - N/A
     - YES




.. [1] The tool version mentioned in this document is preliminary.
       Exact version must be derived before every platform release.

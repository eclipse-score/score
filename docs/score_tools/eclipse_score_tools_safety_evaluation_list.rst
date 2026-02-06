.. *******************************************************************************
.. Copyright (c) 2026 Contributors to the Eclipse Foundation
..
.. See the NOTICE file(s) distributed with this work for additional
.. information regarding copyright ownership.
..
.. This program and the accompanying materials are made available under the
.. terms of the Apache License Version 2.0 which is available at
.. https://www.apache.org/licenses/LICENSE-2.0
..
.. SPDX-License-Identifier: Apache-2.0
.. *******************************************************************************

========================================================
Eclipse SCORE - Complete Tool List for Safety Evaluation
========================================================

:Date: January 26, 2026
:Organization: Eclipse Foundation
:Project: Eclipse SCORE (Scalable & Modular COmponent Runtime Environment)
:Purpose: Comprehensive tool inventory for safety classification and evaluation

.. contents:: Table of Contents
   :depth: 3
   :local:

Overview
========

This document provides a comprehensive initial inventory of all tools used across the Eclipse SCORE project
and its 68+ repositories under https://github.com/eclipse-score. The list includes build tools,
compilers, static analyzers, testing frameworks, documentation generators, and supporting utilities.

Each tool should be evaluated for safety and security impact according to the tool management process
defined in the S-CORE Tool Management Plan.

But first the list must be validated and completed with any missing tools. Also there may be
false positives that need to be removed, e.g. nhlohmann_json is a library, not a tool.

Please review the list below and provide feedback on any missing tools, false positives,
or other discrepancies.

The version is not important for now, but will be tracked in the future.

In future iterations, the following the collection will be enhanced and updated, at least for
version using automatic SBOM generation.


Build & Development Tools
==========================

Build System & Package Management
----------------------------------

.. list-table:: Build System Tools
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 1
     - Bazel
     - 8.3.0
     - LOW
     - YES
     - YES
     - Main build system (documented in score_tools)
   * - 2
     - Bazelisk
     - Latest
     - TBD
     - TBD
     - TBD
     - Bazel version manager, reads .bazelversion file
   * - 3
     - buildifier
     - 8.2.0.2
     - TBD
     - TBD
     - TBD
     - Bazel file formatter and linter
   * - 4
     - rules_python
     - 1.4.1
     - TBD
     - TBD
     - TBD
     - Bazel Python build rules
   * - 5
     - aspect_rules_py
     - 1.6.3
     - TBD
     - TBD
     - TBD
     - Enhanced Python rules (provides py_venv)
   * - 6
     - aspect_rules_lint
     - 1.5.3
     - TBD
     - TBD
     - TBD
     - Generic linting and formatting rules
   * - 7
     - rules_pkg
     - 1.1.0
     - TBD
     - TBD
     - TBD
     - Packaging dependencies
   * - 8
     - rules_java
     - 8.15.1
     - TBD
     - TBD
     - TBD
     - Java build rules
   * - 9
     - rules_cc
     - 0.1.1/0.2.1
     - TBD
     - TBD
     - TBD
     - C/C++ build rules
   * - 10
     - rules_rust
     - 0.61.0-0.63.0
     - TBD
     - TBD
     - TBD
     - Rust build rules for Bazel

Compilers & Toolchains
======================

C++ Compilers
-------------

.. list-table:: C++ Compiler Toolchains
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 11
     - GCC
     - 12+
     - TBD
     - YES
     - YES
     - Host C++ compiler with linker, generates compiler warnings, builds unit tests and binaries for SW integration testing
   * - 12
     - QCC
     - QNX 8.x SDP
     - TBD
     - YES
     - YES
     - Qualifiable compiler/linker from BlackBerry for QNX, used for target compilation
   * - 13
     - LLVM/Clang
     - 19.1.0
     - TBD
     - YES
     - YES
     - Alternative C++ compiler toolchain
   * - 14
     - toolchains_llvm
     - 1.4.0
     - TBD
     - YES
     - YES
     - LLVM toolchain rules for Bazel (host configuration, C++17 standard)

Rust Compilers
--------------

.. list-table:: Rust Compiler Toolchains
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 15
     - Ferrocene
     - Planned
     - TBD
     - YES
     - YES
     - Qualified Rust compiler (planned for target, safety-critical use), see https://github.com/ferrocene
   * - 16
     - Rust (standard)
     - 1.90.0+
     - TBD
     - YES
     - YES
     - For host development, no current selection for S-CORE host compiler

QNX & Platform Toolchains
--------------------------

.. list-table:: Platform-Specific Toolchains
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 17
     - score_toolchains_qnx
     - 0.0.2/0.5
     - TBD
     - YES
     - YES
     - QNX SDP toolchain including compiler, linker, image creation tools
   * - 18
     - score_toolchains_gcc
     - 0.4/0.5
     - TBD
     - YES
     - YES
     - GCC toolchain packages for various targets
   * - 19
     - score_toolchains_rust
     - Various
     - TBD
     - YES
     - YES
     - Rust toolchains for SCORE project

Static Analysis & Code Quality
===============================

C++ Static Analysis
-------------------

.. list-table:: C++ Analysis Tools
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 20
     - clang-tidy
     - 19.x
     - TBD
     - YES
     - YES
     - Static analysis for C++, used with Clang compiler
   * - 21
     - clang-analyzer
     - 19.x
     - TBD
     - YES
     - YES
     - Static analyzer from LLVM project

Rust Static Analysis
---------------------

.. list-table:: Rust Analysis Tools
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 22
     - clippy
     - 1.90.0+
     - HIGH
     - YES
     - YES
     - Rust linter for static code analysis (documented in score_tools)
   * - 23
     - rustfmt
     - 1.8.0+
     - HIGH
     - YES
     - YES
     - Rust code formatter (documented in score_tools, version derived from qualified compiler)
   * - 24
     - rust-analyzer
     - Latest
     - TBD
     - TBD
     - TBD
     - Rust language server for IDE support

Python Analysis
---------------

.. list-table:: Python Analysis Tools
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 25
     - ruff
     - Latest
     - TBD
     - YES
     - YES
     - Fast Python formatter and linter, replaces multiple tools
   * - 26
     - pyright
     - Latest
     - TBD
     - YES
     - YES
     - Python static type checker (99% test coverage)
   * - 27
     - pylint
     - Latest
     - TBD
     - YES
     - YES
     - Python code quality analysis (96% test coverage)
   * - 28
     - pytest
     - Latest
     - TBD
     - YES
     - YES
     - Python testing framework (97% test coverage)
   * - 29
     - pytest-cov
     - Latest
     - TBD
     - YES
     - YES
     - Python test coverage reporting

Other Formatters & Linters
---------------------------

.. list-table:: General Formatters and Linters
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 30
     - yamlfmt
     - Latest
     - TBD
     - TBD
     - TBD
     - YAML file formatter
   * - 31
     - actionlint
     - Latest
     - TBD
     - TBD
     - TBD
     - GitHub Actions workflow linter
   * - 32
     - starpls
     - Latest
     - TBD
     - TBD
     - TBD
     - Starlark (Bazel) language server
   * - 33
     - basedpyright
     - Latest
     - TBD
     - YES
     - YES
     - Alternative Python type checker

Testing Frameworks
==================

.. list-table:: Testing Tools
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 34
     - GoogleTest (gtest)
     - 1.15.0/1.17.0
     - LOW
     - YES
     - YES
     - C++ testing framework (documented in score_tools)
   * - 35
     - ITF
     - 0.1.0
     - LOW
     - YES
     - YES
     - Integration Testing Framework, pytest-based (documented in score_tools)
   * - 36
     - gcovr
     - Latest
     - TBD
     - YES
     - YES
     - Code coverage tool (uses gcov from GCC), part of GNU compiler collection

Documentation Tools
===================

.. list-table:: Documentation Generation Tools
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 37
     - Doc-as-Code
     - 2.0.2/2.2.0/2.3.3
     - LOW
     - YES
     - YES
     - S-CORE documentation generation tool (documented in score_tools)
   * - 38
     - Sphinx
     - Latest
     - TBD
     - YES
     - YES
     - Python documentation generator (underlying Doc-as-Code)
   * - 39
     - sphinx-needs
     - Latest
     - TBD
     - YES
     - YES
     - Requirements tracking extension for Sphinx
   * - 40
     - PlantUML
     - Latest
     - TBD
     - TBD
     - TBD
     - UML diagram generation
   * - 41
     - Graphviz
     - Latest
     - TBD
     - TBD
     - TBD
     - Graph visualization software
   * - 42
     - sphinxcontrib.plantuml
     - Latest
     - TBD
     - TBD
     - TBD
     - PlantUML integration for Sphinx

S-CORE Custom Tooling
=====================

.. list-table:: S-CORE Specific Tools
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 43
     - score_tooling
     - 1.0.2/1.0.4
     - TBD
     - YES
     - YES
     - Copyright checker, CLI helper, license checker
   * - 44
     - score_process
     - 1.4.2
     - TBD
     - YES
     - YES
     - Process description tools (ASPICE 4.0, ISO 26262, ISO 21434, ISO PAS 8926)
   * - 45
     - bazel-tools-cc
     - Latest
     - TBD
     - YES
     - YES
     - Clang-tidy based static code checker for Bazel

Version Control & CI/CD
========================

.. list-table:: Version Control and CI/CD Tools
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 46
     - Git
     - 2.x
     - TBD
     - YES
     - YES
     - Version control system
   * - 47
     - GitHub
     - Cloud
     - TBD
     - YES
     - YES
     - Code hosting and collaboration platform
   * - 48
     - GitHub Actions
     - Cloud
     - TBD
     - YES
     - YES
     - CI/CD automation platform
   * - 49
     - gitlint
     - 0.19.1
     - TBD
     - TBD
     - TBD
     - Commit message linting (Docker: jorisroovers/gitlint)

License & Security
==================

.. list-table:: License and Security Analysis Tools
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 50
     - Eclipse Dash
     - Latest
     - TBD
     - TBD
     - YES
     - License analysis tool
   * - 51
     - REUSE
     - Latest
     - TBD
     - TBD
     - YES
     - License compliance checking

Libraries & Dependencies
========================

C++ Libraries
-------------

.. list-table:: C++ Library Dependencies
   :header-rows: 1
   :widths: 5 20 15 50

   * - ID
     - Library Name
     - Version
     - Purpose
   * - 52
     - Boost
     - 1.87.0
     - C++ libraries (specifically boost.program_options)
   * - 53
     - nlohmann_json
     - Latest
     - JSON library for C++
   * - 54
     - protobuf
     - 29.0
     - Protocol buffers
   * - 55
     - abseil-cpp
     - 20240116.1
     - Abseil C++ common libraries
   * - 56
     - jsoncpp
     - 1.9.5
     - JSON library for C++

Rust Libraries
--------------

.. list-table:: Rust Library Dependencies (via crate_index)
   :header-rows: 1
   :widths: 5 20 15 50

   * - ID
     - Crate Name
     - Version
     - Purpose
   * - 57a
     - futures
     - 0.3.31
     - Asynchronous programming
   * - 57b
     - libc
     - 0.2.155
     - Raw FFI bindings for platform APIs
   * - 57c
     - clap
     - 4.5.4
     - Command line argument parser

Requirements & Traceability
----------------------------

.. list-table:: Requirements Management Tools
   :header-rows: 1
   :widths: 5 20 15 50

   * - ID
     - Tool Name
     - Version
     - Purpose
   * - 58
     - TRLC
     - 2.0.2 (commit 650b51a)
     - BMW Requirements Traceability Language and Compiler
   * - 59
     - LOBSTER
     - Latest
     - Requirements traceability and documentation tool (via custom extension)

Container & Development Environment
===================================

.. list-table:: Container and Development Tools
   :header-rows: 1
   :widths: 5 15 10 10 10 10 40

   * - ID
     - Tool Name
     - Version
     - TCL
     - Safety
     - Security
     - Notes
   * - 60
     - Docker
     - Latest
     - TBD
     - TBD
     - YES
     - Container platform (used in devcontainer)
   * - 61
     - devcontainer
     - Custom
     - TBD
     - TBD
     - TBD
     - VS Code development container configuration
   * - 62
     - QEMU
     - Latest
     - TBD
     - YES
     - YES
     - Emulator for integration testing (qemu-system-aarch64)
   * - 63
     - SSH tools
     - Latest
     - TBD
     - TBD
     - YES
     - Remote connection (sshpass, SSH client)

Additional System Tools
=======================

.. list-table:: System Utilities
   :header-rows: 1
   :widths: 5 20 15 50

   * - ID
     - Tool Name
     - Version
     - Purpose
   * - 64
     - curl
     - Latest
     - HTTP client for downloading dependencies
   * - 65
     - protoc
     - Latest
     - Protocol buffer compiler
   * - 66
     - dot
     - Latest
     - Graphviz command-line tool
   * - 67
     - jq
     - Latest
     - JSON processor
   * - 68
     - yq
     - Latest
     - YAML processor
   * - 69
     - tar
     - Latest
     - Archive utility

Platform & Target Support
=========================

.. list-table:: Platform and OS Support
   :header-rows: 1
   :widths: 5 20 15 50

   * - ID
     - Platform/Tool
     - Version
     - Purpose
   * - 70
     - QNX 8.x SDP
     - 8.x
     - Real-time operating system and development platform
   * - 71
     - score_bazel_platforms
     - Latest
     - Platform definitions (x86_64-qnx, x86_64-linux, etc.)
   * - 72
     - Vulkan
     - Latest
     - Graphics and compute API
   * - 73
     - ISP Driver
     - Custom
     - Image sensor pre-processing

Language Servers & IDE Support
===============================

.. list-table:: IDE Language Servers
   :header-rows: 1
   :widths: 5 20 15 50

   * - ID
     - Language Server
     - Version
     - Purpose
   * - 74
     - clangd
     - Latest
     - C/C++ language server
   * - 75
     - rust-analyzer
     - Latest
     - Rust language server
   * - 76
     - starpls
     - Latest
     - Starlark (Bazel) language server

S-CORE Module Repositories
===========================

The following modules from the eclipse-score organization are part of the ecosystem:

.. list-table:: S-CORE Software Modules
   :header-rows: 1
   :widths: 30 70

   * - Repository
     - Description
   * - score
     - Main platform repository
   * - process_description
     - Process description (ASPICE, ISO standards)
   * - score_baselibs
     - Base libraries including common functionality (C++)
   * - baselibs_rust
     - Rust base libraries
   * - score_communication
     - Communication module (LoLa) (C++)
   * - persistency
     - Persistency framework (Rust)
   * - logging
     - Logging daemon (C++)
   * - orchestrator
     - Orchestration framework (Rust)
   * - kyron
     - Safe async runtime for Rust
   * - lifecycle
     - Lifecycle management
   * - scrample
     - Example component (C++)
   * - docs-as-code
     - Documentation tooling (Python)
   * - tooling
     - S-CORE development tooling (Python)
   * - itf
     - Integration Testing Framework (Python)
   * - bazel_registry
     - Bazel modules registry
   * - bazel_cpp_toolchains
     - C/C++ toolchain configurations
   * - toolchains_qnx
     - QNX toolchain
   * - toolchains_gcc
     - GCC toolchain
   * - toolchains_rust
     - Rust toolchain
   * - bazel_platforms
     - Platform definitions
   * - bazel-tools-cc
     - C/C++ static analysis tools
   * - module_template
     - C++ & Rust Bazel template repository
   * - reference_integration
     - Integration repository
   * - devcontainer
     - Common devcontainer for S-CORE
   * - cicd-workflows
     - Reusable GitHub Actions workflows
   * - nlohmann_json
     - Nlohmann JSON library
   * - ferrocene_toolchain_builder
     - Builder for Ferrocene artifacts
   * - inc_time
     - Time synchronization module (incubation)
   * - inc_someip_gateway
     - SOME/IP gateway (incubation)
   * - inc_security_crypto
     - Security & Cryptography (incubation)
   * - inc_score_codegen
     - DSL/code generation (incubation)
   * - inc_os_autosd
     - AutoSD Development Platform (incubation)
   * - .eclipsefdn
     - Eclipse Foundation configurations

Summary Statistics
==================

Tool Count Overview
-------------------

- **Total Tools Identified**: 77+ distinct tools
- **Tools with Documented TCL**: 7 tools

  - **HIGH TCL**: clippy, rustfmt
  - **LOW TCL**: Bazel, gtest, ITF, Doc-as-Code

- **Safety-Affected Tools**: Majority of development, testing, and compilation tools
- **Security-Affected Tools**: Majority of development, testing, and compilation tools
- **S-CORE Repositories**: 68+ repositories in eclipse-score GitHub organization

Tool Classification by Category
--------------------------------

.. list-table:: Category Summary
   :header-rows: 1
   :widths: 50 50

   * - Category
     - Count
   * - Build System & Package Management
     - 10
   * - Compilers & Toolchains
     - 9
   * - Static Analysis & Code Quality
     - 14
   * - Testing Frameworks
     - 3
   * - Documentation Tools
     - 6
   * - S-CORE Custom Tooling
     - 3
   * - Version Control & CI/CD
     - 4
   * - License & Security
     - 2
   * - Libraries (C++/Rust)
     - 10
   * - Requirements & Traceability
     - 2
   * - Container & Development
     - 4
   * - System Utilities
     - 6
   * - Platform Support
     - 4
   * - Language Servers
     - 3

Recommended Evaluation Priority
================================

Priority 1: Critical Safety-Relevant Tools
-------------------------------------------

These tools directly impact the correctness and safety of generated code:

1. **Compilers**

   - GCC (Host C++ compiler)
   - QCC (Target C++ compiler - qualifiable)
   - Ferrocene (Target Rust compiler - qualified)
   - LLVM/Clang

2. **Build System**

   - Bazel (already documented, TCL: LOW)

Priority 2: Code Quality Gates
-------------------------------

These tools ensure code quality before integration:

3. **Static Analysis**

   - clang-tidy (C++ static analysis)
   - clippy (Rust linter, TCL: HIGH)
   - rustfmt (Rust formatter, TCL: HIGH)
   - ruff (Python linter/formatter)
   - pyright (Python type checker)

Priority 3: Verification Tools
-------------------------------

These tools verify correctness through testing:

4. **Testing Frameworks**

   - GoogleTest/gtest (C++ testing, TCL: LOW)
   - ITF (Integration testing, TCL: LOW)
   - pytest (Python testing)
   - gcovr (Code coverage)

Priority 4: Traceability & Documentation
-----------------------------------------

These tools maintain traceability and documentation:

5. **Documentation & Requirements**

   - Doc-as-Code (Documentation generation, TCL: LOW)
   - TRLC (Requirements traceability)
   - LOBSTER (Traceability tool)
   - Sphinx + sphinx-needs

Priority 5: Supporting Infrastructure
--------------------------------------

All other tools supporting the development process:

6. **Version Control, CI/CD, Utilities**

   - Git, GitHub, GitHub Actions
   - Docker, devcontainer
   - System utilities (curl, protoc, etc.)

Next Steps
==========

For each tool identified in this document, the following activities are recommended:

1. **Tool Classification**

   - Determine Tool Impact
   - Determine Tool Error Detection
   - Calculate Tool Confidence Level

2. **Safety Evaluation**

   - Complete malfunction analysis
   - Identify impact on safety
   - Define safety measures
   - Document in Tool Verification Report

3. **Security Evaluation**

   - Identify security threats
   - Assess impact on security
   - Define security measures

4. **Qualification Strategy**

   - For TCL 2/3: Increased confidence through use
   - For TCL 2/3: Tool qualification
   - Document in Tool Verification Report per :need:`gd_temp__tool_management_verif_rpt_template`

5. **Documentation**

   - Create/update Tool Verification Reports
   - Maintain tool version tracking
   - Link to configuration management

References
==========

- S-CORE Tool Management Plan: :need:`doc__platform_tool_management_plan`
- Tool Verification Report Template: :need:`gd_temp__tool_management_verif_rpt_template`
- Tool Creation Review Checklist: :need:`gd_chklst__tool_cr_review`
- Tool Process Concept: :need:`doc_concept__tool_process`
- S-CORE GitHub Organization: https://github.com/eclipse-score
- S-CORE Bazel Registry: https://github.com/eclipse-score/bazel_registry
- S-CORE Documentation: https://eclipse-score.github.io/score

Document History
================

.. list-table:: Document Revision History
   :header-rows: 1
   :widths: 15 15 70

   * - Version
     - Date
     - Changes
   * - 1.0
     - 2026-01-26
     - Initial comprehensive tool inventory for safety evaluation

----

*This document was generated based on analysis of the Eclipse SCORE project repositories as of January 26, 2026.*

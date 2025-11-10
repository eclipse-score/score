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

.. doc_tool:: Bazel
   :id: doc_tool__bazel
   :status: draft
   :version: 8.3.0
   :tcl: LOW
   :safety_affected: YES
   :security_affected: YES
   :realizes: PROCESS_wp__tool_verification_report
   :tags: tool_management


Bazel Verification Report
=========================

Introduction
------------

Scope and purpose
~~~~~~~~~~~~~~~~~
Bazel is a fast, scalable, multi-language build system developed by Google.
It is used to automate the building and testing of software.

Inputs and outputs
~~~~~~~~~~~~~~~~~~
Inputs:
| - BUILD files and MODULE configuration
| - Source code and dependencies
| - Bazel rules and macros

Outputs:
| - Build log
| - Call tree
| - Call tools via Call tree
| - Built output via Call tools

.. figure:: _assets/bazel.drawio.svg
  :width: 100%
  :align: center
  :alt: Bazel overview

Available information
~~~~~~~~~~~~~~~~~~~~~
Bazel is open-source. Information about key features and functionality
can be found in official documentation:

- Official documentation: https://bazel.build
- GitHub repository: https://github.com/bazelbuild/bazel
- Version: 8.3.0 [1]_


Usage constraints:

- Requires specific directory structure and configuration files
- Remote caching and execution require additional setup and infrastructure


Installation and integration
----------------------------

Installation
~~~~~~~~~~~~

Recommended way of bazel usage in S-Core project is via devcontainers.
Corresponding devcontainers for each module and platform as all provided
in corresponding repositories.

E.g.
https://github.com/eclipse-score/score/tree/main/.devcontainer

The concrete version of bazel determined at runtime from .bazelversion file in project root folder.



Integration
~~~~~~~~~~~
Bazel is orchestrator that works on upper level. Some additional configuration
may require when using cache.

Environment
~~~~~~~~~~~
- Linux
- Windows

Evaluation
----------

.. list-table:: Safety evaluation
   :header-rows: 1
   :widths: 1 2 8 2 6 4 2 2

   * - Malfunction identification
     - Use case Description
     - Malfunctions
     - Impact on safety?
     - Impact safety measures available?
     - Impact safety detection sufficient?
     - Further additional safety measure required?
     - Confidence (automatic calculation)
   * - 1
     - Dependency management
     - | Incorrect dependency graph
       |
       | Bazel builds with wrong dependency order, causing missing or outdated binaries in the final executable
     - yes
     - /
     - no
     - yes(qualification)
     - low
   * - 2
     - Dependency management
     - | Cyclic dependency introduced
       |
       | Bazel fails to resolve dependencies and stops build, leaving safety-critical components unbuilt
     - yes
     - /
     - no
     - yes(qualification)
     - low
   * - 3
     - Dependency management
     - | Dependency not updated
       |
       | Bazel fails to update relevant dependency, keeping old code even though it should update it
     - yes
     - /
     - no
     - yes(qualification)
     - low
   * - 4
     - Build caching
     - | Missed rebuild due to wrong change detection
       |
       | Bazel incorrectly assumes no changes and skips rebuilding, leaving outdated code in safety-critical modules
     - yes
     - /
     - no
     - yes(qualification)
     - low
   * - 5
     - Build caching
     - | Incorrect cache hit
       |
       | Bazel retrieves wrong cached artifact, compiling outdated or incorrect code
     - yes
     - /
     - no
     - yes(qualification)
     - low
   * - 6
     - Build caching
     - | Partial rebuild skips safety-critical module
       |
       | Bazel rebuilds only part of the system, omitting safety-critical components
     - yes
     - /
     - no
     - yes(qualification)
     - low
   * - 7
     - WORKSPACE / BUILD Config
     - | Misconfigured flags
       |
       | Bazel applies wrong compiler flags, disabling safety mechanisms and introducing unsafe behavior
     - yes
     - /
     - no
     - yes(qualification)
     - low
   * - 8
     - WORKSPACE / BUILD Config
     - | Missing dependency
       |
       | Bazel fails to include required dependency, causing incomplete build and missing safety-critical functionality
     - yes
     - /
     - no
     - yes(qualification)
     - low
   * - 9
     - WORKSPACE / BUILD Config
     - | Wrong optimization level
       |
       | Bazel applies unsafe optimization level, breaking timing assumptions and potentially violating safety requirements
     - yes
     - /
     - no
     - yes(qualification)
     - low
   * - 10
     - Custom rules
     - | Bug in custom rule
       |
       | Bazel executes incorrect build steps due to faulty custom rule, producing unsafe binaries
     - yes
     - /
     - no
     - yes(qualification)
     - low
   * - 11
     - Custom rules
     - | Unsafe script logic
       |
       | Bazel skips critical checks because of unsafe Starlark logic, leading to incomplete safety validation
     - yes
     - /
     - no
     - yes(qualification)
     - low
   * - 12
     - Custom rules
     - | Version incompatibility
       |
       | Bazel fails or produces incorrect output due to incompatible Starlark rule versions
     - yes
     - /
     - no
     - yes(qualification)
     - low


.. list-table:: Bazel security evaluation
   :header-rows: 1

   * - Use case Identification
     - Use case Description
     - Threats
     - Impact on security?
     - Impact security measures available?
     - Impact security detection sufficient?
   * - 1
     - TBD
     - TBD
     - TBD
     - TBD
     - TBD

Result
~~~~~~
Tool Qualification Required


Tool Qualification
------------------
Based on method: Validation of the software tool

.. [1] The tool version mentioned in this document is preliminary.
       It is subject to change and will be updated in future.

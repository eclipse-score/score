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
   :realizes: wp__tool_verification_report
   :tags: tool_management


Bazel Verification Report
=========================

Introduction
------------

Scope and purpose
~~~~~~~~~~~~~~~~~
Bazel is a fast, scalable, multi-language build system developed by Google.
It is used to automate the build, integration and testing of software.

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

The preferred way to use Bazel in the S-CORE project is through Bazelisk and the .bazelversion file.
The .bazelversion file is typically located in the project root directory.
When you run any Bazel command, Bazelisk reads the Bazel version specified in .bazelversion and
automatically uses that version for all calls.

Example
https://github.com/eclipse-score/score/tree/main/.devcontainer


Integration
~~~~~~~~~~~
Bazel acts as a high-level build orchestrator.
When using caching mechanisms, additional configuration may be required.

Environment
~~~~~~~~~~~
- Linux
- Windows

Safety evaluation
-----------------

This section outlines the safety evaluation of Bazel for its use within the S-CORE project.

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
     - | Bazel fails to fetch external dependencies
       |
       | Bazel is unable to download or resolve required external dependencies during the build. This halts the build and prevents critical components from being compiled/integrated/tested/etc.
     - yes
     - | Check build output (implicit)
       |
       | This causes build failure and missing output which is detected by Bazel itself.
     - yes
     - no
     - high
   * - 2
     - Dependency management
     - | Bazel fetched redundant external dependencies
       |
       | Bazel downloads unnecessary external dependencies that are not referenced by any target. This increases build time and resource usage without contributing to the final output.
     - | no
       |
       | This is a performance issue, not a safety issue.
     - no
     - yes
     - no
     - high
   * - 3
     - Dependency management
     - | Bazel fetched wrong external dependencies (wrong hit)
       |
       | Bazel retrieves incorrect versions or mismatched external dependencies due to resolution errors. This can lead to inconsistent builds and potential incompatibility in safety-critical modules.
     - yes
     - no
     - no
     - yes(qualification)
     - low
   * - 4
     - Dependency management
     - | Bazel corrupts external dependencies while fetching
       |
       | During download or extraction, Bazel corrupts external dependency files, resulting in broken libraries or tools. This causes build failures.
     - yes
     - | Check build output (implicit)
       |
       | This causes build failure and missing output which is detected by Bazel itself.
     - yes
     - no
     - high
   * - 5
     - Call tree computation
     - | Bazel fails to build call tree
       |
       | Bazel cannot construct the dependency graph (call tree) for the build, leading to incomplete or aborted build processes.
     - yes
     - | Check build output
       |
       | This causes build failure and missing output which is detected by Bazel itself
     - yes
     - no
     - high
   * - 6
     - Call tree computation
     - | Bazel skips relevant target in call tree (missing caching hit or dependency miscalculation)
       |
       | Bazel omits a required target from the build graph due to incorrect cache hits or dependency resolution errors. This results in missing artifacts and incomplete builds.
     - yes
     - no
     - no
     - yes(qualification)
     - low
   * - 7
     - Call tree computation
     - | Bazel adds redundant target in call tree (wrong caching hit or dependency miscalculation)
       |
       | Bazel includes unnecessary targets in the build graph, causing redundant compilation steps. This increases build time and resource consumption without affecting the final output.
     - | no
       |
       | This is a performance issue, not a safety issue.
     - yes
     - yes
     - no
     - high
   * - 8
     - Call tools
     - | Bazel fails to call a tool
       |
       | Bazel does not invoke a required tool during the build process, leading to incomplete or invalid artifacts. This disrupts the expected workflow and may block downstream steps.
     - yes
     - | Check build output
       |
       | This causes build failure and missing output which is detected by Bazel itself.
     - yes
     - no
     - high
   * - 9
     - Call tools
     - | Bazel calls wrong tool
       |
       | Bazel invokes an incorrect tool instead of the intended one, producing invalid outputs or causing build errors. This can compromise consistency and reliability of the build.
     - yes
     - no
     - no
     - yes(qualification)
     - low
   * - 10
     - Call tools
     - | Bazel fails to pass arguments to the tool
       |
       | Bazel omits necessary arguments when invoking a tool, resulting in incorrect execution or failure of the tool. This impacts artifact generation and overall build correctness.
     - yes
     - no
     - no
     - yes(qualification)
     - low
   * - 11
     - Call tools
     - | Bazel wrongly interprets return code from tool
       |
       | Bazel misinterprets the return code from a tool, treating a failure as a success or vice versa. This can result in undetected build errors or invalid artifacts being accepted as correct.
     - yes
     - no
     - no
     - yes(qualification)
     - low
   * - 12
     - Call tools
     - | Bazel passes wrong argument to the tool
       |
       | Bazel provides incorrect arguments to a tool, causing misbehavior or invalid outputs. This can lead to corrupted artifacts or failed verification steps.
     - yes
     - no
     - no
     - yes(qualification)
     - low
   * - 13
     - Save output
     - | Bazel corrupts final output artifact
       |
       | Bazel produces a damaged or incomplete final artifact due to errors.
     - yes
     - no
     - no
     - yes(qualification)
     - low
   * - 14
     - Save output
     - | Bazel saves in wrong place
       |
       | Bazel stores the generated artifact in an incorrect location, breaking expected directory structures.
     - yes
     - no
     - no
     - yes(qualification)
     - low

Security evaluation
-------------------
This section outlines the security evaluation of Bazel for its use within the S-CORE project.

.. list-table:: Security evaluation
   :header-rows: 1

   * - Threat identification
     - Use case description
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
------
Bazel requires qualification for use in safety-related software development according to ISO 26262.


**Tool Qualification**
----------------------
Based on method: validation of the software tool.

Requirements and testing aspects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tool requirements are derived from official documentation: https://bazel.build/

Bazel is an open-source tool and does not provide formal, vendor-defined requirements.
Therefore, the tooling team is responsible for identifying the specific Bazel functionality
used in the project. Based on this, requirements for the utilized features must be derived from
the available documentation and Bazel validated against defined requirements.

.. [1] The tool version mentioned in this document is preliminary.
       It is subject to change and will be updated in future.

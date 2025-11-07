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

.. list-table:: Bazel safety evaluation
   :header-rows: 1
   :widths: 1 2 8 2 6 4 2 2

   * - Use case Identification
     - Use case Description
     - Malfunctions
     - Impact on safety?
     - Impact safety measures available?
     - Impact safety detection sufficient?
     - Further additional safety measure required?
     - Confidence (automatic calculation)
   * - 1
     - Bazel calls other tools
     - Bazel fails to interpreted attributes of the rule call the tool not as defined by rule.
     - yes
     - Check the parameters passed to the tool
     - HIGH
     - no
     - high
   * - 2
     - Bazel calls other tools
     - Bazel fails to set correct (provided) tag string parameter. Tags may trigger certain actions. If tags were handled wrongly, this will lead to missing expected outputs.
     - yes
     - Check the existence of the output
     - HIGH
     - no
     - high
   * - 3
     - Bazel calls other tools
     - Bazel BwoB downloaded some output artifacts that are not relevant for current (re)build.
     - no
     - N/A
     - HIGH
     - no
     - high
   * - 4
     - Bazel calls other tools
     - Bazel BwoB download wrong output artifact, so build was (re)done for outdated or wrong outputs.
     - yes
     - Check results of remote cache fetching (BwtB)
     - HIGH
     - no
     - high
   * - 5
     - Bazel calls other tools
     - Bazel BwoB fails to download relevant output artifacts.
     - no
     - N/A
     - HIGH
     - no
     - high
   * - 6
     - Bazel calls other tools
     - Relevant artifacts from remote cache was not downloaded at all.
     - no
     - N/A
     - HIGH
     - no
     - high
   * - 7
     - Bazel calls other tools
     - Downloaded artifacts are corrupted.
     - yes
     - Check results of remote cache fetching (BwtB)
     - HIGH
     - no
     - high
   * - 8
     - Bazel calls other tools
     - Call of build-in bazel function caused wrong call of tool. Covers scenarios like wrong configuration, wrong property, wrong transition.
     - yes
     - Check parameters passed to the tool; Review target dependencies
     - HIGH
     - no
     - high
   * - 9
     - Bazel calls other tools
     - Wrong list of items was used due to failure of glob function.
     - yes
     - Qualification of Bazel
     - LOW
     - no
     - low
   * - 10
     - Bazel calls other tools
     - Hashes from remote cache do not match workspace, although files are the same.
     - no
     - N/A
     - HIGH
     - no
     - high
   * - 11
     - Bazel calls other tools
     - Hashes match although files differ.
     - yes
     - Qualification of Bazel
     - LOW
     - no
     - low
   * - 12
     - Bazel calls other tools
     - Genrule wrongly called or Bazel fails to determine rebuild need.
     - yes
     - Usage of genrule() is forbidden
     - HIGH
     - yes
     - high
   * - 13
     - Bazel calls other tools
     - Wrong configuration applied without explicit statement.
     - yes
     - Check parameters passed to the tool
     - HIGH
     - no
     - high
   * - 14
     - Bazel calls other tools
     - Correct context incorrectly interpreted by Bazel.
     - yes
     - Check parameters passed to the tool
     - HIGH
     - no
     - high
   * - 15
     - Bazel calls other tools
     - Command line options wrongly passed to the tool.
     - yes
     - Check parameters passed to the tool
     - HIGH
     - no
     - high
   * - 16
     - Bazel calls other tools
     - Bazel fails to pass parameter to the calling tool.
     - yes
     - Check parameters passed to the tool
     - HIGH
     - no
     - high
   * - 17
     - Bazel calls other tools
     - Build failed but Bazel reported success.
     - yes
     - Check output existence; Check parameters passed to the tool
     - HIGH
     - yes
     - high
   * - 18
     - Bazel calls other tools
     - Bazel fails to produce a build.
     - yes
     - Check output existence
     - HIGH
     - yes
     - high
   * - 19
     - Bazel calls other tools
     - Unnecessary steps triggered during build.
     - no
     - N/A
     - HIGH
     - no
     - high
   * - 20
     - Bazel calls other tools
     - Tool called more than once.
     - no
     - N/A
     - HIGH
     - no
     - high
   * - 21
     - Bazel calls other tools
     - Tool specified by build rule not called.
     - yes
     - Check if tool is called by Bazel
     - HIGH
     - yes
     - high
   * - 22
     - Bazel calls other tools
     - Wrong tool called (e.g. Python2 instead of Python3).
     - yes
     - Check that Bazel uses correct tools
     - HIGH
     - yes
     - high
   * - 23
     - Bazel calls other tools
     - Wrong version of tool invoked.
     - yes
     - Check version of tool invoked by Bazel
     - HIGH
     - yes
     - high
   * - 24
     - Bazel calls other tools
     - Input changed but Bazel did not trigger rebuild.
     - yes
     - Qualification of Bazel
     - LOW
     - yes
     - low
   * - 25
     - Bazel calls other tools
     - Internal cache hash incomplete.
     - yes
     - Qualification of Bazel
     - LOW
     - yes
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

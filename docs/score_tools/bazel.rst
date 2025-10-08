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
   :version: v8.3.0
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
Bazel is a fast, scalable, multi-language build system developed by Google. It is used to automate the building and testing of software, particularly in large-scale projects. In the context of safety automotive software development, Bazel supports reproducible builds, dependency tracking, and hermetic execution, which are critical for ensuring traceability and consistency in safety-critical environments.

Inputs and outputs
~~~~~~~~~~~~~~~~~~
Inputs:
- BUILD files and MODULE configuration
- Source code and dependencies
- Bazel rules and macros

Outputs:
- Call tree
- Build log
- Built output via call tree

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


Usage constraints:

- Requires specific directory structure and configuration files
- Remote caching and execution require additional setup and infrastructure


Installation and integration
----------------------------

Installation
~~~~~~~~~~~~

Recommended way of bazel usage in s-core project is via devcontainers.
Corresponding devcontainers for each module and platform as all provided
in corresponding repositories.

E.g.
https://github.com/eclipse-score/score/tree/main/.devcontainer

Integration
~~~~~~~~~~~
Bazel is orchestrator that works on upper level. Some additional configuration m
ay require when using cache.

Environment
~~~~~~~~~~~
- Linux


Evaluation
----------

.. list-table:: Bazel evaluation
   :header-rows: 1

   * - Use case Identification
     - Use case Description
     - Malfunctions
     - Impact on safety?
     - Impact safety measures available?
     - Impact safety detection sufficient?
     - Threats
     - Impact on security?
     - Impact security measures available?
     - Impact security detection sufficient?
     - Further additional safety measure required?
     - Confidence (automatic calculation)
   * - 1
     - Fetch build dependencies
     - Incorrect build due to misconfigured rules or dependencies
     - yes
     - Code reviews, CI validation
     - yes
     - Tampering with build rules or remote cache
     - yes
     - Access control, sandboxing
     - yes
     - Hash verification of artifacts
     - low
   * - 2
     - To-Do
     - To-Do
     - yes
     - To-Do
     - yes
     - To-Do
     - yes
     - To-Do
     - yes
     - To-Do
     - low

Result
~~~~~~
Tool Qualification Required


Tool Qualification
------------------
Based on method: Validation of the software tool

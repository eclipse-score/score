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

.. doc_tool:: clang-tidy
   :id: doc_tool__clang_tidy
   :status: evaluated
   :tool_version: 19.1.1
   :tcl: LOW
   :safety_affected: YES
   :security_affected: YES
   :realizes: wp__tool_verification_report[version==1]
   :tags: tool_management, tools_static_analysis_code_quality

Clang-Tidy Verification Report
==============================

Introduction
------------
Scope and purpose
~~~~~~~~~~~~~~~~~
Clang-Tidy is an open-source static analysis and linting tool for C/C++ code. It is used to detect code quality issues, bugs, and enforce coding standards during development.
In the context of the S-CORE project, Clang-Tidy is used as a development tool to support early detection of code issues. It is not used for production builds or as a safety measure for safety-related software components.
Therefore, the safety and security impact of Clang-Tidy is "NO".

Inputs and outputs
~~~~~~~~~~~~~~~~~~
| Inputs: Software sources (C/C++), Configuration files (e.g., .clang-tidy-\*)
| Outputs: Analysis report, Logs

.. figure:: _assets/clang-tidy.drawio.svg
  :width: 80%
  :align: center
  :alt: Clang-Tidy analysis

  Clang-Tidy overview

Available information
~~~~~~~~~~~~~~~~~~~~~

- Version: 19.1.1 [1]_
- Official repository: https://github.com/llvm/llvm-project
- Official documentation: https://clang.llvm.org/extra/clang-tidy
- Bazel Aspect Rules Lint: https://github.com/aspect-build/rules_lint
- LLVM Releases: https://releases.llvm.org

Installation and integration
----------------------------

Installation
~~~~~~~~~~~~

To add the clang-tidy (and other llvm-toolchain parts) Bazel dependency to your project or module, include the following line in your MODULE.bazel file:

.. code-block:: python

  bazel_dep(name = "toolchains_llvm", version = "1.4.0", dev_dependency = True)

| Bazel will fetch from the Bazel Central Registry (BCR): https://registry.bazel.build/modules/toolchains_llvm

Integration Approaches
~~~~~~~~~~~~~~~~~~~~~~

Different projects may integrate clang-tidy in different ways.
There are currently 2 approaches observed in the S-CORE project:

- | Macro-Based
  | In the project a custom macro/target defiened (e.g., `clang_tidy_extra_checks`).
  | Clang-tidy called as separate target during build/test process(e.g., via `bazel` call)

- | Aspect-Based
  | Clang-tidy integrated via Bazel aspects (e.g., `@aspect_rules_lint`).
  | Called autmatically for all targets releted to clang-tidy aspect (e.g. `bazel test --congfig=clang-tidy //target_name`)

Environment
~~~~~~~~~~~
Requires Linux and Bazel build environment.

Safety evaluation
-----------------
This section outlines the safety evaluation of Clang-Tidy for its use within the S-CORE project.

.. list-table:: Clang-Tidy safety evaluation
   :header-rows: 1
   :widths: 1 2 8 2 6 4 2 2

   * - Malfunction identification
     - Use case description
     - Malfunctions
     - Impact on safety?
     - Impact safety measures available?
     - Impact safety detection sufficient?
     - Further additional safety measure required?
     - Confidence (automatic calculation)
   * - 1
     - Static code analysis
     - | False negative (missed issue)
       | Clang-Tidy fails to report a real code issue.
     - yes
     - no
     - no
     - yes (qualification)
     - low
   * - 2
     - Static code analysis
     - | False positive (spurious warning)
       | Clang-Tidy reports a non-existent issue.
     - no
     - no
     - yes
     - no
     - high
   * - 3
     - Static code analysis
     - | Wrong analysis report
       | Clang-Tidy fails to report all detected issues or reports them incorrectly.
     - no
     - no
     - yes
     - no
     - high

Security evaluation
-------------------
This section outlines the security evaluation of Clang-Tidy for its use within the S-CORE project.

.. list-table:: Clang-Tidy security evaluation
   :header-rows: 1

   * - Threat identification
     - Use case description
     - Threats
     - Impact on security?
     - Impact security measures available?
     - Impact security detection sufficient?
     - Further additional security measure required?
   * - 1
     - TBD
     - TBD
     - TBD
     - TBD
     - TBD
     - TBD

Result
~~~~~~
Clang-Tidy requires qualification for use in safety-related software development according to ISO 26262.


**Tool Qualification**
-------------------------------------------
Based on method: validation of the software tool.

Requirements and testing aspects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clang-Tidy is an open-source tool and does not provide formal, vendor-defined requirements.
Therefore, the testing team is responsible for identifying the specific Clang-Tidy checks and features
used in the project. Based on this, requirements for the utilized features must be derived from
the available documentation and Clang-Tidy validated against defined requirements.


.. [1] The tool version mentioned in this document is preliminary.
       It is subject to change and will be updated in future.

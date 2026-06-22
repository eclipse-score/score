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

.. doc_tool:: clang-format
   :id: doc_tool__clang_format
   :status: evaluated
   :tool_version: 19.1.1
   :tcl: HIGH
   :safety_affected: YES
   :security_affected: YES
   :realizes: wp__tool_verification_report[version==1]
   :tags: tool_management, tools_static_analysis_code_quality

Clang-Format Verification Report
================================

Introduction
------------
Scope and purpose
~~~~~~~~~~~~~~~~~
Clang-Format is an open-source code formatting tool for C/C++ and other languages. It is used to automatically format source code according to defined style rules, improving code readability and consistency.
In the S-CORE project, Clang-Format is used as a development tool to enforce coding style. It does not analyze code correctness or detect bugs.

Inputs and outputs
~~~~~~~~~~~~~~~~~~
| Inputs: Software sources (C/C++), Configuration files (e.g., .clang-format)
| Outputs: Formatted source code, Logs

.. figure:: _assets/clangformat.drawio.svg
  :width: 100%
  :align: center
  :alt: Clang-Format overview

  Clang-Format overview

Available information
~~~~~~~~~~~~~~~~~~~~~
- Version: 19.1.1
- Official repository: https://github.com/llvm/llvm-project
- Official documentation: https://clang.llvm.org/docs/ClangFormat.html
- LLVM Releases: https://releases.llvm.org

Installation and integration
----------------------------
Installation
~~~~~~~~~~~~
To add the clang-format (and other llvm-toolchain parts) Bazel dependency to your project or module, include the following line in your MODULE.bazel file:

.. code-block:: python

  bazel_dep(name = "toolchains_llvm", version = "1.4.0", dev_dependency = True)

Bazel will fetch from the Bazel Central Registry (BCR): https://registry.bazel.build/modules/toolchains_llvm

Integration
~~~~~~~~~~~
Currently, S-CORE modules use clang-format via aspects integration.
This allows to call clang-format locally by developers and as part of the build process in the similar way:

.. code-block:: bash

   bazel build --config=clang_format //path/to:target



Environment
~~~~~~~~~~~
Requires Linux and Bazel build environment.

Safety evaluation
-----------------
This section outlines the safety evaluation of Clang-Format for its use within the S-CORE project.

.. list-table:: Clang-Format safety evaluation
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
     - Code formatting
     - | Incorrect formatting (style not applied as intended)
     - no
     - no
     - yes
     - no
     - high
   * - 2
     - Code formatting
     - | Formatting corrupts code
     - yes
     - | (implicit) Compile source code after formatting to detect issues
     - yes
     - no
     - high

Security evaluation
-------------------
This section outlines the security evaluation of Clang-Format for its use within the S-CORE project.

.. list-table:: Clang-Format security evaluation
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
Clang-Format does not require qualification for use in safety-related software development according to ISO 26262.

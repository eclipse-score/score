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

.. doc_tool:: gcc
   :id: doc_tool__gcc
   :status: draft
   :version: 12.x
   :tcl: HIGH
   :safety_affected: NO
   :security_affected: NO
   :realizes: wp__tool_verification_report
   :tags: tool_management, tools_compiler

GCC Compiler Verification Report
================================

Introduction
------------
Scope and purpose
~~~~~~~~~~~~~~~~~
GCC is open-source C/C++ compiler. It is widely used in the software development industry for compiling C and C++ code.

In the context of the S-CORE project, GCC is used as a development tool to compile software components during the development phase. However, it is not used for production builds of safety-related software components.

Therefore, the safety and security impact of GCC is "NO".


Inputs and outputs
~~~~~~~~~~~~~~~~~~
| Inputs: Software sources (C++), configuration files, dependencies
| Outputs: Object files, binaries, build logs, coverage data

.. figure:: _assets/gcc.drawio.svg
  :width: 80%
  :align: center
  :alt: GCC build

.. figure:: _assets/gcc-instrumentation.drawio.svg
  :width: 80%
  :align: center
  :alt: Code coverage with GCC

  GCC overview

Available information
~~~~~~~~~~~~~~~~~~~~~
- Version: 12.x [1]_
- Official repository: https://gcc.gnu.org/
- Official documentation: https://gcc.gnu.org/onlinedocs/

Installation and integration
----------------------------
Installation
~~~~~~~~~~~~
To use GCC in a project, add the appropriate toolchain configuration to the `MODULE.bazel` file.

.. code-block:: Python

  # Configure the gcc toolchain.
  bazel_dep(name = "score_toolchains_gcc", version = "<X.Y>", dev_dependency = True)

  gcc = use_extension("@score_toolchains_gcc//extentions:gcc.bzl", "gcc", dev_dependency = True)
  gcc.toolchain(
    sha256 = "<SHA256_CHECKSUM>",
    strip_prefix = "x86_64-unknown-linux-gnu",
    url = "https://github.com/eclipse-score/<path_to_gcc>/x86_64-unknown-linux-gnu_gcc12.tar.gz",
  )
  use_repo(gcc, "gcc_toolchain", "gcc_toolchain_gcc")

If your project uses multiple toolchains or configurations, update the `.bazelrc` file in the project root to reference the GCC toolchain.

.. code-block:: Python

  ...
  common --extra_toolchains=@gcc_toolchain//:host_gcc_12
  ...

In this case default host toolchain is set to GCC and it will be used for all cc_* rules in the project.

Detailed instructions for setting up and tuning of GCC toolchain can be found in the S-CORE toolchains documentation, i.e. https://github.com/eclipse-score/toolchains_gcc

Integration
~~~~~~~~~~~
GCC is invoked by Bazel as the C/C++ compiler for cc_* targets.
The specific compiler flags and configurations are defined in the Bazel build files and can be customized as needed for different build configurations (e.g., debug, release, with instrumentation).

Environment
~~~~~~~~~~~
Requires Linux and Bazel build environment.

Safety evaluation
-----------------
This section outlines the safety evaluation of GCC for its use within the S-CORE project.


.. list-table:: GCC safety evaluation
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
     - GCC compile
     - | Semantically wrong binary object file
       | GCC built syntactically correct but semantically wrong object file.
     - no
     - no
     - yes
     - no
     - high
   * - 2
     - GCC compile
     - | Syntactically wrong object code file
       | GCC built syntactically wrong object file.
     - no
     - no
     - yes
     - no
     - high
   * - 3
     - GCC link
     - | Semantically wrong binary
       | GCC built syntactically correct but semantically wrong binary.
     - no
     - no
     - yes
     - no
     - high
   * - 4
     - GCC link
     - | Syntactically wrong binary
       | GCC built syntactically wrong binary.
     - no
     - no
     - yes
     - no
     - high
   * - 5
     - Instrumentation / code coverage
     - | Coverage data too high
       | compiler with instrumentation reports higher coverage than actual, masking untested code.
     - no
     - no
     - yes
     - no
     - high
   * - 6
     - Instrumentation / code coverage
     - | Coverage data too low
       | Instrumentation reports lower coverage than actual, leading to unnecessary rework.
     - no
     - no
     - yes
     - no
     - high

Security evaluation
-------------------
This section outlines the security evaluation of GCC for its use within the S-CORE project.

.. list-table:: GCC security evaluation
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
------
GCC is not used for production builds nor during software verification phases.
The tool is used for development purposes only to support early-stage issue identification and resolution.


.. [1] The tool version mentioned in this document is preliminary. It is subject to change and will be updated in future.

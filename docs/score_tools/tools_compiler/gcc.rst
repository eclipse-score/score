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
   :tcl: LOW
   :safety_affected: YES
   :security_affected: YES
   :realizes: wp__tool_verification_report
   :tags: tool_management, tools_compiler

GCC Compiler Verification Report
================================

Introduction
------------
Scope and purpose
~~~~~~~~~~~~~~~~~
GCC is open-source C/C++ compiler. Used for both safety-related and non-safety-related software in the S-CORE project.

Inputs and outputs
~~~~~~~~~~~~~~~~~~
| Inputs: Software sources (C++), configuration files, dependencies
| Outputs: Object files, binaries, build logs

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
GCC is invoked by Bazel as the C/C++ compiler for host builds, unit tests and integration testing.

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
     - yes
     - no
     - no
     - yes (qualification)
     - low
   * - 2
     - GCC compile
     - | Syntactically wrong object code file
       | GCC built syntactically wrong object file.
     - yes
     - (implicit) Linker will fail due to invalid object file
     - yes
     - no
     - high
   * - 3
     - GCC link
     - | Semantically wrong binary
       | GCC built syntactically correct but semantically wrong binary.
     - yes
     - no
     - yes
     - yes (qualification)
     - low
   * - 4
     - GCC link
     - | Syntactically wrong binary
       | GCC built syntactically wrong binary.
     - no
     - (implicit) Binary will crash during start
     - yes
     - no
     - high
   * - 5
     - Instrumentation / code coverage
     - | Coverage data too high
       | compiler with instrumentation reports higher coverage than actual, masking untested code.
     - yes
     - no
     - no
     - yes (qualification)
     - low
   * - 6
     - Instrumentation / code coverage
     - | Coverage data too low
       | Instrumentation reports lower coverage than actual, leading to unnecessary rework.
     - no
     - | (implicit) Manual review or redundant testing
       | Required coverage goals are defined for software components. If reported coverage is lower than the goal, the required coverage objective is not achieved.
       | Any coverage gaps identified must be addressed through manual review.
     - yes
     - no
     - low

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
GCC requires qualification for use in safety-related software development according to ISO 26262.


**Tool Qualification**
----------------------
Based on method: validation of the software tool.

Requirements and testing aspects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GCC is an open-source tool and does not provide formal, vendor-defined requirements.
Therefore, the tooling team is responsible for qualification of GCC used for the the project.
The requirements for testing must be derived from tool version, configuration (compiler flags, etc.)
and environment.

.. [1] The tool version mentioned in this document is preliminary. It is subject to change and will be updated in future.

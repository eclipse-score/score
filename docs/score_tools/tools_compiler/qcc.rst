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

.. doc_tool:: qcc
   :id: doc_tool__qcc
   :status: draft
   :version: 8.x
   :tcl: LOW
   :safety_affected: YES
   :security_affected: YES
   :realizes: wp__tool_verification_report
   :tags: tool_management, tools_compiler

QCC Compiler Verification Report
================================

Introduction
------------
Scope and purpose
~~~~~~~~~~~~~~~~~
QCC (QNX C Compiler) is a C/C++ target compiler from BlackBerry to build software for QNX boards.
It is used for both safety-related and non-safety-related software in the S-CORE project.

Inputs and outputs
~~~~~~~~~~~~~~~~~~
| Inputs: Software sources (C++), configuration files, dependencies
| Outputs: Object files, binaries, build logs, coverage data

.. figure:: _assets/qcc.drawio.svg
  :width: 80%
  :align: center
  :alt: QCC build

.. figure:: _assets/qcc-instrumentation.drawio.svg
  :width: 80%
  :align: center
  :alt: Code coverage with QCC


  QCC overview

Available information
~~~~~~~~~~~~~~~~~~~~~
- Version: 8.x [1]_
- Official documentation: https://www.qnx.com/developers/docs/index.html

Installation and integration
----------------------------
Installation
~~~~~~~~~~~~
To use QCC in a project, add the appropriate toolchain configuration to the `MODULE.bazel` file.

.. code-block:: Python

  # Configure the target toolchain.
  bazel_dep(name = "score_toolchains_qnx", version = "0.0.6", dev_dependency = True)

  toolchains_qnx = use_extension(
      "@score_toolchains_qnx//:extensions.bzl",
      "toolchains_qnx",
      dev_dependency = True,
  )
  toolchains_qnx.sdp(
      sha256 = "<SHA256_CHECKSUM>",
      strip_prefix = "installation",
      url = "https://www.qnx.com/<path_to>/installation.tgz",
  )
  use_repo(toolchains_qnx, "toolchains_qnx_sdp")
  use_repo(toolchains_qnx, "toolchains_qnx_qcc")

If your project uses multiple toolchains or configurations, update the `.bazelrc` file in the project root to reference the QCC toolchain.

.. code-block:: Python

  ...
  build:qnx_x86_64 --extra_toolchains=@toolchains_qnx_qcc//:qcc_x86_64
  ...

And during the build process, set appropriate configuration flags to select the QCC toolchain.

.. code-block:: bash

  bazel build --config=qnx_x86_64 //path/to:target


Bazel will automatically download the required dependencies and configure the QCC toolchain for your project as specified.

Detailed instructions for setting up QCC toolchain can be found in the S-CORE toolchains documentation, i.e. https://github.com/eclipse-score/toolchains_qnx


Integration
~~~~~~~~~~~
QCC is invoked by bazel as the C/C++ compiler for QNX targets.



Environment
~~~~~~~~~~~
Requires linux and bazel build environment.


Safety evaluation
-----------------
This section outlines the safety evaluation of QCC for its use within the S-CORE project.

.. list-table:: QCC safety evaluation
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
     - QCC compile
     - | Semantically wrong binary object file
       | QCC built syntactically correct but semantically wrong object file.
     - yes
     - no
     - no
     - yes (qualification)
     - low
   * - 2
     - QCC compile
     - | Syntactically wrong object code file
       | QCC built syntactically wrong object file.
     - yes
     - (implicit) Linker will fail due to invalid object file
     - yes
     - no
     - high
   * - 3
     - QCC link
     - | Semantically wrong binary
       | QCC built syntactically correct but semantically wrong binary.
     - yes
     - no
     - yes
     - yes (qualification)
     - low
   * - 4
     - QCC link
     - | Syntactically wrong binary
       | QCC built syntactically wrong binary.
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
This section outlines the security evaluation of QCC for its use within the S-CORE project.

.. list-table:: QCC security evaluation
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
QCC requires qualification for use in safety-related software development according to ISO 26262.


**Tool Qualification**
----------------------
Based on method: validation of the software tool.

Requirements and testing aspects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
QCC is a proprietary tool and has already been qualified by the tool provider.
For use in safety-related contexts, it is mandatory to follow the QCC safety manual and ensure that all relevant mitigations and user responsibilities described therein are fully applied.

.. [1] The tool version mentioned in this document is preliminary. It is subject to change and will be updated in future.

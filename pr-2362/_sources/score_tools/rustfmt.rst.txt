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

.. doc_tool:: rustfmt
   :id: doc_tool__rustfmt
   :status: evaluated
   :version: 1.8.0 (exact version shall be derived from qualified Rust compiler)
   :tcl: HIGH
   :safety_affected: YES
   :security_affected: YES
   :realizes: wp__tool_verification_report
   :tags: tool_management

Rustfmt Verification Report
===========================

Introduction
------------
Scope and purpose
~~~~~~~~~~~~~~~~~
Rustfmt is the standard formatting tool for the Rust programming language. It automatically
formats Rust code according to style guidelines defined in the Rust community. By using Rustfmt,
developers can ensure that their code adheres to a consistent style, improving readability and
maintainability across projects. Rustfmt can be integrated into development workflows, including
IDEs and continuous integration pipelines, to enforce coding standards automatically.

Inputs and outputs
~~~~~~~~~~~~~~~~~~
| Inputs: Software sources (Rust)
| Outputs: Formatted software sources (Rust)

.. figure:: _assets/rustfmt.drawio.svg
  :width: 100%
  :align: center
  :alt: Rustfmt overview

  Rustfmt overview

Available information
~~~~~~~~~~~~~~~~~~~~~
- Version: >= 1.8.0
- Official repository: https://github.com/rust-lang/rustfmt
- Official documentation: https://rust-lang.github.io/rustfmt
- Rustfmt configuration in S-CORE module repository: https://github.com/eclipse-score/score/issues/2011


Installation and integration
----------------------------
Installation
~~~~~~~~~~~~
| To add the Rustfmt Bazel targets to your project or module, include the following line in your MODULE.bazel file:

.. code-block:: Python

  To be added once https://github.com/eclipse-score/score/issues/2011 is done


Integration
~~~~~~~~~~~
Integrated in bazel.

Environment
~~~~~~~~~~~
Requires Rust toolchain and Bazel build environment.

Safety evaluation
-----------------
This section outlines the safety evaluation of Rustfmt for its use within the S-CORE project.


.. list-table:: Safety evaluation
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
     - Run formatting on source files and does not format according to rules
     - | The source code is not formatted according to the defined style guidelines, leading to inconsistent code style across the project.
     - no
     - no
     - yes
     - no
     - high
   * - 2
     - Run formatting on source files changes code unintentionally
     - | The source code changes its logical structure or behavior due to incorrect formatting, potentially introducing bugs.
     - yes
     - | Likelihood: Low. Rustfmt is used in virtually every Rust project. This gives high confidence in its quality.
       | Also, auto formatting happens only before `commiter` commits it's changes, so **before** compilation (CI), testing(CI) and review.
       | Countermeasures:

       - The compiler will catch syntax errors introduced by incorrect formatting and fail to compile
       - The logic change can be detected by code reviews and automated testing (CI).
     - yes
     - no
     - high

Security evaluation
-------------------
This section outlines the security evaluation of Rustfmt for its use within the S-CORE project.


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
~~~~~~
Rustfmt does not require qualification for use in safety-related software development according to ISO 26262.

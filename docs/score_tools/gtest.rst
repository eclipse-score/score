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

.. doc_tool:: gtest
   :id: doc_tool__gtest
   :status: draft
   :version: 1.15.0
   :tcl: LOW
   :safety_affected: YES
   :security_affected: YES
   :realizes: wp__tool_verification_report
   :tags: tool_management

GoogleTest (GTest) Verification Report
======================================

Introduction
------------
Scope and purpose
~~~~~~~~~~~~~~~~~
GoogleTest (GTest) is a C++ testing framework developed by Google to support the creation
of robust, maintainable, and portable tests. It is designed to help developers write tests
by offering a rich set of assertions, test fixtures, and test discovery
mechanisms. GTest is compatible with various platforms.

Inputs and outputs
~~~~~~~~~~~~~~~~~~
| Inputs: Software sources (C++), GTest-based test files (C++)
| Outputs: Test binary, Test report (txt, json, xml).

.. figure:: _assets/gtest.drawio.svg
  :width: 100%
  :align: center
  :alt: GTest overview

  GTest overview

Available information
~~~~~~~~~~~~~~~~~~~~~
- Version: 1.15.0 [1]_
- Official repository: https://github.com/google/googletest
- Official documentation: https://google.github.io/googletest
- API Reference: https://google.github.io/googletest/reference/testing.html
- Example of GTest configuration in S-CORE module repository: https://github.com/eclipse-score/baselibs/blob/main/MODULE.bazel


Installation and integration
----------------------------
Installation
~~~~~~~~~~~~
| To add the GTest Bazel dependency to your project or module, include the following line in your MODULE.bazel file:

.. code-block:: Python

  bazel_dep(name = "googletest", version = "1.15.0")

| Bazel will fetch from the Bazel Central Registry (BCR): https://registry.bazel.build/modules/googletest


Integration
~~~~~~~~~~~
Integrated in bazel.

Environment
~~~~~~~~~~~
Requires C++ compiler and bazel build environment.

Safety evaluation
-----------------
This section outlines the safety evaluation of GTest for its use within the S-CORE project.


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
     - Run tests and generate test report
     - | Fails to load input files
       |
       | GTest fails to load provided file even if file is present and accessible.
     - yes
     - (implicit) Check test run status
     - yes
     - no
     - high
   * - 2
     - Run tests and generate test report
     - | Fails to write result to file
       |
       | GTest was not able to save results in file(s).
     - yes
     - (implicit) Check test run status
     - yes
     - no
     - high
   * - 3
     - Run tests and generate test report
     - | Fails to collect results of the test(s)
       |
       | GTest was not able to collect results of executed test.
     - no
     - no
     - yes
     - no
     - high
   * - 4
     - Run tests and generate test report
     - | Fails to detect an existing error
       |
       | GTest fails to detect the presence of existing errors.
     - yes
     - no
     - no
     - yes (qualification)
     - low
   * - 5
     - Run tests and generate test report
     - | Fails to execute the test
       |
       | GTest fails to execute specific test from the test plan
     - no
     - no
     - yes
     - no
     - high
   * - 6
     - Run tests and generate test report
     - Indicates presence of a non-existing error

       GTest indicates the presence of errors that do not exist.
     - no
     - no
     - yes
     - no
     - high
   * - 7
     - Run tests and generate test report
     - | Produces wrong test report
       |
       | GTest fails to save correct test result in test report.
     - yes
     - Review test report
     - yes
     - no
     - high

Security evaluation
-------------------
This section outlines the security evaluation of GTest for its use within the S-CORE project.


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
GTest requires qualification for use in safety-related software development according to ISO 26262.


**Tool Qualification**
-------------------------------------------
Based on method: validation of the software tool.

Requirements and testing aspects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tool requirements are derived from official documentation: https://google.github.io/googletest

GTest is an open-source tool and does not provide formal, vendor-defined requirements.
Therefore, the testing team is responsible for identifying the specific GTest functionality
used in the project. Based on this, requirements for the utilized features must be derived from
the available documentation and GTest validated against defined requirements.


.. [1] The tool version mentioned in this document is preliminary.
       It is subject to change and will be updated in future.

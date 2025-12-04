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

.. doc_tool:: ITF
   :id: doc_tool__itf
   :status: draft
   :version: 0.1.0
   :tcl: LOW
   :safety_affected: YES
   :security_affected: YES
   :realizes: wp__tool_verification_report
   :tags: tool_management

ITF (Integration Testing Framework) Verification Report
=======================================================

Introduction
------------
Scope and purpose
~~~~~~~~~~~~~~~~~
ITF is a pytest-based integration testing framework that simplifies writing and
running integration tests. It provides utilities for common integration tasks
— for example, SSH connection setup, interpreting dataframes, parsing
diagnostic messages, etc. ITF can execute tests on emulators (QEMU) as well as on
physical hardware.

Inputs and outputs
~~~~~~~~~~~~~~~~~~
| Inputs: Software image (binary), Pytest-based test files (python)
| Outputs: Test report

.. figure:: _assets/itf.drawio.svg
  :width: 100%
  :align: center
  :alt: ITF overview

  ITF overview

Available information
~~~~~~~~~~~~~~~~~~~~~
- Version: 0.1.0 [1]_
- Repository: https://github.com/eclipse-score/itf
- Example of ITF test in S-CORE ITF repository: https://github.com/eclipse-score/itf/blob/main/examples/examples/itf/test_docker.py


Installation and integration
----------------------------
Installation
~~~~~~~~~~~~
| To add the ITF Bazel dependency to your project or module, include the following line in your MODULE.bazel file:

.. code-block:: Python

  bazel_dep(name = "score_itf", version = "0.1.0")

| And verify that the `.bazelrc` configuration file contains the following directive to register the S-CORE module registry:

.. code-block:: Python

  common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/

| The sources of bazel S-CORE ITF module configuration can be found at: https://github.com/eclipse-score/bazel_registry/tree/main/modules/score_itf


Integration
~~~~~~~~~~~
Integrated in bazel.

Environment
~~~~~~~~~~~
Running application software instance with configured connection.

Safety evaluation
-----------------
This section outlines the safety evaluation of ITF for its use within the S-CORE project.


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
       | ITF fails to load provided file even if file is present and accessible.
     - yes
     - (implicit) Check ITF test run status
     - yes
     - no
     - high
   * - 2
     - Run tests and generate test report
     - | Fails to write result to file
       |
       | ITF was not able to save results in file(s).
     - yes
     - (implicit) Check ITF test run status
     - yes
     - no
     - high
   * - 3
     - Run tests and generate test report
     - | Fails to collect results of the test(s)
       |
       | ITF was not able to collect results of executed test.
     - no
     - no
     - yes
     - no
     - high
   * - 4
     - Run tests and generate test report
     - | Fails to detect an existing error
       |
       | ITF fails to detect the presence of existing errors.
     - yes
     - no
     - no
     - yes (qualification)
     - low
   * - 5
     - Run tests and generate test report
     - | Fails to execute the test
       |
       | ITF fails to execute specific test from the test plan
     - no
     - no
     - yes
     - no
     - high
   * - 6
     - Run tests and generate test report
     - | Indicates presence of a non-existing error
       |
       | ITF indicates the presence of errors that do not exist.
     - no
     - no
     - yes
     - no
     - high
   * - 7
     - Run tests and generate test report
     - | Produces wrong test report
       |
       | ITF fails to save correct test result in test report.
     - yes
     - Review test report
     - yes
     - no
     - high

Security evaluation
-------------------
This section outlines the security evaluation of ITF for its use within the S-CORE project.


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
ITF requires qualification for use in safety-related software development.


**Tool Qualification**
-------------------------------------------
Based on method: validation of the software tool.

Requirements and testing aspects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tool requirements are derived from official documentation (currently missing): https://github.com/eclipse-score/itf

The testing team is responsible for identifying the specific ITF functionality
used in the project. Based on this, requirements for the utilized features must be derived from
the available documentation and ITF validated against defined requirements.


.. [1] The tool version mentioned in this document is preliminary.
       It is subject to change and will be updated in future.

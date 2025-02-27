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

Verification Guidance
=====================

This guideline outlines the responsibilities and procedures for developers performing verification activities (test
case creation, inspection, and review) for documentation, Rust and C/C++ elements of the platform and its tooling.
Rust, python and gTest are used for test case creation.

General Principles
------------------

* **Verification is everyone's responsibility:** While dedicated testing responsible may exist, every developer is
  accountable for the quality and correctness of their code and related artifacts.
* **Early and often:** Verification activities should be integrated throughout the development lifecycle,
  not just at the end. This includes unit tests, integration tests, code reviews, and inspections.
* **Traceability:** All verification activities should be traceable to requirements, architectural design, etc.
* **Independence:** Where possible, verification activities should be performed by someone other than the original author of the code or documentation.
* **Documentation:** All verification activities and their results must be documented appropriately.

More details on the test strategy and execution can be found in the :need:`wp__verification__plan` implemented by
:need:`doc__verification_plan`.

Test Case Development
------------------------

Following aspect should be considered when developing test cases:

* **Comprehensive Coverage:** Test cases should cover all functional and non-functional requirements, including
  positive, negative, and boundary conditions. Specific attention should be given to corner cases and error handling.
* **Unit Testing:** Focus on isolating and testing individual units or components of the code. Strive for high code coverage.
    * **Rust:** Utilize the built-in testing framework with ``#[test]`` attributes and the ``cargo test`` command.
    * **Python:** Use ``pytest`` frameworks.
    * **C++:** Use Google Test frameworks.
* **Integration Testing:** Verify the interaction between different components or modules.
* **Platform Testing:** Test the platform with configured features as a whole.
* **Regression Testing:** Ensure that changes do not introduce new defects.
  Automate regression tests where possible and execute them as part of CI execution.
* **Performance Testing (when applicable):** Evaluate the performance characteristics of the code, such as execution
  time, memory usage, and resource utilization.
* **Tool Qualification Testing:** Test the platform tools based on their tool requirements to achive tool qualification.

Test specification
------------------

.. list-table:: Test specification properties
    :header-rows: 1

   * - Property
     - Type
     - Description
     - Helpful links
   * - Verifies
     - Sphinx-needs Ids
     - Links to one or more requirement Ids
     -
   * - Description
     - Text
     - The description should include
       - The objective of the test.
       - Inputs
       - Expected outcome (e.g. "A success message is displayed.")
       - Test environment (e.g. network configuration, clean system state)
     -
   * - Status
     - valid | invalid
     -
     -
   * - TestType
     - Requirements-based test | Design based tests
     - Assumptions of Use are treated as requirements.
     -
   * - DerivationTechnique
     - Analysis of requirements | Analysis of design
     - Assumptions of Use are treated as requirements.
     -

Test Case Description
---------------------

A good test description clearly explains the purpose and scope of a test case.
It provides enough information for anyone (including someone unfamiliar with the system) to understand
what is being tested and how.

Basic qualities of a good test case description are that the test is:
  - Clear: Easy to understand and avoids ambiguity.
  - Specific: Provides enough detail to reproduce the test.
  - Measurable: Defines clear pass/fail criteria.
  - Complete: Covers all relevant aspects of the test.

Further recommendation can be found in the verification templates :doc:`./verification_templates`

Structuring of the Test Case
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To fulfil the requirements for the workproduct *Software Verification Specification* the test case shall be structured using the Given-When-Then pattern:

* | Given (alternatively // Setup )
  | This section contains the setup of the input.
* | Expected
  | This Section contains the expectation for calls to mocks or stubs
* | When (alternatively  // Call )
  | This section contains the call to the software under test.
* | Then (alternatively // Expect )
  | This section contains the verification criteria of the test (e.g. all EXPECT statements).

.. code-block:: cpp

   TEST(CreateObjectHistory, GivenVehicleInFront_ExpectHistoryBehindFrontVehicle)
   {
      // Given
      const auto whatever_input_values = CreateVehicleInFront();

      // Expected
      EXPECT_CALL(..., ...);

      // When
      const auto history = CreateObjectHistory(whatever_input_values, ...);

      // Then
      for (const auto point : history)
      {
         EXPECT_EQ(..., ...);
      }
   }


General Traceability Concept
----------------------------

To allow a traceability from any line of code to a written requirement, unit tests are linked (in a hierarchical
manner) to other unit tests or component tests which in turn are linked to software requirements directly.
This linking is done using metatags.

Traceability of integration tests shall be established through linking those test cases to feature requirements as
features describe the integrated behavior of all components.
A more detailed description of how to link code to requirements is available here: :need:`gd_req__link_tests`

Workflow for Verification Guidance
----------------------------------

.. _requirement_verification_workflow:

.. figure:: ../_assets/requirements_workflow_verification.svg
    :alt: Requirements Versioning
    :align: center
    :width: 100%

    Requirements Workflow

The :ref:`requirement_verification_workflow` above displays the whole workflow including the traceability concept for the
requirements where requirements shall be linked to test cases on the respective level. However also a statement
concerning the completeness of the test suite shall be generated. This means that also a linkage document shall be
generated including:

- the hash and UID of the requirement which was evaluated for test coverage
- the UIDs of the test cases which are required to fully cover the requirement.

So if the content of the requirement is altered also the hash will change making it necessary to revisit the linkage of all test cases to the requirement again.

If the status of the linked test case and the linkage document is valid the attribute *testcovered* shall be set to *YES* during the Sphinx Build.

Verify Requirements Detailed Flow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Implement test case
#. Link test case to requirements and specify metatags
#. Confirm requirement test coverage by creating linkage document
#. Set requirement attribute [testcovered=YES] during Sphinx build

..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

Test Specification Guideline
============================

.. gd_guidl:: Test Specification Guideline
   :id: gd_guidl__verification_specification
   :status: valid
   :complies: std_wp__iso26262__support_952

Test specification
------------------

A test specification contains the following attributes.

.. list-table:: Test specification properties
   :header-rows: 1
   :widths: 10 30 40 20

   * - Property
     - Type / Values
     - Description
     - Helpful links
   * - Partially and/or Fully Verifies
     - Sphinx-needs Id(s)
     - Links to one or more requirement Ids. Can be partial or full coverage of a
       requirement, as per test property.
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
     -
       - valid
       - invalid
     -
     -
   * - TestType
     - Examples are:

       - requirements-based
       - interface-test
       - boundary
       - coverage (various types apply, shall be tool supported)
       - for :need:`wp__verification__sw_unit_test` also fault-injection
     - These are example values and an incomplete list.
       A full list of test types is available in :need:`doc_concept__verification__process` at
       :ref:`verification_concept_types_methods`.
     -
   * - DerivationTechnique
     - Examples are:

       - requirements-analysis
       - boundary-values
       - equivalence-classes
       - error-guessing
     - These are example values and an incomplete list.
       A full list of test methods is available in :need:`doc_concept__verification__process` at
       :ref:`verification_concept_types_methods`.
     -

The implementation of :need:`wp__verification__plan` defines the full list of allowed types and methods.


Test description
----------------

Following Given-When-Then is a preferred way to write test specifications.

* | Given (alternatively // Setup  )
  | This section contains the setup of the input.
* | Expected
  | This Section contains the expectation for calls to mocks or stubs
* | When (alternatively  // Call   )
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

Another example for a good test description could be:

  | Verify successful login with valid credentials.
  | Input:
  | - Username: testuser
  | - Password: password123
  | Expected Outcome:
  | - User is redirected to the home page and the welcome message "Hello, testuser!" is displayed.

A example for a bad test description could be:

   Test user login

Additional information can also be found in :need:`gd_guidl__verification_guide`.

The specification is part of the test implementation and has to comply to the requirements
specified in :need:`gd_req__link_tests`.

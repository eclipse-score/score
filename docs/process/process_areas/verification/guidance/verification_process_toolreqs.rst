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

.. _verification_process_reqs:

Test Linking to Requirements
============================


.. gd_req:: Linking Requirements to Tests
    :id: gd_req__link_tests
    :status: valid
    :complies: std_req__iso26262__support_6432

    For linking test suites to requirements following metadata shall be used:

    * Verifies
        * PartiallyVerifies
        * FullyVerifies
    * ASIL
        * QM
        * ASIL_B
    * Description
    * Status
        * valid
        * invalid
    * TestType
        * Control Flow Analysis (control-flow-analysis)
        * Data Flow Analysis (data-flow-analysis)
        * Fault Injection (fault-injection)
        * Inspection (inspection)
        * Interface Test (interface-test)
        * Requirements-based Test (requirements-based)
        * Resource Usage Evaluation (resource-usage)
        * Static Code Analysis (static-code-analysis)
        * Structural Statement coverage (structural-statement-coverage)
        * Structural Branch Coverage (structural-branch-coverage)
        * Walkthrough (walkthrough)
    * DerivationTechnique
        * Analysis of requirements (requirements-analysis)
        * Analysis of design (design-analysis)
        * Analysis of boundary values (boundary-values)
        * Analysis of equivalence classes (equivalence-classes)
        * Error guessing based on knowledge or experience (error-guessing)
        * Random testing (monkey-testing)
        * Exlporative testing (explorative-testing)

    More information can be found in the :need:`gd_guidl__verification_guide`, :need:`doc_concept__verification__process`,
    and :need:`gd_guidl__verification_specification`.

.. gd_req:: Linking Requirements to Tests (C++)
    :id: gd_req__link_tests_cpp
    :status: valid
    :complies: std_req__iso26262__support_6432

    For linking C++ test suites to requirements **record properties** shall be used. Attributes
    which are common for all test cases can be specified in the Setup Function (SetUp()), the other
    attributes which are specific for each test case need to be specified within the test case:

    .. code-block:: cpp

      class TestSuite : public ::testing::Test{
         public:
            void SetUp() override
            {
               RecordProperty("Status", "<Status>");
               RecordProperty("ASIL", "<ASIL>");
               RecordProperty("TestType", "<TestType>");
               RecordProperty("DerivationTechnique", "<DerivationTechnique>");
               ...
            }
      };

      TEST_F(TestSuite, <Test Case>)
      {
         RecordProperty("PartiallyVerifies", "ID_2, ID_3, ...");
         RecordProperty("FullyVerifies", "ID_4, ID_5, ...");
         RecordProperty("Description", "<Description>");

         ASSERT ...
      }

.. gd_req:: Linking Requirements to Tests (Python)
    :id: gd_req__link_tests_python
    :status: valid
    :complies: std_req__iso26262__support_6432

    For linking python tests to requirements **metadata** shall be used. Attributes which are
    common for all test cases can be specified in the Test Suite (above the class), the other
    attributes which are specific for each test case need to be specified above the test case:

    .. code-block:: python

      @pytest.fixture(scope="session", autouse=True)
      def add_metadata(record_testsuite_property):
         record_testsuite_property("ASIL", "<ASIL>")
         record_testsuite_property("TestType", "<TestType>")
         record_testsuite_property("DerivationTechnique", "<DerivationTechnique>")
      class Testclass(TestSim):

         def TestFunction(self, record_property):
            record_property("PartiallyVerifies", "ID_2, ID_3, ...")
            record_property("FullyVerifies", "ID_4, ID_5, ...")
            record_property("Description","<Description>")

.. gd_req:: Linking Requirements to Tests (Rust)
    :id: gd_req__link_tests_rust
    :status: valid
    :complies: std_req__iso26262__support_6432

    For linking Rust tests to requirements **#[record_property]** shall be used:

    .. code-block:: rust

        use test_properties::record_property;

        #[record_property("PartiallyVerifies", "ID_2, ID_3, ...")]
        #[record_property("FullyVerifies", "ID_4, ID_5, ...")]
        #[record_property("Description", "<Description>")]
        #[record_property("Status", "<Status>")]
        #[record_property("ASIL", "<ASIL>")]
        #[record_property("TestType", "<TestType>")]
        #[record_property("DerivationTechnique", "<DerivationTechnique>")]
        #[test]
        fn test_case_function() {
            ...
        }

.. gd_req:: Test Independence
    :id: gd_req__verification_independence
    :status: draft

    The approver of a pull request shall differ from the author(s) of the pull request in all pull requests.

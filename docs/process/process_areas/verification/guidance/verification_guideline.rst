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

Verification Guideline
======================
.. gd_guidl:: Verification Guideline
   :id: gd_guidl__verification_guide
   :status: valid

   This guideline outlines the responsibilities and procedures for developers performing
   verification activities (testcase creation, inspection, and review) for documentation,
   Rust and C/C++ elements of the platform and its tooling.

   Note that rust, python and gTest are used for test case creation.

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

Test specifications should follow :need:`gd_guidl__verification_specification`

Structuring of the Test Case
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To fulfill the demands of the work product :need:`wp__verification__plan` the
templates in :ref:`verification_process_reqs` shall be used and the :need:`gd_guidl__verification_specification`
should be followed . This includes general information and templates for the allowed programming languages.


Verify Requirements Execution Work Flow
---------------------------------------

Simplified in a nutshell:

#. Implement test case
#. Link test case to requirements and specify metatags
#. Confirm requirement test coverage by creating linkage document
#. Set requirement attribute [testcovered=YES] during Sphinx build

More information on the concept of requirements verification can be found in :ref:`requirement_verification_workflow`

A more detailed description of how to link code to requirements is available here: :need:`gd_req__link_tests`

Traceability matrix and consistency checks will be automatically established with tool support.

Two properties exists; one to show partial and one to show full coverage of a requirement.
For multiple test cases having a "partial coverage" a review has to be conducted to confirm
that a requirement is fully covered. The pull request description should indicate which requirements
are fully covered by the PR commits and which test cases are needed to fully cover the test case.
This is important, as multiple PRs may be needed to fully verify a single requirement.


Test case execution
-------------------

The execution of the tests is based on a full automation defined by build pipelines.
The analysis of the test results needs to be performed by the contributor.

In order to check the test results for the impact of a change or addition, it is recommended to
execute affected test cases locally upfront using the execution framework of the build tooling
following basically the steps the CI does locally.

There may be the need for limited number of manually executed test cases.
These manually executed test cases are execution script driven, where a script guides through the
test cases and reports the result in the same logging format as automated tests do.

Reporting of failing test cases
-------------------------------

Any failing test case requires an ISSUE.
The passing rate of safety-critical test cases need to be 100% in order to release the affected component.
In case of a lower pass rate than 100% for QM level tests, the :need:`rl__technical_lead` and
:need:`rl__project_lead` can decide, if the platform is in a releasable state. The accepted minimal
path rate is defined in the :need:`wp__verification__plan`. Due to the high degree of automation, a
it is recommended that a path rate lower 95% is not acceptable.

In case an existing test case is failing due to regression in the CI, the respective issuer of the
PR in their role as :need:`rl__contributor` is responsible for fixing the test case as part of
respective PR.

Reuse of existing test cases
----------------------------

In case pre-existing test cases from components can be used, they have to be reviewed and checked
for their fit to the defined requirements. The test cases should get patch files to cover missing
specification parts following :need:`gd_guidl__verification_specification` and have the necessary
:need:`gd_req__link_tests` followed. These patches are applied on top of the untouched actual
implementation of the software code.

Additionally needed test cases should be added as standalone parts. They are developed as any
other test case as part of the platform. If upstreaming of the newly created tests is judged as
useful, this shall be planned and added to the project milestone plan.

Verification types and methods
------------------------------

Verification types and methods are described in the :need:`doc_concept__verification__process`.

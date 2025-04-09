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

Verification Concept
####################

.. doc_concept:: Verification Concept
   :id: doc_concept__verification__process
   :status: valid
   :tags: requirements_engineering

   In this section a concept for the verification activities will be discussed.
   Inputs for this concepts are mainly the requirements and work products from

   * ISO26262 Part 6: "Product development at the software level"
   * ISO26262 Part 8: "Supporting processes"
   * ISO26262 Part 9: "Automotive Safety Integrity Level (ASIL)-oriented and safety-oriented analysis"

Inputs
======

#. Stakeholders for the verification work products?
#. What kind of tests are developed?
#. How is traceability established?
#. What tooling do we use?


Stakeholder
===========

#. :need:`Technical Lead <rl__technical_lead>`

   * Set the scope of platform and testing
   * Status reporting of verification activities
   * Defining release content
   * Judge the releasable software state in case of failing test cases.

     This may need involvement of :need:`rl__project_lead`,
     :need:`rl__safety_manager`, and :need:`rl__security_manager`

#. :need:`SW developer/Architects <rl__contributor>`

   * Create work products based on the requirements
   * Provides the input work products for verification activities
   * SW developer create unit tests.

#. :need:`Test Contributors <rl__contributor>`

   * Create verification artifacts

#. :need:`Test Committer <rl__committer>`

   * Review and approve verification artifacts
   * Get support by the :need:`rl__safety_manager` for safety-critical artifacts

#. :need:`Technical Lead <rl__committer>`

   * Set the scope of platform and testing
   * Status reporting of verification activities
   * Defining release content

#. :need:`Infrastructure/Tooling Developer <rl__infrastructure_tooling_community>`

   * Enables execution of test cases in CI
   * Generation of verification reports
   * Provides tools for test generation
   * Integrates static analysis, linting, test frameworks into CI

#. :need:`Safety Manager <rl__safety_manager>`

   * Supports the verification activities for safety-critical work products.

#. :need:`External Auditor <rl__external_auditor>`

   * Understand activities, planning, processes definition, and execution reports for verification activities

#. "Distributor" (external role)

   * Re-execution of test cases
   * Testing OSS parts on product hardware
   * Integrate the test cases in their product (distribution)
   * Create issue reports and provide improvements

.. _verification_concept_types_methods:

Verification Methods
=====================

A verification is based on different methods. An overview of the different methods that are
applicable are:

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

The derivation of test cases can also be based on certain methods.

 * Analysis of boundary values (boundary-values)
 * Analysis of equivalence classes (equivalence-classes)
 * Analysis of requirements (requirements-analysis)
 * Error guessing based on knowledge or experience (error-guessing)
 * Fuzzy testing (fuzz-testing)
 * Exlporative testing (explorative-testing)

Usually the defined methods are not applied on each verification level between unit and platform level.
Also their execution may differ whether it is a QM or ASIL rated test case.
The rigor is described in the implementation of :need:`wp__verification__plan`.


Automated test cases should contain further information about which methods have been applied.
The corresponding guidance is given here: :need:`gd_guidl__verification_guide`.
The identifier of the respective method is to be used as meta data (*TestType* and *DerivationTechnique*).

Test Case Development
=====================

Following aspect should be considered when developing test cases:

* **Comprehensive Coverage:** Test cases should cover all functional and tool requirements, including
  positive, negative, and boundary conditions. Specific attention should be given to corner cases and error handling.
* **Requirements Testing:** Guarantees testing of Component, Feature, and Stakeholder requirements.
* **Unit Testing:** Focus on isolating and testing individual units or components of the code.
  Strive for high code coverage for branches and lines.
  Coverage goals are defined in the :need:`wp__verification__plan`.

  Use the following frameworks for unit testing:

  * **Rust:** Utilize the built-in testing framework with ``#[test]`` attributes and the ``cargo test`` command.
  * **Python:** Use ``pytest`` frameworks.
  * **C++:** Use Google Test frameworks.
* **Integration Testing:** Verify the interaction between different components or modules.
    For integration testing, the ITF (Integration Test Framework) is used.

    For more information, see ``[TODO: Link to ITF documentation once available. Related feature request is #599]``.
* **Platform Testing:** Test the platform with configured features as a whole.
* **Regression Testing:** Ensure that changes do not introduce new defects.
  Automate regression tests where possible as they will get executed as part of the CI.
* **Performance Testing (when applicable):** Evaluate the performance characteristics of the code,
  such as execution time, memory usage, and resource utilization.
* **Tool Qualification Testing:** Test the platform tools based on their tool requirements to achieve tool qualification.


General Traceability Concept
============================

To allow a traceability of code to a written requirement, unit tests are linked to other unit
tests or component tests. This linking is done using metatags. This is also true for component
integration tests linking to the component architecture.

Component tests are linked to component requirements directly.

Traceability of feature integration tests shall be established through linking those test cases to
feature requirements and architecture as features describe the integrated behavior of all components.

Traceability of platform integration tests shall be established through linking those test cases to
stakeholder requirements as stakeholder requirements describe the platform behavior.

Requirements always include Assumptions Of Use.

A more detailed description of how to link code to requirements is available here: :need:`gd_req__link_tests`

Workflow for Verification Guidance
----------------------------------

.. _requirement_verification_workflow:

.. figure:: ./_assets/requirements_workflow_verification.drawio.svg
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

So if the content of the requirement is altered also the hash will change making it necessary to
revisit the linkage of all test cases to the requirement again.

If the status of the linked test case and the linkage document is valid the attribute *testcovered* shall be set to *YES* during the Sphinx Build.
Further information can also be depicted from the :ref:`requirements_engineering` process.

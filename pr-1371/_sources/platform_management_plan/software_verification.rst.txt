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

.. document:: Software Verification Plan
   :id: doc__verification_plan
   :status: draft
   :safety: ASIL_B
   :security: YES
   :tags: platform_management
   :realizes: wp__verification_plan

Software verification
*********************

Purpose
=======

The present document describes the plan for software integration and verification of the project. It intends to give
an overview by linking to other relevant sources and provide further information about the verification and testing
activities.

Main purpose of this document is to show the objectives, approaches, and strategies that are defined to contribute to
the overall quality of the software project. The target groups of this document are mainly :need:`rl__contributor`
and :need:`rl__committer`.

Objectives and scope
====================

Objectives
----------

The overall objectives of the projects software integration and verification activities are the following:

#. **Correctness** - Verify that the software platform and its modules perform their intended functions correctly and
   produce the expected results.
#. **Completeness** - Ensure that all specified requirements have been implemented.
#. **Reliability** - Confirm that the software operates reliably under specified conditions and can handle errors
   properly.
#. **Performance** - Assess the software's performance to ensure it meets the required performance criteria, such as
   response time and throughput.
#. **Maintainability** - Check that the software is maintainable, with clear documentation and code.
#. **Compliance** - Ensure that the software complies with defined processes and guidelines of the project.
#. **Traceability** - Verify that all requirements are traceable through the development process and that changes are
   properly managed and documented according to the processes defined in this project.

Verification scope and constraints
----------------------------------

The software verification aspects described in this document focus on the verification of the software platform
and modules developed within this project. The integration of the platform on a target device and the respective
verification and validation should be considered by the distributor of the platform. On target integration tests that
are running on a reference hardware in context of this project can be taken as a starting point.

Risks and mitigation
--------------------

Potential risks that derived from the verification activities and their respective mitigation measures are handled by
the :doc:`project_management`.

Schedules
---------

The integration of software elements is driven by change requests and their respective
:need:`doc_getstrt__change_process` model. The contribution of a feature itself implies that it gets fully
verified.

Approach
========

General approach
----------------

The above defined objectives are supposed to be achieved by the following approaches.

The projects infrastructure is highly driven by a Continuous Integration (CI) methodology. Thus, not just the
integration but also the verification approaches of the project are following that. Another aspect is the fact that
software build and verification processes are fully automated. Software elements, infrastructure, tests, and
documentation are defined as code. The following sections provide more details about the software integration as well
as the software verification.

Software integration
--------------------

The already mentioned approach of Continuous Integration means that software integration is performed with each fully
automated software build at any time.

The following types of integrations are applicable:

#. **New software elements** get integrated according to the :need:`doc__contr_guideline`
#. **Fixes of defects** get integrated based on their prioritization described by the
   :doc:`problem_resolution`.
#. **Changes** get integrated based on the :need:`wf__change_create_cr` and will follow
   the :need:`doc__pull_request_guideline` as any other artifact.

Levels of integration and verification
--------------------------------------

There are the following different levels of integration and verification defined:

1. Software unit (incl. detailed design) and component verification to verify the integration of
   units to a component and also the integration of smaller component(s) to a complex component based on

   #. detailed design and
   #. component architecture and
   #. component requirements

2. Software feature verification to verify the integration of components to a feature based on

   #. feature architecture and
   #. feature requirements

3. Platform testing (on reference hardware)

   #. Stakeholder requirements


  **Note:** These three levels translate to the levels of ISO 26262 part 6 clauses 9 to 11. The platform
  testing will be executed by the integrator. S-CORE project only executes tests on reference hardware.
  These tests serve as an optional base for the integrator and will also be part of the
  :need:`wp__verification_platform_ver_report`, but more on an informative character. The full scope
  of clause 11 is tailored out accordingly for S-CORE. Practically, this means S-CORE will implement
  Platform Integration Test of stakeholder requirements for demonstration, but these are not intended to completely
  covering all stakeholder requirements.

Verification Methods
--------------------

A verification is based on different methods. The derivation of test cases can also be based on certain methods. An
overview of the different methods that are applicable in the project are given in this section. Usually the defined
methods are not applied on each verification level. Due to that the following tables contain a column that defines the
applicable level. Another column defines if a respective method is supposed to be applied if the linked references are
QM or ASIL B relevant.

Automated test cases should contain further information about which methods have been applied. The corresponding
guidance is given here: :need:`gd_guidl__verification_guide`. The identifier of the respective
method is to be used as meta data (*TestType* and *DerivationTechnique*).

.. list-table:: Software verification methods (TestType)
   :header-rows: 1
   :align: center

   * - Methods
     - Identifier
     - Applicable on level
     - Applicable for QM / ASIL B
   * - Static Code Analysis
     - static-code-analysis
     - 1, -, -
     - QM & ASIL B
   * - Structural Statement Coverage (Code coverage)
     - structural-statement-coverage
     - 1, -, -
     - QM & ASIL B
   * - Structural Branch Coverage (Code coverage)
     - structural-branch-coverage
     - 1, -, -
     - QM & ASIL B
   * - Walkthrough
     - walkthrough
     - 1, 2, 3
     - QM
   * - Inspection
     - inspection
     - 1, 2, 3
     - ASIL B
   * - Interface Test
     - interface-test
     - 1, 2, -
     - QM & ASIL B
   * - Requirements-based Test
     - requirements-based
     - 1,  2, -
     - QM & ASIL B
   * - Resource Usage Evaluation (only on reference environment)
     - resource-usage
     - -, 2, -
     - QM & ASIL B


For QM software some of the methods may be executed with less rigor compared to safety-critical elements.
These may be interface testing or resource usage evaluation, in case there is an argument for
sufficient freedom from interference with safety critical software parts.

Static code analysis is part of the :need:`wp__sw_implementation`.

As an additional measure the resource usage evaluation ``resource-usage`` should also be considered
for level 3 testing as this is the level executed also on reference hardware with the integrated
platform. This can help to identify resource constraints on "system" level from a security and safety
perspective.

Additionally, while ``requirements-based`` testing is not mandatory to cover 100% of the stakeholder
requirements, where demos or test cases suffice to verify stakeholder requirements the traceability
should be established. The tailoring is also explained in the :need:`doc__platform_safety_plan`.

The following test methods are optional for lower safety integrity levels, but may become required
at higher levels:

   #. Control Flow Analysis (``control-flow-analysis``):

      Most beneficial for testing level 1 and 2.
   #. Data Flow Analysis (``data-flow-analysis``):

      Most beneficial for testing level 1 and 2.
   #. Fault Injection (``fault-injection``):

      Most beneficial for testing level 2.
   #. Structural Function/Call Coverage (``struct-func-cov`` & ``struct-call-cov``)

      Most beneficial for testing level 2.


Test Derivation Methods
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Test case derivation methods (DerivationTechnique)
   :header-rows: 1
   :align: center

   * - Methods
     - Identifier
     - Applicable on level
     - Applicable for QM / ASIL B
   * - Analysis of Requirements
     - requirements-analysis
     - 1, 2, 3
     - QM, ASIL B
   * - Analysis of Boundary Values
     - boundary-values
     - 1, 2, -
     - ASIL B
   * - Analysis of Equivalence Classes
     - equivalence-classes
     - 1, 2, -
     - ASIL B
   * - Fuzzy Testing (focus security)
     - fuzz-testing
     - 1, 2, -
     - QM, ASIL B

The ``fuzz-testing`` should especially be taken into account to increase security of the software.

For non-safety-critical(QM) software parts, you can generally reduce the rigor of the
testing approaches, but cannot omit them completely. It may be possible to reduce the
number of boundary-values tested based on a risk assessment and focus on impactful boundaries.
Similar for the equivalence-classes the focus can be put on more likely classes such as
invalid classes, empty/null/zero values, system limits. Equivalence Classes should be
supplemented by Boundary Value Analysis.

The following test derivation methods are optional, but may become required at higher safety levels:

   * Error Guessing derived from knowledge or experience of the contributor valid for all test levels
     indicated by ``error-guessing`` as derivation technique.
   * Explorative Testing (based on platform integration use cases) for feature and platform testing level
     indicated by ``explorative-testing`` as derivation technique.

Quality criteria
----------------

The quality criteria of the software verification activities are defined at the following table. The defined goals are
to be reached with every contribution.

.. list-table:: Quality criteria and respective goals
   :header-rows: 1
   :align: center

   * - #
     - Criterion
     - Goal for QM
     - Goal for Safety
   * - 1
     - Structural Statement Coverage
     - 85%
     - 100%
   * - 2
     - Structural Condition Coverage
     - 85%
     - 100%
   * - 3
     - Verification coverage of software detailed design (test coverage)
     - 100%
     - 100%
   * - 4
     - Verification coverage of software architecture design (test coverage)
     - 100%
     - 100%
   * - 5
     - Verification coverage of software requirements specifications (test coverage)
     - 100%
     - 100%
   * - 6
     - Relative amount of executed tests
     - 100%
     - 100%
   * - 7
     - Relative amount of failed tests
     - 0%
     - 0%

Further quality goals are defined in section :doc:`quality_management`.

Coverage of detailed design
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Beside :need:`wp__verification_comp_int_test` and :need:`wp__verification_sw_unit_test` the
following aspects define the coverage of detailed design.

- Statement/Branch/Path coverage as defined by their specific thresholds
- Static analysis and Linting
- :need:`wp__sw_implementation_inspection` for safety-critical implementation

Coverage of architectural design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Beside :need:`wp__verification_comp_int_test` and :need:`wp__verification_feat_int_test` the
following aspects define the coverage of the architectural design.

- :need:`wp__sw_arch_verification` - done by walkthrough (QM) or inspection (safety-critical parts)
- :need:`wp__sw_component_fmea` and :need:`wp__sw_component_dfa` for safety-critical parts
- :need:`wp__feature_fmea` and :need:`wp__feature_dfa` for safety-critical parts

Each architectural element has at least one test case linked with attribute "fully verified" or
multiple test cases with attribute "partially verified".

Coverage of software requirements specifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a release all ``valid`` requirements need to have a complete test coverage of linked test cases.


Test development
----------------

The verification steps as well as the development of test cases is done along with the implementation
of code. A full automation of tests should be achieved and the derived test cases should contain meta
data that gives further information as defined in :need:`gd_req__verification_link_tests`. The list of
relevant work products is shown above (as part of the development of the product).

The different environments that can be used for the test development are defined below.

Pre-existing test cases
^^^^^^^^^^^^^^^^^^^^^^^

The recommendations according to the :need:`gd_guidl__verification_guide` for pre-existing test
cases is followed. Any pre-existing test case (e.g. from OSS components) is reviewed and adopted
to follow the :need:`gd_guidl__verification_specification` and :need:`gd_req__verification_link_tests`.

Test execution and result analysis
----------------------------------

The execution of the tests is based on a full automation defined by build pipelines. The analysis of the test results
needs to be performed by the contributor.

Test selection and regression testing
-------------------------------------

All existing test cases should be executed within continuous integration pipelines to verify initially developed
components or software changes. A specific selection of sub sets is not planned. The fact that all existing and
automated tests get executed continuously covers the approach to identify regressions.

Work products and traceability
------------------------------

The traceability between verification relevant work products is one of the defined objectives.
An overall overview of the different work products and their relationship is given in project
context - see :need:`wp__verification_plan`.

The work products are related to verification can be found in :need:`wp__verification_plan`.

The link between a test specification and the respective requirement or design specification is given by the
identifier of the reference annotated to the verification specification.

Environments and resources
==========================

Roles
-----

In general, the different roles of this project are defined within the Process documentation:
:need:`rl__project_lead`. The following roles are crucial to comply with the aspects defined in this
document:

#. The :need:`rl__contributor` needs to make sure that the objectives of the software integration and verification are
   fulfilled when contributing to the project.
#. The :need:`rl__committer` needs to verify that the contributor has fulfilled the expected objectives.

In this way roles are followed as defined in :need:`doc_concept__verification_process`.

Independence of verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As there are no separated roles for a software developer and test developer with :need:`rl__contributor` and
:need:`rl__committer` it is important to achieve independence. This is done by having different
people responsible for the test implementation and the actual code which gets tested.

The following test level fall in the responsibility of the :need:`rl__testing_community`:

* :need:`wp__verification_comp_int_test`
* :need:`wp__verification_feat_int_test`
* :need:`wp__verification_platform_int_test`

Still a :need:`rl__contributor` of one function in a component doesn't prevent them from writing tests
for other functions they do not own.
Independence is achieved by the establishment of :need:`rl__testing_community` performing reviews.

The following test level fall in the responsibility of the :need:`rl__contributor`:

* :need:`wp__verification_sw_unit_test`

Unit tests can be the developed by the same :need:`rl__contributor` who also contributed the unit code.
A level of independence is achieved as the review process demands to have a review by a :need:`rl__committer`
different to the author of a Pull Request. This is also described in process requirement :need:`gd_req__verification_independence`.

Note that, each :need:`rl__contributor` of the project acts in a publicly visible space where also
others see the contribution and have the possibility to perform additional reviews independent from
the :need:`rl__committer` and :need:`rl__testing_community`.

Tools
-----

The list of the tools mentioned here does not reflect the full list of tools that are used for the whole project. Only
tools that have an important impact on the test execution and reporting are given here. A full list of tools (and their
versions) is maintained by :doc:`tool_management`. The aim of the given list here is to provide a better picture of
the software test strategy and corresponding processes.

.. rubric:: Bazel

The main build environment of the project is based on `Bazel <https://bazel.build>`__. It it used to build software
components, documentation, and automated tests.

.. rubric:: GoogleTest (gtest)

The software components of the project written in C++ are unit tested with the help of
`GoogleTest <https://google.github.io/googletest/>`__.

.. rubric:: gcov/gcovr

The structural coverage reached by unit testing in the project is evaluated by the gcov/gcovr tool chain
`gcovr <https://github.com/gcovr/gcovr>`__ - gcov is part of the GNU compiler collection (gcc).

Note that gcov/gcovr supports several coverage metrics:

- "statement" - used in S-CORE for the structural-statement-coverage method
- "decision" - used in S-CORE for the structural-branch-coverage method
- "branch" - used in S-CORE to support manual analysis of the code coverage if the "decision"
  coverage is reported as "cannot be determined" by the tooling. As the "branch" coverage on target
  is determined by the tool as object code coverage and as the compiler adds object branches for
  fast evaluation of complex conditions in decisions, this is more than required by the
  structural-branch-coverage method.

.. rubric:: Integration Testing Framework (ITF)

The integration of software components can be verified with the help of the ITF. It allows the definition and execution
of test based on `pytest <https://pytest.org>`__.

.. rubric:: Rust

The platform developed in this project supports `Rust <https://www.rust-lang.org>`__ as a programming language. Its
built-in test framework is used to test respective software components.

Verification setups and variants
--------------------------------

Different test frameworks get used to verify software components and their integration into the platform (see Tools
section above). Driven by that the following test setups can be derived:

#. GoogleTest
#. Rust
#. ITF

All defined setups are used to run automated tests within continuous integration pipelines.


Test execution environment and reference hardware
-------------------------------------------------

The platform is consisting solely on features that are considered as "middleware" as the layer
above the hardware abstraction layer. The platform itself doe not require to be running on
a specific hardware. It integrates with an Posix Operating System which is the first level of
abstraction to the physical hardware.

The simulation environment will be based on x86 and arm64 architecture, to be close to later
target hardware.

The integration of the platform on a target device and the respective verification and validation
should be considered by the distributor of the platform. On target integration tests that are
running on a reference hardware in context of this project can be taken as a starting point.

The reference hardware is not yet decided.

Reference hardware interaction with infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the reference hardware is decided, this section will inform about the location of the
reference hardware, how it interacts with the CI system and how access rights are handled.
This includes physical maintenance as well as virtual access.

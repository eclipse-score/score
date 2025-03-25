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

Verification types and methods are described in the :need:`doc_concept__verification__process` in
section :ref:`verification_concept_types_methods`. This guide helps to get an understanding what
the different methods and derivation techniques mean and how to create test cases using the same.

Methods
^^^^^^^

Fault Injection
"""""""""""""""

As part of ``fault-injection`` instrumentation of source code is the preferred method.
While it is theoretically possible to modify binaries, this is not considered as it is hard to
maintain and should only be done, when no source code access is possible. Therefore, this is not
applicable to software provided as open source.

Practical approaches are:

  - **Conditional Fault Injection with Macros**

    Use preprocessor macros and conditional compilation to enable or disable fault injection code.
    This makes it easy to turn fault injection on during testing and off during normal operation.
  - **Function wrapping**

    Create wrapper functions around critical functions to inject faults before or after the original
    function call.
  - **Instrumentation with Error Code Injection**

    Modify the code to explicitly return error codes under certain conditions to simulate failures.
    This is especially useful if the components use a standardized error handling mechanism.
  - **Data Corruption**

    Introduce code to corrupt data structures or variables in memory.

Interface Test
""""""""""""""
Interface testing is a type of software testing that focuses on verifying the proper communication
and data exchange between different software components or features. It's about ensuring that the
interfaces (the points where different parts of the system connect and interact) are working
correctly and reliably. This includes validating data formats, protocols, error handling, and
overall communication integrity.

It can be distinguished between internal and external interfaces. Internal interfaces are best covered
on unit level. External interfaces work best on component integration and feature level.

Types of ``interface-test`` are:

  - **Parameter Passing Tests**

    Verify that parameters are passed correctly between components (data types, ranges, units).
  - **Data Format Tests**

    Ensure that data is formatted correctly according to the interface specification
    (e.g., byte order, data alignment, encoding).
  - **Protocol Tests**

    Verify that the communication protocol is implemented correctly (e.g., message sequencing,
    checksums, error handling).
  - **Error Handling Tests**

    Test how the software handles communication errors (e.g., lost messages, corrupted data, timeouts).
  - **Stress Tests**

    Stress the interfaces to see how they behave under heavy load (e.g., sending a large number of
    messages simultaneously).
  - **Security Tests:** (Relevant for code interacting with security critical parts)

    Verify that the interfaces are protected against unauthorized access and data breaches.
  - **Timing and Performance Tests** (Relevant for realtime constraints)

    Measure the latency and throughput of the interfaces. This is mainly on integration level and is
    hard to have reasonable testing in the reference implementation

Derivation Techniques
^^^^^^^^^^^^^^^^^^^^^

Boundary Values
"""""""""""""""

Boundary Value Analysis (BVA) is a software testing technique where test cases are designed to
focus on the boundaries of input domains. The underlying principle is that errors tend to cluster
at or near the boundaries of input values. Instead of randomly selecting test values, BVA
systematically targets these boundary conditions, increasing the likelihood of finding defects.
BVA is often considered a type of black-box testing, meaning it doesn't require knowledge of the
internal code structure.

Examples to derive the scope of middleware layers following ``boundary-values``

    - **Sensor Ranges**

      For example temperature, pressure, and acceleration sensors have minimum and maximum values they can report.
    - **Control Signals**

      PWM duty cycles, motor speeds, valve positions have upper and lower limits.
    - **Communication Protocols**

      For example CAN message IDs, data lengths, signal values have boundaries defined by the protocol specification.
    - **Memory Allocation**

      Buffer sizes, data structures have defined limits.

How to perform the analysis:

    **1. Identify Input Variables**

    List all the input variables (parameters) of the component or function you want to test.

    This includes:

    - Input parameters of functions
    - Data received from sensors
    - Data received from other ECUs (via CAN, Ethernet, etc.)
    - Configuration parameters

    **2. Determine Boundaries**

    For each input variable, identify its boundaries:

    - **Minimum Value**

      The smallest possible value.
    - **Maximum Value**

      The largest possible value.
    - **Nominal/Typical Value**

      A representative value within the normal operating range. This is *not* strictly required
      for BVA but can be helpful for context.
    - **Consider Data Types**

      Use appropriate data types to define the variables and boundaries.
      ``int8_t`` (signed 8-bit integer), ``uint16_t`` (unsigned 16-bit integer), ``float``, ``double``, etc.

    **3. Define Test Values**

    For each input variable, create test values using the following:

    - **Minimum Value**
    - **Maximum Value**
    - **Just Above the Minimum Value** (Minimum + 1 or next representable value)
    - **Just Below the Maximum Value** (Maximum - 1 or previous representable value)
    - **A Value Within the Nominal Range** (Although not strictly *boundary* it provides a basis for comparison).

    **4. Design Test Cases**

    Create test cases that combine the test values for all input variables.

    Follow these guidelines:

    - **Single Variable Variation:**

      Vary one input variable at a time, keeping other variables at their nominal values.
      This helps isolate the impact of each variable.
    - **Combination Tests**

      In some cases, you may want to create test cases that combine boundary values for multiple
      input variables simultaneously. This is especially important if there are dependencies
      between the variables.

Equivalence Classes
"""""""""""""""""""
Equivalence Classes or also called Equivalence Partitioning (EP) is a software testing technique
that divides the input domain of a program into equivalence classes or partitions. The principle
is that all values within a single partition are treated equivalently by the software. Therefore,
only one test case from each partition is needed to achieve adequate test coverage. This reduces
the number of test cases significantly compared to testing all possible inputs.

Equivalence Classes provide a different perspective compared to Boundary Value Analysis.

The following perspectives are included in ``equivalence-classes``:

  - **Reduce Test Case Volume**

    Components may have complex input domains. EP allows you to focus testing efforts on
    representative values within each partition, drastically reducing the number of test cases needed.
  - **Improve Test Coverage**

    By testing at least one value from each partition, you ensure that you've covered all the
    different behaviors of the software.
  - **Address Different Input Types**

    EP is applicable to various input types, including numerical ranges, enumerated values,
    boolean flags, and more.
  - **Find Different Types of Errors**

    While BVA focuses on boundary-related errors, EP helps find errors related to how the software
    processes different categories of inputs.

How to perform the analysis:

    **1. Identify Input Variables**

    List all the input variables (parameters) of the component or function you want to test.

    This includes:

    - Input parameters of functions
    - Data received from sensors
    - Data received from other system elements (via Ethernet, CAN, etc.)
    - Configuration parameters

    **2. Divide into Equivalence Classes**

    For each input variable, divide the input domain into equivalence classes.

    Consider:

    - **Valid Input Classes**

      Classes that contain valid input values according to the specifications.
    - **Invalid Input Classes**

      Classes that contain invalid input values (out of range, incorrect data type, etc.).
    - **Special Cases**

      Classes representing specific or unusual input values that might trigger special behavior
      in the software.

    **3. Define Test Values**

    Choose one representative test value from each equivalence class. It doesn't matter *which*
    value you choose, as long as it's within the class. As an easy example consider the motor speed.
    Test Values could be:

    - Class 1 (Valid): 50 (A value within the valid range)
    - Class 2 (Below Minimum): -10
    - Class 3 (Above Maximum): 150

    **4. Design Test Cases**

    Create test cases using the representative values from each equivalence class.
    Aim to cover all classes in your test suite.

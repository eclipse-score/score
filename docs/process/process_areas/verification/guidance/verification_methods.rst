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

.. _verification_methods:

Verification methods and derivation techniques
----------------------------------------------

This guide helps to get an understanding what the different methods and derivation techniques mean
and how to create test cases using the same.

Methods
^^^^^^^

.. gd_method:: Verification Methods
   :id: gd_meth__verification__methods
   :status: valid

   Following methods are explained

   * :ref:`Fault Injection <ver_fault>`
   * :ref:`Interface Test <ver_interface>`
   * :ref:`Structural Coverage <ver_structural>`

.. _ver_fault:

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

.. _ver_interface:

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

.. _ver_structural:

Structural Coverage
"""""""""""""""""""

Structural coverage is a white-box testing technique used to check if the testing is sufficient by
analyzing if code constructs were called during testing.

In S-CORE we do both:

* **Statement Coverage:** Measures whether each executable source code statement has been executed.

* **Branch Coverage:** Measures whether each possible branch (decision outcome) in the code has
  been executed. It focuses on the overall boolean result of a decision point (if, while, etc.).

S-CORE evaluates this coverage using the compiler selected for the target reference platform.

If a sufficient structural coverage is not reached then additional test cases are added.
What is sufficient and how to determine the coverage is defined in the :need:`doc__verification_plan`.


Derivation Techniques
^^^^^^^^^^^^^^^^^^^^^

.. gd_method:: Verification Derivation Technique
   :id: gd_meth__verification__derivation
   :status: valid

   Following derivation techniques are explained

   * :ref:`Boundary Values <ver_boundary>`
   * :ref:`Equivalence Classes <ver_equivalence>`
   * :ref:`Fuzzy Testing <ver_fuzzy>`

.. _ver_boundary:

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

.. _ver_equivalence:

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

.. _ver_fuzzy:

Fuzzy Testing
"""""""""""""

Fuzzy Testing, often called Fuzz Testing, is a software testing technique that involves providing
invalid, unexpected, or random data as inputs to a component or system to detect defects. The goal
of fuzzy testing is to expose unhandled exceptions, memory leaks, assertion failures, and other
critical issues by generating semi-random inputs and observing the system's behavior.

The following perspectives are included in ``fuzz-testing``:

   **Detect Security Vulnerabilities**

   By feeding malformed or unexpected inputs, fuzzy testing can reveal security vulnerabilities
   like buffer overflows, SQL injections, and other input validation issues.

   **Uncover Edge Cases**

   Fuzzy testing can discover edge cases that might not be covered by traditional testing methods,
   as it generates inputs that developers might not have anticipated.

   **Automate Input Generation**

   Instead of manually creating test inputs, fuzzy testing automates the process, allowing for a
   much larger number of test cases to be executed.

   **Improve Robustness**

   By exposing the system to a wide variety of inputs, fuzzy testing helps ensure that the
   software can handle unexpected situations gracefully.

How to perform fuzzy testing:

   **1. Identify Target Functions** Determine which functions or interfaces are suitable for
   fuzzy testing, focusing on those that process external inputs.

   **2. Define Input Structure** Understand the basic structure or format of valid inputs to
   create effective fuzzers that can produce semi-valid inputs.

   **3. Generate Fuzzy Inputs** Create inputs that are slightly malformed or unexpected, either
   through complete randomization or by mutating valid inputs.

   **4. Monitor System Behavior** Execute the system with fuzzy inputs and monitor for crashes,
   hangs, memory leaks, or other unexpected behaviors.

   **5. Analyze and Fix Issues** When a problem is detected, analyze the input that caused it
   and fix the underlying issue in the code.

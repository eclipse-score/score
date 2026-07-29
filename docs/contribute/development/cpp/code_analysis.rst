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

Code Analysis C++
#################

.. document:: Static Code Analysis C++
   :id: doc__cpp_code_analysis
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_development_plan[version==1]

   Guideline for Static Code Analysis

Static Code Analysis
====================
In order to fulfil the S-CORE related standard requirements a concept for *Static Code Analysis* needs to be established. Input for the analysis is based upon *MISRA* and *ISO26262* standards in accordance to the :need:`doc__cpp_coding_guidelines`.

Checking those rules can partially be automated and implemented by a combination of different tools. Thus a mapping needs to be established which provides a linkage of all *MISRA* requirements to the respective tool requirements/rules. For *MISRA C++:2023* this mapping is established: :need:`here <doc__cpp_misra2023_rule_mapping>`

.. needuml::

   object "Static Code Analysis" as static
   object "Clang-Tidy" as ct
   object "Compiler Warnings" as cw
   object gcc
   object clang
   object "Coverity" as cov

   static --> ct
   static --> cw
   cw --> gcc
   cw --> clang
   static --> cov

One of the reasons why this tooling setup is selected is, that it was already proven in use. Also with a combination of the two compilers a lager set of findings could be addressed.

If for some technical reason any *MISRA* finding can not be addressed it needs to be justified appropriately. This means that it needs to be explained why it does not have any impact on the safety of the code and finally documented within the source code. A detailed workflow will follow on demand.

Dynamic Code Analysis
=====================
A dynamic code analysis is not explicitly required by any S-CORE related standards. However to provide a sufficient good SW quality following tools should be used to catch most common errors:

.. needuml::

   object "Dynamic Code Analysis" as dynamic
   object "Sanitizers" as sanitizers
   object "gcc" as gcc
   object "ASAN/LSAN" as asan
   object "TSAN" as tsan
   object "UBSAN" as ubsan
   object "Memcheck" as memcheck

   dynamic --> sanitizers
   sanitizers --> gcc
   gcc --> asan
   gcc --> tsan
   gcc --> ubsan
   sanitizers --> memcheck

Following sections provide a short overview of the most important features of each applied tool:

Memcheck
--------
* Use of non initialized memory
* Read- and write access on released memory
* Writing out of bounds of memory sections
* Memory Leaks

`Full description: Memcheck <https://valgrind.org/docs/manual/mc-manual.html#mc-manual.overview>`_

Thread Sanitizer (TSAN)
-----------------------
* Detect Data Races between Threads

`Full description: TSAN <https://github.com/google/sanitizers/wiki/threadsanitizercppmanual>`_

Undefined Behaviour Sanitizer (UBSAN)
-------------------------------------
Detect undefined behaviour, e.g.

* array out of bounds
* null pointer dereferencing
* integer overflow
* conversions which would lead to overflow

Adress/ Leak Sanitizer (ASAN/LSAN)
----------------------------------

If both tools are combined at runtime memory leaks and the corresponding address can be investigated.

Code Coverage
=============

As required by the verification guideline code coverage needs to be calculated for the code which is used in the project. Coverage is calculated on the host using LLVM's source-based coverage:

* Coverage is calculated on the host via clang/llvm. This method is also used for the reporting.

Since ``qcc`` does not support LLVM's source-based coverage instrumentation, coverage is not collected on the QNX target. LLVM's source-based coverage natively supports MC/DC, which is required for the higher ASIL levels.

To enable this, following tools are used:

.. needuml::

   object "Coverage" as coverage
   object "gtest" as gtest
   object "llvm-cov + llvm-profdata" as llvm
   object "host" as host

   coverage --> gtest
   gtest --> llvm
   llvm --> host

Argumentation: Host-based Coverage with Target Test Execution
------------------------------------------------------------

Measuring code coverage exclusively on the **Linux host** (via LLVM) is considered sufficient for safety certification, provided that a **two-step verification** is performed to demonstrate equivalence on the target:

#. **Quantitative Verification (Host):** The complete test suite is executed on the Linux host with code coverage enabled. This demonstrates that the test cases are structurally complete (100% C0/C1 coverage) and that no dead code exists.
#. **Qualitative Verification (Target):** The identical test suite is executed on the **QNX target**, but with code coverage instrumentation turned off. This demonstrates that the software compiles, links, and behaves identically on the real target hardware (correctness of execution, no compiler/linker optimization bugs, no endianness or memory alignment issues).

This approach satisfies *ISO 26262-6* for *ASIL_B* for the following reasons:

* **Identical Test Results:** Passing 100% of the tests on both the host and the target demonstrates that the control flow under test is identical.
* **Mitigation of Target Instrumentation Risks:** Turning off coverage instrumentation on the target is recommended for embedded systems, as active instrumentation alters the timing behavior, memory footprint, and compiler optimizations on the target. Testing the uninstrumented code on QNX ensures that the actual production binary is verified (mitigating "Heisenbugs").
* **Equivalence Justification:** The host-based coverage measurement is justified by confirming that no platform-specific code paths (e.g., ``#ifdef QNX`` blocks) are bypassed. Any target-specific hardware abstraction layer (HAL) is verified separately via system-level integration tests.

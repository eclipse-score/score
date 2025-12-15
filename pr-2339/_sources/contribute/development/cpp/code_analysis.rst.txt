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
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_development_plan

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

Coverage
========

As required by the verification guideline coverage needs to be calculated for the code which is used in the project. Therefore two approaches should be available:

* As a quick solution it is possible to calculate the coverage on the host via gcc.
* But for a more accurate statement coverage can also be calculated with the qcc compiler with the appropriate libraries and POSIX interfaces. This method will also be used for the reporting.

To enable this, following tools are used:

.. needuml::

   object "Coverage" as coverage
   object "gtest" as gtest
   object "gcov + gcovr" as gcov
   object "host" as host
   object "QNX" as qnx

   coverage --> gtest
   gtest --> gcov
   gcov --> host
   gcov --> qnx

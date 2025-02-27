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

.. gd_guidl:: Static Code Analysis
   :id: gd_guidl__cpp__code_analysis
   :status: valid
   :complies: std_req__iso26262__software_1, std_req__iso26262__software_2, std_req__iso26262__software_3, std_req__iso26262__software_31

   Guideline for Static Code Analysis

Static Code Analysis
====================
In order to fulfil standard requirements a concept for *Static Code Analysis* needs to be established. Input for this is based upon *MISRA* and *ISO26262*.

*MISRA* introduces coding rules which need to be implemented and enforced. Checking those rules can partially be automated and implemented by a combination of different tools. Thus a mapping needs to be established which provides a linkage of all *MISRA* requirements to the respective tool requirements/rules. For *MISRA C++:2023* this mapping is established: :need:`here <gd_guidl__cpp__misra2023_rule_mapping>`

Additionally several other SW Analyses are required by *ISO26262*. Together with the *MISRA* rules those can be fulfilled by following toolset:

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

Dynamic Code Analysis
=====================
A dynamic code analysis is not explicitly required by a standard. However to provide a sufficient good SW quality following tools should be used to catch most common errors:

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

As required by the verification guideline coverage needs to be calculated for the code which is used in the project. For a release the coverage needs to be calculated on the target (QNX). However for development also a quicker approach on the host shall be available.

To enable this, following tools shall be used:

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

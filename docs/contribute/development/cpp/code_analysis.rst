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

In Bazel-based development, this does not imply that every build uses the same compiler configuration. Normal host builds may use the default host compiler/toolchain, while coverage builds select a dedicated host configuration with LLVM source-based instrumentation enabled. The resulting raw profiles are merged with ``llvm-profdata`` and evaluated with ``llvm-cov``.

Since ``qcc`` does not support LLVM's source-based coverage instrumentation, coverage is not collected on the QNX target. LLVM's source-based coverage natively supports MC/DC, which is required for the higher ASIL levels.

LLVM's source-based coverage is preferred over ``gcov``-based coverage for the following reasons:


* **Precision with templates, generics and modern C++:** legacy GCC line-based coverage ``gcov`` is line-oriented, so with heavy templating, inlining and macros the mapping is coarse and multiple template instantiations collapse onto the same lines, producing imprecise or misleading results. LLVM's source-based coverage is region- and instantiation-based and therefore significantly more accurate for modern C++.
* **MC/DC support:** LLVM/clang supports MC/DC natively (``-fcoverage-mcdc``), which is required for the higher ASIL levels.

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
-------------------------------------------------------------

Measuring code coverage exclusively on the **Linux host** (via LLVM) is considered sufficient for safety certification, provided that a **two-step verification** is performed to demonstrate equivalence on the target:

#. **Quantitative Verification (Host):** The complete test suite is executed on the Linux host with code coverage enabled. This demonstrates that the test cases are structurally complete (100% C0/C1 coverage) and that no dead code exists.
#. **Qualitative Verification (Target):** The identical test suite is executed on the **QNX target**, but with code coverage instrumentation turned off. This demonstrates that the software compiles, links, and behaves identically on the real target hardware (correctness of execution, no compiler/linker optimization bugs, no endianness or memory alignment issues).

This approach satisfies *ISO 26262-6* for *ASIL_B* for the following reasons:

* **Identical Test Results:** Passing 100% of the tests on both the host and the target demonstrates that the control flow under test is identical.
* **Mitigation of Target Instrumentation Risks:** The two-step verification deliberately splits the two concerns onto the environment best suited for each: the **host run is instrumented** (to measure structural coverage), and the **target run is uninstrumented** (to confirm the tests still pass on the real production binary). This is the same "measure coverage with instrumentation, then re-run without instrumentation to confirm behaviour" pattern applied across two environments. Running uninstrumented on QNX matters because active instrumentation alters timing behaviour, memory footprint and compiler optimizations on embedded targets (mitigating "Heisenbugs"). Note that ``qcc`` cannot produce LLVM source-based coverage, so an *instrumented* coverage run on the target is not an available option.
* **Equivalence Justification:** The host-based coverage measurement is justified by confirming that no platform-specific code paths (e.g., ``#ifdef QNX`` blocks) or QNX-only source files are silently bypassed by the host measurement. The reconciliation strategy for such code, and the process a developer uses to identify it, is described in `Handling Platform-Specific Code`_ below. Any target-specific hardware abstraction layer (HAL) is additionally verified via system-level integration tests.

Handling Platform-Specific Code
-------------------------------

Because structural coverage is measured on the **Linux host** while the QNX target is only tested for pass/fail, the coverage *baseline* (the set of source files and lines expected to be covered) differs between the two environments. Code that is strictly platform-specific therefore needs an explicit reconciliation strategy so that it neither skews the release metrics nor becomes unverified "dead" code in the safety case.

Three cases are distinguished.

Linux-only code (mocks, emulation, host utilities)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This code is compiled and executed only on the host and is absent on the QNX target. It must not contribute to the ASIL-B production coverage figures.

* Linux-only helper code and mocks are kept structurally separate from production code (e.g. under dedicated ``mock/`` or ``test/`` directories) and are classified as Quality Managed (QM) / test-support code.
* Such directories are excluded when the coverage report is generated, so this code is not part of the ASIL-B production coverage baseline and cannot inflate or deflate the reported figures.

QNX-only code inside mixed files (conditional compilation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For files that are compiled on the host but contain small target-specific blocks (e.g. guarded by ``#ifdef __QNX__``), those blocks are not compiled into the host binary and would otherwise appear as non-covered or non-existent regions.

* These target-only regions are marked with standardized coverage-exclusion markers understood by the coverage report generator, together with a justification stating that the region is executed and verified on the QNX target rather than on the host.
* The applicable exclusion markers and their justification format are governed centrally (rather than chosen per developer) so that exclusions remain auditable and consistent across repositories.

.. note::

   The exclusion-marker syntax must match the coverage tooling actually in use. Because coverage in S-CORE is produced by **LLVM source-based coverage** (``llvm-cov`` / ``llvm-profdata``), the marker mechanism supported by that toolchain (line/region exclusion) must be used; ``LCOV_EXCL_*`` markers from lcov/GCC workflows are *not* interpreted natively by ``llvm-cov`` and must not be assumed to work unless an ``lcov`` conversion/merge step is explicitly part of the pipeline.

QNX-only files excluded from the host build
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some modules or files are compiled **only** for QNX and cannot be built on the host at all (e.g. sources that call QNX-specific OS APIs). These would report 0% coverage in a host-only measurement.

* Such files are excluded from the **host structural-coverage baseline**, so they do not produce misleading false-negative 0% figures.
* Because ``qcc`` cannot produce LLVM source-based coverage, **no structural coverage can be obtained for these files**. This is a *justified deviation* from the unit-level structural-coverage objective, not a claim of equivalence: the residual risk is that unit-level statement/branch coverage evidence does not exist for this code.
* The deviation is compensated by verifying these files **on the QNX target** through requirements-based integration tests executed on the real hardware, and by arguing the safety case on the basis of a 100% pass rate of the associated functional requirements. Each such file/module and its compensating verification is recorded so the deviation is traceable and reviewable.

Identifying platform-specific code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A developer must be able to determine which code falls into the categories above; this cannot rely on manually reading source for ``#ifdef`` guards, because whole files may be excluded from the host build. The following mechanisms are used:

* **Build-set comparison:** The set of source files compiled for the host is compared against the set compiled for the QNX target. Files present only in the QNX build are, by construction, the "QNX-only files" case and are flagged automatically.
* **Explicit exclusion manifest:** Every host-coverage exclusion (whether a per-file exclusion or a within-file region marker) is recorded in a reviewable list, so the complete delta between the host coverage baseline and the full target code base is visible in one place rather than scattered across the sources.
* **CI gate:** The comparison and the manifest are checked in CI, so newly added QNX-only files or new conditional blocks that are not accompanied by a documented exclusion and a compensating target verification cause the quality gate to fail.

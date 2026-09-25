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

Host baseline
-------------

As required by the verification guideline code coverage needs to be calculated for the code which is used in the project. The basis of the code-coverage analysis is always the host system (Linux) using LLVM's source-based coverage with clang and ``llvm-cov``. This method is also used for the reporting.

In Bazel-based development, this does not imply that every build uses the same compiler configuration. Normal host builds may use the default host compiler/toolchain, while coverage builds select a dedicated host configuration with LLVM source-based instrumentation enabled. The resulting raw profiles are merged with ``llvm-profdata`` and evaluated with ``llvm-cov``.

The structural coverage metrics to be achieved and their ASIL-dependent recommendation (statement coverage, branch coverage and MC/DC as per ISO 26262-6:2018, Table 9) as well as the completion criteria are defined by the :need:`gd_guidl__verification_guide`. The concrete coverage percentage goals (e.g. 100% statement and branch coverage for safety-critical code and 85% for QM code) are listed in the quality criteria of the :need:`doc__verification_plan`. In practice, the line coverage reported by the LLVM tooling is used as the statement-coverage metric. Where the required coverage is not achieved, a rationale shall be provided and documented for the uncovered code, independent of whether the coverage is obtained on the host or on the target (ISO 26262-6:2018, 9.4.5).

Structural coverage on the target, in contrast to the host baseline, may be provided either by S-CORE (for example for a reference target) or by the integrator or distributor for the target on which the S-CORE software is integrated. Target structural coverage is needed to identify uncovered target-specific code paths, including those that could exhibit undefined behaviour on the target. Evidence for the absence of undefined behaviour itself is provided by the dynamic analysis tools (e.g. UBSAN) together with the target execution, not by structural coverage alone.

LLVM's source-based coverage is preferred over ``gcov``-based coverage for the following reasons:

* **Precision with templates, generics and modern C++:** legacy GCC line-based coverage ``gcov`` is line-oriented, so with heavy templating, inlining and macros the mapping is coarse and multiple template instantiations collapse onto the same lines, producing imprecise or misleading results. LLVM's source-based coverage is region- and instantiation-based and therefore significantly more accurate for modern C++.
* **MC/DC support:** LLVM/clang supports MC/DC natively (``-fcoverage-mcdc``). Per ISO 26262-6:2018, Table 9, MC/DC is highly recommended only for ASIL D and recommended for ASIL A to C, while branch coverage is the highly recommended metric for ASIL B and C.

The coverage measurement tools themselves (on the host the LLVM ``llvm-cov``/``llvm-profdata`` chain, on the target the tools of the chosen approach below) are subject to tool classification and, where applicable, tool qualification according to ISO 26262-8:2018, Clause 11.

To enable this, following tools are used:

.. needuml::

   object "Coverage" as coverage
   object "gtest" as gtest
   object "llvm-cov + llvm-profdata" as llvm
   object "host" as host

   coverage --> gtest
   gtest --> llvm
   llvm --> host

The structural coverage for the target used for integration, including target-specific code paths, has to be rationalized separately, as described in `Target coverage rationalization`_. Target execution tests and target structural-coverage results are separate verification evidence and shall not be treated as interchangeable.

Target coverage rationalization
-------------------------------

The host result described above is the baseline of the coverage analysis. For the target system, the coverage of the source code that actually runs on the target has to be rationalized on top of this baseline. Depending on how much the source code deviates between host and target and on the effort and availability of a solution for the target, a module or project may choose one of the following four approaches:

1. **Similarity argument (with or without manual review):** the host coverage result is reused for the target based on the argument that the source code executed on the target is equivalent to the source code covered on the host.
2. **Code coverage on the target with clang/llvm:** structural coverage is measured directly on the target using clang and ``llvm-cov``, i.e. the same source-based coverage method as on the host.
3. **Code coverage on the target with qcc + llvm-cov:** structural coverage is measured on the target using the QNX compiler ``qcc`` importing and analyzing the host coverage data together with ``llvm-cov``.
4. **Code coverage on the target with qcc + gcov:** structural coverage is measured on the target using the QNX compiler ``qcc`` together with ``gcov``.

The selection of the approach depends on the source-code deviation between host and target and on the effort and availability of the respective target solution:

* If there is no source-code deviation between host and target, approach 1 (similarity argument) can be chosen. Even in this case an equivalence justification shall be documented, because compiler and target differences (e.g. optimization, inlining, integer widths, alignment, library implementations) can affect the executed code independently of the source (ISO 26262-6:2018, 9.4.6 / 11.4.8).
* If there are only few local deviations (e.g. guarded by ``#ifdef __QNX__``), approach 1 with manual review and documentation of these specific locations shall be chosen.
* For larger deviations (different code paths or implementations between host and target, e.g. whole files compiled only for the target such as QNX-only files, or host-only code such as mocks), approach 2, 3 or 4 should be chosen for the target-specific code, provided the respective solution is available for the target system. Host-only code (e.g. mocks or emulation) is excluded from the safety-relevant coverage baseline. These three approaches differ only in the effort for tool classification/qualification, the tool quality, and the effort for infrastructure and workflow implementation.

Regardless of the chosen approach, differences between the host and target compilers and coverage tools can introduce side effects in the reported coverage output. Typical effects are: branches or regions that appear or disappear because of compiler-specific optimization, inlining or dead-code elimination; a different source-line-to-region mapping (e.g. ``gcov`` line-based versus ``llvm-cov`` region-based counting) leading to differing coverage percentages for the same source; additional or missing branches introduced by the instrumentation itself or by different standard-library implementations; and diverging results for template instantiations or target-specific ``#ifdef`` code paths. As a consequence, the same source can report different structural coverage depending on the compiler and coverage tool used. The validity of the code-coverage result is therefore rationalized by executing the unit tests with and without code-coverage instrumentation and across the relevant build configurations and target systems, and by demonstrating that the results are equivalent. This execution shall be performed as required by :need:`aou_req__platform__ut_execution_consistency`.

.. note::

   Identifying platform-specific code (in particular whole files compiled only for one platform) should not rely on manually searching for ``#ifdef`` guards. A reliable approach is a build-set comparison: the set of source files compiled for the host is diffed against the set compiled for the target (e.g. via ``bazel aquery``/``cquery`` per platform configuration or per-configuration ``compile_commands.json``); files present only in the target build are flagged as target-only. Within-file conditional regions can be detected by comparing the preprocessed output or the coverage region data of the two configurations. This build-set comparison and a corresponding reviewed exclusion list might become a requirement towards the infrastructure tooling to make the delta between the host baseline and the target code base visible and enforceable in CI.

   For example, the set of source files that participate in a build can be extracted per platform configuration with ``bazel aquery`` and then diffed:

   .. code-block:: bash

      # List the source inputs of all C++ compile actions for the host configuration.
      bazel aquery --output=jsonproto \
        --platforms=//path/to/platforms:x86_64_linux \
        'mnemonic("CppCompile", deps(//path/to:target))' \
        | jq -r '.artifacts[].execPath' | sort -u > host_sources.txt

      # Same for the target configuration.
      bazel aquery --output=jsonproto \
        --platforms=//path/to/platforms:qnx_aarch64 \
        'mnemonic("CppCompile", deps(//path/to:target))' \
        | jq -r '.artifacts[].execPath' | sort -u > target_sources.txt

      # Files compiled only for the target (candidates for target-specific coverage).
      comm -13 host_sources.txt target_sources.txt

      # Files compiled only for the host (e.g. mocks, excluded from the safety baseline).
      comm -23 host_sources.txt target_sources.txt

   Within-file conditional regions can be compared by preprocessing the same source with both toolchains and diffing the result:

   .. code-block:: bash

      clang -E -P path/to/file.cpp > host_preprocessed.cpp
      qcc  -E -P path/to/file.cpp > target_preprocessed.cpp
      diff host_preprocessed.cpp target_preprocessed.cpp

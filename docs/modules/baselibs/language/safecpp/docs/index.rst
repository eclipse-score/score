..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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


safecpp
#######

.. document:: Safecpp Library
   :id: doc__safecpp
   :status: draft
   :safety: ASIL_B
   :security: YES
   :tags: baselibs_safecpp
   :realizes: wp__cmpt_request


.. toctree::
   :hidden:

Abstract
========

SafeCPP is a collection of utilities that helps developers write safer C++ code.

Motivation and Rationale
========================

The C++ standard library targets general-purpose software and often lacks the stricter semantics needed in safety-critical code. SafeCPP fills these gaps with small, opt-in utilities that make failure modes explicit and are easy to adopt incrementally.

Following components are provided by SafeCPP:

- **aborts_upon_exception**: Globally replaces C++ exception handling with ``std::abort()`` calls for safety compliance.
- **coverage_termination_handler**: Ensures coverage data is preserved in GoogleTest death tests.
- **safe_atomics**: Prevents overflow when adding numbers to atomic variables (thread-safe addition with `TryAtomicAdd`).
- **safe_math**: Provides overflow-safe arithmetic operations for integral and floating-point types.
- **scoped_function**: Offers controlled callable execution with explicit lifetime guarantees.
- **string_view**: Provides null-terminated string view types and safety utilities for secure string handling.

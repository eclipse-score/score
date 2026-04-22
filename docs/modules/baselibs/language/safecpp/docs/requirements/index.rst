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

Requirements
############

.. document:: Safecpp Requirements
   :id: doc__safecpp_requirements
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__requirements_comp
   :tags: requirements

Functional Requirements
=======================

.. comp_req:: C++ Exception Abort
   :id: comp_req__safecpp__aborts_upon_exception
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_safecpp

   The safecpp library shall provide a mechanism to abort the program upon C++ exception allocation,
   allowing users to prevent any exception object from being created and hence to guarantee that
   no single exception will be possible to be thrown within an executable.

   .. Note::
         This satisfies :need:`aou_req__platform__no_exceptions`

.. comp_req:: Safe Arithmetic Operations
   :id: comp_req__safecpp__safe_math
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_safecpp

   The safecpp library shall provide arithmetic operations
   (addition, subtraction, multiplication, division, negation, absolute value, type casting, and comparison operations)
   that detect overflow, underflow, divide-by-zero, and precision loss for both integer and floating-point types,
   ensuring errors are handled safely and undefined behavior is prevented.

.. comp_req:: Scoped Guards
   :id: comp_req__safecpp__scoped_guards
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_safecpp

   The safecpp library shall provide scope-bound callable wrappers that prevent resource leaks.

.. comp_req:: Null-Terminated String
   :id: comp_req__safecpp__nullstring
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_safecpp

   The safecpp library shall provide a view type which guarantees that an underlying character sequence is guaranteed to be null-terminated.
   Such views type's underlying character sequence shall not be possible to get modified via such view type's methods.

.. comp_req:: Safe Atomic operations
   :id: comp_req__safecpp__safe_atomic
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_safecpp

   The safecpp library shall provide a lock-free atomic addition operation for integral types with overflow detection.

Non-Functional Requirements
===========================

.. comp_req:: Code Coverage Termination
   :id: comp_req__safecpp__coverage_termination
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__maintainable_design
   :status: valid
   :belongs_to: comp__baselibs_safecpp

   The safecpp library shall provide a mechanism which automatically registers a termination handler
   which ensures that code coverage data is also persisted upon any process exit (e.g. during gtest's Death Tests).

.. needextend:: "__safecpp__" in id
   :+tags: baselibs
.. needextend:: "safecpp" in id
   :+tags: safecpp

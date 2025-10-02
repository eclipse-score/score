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

Requirements
############

.. document:: Utils Library Requirements
   :id: doc__utils_lib_requirements
   :status: draft
   :safety: ASIL_B
   :realizes: PROCESS_wp__requirements_comp
   :tags: requirements, utils_library

Functional Requirements
=======================

.. comp_req:: String Hash Utilities
   :id: comp_req__utils__string_hash
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The Utils module shall provide hash calculation functions for string types to support efficient string-based lookups and comparisons.

.. comp_req:: Time Conversion Utilities
   :id: comp_req__utils__time_conversion
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The utils module shall provide functions for converting between time duration, including support for absolute timeout calculations.

.. comp_req:: PIMPL Pointer Implementation
   :id: comp_req__utils__pimpl_ptr
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__consistent_apis, feat_req__baselibs__safety
   :status: valid

   The utils module shall provide a stack-based Pointer to Implementation idiom implementation that avoids dynamic memory allocation using fixed-size aligned storage buffers.

.. comp_req:: Payload Validation
   :id: comp_req__utils__payload_validation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The Utils library shall provide payload validation utilities for domain-specific data integrity checks.

.. comp_req:: Scoped Operation Management
   :id: comp_req__utils__scoped_operation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The utils module shall provide RAII wrapper functionality to ensure callable objects are executed when the wrapper goes out of scope.

Non-Functional Requirements
===========================

.. comp_req:: Deterministic Behavior
   :id: comp_req__utils__deterministic_behavior
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The Utils library shall provide deterministic behavior with no dynamic memory allocation.

.. comp_req:: Exception-Free Operation
   :id: comp_req__utils__exception_free_operation
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The Utils library shall operate without throwing C++ exceptions.

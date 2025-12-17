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
   :realizes: wp__requirements_comp
   :tags: requirements, utils_library

Functional Requirements
=======================

.. comp_req:: Base64 Encoding and Decoding
   :id: comp_req__utils__base64
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The Utils component shall provide functions for encoding data to Base64 format and decoding Base64 data back to its original form.

.. comp_req:: PIMPL Pointer Implementation
   :id: comp_req__utils__pimpl_ptr
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__consistent_apis, feat_req__baselibs__safety
   :status: valid

   The Utils component shall provide a stack-based Pointer-to-Implementation Idiom implementation that avoids dynamic memory allocation by using fixed-size, aligned storage buffers.

.. comp_req:: Scoped Operation Management
   :id: comp_req__utils__scoped_operation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The Utils component shall provide a functionality that stores a callback and executes it automatically when the class is destructed

Non-Functional Requirements
===========================

.. comp_req:: Deterministic Behavior
   :id: comp_req__utils__deterministic_behavior
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The Utils component shall ensure that all operations complete in a predictable manner and without dynamic memory allocation.

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

.. document:: Containers Library Requirements
   :id: doc__containers_lib_requirements
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_comp
   :tags: requirements, containers_library

Functional Requirements
=======================

.. comp_req:: Dynamic Array
   :id: comp_req__containers__dynamic_array
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__containers_library, feat_req__baselibs__safety
   :status: valid

   The Containers library shall provide a fixed-size array container with construction-time size specification.

.. comp_req:: Intrusive List
   :id: comp_req__containers__intrusive_list
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__containers_library, feat_req__baselibs__safety
   :status: valid

   The Containers library shall provide an intrusive doubly-linked list based on the C++ standardization proposal P0406R1.

.. comp_req:: Type Safety
   :id: comp_req__containers__type_safety
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__consistent_apis, feat_req__baselibs__safety
   :status: valid

   The Containers library shall enforce compile-time type safety for all container operations.

.. comp_req:: Non-Relocatable Vector
   :id: comp_req__containers__non_relocatable_vector
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__containers_library, feat_req__baselibs__safety
   :status: valid

   The Containers library shall provide a non-relocatable vector container that maintains stable element addresses.


Non-Functional Requirements
===========================

.. comp_req:: Deterministic Behavior
   :id: comp_req__containers__deterministic_behavior
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The Containers library shall provide deterministic behavior with no dynamic memory allocation.

.. needextend:: "__containers__" in id
   :+tags: baselibs

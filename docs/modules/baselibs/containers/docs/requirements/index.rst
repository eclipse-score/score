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
   :belongs_to: comp__baselibs_containers

   The Containers library shall provide a fixed-size array container with construction-time size specification.

.. comp_req:: Intrusive List
   :id: comp_req__containers__intrusive_list
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__containers_library, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_containers

   The Containers library shall provide an intrusive doubly-linked list based on the C++ standardization proposal P0406R1.

.. comp_req:: Type Safety
   :id: comp_req__containers__type_safety
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__consistent_apis, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_containers

   The Containers library shall enforce compile-time type safety for all container operations.

.. comp_req:: Non-Relocatable Vector
   :id: comp_req__containers__non_relocatable_vector
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__containers_library, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_containers

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
   :belongs_to: comp__baselibs_containers

   The Containers library shall provide deterministic behavior with no dynamic memory allocation.

Assumptions of Use (AoU)
========================

.. aou_req:: Check Capacity
   :id: aou_req__containers__capacity_management
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall verify sufficient capacity or handle allocation failures before insertion operations to prevent exceeding container limits and undefined behavior.

.. aou_req:: Iterator Validity
   :id: aou_req__containers__iterator_validity
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall ensure that iterators are not used after operations that invalidate them and refresh iterators after modifying operations.

.. aou_req:: Element Lifetime and Ownership
   :id: aou_req__containers__element_lifetime
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall ensure that elements stored in containers remain valid throughout their lifetime in the container, and for intrusive containers, that element objects are not destroyed or moved while contained within the container.

.. aou_req:: Thread Safety
   :id: aou_req__containers__thread_safety
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall implement external synchronization mechanisms when accessing or modifying container objects from multiple threads concurrently, as the library provides no internal thread safety guarantees.

.. aou_req:: Index Bounds Checking
   :id: aou_req__containers__bounds_checking
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall ensure that all index-based access operations use valid indices within the container's current size range to prevent out-of-bounds access and undefined behavior.

.. aou_req:: Container State Verification
   :id: aou_req__containers__state_verification
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall verify container state before performing operations that depend on specific states, such as checking if a container is non-empty before accessing elements.

.. aou_req:: Memory Resource Management
   :id: aou_req__containers__memory_management
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall provide sufficient memory resources for all container operations.

.. aou_req:: Element Type Requirements
   :id: aou_req__containers__ele_type_requirements
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall ensure that element types are copy constructible, move constructible and destructible, and additionally for intrusive containers that they provide the required intrusive node members.

.. needextend:: "__containers__" in id
   :+tags: baselibs

.. needextend:: "containers" in id
   :+tags: containers

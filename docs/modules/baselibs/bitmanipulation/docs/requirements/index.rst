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


.. _bitmanipulation_requirements:

Requirements
############

.. document:: Bit Manipulation Requirements
   :id: doc__bitmanipulation_requirements
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_comp
   :tags: requirements, bitmanipulation

Functional Requirements
=======================

.. comp_req:: Support for Bit Operations
   :id: comp_req__bitmanipulation__bit_operations
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__bitmanipulation, feat_req__baselibs__core_utilities
   :status: valid
   :belongs_to: comp__baselibs_bit_manipulation

   The bit manipulation component shall provide an API for setting, clearing, toggling, and checking individual bits for any integral type up to 64 bits.

.. comp_req:: Support for Byte and Half-Byte Operations
   :id: comp_req__bitmanipulation__byte_operations
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__bitmanipulation, feat_req__baselibs__core_utilities
   :status: valid
   :belongs_to: comp__baselibs_bit_manipulation

   The bit manipulation component shall provide an API for extracting and setting bytes and half-bytes for any integral type up to 64 bits.

.. comp_req:: Support for Bitmask Operators for Enum Classes
   :id: comp_req__bitmanipulation__bitmask_operators
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__bitmanipulation, feat_req__baselibs__core_utilities
   :status: valid
   :belongs_to: comp__baselibs_bit_manipulation

   The bit manipulation library shall provide type-safe bitmask operations for scoped enumeration types.

.. comp_req:: Bounds and Safety Checks
   :id: comp_req__bitmanipulation__bounds_safety
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__bitmanipulation, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_bit_manipulation

   All bit manipulation functions shall validate input parameters to ensure that bit positions, byte indices, and half-byte indices are within valid bounds for the target integral type.

Non-Functional Requirements
===========================

.. comp_req:: Header-only API
   :id: comp_req__bitmanipulation__header_only
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__bitmanipulation
   :status: valid
   :belongs_to: comp__baselibs_bit_manipulation

   The bit manipulation API shall be header-only and not require external dependencies.

Assumptions of Use (AoU)
========================

.. aou_req:: Integral Type Constraints
   :id: aou_req__bitmanipulation__type_constraints
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   The user shall use bit manipulation functions only with integral types (integers, enumerations) as specified in the library's type constraints.

   Note: Operations on floating-point or non-integral types are not supported.

.. aou_req:: Enum Class Type Safety
   :id: aou_req__bitmanipulation__enum_type_safety
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   The user shall use scoped enumeration types (enum class) whose enumerators are defined as non-zero power-of-two values.

.. aou_req:: No Side Effects on Concurrent Access
   :id: aou_req__bitmanipulation__concurrent_access
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   The user shall implement external synchronization mechanisms (e.g., mutexes, atomic operations, or locks) when accessing or modifying the same integral value from multiple threads concurrently.

   Note: The library provides no internal thread safety guarantees.

.. aou_req:: Bit Extraction Index Validation
   :id: aou_req__bitmanipulation__bit_validation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   The user shall validate byte and half-byte extraction indices to ensure they correspond to valid positions within the target integral type to prevent accessing invalid memory ranges.

.. needextend:: "__bitmanipulation__" in id
   :+tags: baselibs

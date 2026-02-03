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

.. document:: Result Library Requirements
   :id: doc__result_lib_requirements
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_comp
   :tags: requirements, result_library

Functional Requirements
=======================

.. comp_req:: Result-Based Error Handling
   :id: comp_req__result__error_handling
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__result_library, feat_req__baselibs__safety
   :status: valid
   :tags: inspected

   The Result library shall provide an error handling mechanism that enables functions to return either successful values ("Get Value") or error information ("Get Error") without using C++ exceptions.

.. comp_req:: Set Result
   :id: comp_req__result__set_result
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__result_library
   :status: valid
   :tags: inspected

   The Result library shall provide a "Set Result" operation that accepts either a successful value of type T or an Error object.

.. comp_req:: Domain-Specific Error Information
   :id: comp_req__result__domain_error_information
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__result_library, feat_req__baselibs__safety
   :status: valid
   :tags: inspected

   The Result library shall support user-defined error domains and error codes.

.. comp_req:: Type-Safe Error Handling
   :id: comp_req__result__type_safety
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__consistent_apis, feat_req__baselibs__safety
   :status: valid
   :tags: inspected

   The Result library shall enforce compile-time type safety for error handling operations.

.. comp_req:: Standard Library Integration
   :id: comp_req__result__std_integration
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__consistent_apis, feat_req__baselibs__safety
   :status: valid
   :tags: inspected

   The Result library shall provide conversion utilities to transform Result objects into std::optional<T> types. The conversion shall require explicit handling of error cases before discarding error information, ensuring that errors cannot be silently ignored.

Non-Functional Requirements
===========================

.. comp_req:: Deterministic Behavior
   :id: comp_req__result__deterministic_behavior
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid
   :tags: inspected

   The Result library shall provide deterministic behavior with no dynamic memory allocation.

.. comp_req:: Exception-Free Operation
   :id: comp_req__result__exception_free_operation
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid
   :tags: inspected

   The Result library shall operate without throwing C++ exceptions.

Assumptions of Use (AoU)
========================

.. aou_req:: Error Domain Implementation
   :id: aou_req__result__error_domain_implementation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall implement error domain classes and error code enumerations according to the library's interface specification.

.. aou_req:: Result Value Handling
   :id: aou_req__result__value_handling
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall check and handle both successful and error states of Result objects before accessing contained values to prevent undefined behavior.

.. aou_req:: Error Reaction and Safe State
   :id: aou_req__result__error_reaction
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall implement error reaction mechanisms that transition the system to a safe state when error conditions are detected in Result objects.

.. aou_req:: Thread Safety
   :id: aou_req__result__thread_safety
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall implement external synchronization mechanisms (e.g., mutexes, atomic operations, or locks) when accessing or modifying Result objects from multiple threads concurrently, as the library provides no internal thread safety guarantees.

.. aou_req:: Resource Lifetime
   :id: aou_req__result__resource_lifetime
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: inspected

   The user shall ensure that error domain objects and referenced resources remain valid throughout the entire lifetime of any dependent Result or Error objects.


.. needextend:: "__result__" in id
   :+tags: baselibs, result_library

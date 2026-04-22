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

.. document:: OS Library Requirements
   :id: doc__os_lib_requirements
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_comp
   :tags: requirements, os_library

Functional Requirements
=======================

.. comp_req:: Operating System API Abstraction
   :id: comp_req__os__api_abstraction
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__os_library, feat_req__baselibs__consistent_apis
   :status: valid
   :belongs_to: comp__baselibs_os

   The OS library shall provide a C++ abstraction layer that wraps operating system interfaces using type-safe, idiomatic C++ constructs.

   .. Note::
         Operating system interfaces include POSIX system calls, POSIX library functions, C standard library functions, and platform-specific OS APIs

.. comp_req:: Thin Wrapper Principle
   :id: comp_req__os__thin_wrapper
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__os_library, feat_req__baselibs__consistent_apis
   :status: valid
   :belongs_to: comp__baselibs_os

   The OS library wrappers shall not add application-level logic beyond parameter type conversion and error translation.

.. comp_req:: Result-Based Error Propagation
   :id: comp_req__os__error_propagation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__os_library, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_os

   The OS library shall propagate errors from operating system interfaces using a result type that either contains the successful return value or an error.

.. comp_req:: Linux Operating System Support
   :id: comp_req__os__linux_support
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__os_library
   :status: valid
   :belongs_to: comp__baselibs_os

   The OS library shall provide platform-specific abstractions for Linux operating system APIs, including Linux-specific system calls and services not available in the POSIX standard.

.. comp_req:: QNX Operating System Support
   :id: comp_req__os__qnx_support
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__os_library
   :status: valid
   :belongs_to: comp__baselibs_os

   The OS library shall provide platform-specific abstractions for QNX operating system APIs, including QNX-specific system calls and services not available in the POSIX standard.

Assumptions of Use (AoU)
========================

.. aou_req:: Thread Safety
   :id: aou_req__os__thread_safety
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   The user shall implement external synchronization mechanisms (e.g., mutexes, atomic operations, or locks) when accessing or modifying OS library objects from multiple threads concurrently.

   .. Note::
         The OS library provides no internal thread safety guarantees beyond those of the underlying system calls.

.. needextend:: "__os__" in id
   :+tags: baselibs, os_library

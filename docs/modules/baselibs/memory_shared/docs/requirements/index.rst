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

.. document:: Memory Library Requirements
   :id: doc__memory_lib_requirements
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_comp
   :tags: requirements, memory_library

Functional Requirements
=======================

.. comp_req:: Shared Memory Management
   :id: comp_req__memory__shared_memory
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__memory_library, feat_req__baselibs__safety
   :status: valid

   The Memory library shall provide capabilities for creating, opening and managing shared memory.

.. comp_req:: Polymorphic OffsetPtr Allocator
   :id: comp_req__memory__offset_ptr
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__memory_library, feat_req__baselibs__safety
   :status: valid

   The Memory library shall provide polymorphic memory resource allocators using offset pointers instead of raw pointers to enable allocation in shared memory regions accessible across multiple processes. The standard library's std::pmr::polymorphic_allocator is not applicable as it uses raw pointers that are invalid when shared memory is mapped at different virtual addresses in different processes.

.. comp_req:: Shared Memory Containers
   :id: comp_req__memory__shared_containers
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__memory_library, feat_req__baselibs__safety
   :status: valid

   The Memory library shall provide type aliases for STL containers (vector, map, string) that use offset pointers for shared memory storage.

.. comp_req:: Inter-Process Synchronization
   :id: comp_req__memory__ipc_sync
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__memory_library, feat_req__baselibs__safety
   :status: valid

   The Memory library shall provide file-based locking mechanisms for inter-process synchronization and mutual exclusion.

.. comp_req:: Memory Region Bounds Checking
   :id: comp_req__memory__bounds_check
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__safety, feat_req__baselibs__memory_library
   :status: valid

   The Memory library shall track and validate memory region boundaries to prevent out-of-bounds access in shared memory.

.. comp_req:: Endianness Conversion
   :id: comp_req__memory__endianness
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__memory_library
   :status: valid

   The Memory library shall provide byte order conversion between host and network byte order (big/little endian).

.. comp_req:: Sealed Shared Memory
   :id: comp_req__memory__sealed_shm
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__safety, feat_req__baselibs__memory_library, feat_req__baselibs__security
   :status: valid

   The Memory library shall provide immutable shared memory segments that become read-only after initialization.

.. comp_req:: Typed Memory
   :id: comp_req__memory__typed_memory
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__safety, feat_req__baselibs__memory_library
   :status: valid

   The Memory library shall provide an interface to allocate shared memory from typed memory regions.

.. comp_req:: Memory Resource Registry
   :id: comp_req__memory__resource_registry
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__memory_library
   :status: valid

   The Memory library shall provide a global registry for memory resource lookup and management.

.. comp_req:: String Utilities
   :id: comp_req__memory__string_utils
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__memory_library
   :status: valid

   The Memory library shall provide zero-allocation string utilities including splitting, comparison, and compile-time literals.

.. comp_req:: Atomic Operations in Shared Memory
   :id: comp_req__memory__atomic_ops
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__memory_library, feat_req__baselibs__safety
   :status: valid

   The Memory library shall provide atomic operations on shared memory data for lock-free inter-process communication.


Non-Functional Requirements
===========================

.. comp_req:: Deterministic Memory Allocation
   :id: comp_req__memory__deterministic_alloc
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The shared memory allocation shall provide deterministic behavior with predictable execution time suitable for real-time automotive systems.

.. comp_req:: Process Address Space Independence
   :id: comp_req__memory__address_independence
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__safety, feat_req__baselibs__memory_library
   :status: valid

   The Memory library shall ensure shared memory data structures remain valid regardless of process virtual address space mappings.

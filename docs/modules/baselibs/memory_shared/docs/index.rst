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

.. _comp_doc_memory_shared:

memory
######

.. document:: Memory Library
   :id: doc__memory
   :status: draft
   :safety: ASIL_B
   :tags: baselibs_memory
   :realizes: wp__cmpt_request
   :security: YES

.. toctree::
   :hidden:

   architecture/index
   requirements/index.rst

Abstract
========

The Memory library provides APIs for memory management to facilitate inter-process communication (IPC) in the S-CORE software platform.

Motivation and Rationale
========================

The Memory library shall provide mechanisms for creating, accessing, and managing shared memory between different processes.
It includes support for polymorphic memory resource allocators using offset pointers and additional utilities to deal with memory use-cases.

The Memory library is needed in the S-CORE software platform because subsystems like Communication and Logging rely on shared memory for inter-process communication.

Specification
=============

The following details and requirements describe the aspects of the current feature in the context of S-CORE.

General considerations
----------------------

The Memory Library should provide APIs for memory management:

* :need:`comp_req__memory__shared_memory`
* :need:`comp_req__memory__offset_ptr`
* :need:`comp_req__memory__shared_containers`
* :need:`comp_req__memory__ipc_sync`
* :need:`comp_req__memory__bounds_check`
* :need:`comp_req__memory__endianness`
* :need:`comp_req__memory__sealed_shm`
* :need:`comp_req__memory__typed_memory`
* :need:`comp_req__memory__resource_registry`
* :need:`comp_req__memory__string_utils`
* :need:`comp_req__memory__atomic_ops`

The library should ensure that all memory operations are performed safely, with appropriate bounds checking and synchronization mechanisms to prevent memory corruption.

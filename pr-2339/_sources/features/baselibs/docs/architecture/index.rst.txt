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
.. _baselibs_architecture:

Architecture
=====================

.. document:: Baselibs Architecture
   :id: doc__baselibs_architecture
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feature_arch

Overview
--------

A brief overview of Baselibs is described :ref:`baselibs_feature`.

Description
-----------

A detailed description of the Baselibs module requirements is located :need:`feat_req__baselibs__core_utilities`.

The Baselibs module provides foundational software utilities, safety mechanisms and robust infrastructure components. It comprises essential libraries organized into functional categories:

**Core Utility Libraries**

- **bitmanipulation**: Utilities for bit manipulation operations
- **containers**: Specialized container implementations including ``DynamicArray`` and intrusive linked lists
- **utils**: Reusable utilities including type traits, mathematical utilities and string manipulation helpers

**Threading and Concurrency**

- **concurrency**: Interface for parallel execution of C++ callables with thread pool management

**Data Processing and Serialization**

- **json**: JSON abstraction layer with pluggable backend support
- **static_reflection_with_serialization**: Binary serialization/deserialization with compile-time type reflection

**File System and I/O Operations**

- **filesystem**: Filesystem manipulation library similar to ``std::filesystem``

**Memory Management**

- **memory**: Memory handling utilities for safety-critical applications with shared memory support

**Operating System Abstraction**

- **os**: OS Abstraction Layer (OSAL) for POSIX-like systems including Linux and QNX

**Error Handling and Safety**

- **result**: Error handling without exceptions, conforming to C++23 ``std::expected`` specification
- **safecpp**: Safety framework including exception prevention and overflow-safe implementations

**Modern C++ Extensions and Logging**

- **futurecpp**: C++14 Standard Library extensions with backported components
- **mw::log**: Logging library for automotive systems with structured logging and multiple backends

These libraries form an integrated ecosystem designed for code reuse, consistency and safety throughout the platform.



Rationale Behind Architecture Decomposition
*******************************************

The decomposition of Baselibs into modular libraries is motivated by the need for code reuse, maintainability and consistent APIs across the platform. This approach enables platform modules to leverage common infrastructure, reduces duplication and supports safety and security requirements.

Static Architecture
-------------------

.. feat_arc_sta:: Static View
   :id: feat_arc_sta__baselibs__static_view_arch
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__baselibs__core_utilities
   :includes: logic_arc_int__baselibs__json, logic_arc_int__baselibs__memory_shared, logic_arc_int__baselibs__message_passing, logic_arc_int__baselibs__result, logic_arc_int__baselibs__bit_manipulation, logic_arc_int__baselibs__bit_mask_operator, logic_arc_int__baselibs__dynamic_array, logic_arc_int__baselibs__intrusive_list, logic_arc_int__baselibs__filesystem

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}

Logical Interfaces
------------------

The Baselibs feature exposes the following logical interfaces:

.. needtable::
   :style: table
   :columns: title;id;status
   :sort: title
   :filter: id in ['logic_arc_int__baselibs__json', 'logic_arc_int__baselibs__memory_shared', 'logic_arc_int__baselibs__message_passing' ,'logic_arc_int__baselibs__result', 'logic_arc_int__baselibs__bit_manipulation', 'logic_arc_int__baselibs__bit_mask_operator', 'logic_arc_int__baselibs__dynamic_array', 'logic_arc_int__baselibs__intrusive_list', 'logic_arc_int__baselibs__filesystem']

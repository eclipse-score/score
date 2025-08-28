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
   :includes: logic_arc_int__baselibs__json, logic_arc_int__baselibs__memory_shared, logic_arc_int__baselibs__message_passing

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}

Logical Interfaces
------------------

The Baselibs feature exposes the following logical interfaces defined in the modules:

- :need:`logic_arc_int__baselibs__json`: JSON parsing and serialization capabilities with pluggable backend support. See :doc:`JSON Module Architecture </modules/baselibs/json/docs/architecture/index>` for detailed implementation.

- :need:`logic_arc_int__baselibs__memory_shared`: Shared memory operations for inter-process communication with safety guarantees. See :doc:`Memory Shared Module Architecture </modules/baselibs/memory_shared/docs/architecture/index>` for detailed implementation.

- :need:`logic_arc_int__baselibs__message_passing`: Inter-process and inter-thread message communication with deterministic behavior. See :doc:`Message Passing Module Architecture </modules/baselibs/message_passing/docs/architecture/index>` for detailed implementation.

Module Viewpoint
----------------

.. mod_view_sta:: Baselibs
   :id: mod_view_sta__baselibs__baselibs_arch
   :includes: comp_arc_sta__baselibs__json, comp_arc_sta__baselibs__memory_shared, comp_arc_sta__baselibs__message_passing

   .. uml::
      :scale: 50
      :align: center
      :name: doc__baselibs__modules
      :caption: Baselibs Core Modules

      package "Baselibs" <<Rectangle>> {
          package "JSON Module" <<Frame>> #D5E8D4 {
              object "JSON Parser" as json_parser
              object "Serialization" as json_serial
          }
          package "Memory Shared Module" <<Frame>> #DAE8FC {
              object "Shared Memory" as shared_mem
              object "Safety Guarantees" as mem_safety
          }
          package "Message Passing Module" <<Frame>> #FFF2CC {
              object "IPC Messages" as ipc_msg
              object "Thread Messages" as thread_msg
          }
      }

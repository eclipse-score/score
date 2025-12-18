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

.. _abi_compatible_data_types_feature:

ABI Compatible Data Types
#########################

.. document:: ABI Compatible Datatypes
   :id: doc__abi_compatible_data_types
   :status: valid
   :safety: ASIL_B
   :tags: feature_request, change_management, communication, abi_compatible_data_types
   :security: YES
   :realizes: wp__feat_request


.. toctree::
   :hidden:

   requirements.rst


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_abi_compatible_data_types``


Abstract
========

This feature request defines a set of ABI-compatible data types and a runtime type description format to support zero-copy inter-process communication between C++17 and Rust 1.8x processes using the same endianness. It ensures consistent type layouts across languages by requiring fixed-size, statically allocated types without absolute pointers or language-specific metadata.

The specification covers primitive types, structs, enums, arrays, and introduces ABI-stable representations for vectors, options, and results. A runtime-readable type description enables processes to interpret shared memory without compile-time access to type definitions.


Motivation
==========

This feature request addresses specific challenges in achieving type compatibility within our inter-process communication (IPC) framework that leverages zero-copy shared memory mechanisms. Two essential scenarios are under evaluation:

1. **ABI Compatibility**: Processes implemented in different programming languages (C++17 and Rust 1.8x) must interpret a shared memory location consistently as the same native type, provided both have compile-time access to the type definition. This scenario eliminates serialization overhead and allows direct memory access.

2. **Type Description**: It should be possible to record arbitrary data streams, and convert or analyze them at a later time and/or on a different system, without having to recompile the conversion or analysis tools for that particular data format. A machine-readable description of the format, including any user-defined data types, should be available on request during runtime. In addition, this description could potentially be used by gateway processes to perform relatively simple but generic transformations between different data representations.


ABI Compatibility
-----------------

Our communication feature relies on shared memory to transfer data between processes. For effective zero-copy data exchange, processes written in C++17 and Rust 1.8x must inherently understand the data at shared memory locations identically. Achieving this requires ensuring that data types have consistent, fixed-size memory layouts.

This evaluation initially targets the following process configurations:

* Processes running on the same operating system.
* Processes running on different operating systems but under the same hypervisor.

Supporting different endianness between processes is explicitly out of scope, as it inherently demands bit manipulation, effectively requiring serialization.
Different bit widths, however, are implicitly supported by specifying the width of all types and excluding word-size integers.

The following data types shall be supported:

* **Primitive Types**:

  * Boolean
  * Numeric (fixed-size integers 8-128 bits, signed and unsigned; IEEE 754 floating-point numbers)

* **Sequence Types**:

  * Array (fixed-length)

* **User-Defined Types**:

  * Struct
  * Tuple
  * Enum (tag-only)
  * Variant ("tagged union"; *optional*)

* **Fixed-Size, Variable-Length Containers**:

  * Vector
  * Queue
  * Hash map (*optional*)
  * Hash set (*optional*)
  * Binary tree (*optional*)

* **Specialized Variants**:

  * Result
  * Option

All provided data types must ensure fixed size and consistent memory layouts.

Type Description
----------------

A critical scalability feature involves gateway processes, which subscribe to IPC endpoints and translate ABI-compatible data types into external serialization formats. These gateways require the ability to interpret data without compile-time access to type definitions. To address this, an explicit runtime-readable type description format is necessary. This description allows dynamic, runtime interpretation of data structures, enabling the addition of new IPC topics without recompiling gateway processes.

In summary, the motivation behind this feature request is to define and standardize ABI-compatible data types and a runtime-accessible type description mechanism to ensure interoperability and scalability in zero-copy IPC scenarios involving multiple languages and dynamic environments.


.. Rationale
.. ==========


Specification
=============

ABI Compatibility
-----------------

This specification defines the set of rules and constraints for representing data types in shared memory such that they can be interpreted consistently across processes implemented in C++17 and Rust 1.8x. These types enable zero-copy inter-process communication by enforcing ABI compatibility at the memory layout level. The focus is on data exchange between processes using the same endianness.

Assumptions
^^^^^^^^^^^

* Shared memory regions are mapped at correctly aligned virtual addresses in both processes.
* No serialization or runtime copying occurs when interpreting a type from memory.
* Processes use the same endianness.
* No synchronization or atomicity guarantees are defined at the data type level; these must be provided by the accessing code.
* All memory is allocated statically or pre-reserved. Dynamic memory allocation is disallowed.

Type Conformance
^^^^^^^^^^^^^^^^

Types used in shared memory must meet the following criteria:

1. **Fixed size and alignment**: Every type must have a known, constant size and alignment at compile time.
2. **Consistent layout across languages**: The layout of a type must be identical in Rust and C++, and on all platforms.
3. **No absolute pointers or references**: Types must not contain absolute pointers/function pointers/references or any pointers/references that point out of the transferred data.
4. **No language-specific metadata**: No vtables, slice headers, or implementation-specific type markers are allowed.

Each type definition must clearly indicate whether it conforms to these rules natively or requires a custom definition to do so.

Type Categories
^^^^^^^^^^^^^^^

Primitive Types
"""""""""""""""

These types are ABI-compatible when declared using fixed-size standard types:


.. list-table:: Native Type Mapping
   :header-rows: 1

   * - Concept
     - Rust
     - C++17
   * - Boolean
     - ``bool``
     - ``bool`` (1 byte, with ``0x00`` and ``0x01`` as the only valid bit patterns)
   * - Integers (N = 8, 16, 32, 64)
     - ``uN``, ``iN``
     - ``std::uintN_t``, ``std::intN_t``
   * - Floating point
     - ``f32``, ``f64``
     - ``float``, ``double`` (compliant with IEEE 754)

All types must avoid trap representations and undefined padding.

Structs and Tuples
""""""""""""""""""

Structs and tuples are supported using standard layout rules:

* **Rust**: Requires ``#[repr(C)]``
  (guarantees C-compatible memory layout;
  `full specification <https://doc.rust-lang.org/reference/type-layout.html#the-c-representation>`__)
* **C++**: Requires ``standard_layout``
  (no virtual functions, no virtual inheritance, and only one class in the hierarchy has non-static data members;
  `full specification <https://en.cppreference.com/w/cpp/language/classes.html#Standard-layout_class>`__)

Field ordering must be preserved and padding must be identical across compilers. Any alignment greater than the default must be explicitly declared.

Enums
"""""

Only fieldless enums with a defined underlying integer type are supported. These must use:

* ``#[repr(u8)]``, ``#[repr(u16)]``, etc. in Rust
* ``enum class MyEnum : std::uint8_t`` in C++

*Note:* Enums with payloads ("variants" or "tagged unions") are optionally supported.

Arrays
""""""

Fixed-size arrays are naturally ABI-compatible and supported in both languages.

* Rust: ``[T; N]``
* C++: wrapper around ``T[N]`` to enforce bounds-checking for element access

Element types must also conform to this specification. No dynamic length information is allowed.

Vectors
""""""""

To provide bounded sequence types with familiar APIs, a custom vector implementation must be provided in both languages that matches the memory layout defined below.

.. code-block:: rust

    #[repr(C)]
    pub struct AbiVec<T> {
        len: u32,
        capacity: u32,
        elements: [T; N],
    }

.. code-block:: cpp

    template<typename T, std::size_t N>
    struct AbiVec {
    private:
        std::uint32_t len;
        std::uint32_t capacity;
        T elements[N];
    };

* Capacity is fixed and equal to ``N`` at compile time.
* Overflow beyond capacity must be a checked error.
* No heap allocation is permitted.
* Internally, these are ABI-compatible with ``len``, ``capacity`` and ``elements`` accessible from both languages.
* The public API must match standard vector types in usability (e.g. ``push()``, ``pop()``).

Option Types
""""""""""""

ABI-compatible optional types must be implemented manually using a one-byte tag followed by a payload.

.. code-block:: rust

    #[repr(C)]
    pub struct AbiOption<T> {
        is_some: u8,
        value: T,
    }

.. code-block:: cpp

    template<typename T>
    struct AbiOption {
    private:
        std::uint8_t is_some;
        T value;
    };

* ``is_some == 0`` indicates absence; ``1`` indicates presence.
* The value field is always initialized and occupies memory regardless of state.
* The public API must match standard optional types in usability.

Result Types
""""""""""""

Result types represent tagged unions with two possible states.

.. code-block:: rust

    #[repr(C)]
    pub struct AbiResult<T, E> {
        is_ok: u8,
        value: AbiResultUnion<T, E>,
    }

    #[repr(C)]
    union AbiResultUnion<T, E> {
        ok: T,
        err: E,
    }

.. code-block:: cpp

    template<typename T, typename E>
    struct AbiResult {
    private:
        std::uint8_t is_ok;
        union {
            T ok;
            E err;
        } value;
    };

* ``is_ok == 1`` indicates ``ok`` field is valid
* ``is_ok == 0`` indicates ``err`` field is valid
* The layout must guarantee correct union member interpretation based on the discriminant

Language Conformance Summary
""""""""""""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Feature
     - Rust Native Support
     - C++ Native Support
     - Specification Status
   * - Primitives
     - ✅ Native types
     - ✅ Native types
     - Conforming
   * - Structs
     - ✅ ``#[repr(C)]``
     - ✅ ``standard_layout``
     - Conforming
   * - Enums (fieldless)
     - ✅ ``#[repr(C)]``
     - ✅ With fixed base
     - Conforming
   * - Arrays
     - ✅ ``[T; N]``
     - ✅ ``T[N]``
     - Conforming
   * - Vector
     - ❌ ``Vec<T>``
     - ❌ ``std::vector<T>``
     - ✅ ``AbiVec<T, N>`` required
   * - Option
     - ❌ ``Option<T>``
     - ❌ ``std::optional<T>``
     - ✅ ``AbiOption<T>`` required
   * - Result
     - ❌ ``Result<T, E>``
     - ❌ ``std::expected<T, E>``
     - ✅ ``AbiResult<T, E>`` required



Type Description
----------------

To address the scenarios outlined in the motivation, a clearly defined type description mechanism is required. The type description provides sufficient information during runtime, enabling a process without compile-time access to type definitions to correctly interpret a given memory location according to the previously established ABI rules.

The goals are:

* Enable interpretation of shared memory content without compile-time access to type definitions.
* Support all ABI-compatible data types previously defined.
* Include versioning to manage schema evolution and compatibility.
* Allow easy generation and parsing by tooling in both C++ and Rust.

Workflows
^^^^^^^^^

Two potential workflows are considered for creating type descriptions:

**Description-first Workflow**: The type description is defined independently (e.g., via a schema or domain-specific language). The C++ and Rust type definitions are then generated based on this description as part of the application build process.

**Definition-first Workflow**: Existing type definitions in Rust or C++ are the source of truth, and the corresponding type description is generated during the build process via compiler tooling.

Both workflows are valid, and the final decision is deferred pending further feasibility analysis.

Type Description Format
^^^^^^^^^^^^^^^^^^^^^^^

The format of the type description shall explicitly support versioning to allow schema evolution and backward compatibility. It must accommodate all data types described earlier in the ABI compatibility section. It should be simple, human-readable, and easily machine-parsable.

The choice of serialization format is left open but may include RON, JSON5, or a custom DSL, based on readability, tooling support, and maintainability.


.. Backwards Compatibility
.. =======================


Security Impact
===============

.. note::

   This section does not replace a formal security impact analysis. This only guides the design thoughts behind security related topics and is to be understood as a starting point for later workflows.

The memory underlying an ABI compatible type may potentially be corrupted, e.g., because it originates from an untrusted process, or because of a bug in the producer. As a consequence, any pointers, indices, and offsets need to be validated before they're used to access memory, to ensure they don't address any out-of-bounds locations. In addition, care must be taken to avoid TOC/TOU (*time-of-check to time-of-use*) issues, where the producer might maliciously or inadvertently modify a value after the consumer has already validated it.


Safety Impact
=============

.. note::

   This section does not replace a formal safety impact analysis. This only guides the design thoughts behind safety related topics and is to be understood as a starting point for later workflows.

All functionality shall be available to applications rated up to ASIL-B.


.. License Impact
.. ==============


.. How to Teach This
.. ==================


Rejected Ideas
==============

Reflection
----------

Reflection, in this context, is the ability to inspect data at runtime even if its structure is not or not fully known at compile time.
Benefits of reflection include being able to translate recorded data into a human-readable format (e.g., JSON or CSV) without having to know the type definitions at compile time; this enables general-purpose data recording and transformation tools.

This ability requires some form of *type description* being available at runtime, so that a sequence of bytes can be interpreted as a data structure.
There are two primary approaches to achieve this goal:

* *inline type descriptions*, which precede each instance of every type, and
* *external type descriptions*, which are stored separately from the data.

Inline Type Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^

An explicit transformation step between the in-memory representation and the SOME/IP+TLV format can – in theory – be avoided by adding TLVs to ABI compatible types.
This approach, however, comes with significant downsides:

* Adding inline type descriptions incurs a significant memory overhead across the board, and leads to worse cache behavior.
* It mandates TLV for *all* instances of *all* ABI compatible types, even when TLV is not needed (for example, in a non-TLV SOME/IP gateway).
  * This might be mitigated by making TLV optional through a generic respectively a template parameter on the type declaration.
* SOME/IP's specification of big-endianness is in conflict with the requirement of native-endianness for ABI compatible types, making the feasibility of this approach questionable.
* SOME/IP doesn't support "unused" slots in dynamic arrays, so ABI compatible types containing *vectors* (which differentiate between the length and the capacity) couldn't be directly represented in SOME/IP anyway.

Alternative Approach
^^^^^^^^^^^^^^^^^^^^

Instead of inserting inline type descriptions into each instance of an ABI compatible type, the full type description can be made available to a consumer only once, either proactively or on request.
The consumer decides if it uses or ignores this metadata.

This type description can be used to dynamically translate between the compact, non-reflective ABI compatible data structures on one side, and a reflective, inline-describing format on the other side.
Although this incurs a copy and some minor processing, the overhead should be negligible compared to other computational tasks involving the payload.

One method to efficiently translate a payload consisting of ABI compatible types to an inline-described reflective format is to convert the hierarchical type description to a flat list of *instructions* which can be executed by an interpreter.
Both the instructions and the interpreter would be specific for the target format.
For example, to translate in-memory ABI compatible types to SOME/IP data structures, the instructions could look like this:

.. code-block:: rust

    enum Transformation {
        /// Copies `length` bytes from input to output.
        Copy { length: usize, }

        /// Copies 2 bytes from input to output, swapping endianness.
        SwapEndian2,

        /// Copies 4 bytes from input to output, swapping endianness.
        SwapEndian4,

        /// Copies 8 bytes from input to output, swapping endianness.
        SwapEndian8,

        /// Reads an ABI compatible vector (with an element size of `stride` bytes) from the input,
        /// writes the length as big-endian to the output, and writes the given number of elements
        /// to the output.
        CopyVectorWithLength { stride: usize },

        ...
    }

Rationale for Rejection
^^^^^^^^^^^^^^^^^^^^^^^

Reflection will not be part of version 1.0 of this feature request.

* Inline type descriptions are too intrusive and generate too much overhead:

  1. Choosing one particular format, like SOME/IP TLV, would bias the entire system against other formats.
  2. To take full advantage of zero-copy IPC, ABI compatible types must be used during production and consumption of the transmitted data. Having to carry around inline type descriptions in those computations would have a non-negligible performance overhead.
  3. The specification for SOME/IP types is incompatible with the requirement of ABI vectors that can grow dynamically during construction, i.e., vectors which contain fewer valid elements than they take up space in memory.
  4. Inserting inline type descriptions on demand is expected to be a relatively cheap operation, which negates the main motivation for including them directly in ABI types in the first place.

* External type descriptions will probably be included in a later version of this feature request.
  For now, they're postponed until we have a better understanding of the relevant use cases.


.. Open Issues
.. ===========

.. Glossary
.. ========

.. .. _footnotes:

.. Footnotes
.. =========

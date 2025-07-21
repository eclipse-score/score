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
   :realizes: wp__feat_request
   :tags: feature_request, change_management, communication, abi_compatible_data_types


.. toctree::
   :hidden:

   requirements.rst


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_abi_compatible_data_types``


Abstract
========
This feature request defines a set of ABI-compatible data types and a runtime type description format to support zero-copy inter-process communication between C++17 and Rust 1.8x processes on the same architecture and endianness. It ensures consistent type layouts across languages by requiring fixed-size, statically allocated types with no pointers or language-specific metadata.

The specification covers primitive types, structs, enums, arrays, and introduces ABI-stable representations for vectors, options, and results. A runtime-readable type description enables processes to interpret shared memory without compile-time access to type definitions.


Motivation
==========

This feature request addresses specific challenges in achieving type compatibility within our inter-process communication (IPC) framework that leverages zero-copy shared memory mechanisms. Two essential scenarios are under evaluation:

1. **ABI Compatibility**: Processes implemented in different programming languages (C++17 and Rust 1.8x) must interpret a shared memory location consistently as the same native type, provided both have compile-time access to the type definition. This scenario eliminates serialization overhead and allows direct memory access.

2. **Type Description**: Processes responsible for translating data between internal ABI-compatible formats and external serialization formats should perform this translation without compile-time knowledge of type definitions. This runtime interpretation capability is critical for scalability, ensuring that gateway processes (or similar entities) can dynamically handle new data types without recompilation.


ABI Compatibility
-----------------

Our communication feature relies on shared memory to transfer data between processes. For effective zero-copy data exchange, processes written in C++17 and Rust 1.8x must inherently understand the data at shared memory locations identically. Achieving this requires ensuring that data types have consistent, fixed-size, coherent memory layouts.

This evaluation initially targets the following process configurations:

* Processes running on the same operating system.
* Processes running on different operating systems but under the same hypervisor.

Future considerations may include processes running on different chips or architectures with the same endianness. Supporting different endianness is explicitly out of scope, as it inherently demands bit manipulation, effectively requiring serialization.

The following data types shall be supported by the IPC mechanism:

* **Primitive Types**:

  * Boolean
  * Numeric (Fixed-size integers 8-128 bits, signed and unsigned; IEEE 754 floating-point numbers)
  * TypeTag

* **Sequence Types**:

  * Tuple
  * Array

* **User-defined Types**:

  * Struct
  * Enum

* **Fixed-size Containers**:

  * Vector
  * Hash map (optional)
  * Hash set (optional)
  * Binary tree (optional)

* **Union-like Constructs** (no direct unions):

  * Result
  * Option
  * Variant (optional)

All provided data types must ensure fixed size and coherent memory layouts.
Additionally, they should provide means to safety access memory. That is why C-style unions should
not exist for ABI compatible types.

Type Description
----------------

A critical scalability feature involves gateway processes, which subscribe to IPC endpoints and translate ABI-compatible data types into external serialization formats. These gateways require the ability to interpret data without compile-time access to type definitions. To address this, an explicit runtime-readable type description format is necessary. This description allows dynamic, runtime interpretation of data structures, enabling the addition of new IPC topics without recompiling gateway processes.

In summary, the motivation behind this feature request is to define and standardize ABI-compatible data types and a runtime-accessible type description mechanism to ensure interoperability and scalability in zero-copy IPC scenarios involving multiple languages and dynamic environments.

Reflection
^^^^^^^^^^

Reflection, in this context, is the ability to retrieve information on ABI data types at runtime.
Type information allows software at runtime to correctly interpret the memory layout of data seen.

We distinguish to reflection approaches:
* Static reflection allows access to types that are known at compile-time
* Dynamic reflection allows access to types that are only known at runtime.

Benefits of reflection include:

* Consumers can perform additional consistency checks, because reflection provides a second, redundant description of the structure of the received data stream.
* Recorded data can be translated into a human-readable format (e.g., JSON or CSV) without having to know the type definitions beforehand; this allows general-purpose data recording and transformation tools.
* As a special case, if a data structure already contains *inline type descriptions* in the form of SOME/IP TLV tags, it doesn't need to be transformed before being sent over a SOME/IP connection.

Type Tags & Type Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With ABI types the ability to communicate on types appears desireable.

Transporting information on a type minimally requires a globally unique type tag that every application
can interpret identically. This `TypeTag` should map to a single value, ideally primitive and atomic.

The `TypeTag` itself is an ABI type.

Note: We choose the name `TypeTag` to not collide with compiler-specific `type_id` and similar data.

Using the type tag the ABI type system can provide more details on the inner structure and layout of the type.
These details we call type information.

Examples:

* An IEEE-754 32 bit single precision floating-point value has unique `TypeTag` value 'AA__F_32'.
  The associated type information reveals it is primitive, floating, and sized 4 bytes.

* A CAN message has a `TypeTag`value 'AA__BCAN_'.
  The associated type information reveals it is a struct with the fields id, len, and data. Data's
  type code resolving into the information it beeing an array of 8 bytes.


Inline Type Reflection
^^^^^^^^^^^^^^^^^^^^^^^

Inline type reflection means storing on type reflection data together with value data.

There are two ways to achieve this:

* Store the type tag only, type information is implicit: This is type tag inlining.
* Store the full type information explicitly: This is type information inlining.

While storing any kind of reflection with values has its proper use-cases, e.g. to protect certain memory
structures in (shared) memory, storing reflection data in general is a discouraged practise.

SOME/IP considerations
""""""""""""""""""""""

An explicit transformation step between the in-memory representation and the SOME/IP+TLV format can – in theory – be avoided by adding TLVs to ABI compatible types.
This approach, however, comes with significant downsides:

* Adding inline type descriptions incurs a significant memory overhead across the board, and leads to worse cache behavior.
* It mandates TLV for *all* instances of *all* ABI compatible types, even when TLV is not needed (for example, in a non-TLV SOME/IP gateway).
  * This might be mitigated by making TLV optional through a generic respectively a template parameter on the type declaration.
* SOME/IP's specification of big-endianness is in conflict with the requirement of native-endianness for ABI compatible types, making the feasibility of this approach questionable.
* SOME/IP doesn't support "unused" slots in dynamic arrays, so ABI compatible types containing *vectors* (which differentiate between the length and the capacity) couldn't be directly represented in SOME/IP anyway.

Alternative Approach
""""""""""""""""""""

Instead of inserting inline type descriptions into each instance of an ABI compatible type, the full type description can be made available to a consumer only once, either proactively or on request.
The consumer decides if it uses or ignores this metadata.

This type description can be used to dynamically translate between the compact, non-reflective ABI compatible data structures on one side, and a reflective, inline-describing format on the other side.
Although this incurs a copy and some minor processing, the overhead should be negligible compared to other computational tasks involving the payload.

One method to efficiently translate a payload consisting of ABI compatible types to an inline-described reflective format is to convert the hierarchical type description to a flat list of *instructions* which can be executed by an interpreter.
Both the instructions and the interpreter would be specific for the target format.
For example, to translate in-memory ABI compatible types to SOME/IP data structures, the instructions could look like this:

.. code: rust

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

.. Rationale
.. ==========



Specification
=============

ABI Compatibility
-----------------

This specification defines the set of rules and constraints for representing data types in shared memory such that they can be interpreted consistently across processes implemented in C++17 and Rust 1.8x. These types enable zero-copy inter-process communication by enforcing ABI compatibility at the memory layout level. The focus is on data exchange between processes running on the same CPU architecture and using the same endianness.

Assumptions
^^^^^^^^^^^

* Shared memory regions are mapped at correctly aligned virtual addresses in both processes.
* No serialization or runtime copying occurs when interpreting a type from memory.
* Processes execute on the same instruction set architecture and use the same endianness.
* No synchronization or atomicity guarantees are defined at the data type level; these are provided by the IPC framework.

Type Conformance
^^^^^^^^^^^^^^^^

Types used in shared memory must meet the following criteria:

1. **Fixed size and alignment**: Every type must have a known, constant size and alignment at compile time.
2. **Consistent layout across languages**: The layout of a type must be identical in Rust and C++ on the same platform.
3. **No pointers or references**: Types must not contain pointers to heap memory, function pointers, or references.
4. **No language-specific metadata**: No vtables, slice headers, or implicit implementation-specific type markers are allowed.

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
     - ``bool`` (1 byte)
   * - Integers (N = 8..128)
     - ``uN``, ``iN``
     - ``std::uintN_t``, ``std::intN_t``
   * - Floating point
     - ``f32``, ``f64``
     - ``float``, ``double``^
   * - Type tag
     - ``TypeTag`` proposed to equal `u64` and be able to
      * encode 8 ASCII characters if MSB is `0` and
      * any 63 bit value if MSB is `1`

All types must avoid trap representations and undefined padding.

Structs and Tuples
""""""""""""""""""

Structs and tuples are supported using standard layout rules:

* **Rust**: Requires ``#[repr(C)]``
* **C++**: Requires ``standard_layout`` types with no inheritance or virtual functions

Field ordering must be preserved and padding must be identical across compilers. Any alignment greater than the default must be explicitly declared.

Enums
"""""

Only fieldless enums with a defined underlying integer type are supported. These must use:

* ``#[repr(u8)]``, ``#[repr(u16)]``, etc. in Rust
* ``enum class MyEnum : std::uint8_t`` in C++

Enums with payloads (discriminated unions) are not supported.

Arrays
""""""

Fixed-size arrays are naturally ABI-compatible and supported in both languages.

* Rust: ``[T; N]``
* C++: ``T[N]``

Element types must also conform to this specification. No dynamic length information is allowed.

Vectors
""""""""

To provide bounded sequence types with familiar APIs, a custom vector implementation must be provided in both languages that matches the memory layout defined below.

.. code-block:: rust

    #[repr(C)]
    pub struct AbiVec<T> {
        pub len: u32,
        pub capacity: u32,
        pub elements: [T; N],
    }

.. code-block:: cpp

    template<typename T, std::size_t N>
    struct AbiVec {
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
        pub is_some: u8,
        pub value: T,
    }

.. code-block:: cpp

    template<typename T>
    struct AbiOption {
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
        pub is_ok: u8,
        pub value: AbiResultUnion<T, E>,
    }

    #[repr(C)]
    pub union AbiResultUnion<T, E> {
        pub ok: T,
        pub err: E,
    }

.. code-block:: cpp

    template<typename T, typename E>
    struct AbiResult {
        std::uint8_t is_ok;
        union {
            T ok;
            E err;
        } value;
    };

* ``is_ok == 1`` indicates ``ok`` field is valid
* ``is_ok == 0`` indicates ``err`` field is valid
* The layout must guarantee correct union member interpretation based on the discriminant

Variant Types
""""""""""""

Variant types represent tagged unions with arbitrary (256 max) possible states.

.. code-block:: rust

    #[repr(C)]
    ...

.. code-block:: cpp

    template<typename T, typename R...>
    struct AbiResult {
        std::uint8_t tag;
        union {
            T value;
            AbiResult<R...> r;
        } value;
    };

    template<typename T>
    struct AbiResult {
       std::uint8_t tag;
       T value;
    };

* ``tag`` containing the current variant.
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

No assumed impact on security.


Safety Impact
=============

.. note::

   This section does not replace a formal safety impact analysis. This only guides the design thoughts behind safety related topics and is to be understood as a starting point for later workflows.

All functionality shall be available to applications rated up to ASIL-B.


.. License Impact
.. ==============


.. How to Teach This
.. ==================

.. Rejected Ideas
.. ==============

.. Open Issues
.. ===========

.. Glossary
.. ========

.. .. _footnotes:

.. Footnotes
.. =========

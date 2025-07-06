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

ABI Compatibility
=================

Restrictions on Native Types
----------------------------

.. feat_req:: Restrict boolean size
   :id: feat_req__abi_compatible_data_types__bool_sz
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   For ABI compatibility, the implementation shall restrict boolean types to one byte (`bool` in Rust and C++).

.. feat_req:: Fixed-width integers
   :id: feat_req__abi_compatible_data_types__int_fix
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   For ABI compatibility, all integer types shall use fixed-width definitions (`uN`/`iN` in Rust; `std::uintN_t`/`std::intN_t` in C++), for N ∈ {8, 16, 32, 64, 128}.

.. feat_req:: Limit floating-point sizes
   :id: feat_req__abi_compatible_data_types__flt_sz
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   For ABI compatibility, floating-point types shall be limited to 32-bit (`f32` in Rust / `float` in C++) and 64-bit (`f64` in Rust / `double` in C++).

.. feat_req:: Fixed-size arrays
   :id: feat_req__abi_compatible_data_types__arr_fix
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   For ABI compatibility, fixed-size arrays shall be declared as `[T; N]` in Rust and `T[N]` in C++, where T itself conforms to the ABI compatibility rules.

.. feat_req:: Struct and tuple ABI layout
   :id: feat_req__abi_compatible_data_types__st_tpl
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   For ABI compatibility, tuples and structs shall preserve field order, use `#[repr(C)]` in Rust, and be `standard_layout` in C++ (no inheritance or virtuals).

.. feat_req:: Explicit enum representation
   :id: feat_req__abi_compatible_data_types__enum_udr
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   For ABI compatibility, enums shall have an explicit, fixed underlying representation (e.g. `#[repr(u8)]` in Rust; `enum class E : std::uint8_t` in C++).

.. feat_req:: Disallow pointers and metadata
   :id: feat_req__abi_compatible_data_types__nop_mt
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   For ABI compatibility, types shall not contain pointers, references, slices, function pointers, vtables, or any language-specific metadata.

.. feat_req:: Compiler-agnostic ABI
   :id: feat_req__abi_compatible_data_types__compabi
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   For ABI compatibility, all native types shall be ABI-compatible across compilers (e.g. GCC and Clang) on the same architecture and endianness.

Custom Types
------------

Vector
^^^^^^

.. feat_req:: Provide AbiVec<T,N>
   :id: feat_req__abi_compatible_data_types__prv_abv
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   An ABI-compatible ``AbiVec<T, N>`` type shall be provided in both C++ and Rust with the specified layout.

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

.. feat_req:: AbiVec field semantics
   :id: feat_req__abi_compatible_data_types__abv_fld
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   ``AbiVec.len`` shall report the current element count; ``AbiVec.capacity`` shall equal the compile-time size ``N``.

.. feat_req:: AbiVec API
   :id: feat_req__abi_compatible_data_types__abv_noa
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   The ``AbiVec`` API shall mirror ``std::vector`` / ``Vec<T>`` but shall not allocate or reallocate memory.

.. feat_req:: AbiVec overflow check
   :id: feat_req__abi_compatible_data_types__abv_ovf
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   Any attempt to exceed ``AbiVec.capacity`` shall result in a checked runtime error.

Option
^^^^^^
.. TODO: Uncomment when issue with "some" in description is resolved

.. .. feat_req:: Provide AbiOption<T>
..    :id: feat_req__abi_compatible_data_types__prv_abo
..    :reqtype: Functional
..    :security: NO
..    :safety: QM
..    :satisfies: stkh_req__communication__abi_compatible
..    :status: valid

..    An ABI-compatible ``AbiOption<T>`` type shall be provided in both C++ and Rust with the specified layout.

..    .. code-block:: rust

..       #[repr(C)]
..       pub struct AbiOption<T> {
..          pub is_some: u8,
..          pub value: T,
..       }

..    .. code-block:: cpp

..       template<typename T>
..       struct AbiOption {
..          std::uint8_t is_some;
..          T value;
..       };

.. .. feat_req:: AbiOption is_some flag
..    :id: feat_req__abi_compatible_data_types__abo_flg
..    :reqtype: Functional
..    :security: NO
..    :safety: QM
..    :satisfies: stkh_req__communication__abi_compatible
..    :status: valid

..    ``AbiOption.is_some`` shall be ``0`` when empty and ``1`` when containing a value.

.. feat_req:: AbiOption API
   :id: feat_req__abi_compatible_data_types__abo_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   The ``AbiOption`` API shall mirror ``std::optional``/``Option<T>`` without introducing extra fields or indirections.

Result
^^^^^^

.. feat_req:: Provide AbiResult<T,E>
   :id: feat_req__abi_compatible_data_types__prv_ari
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   An ABI-compatible ``AbiResult<T, E>`` type shall be provided in both C++ and Rust with the specified layout.

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

.. feat_req:: AbiResult is_ok flag
   :id: feat_req__abi_compatible_data_types__ari_flg
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   ``AbiResult.is_ok`` shall be ``1`` if ``value.ok`` is valid, and ``0`` if ``value.err`` is valid.

.. feat_req:: AbiResult API
   :id: feat_req__abi_compatible_data_types__ari_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible
   :status: valid

   The ``AbiResult`` API shall mirror ``std::expected``/``Result<T, E>`` without hidden storage or pointers.

Type Description
================

.. feat_req:: Runtime type description
   :id: feat_req__abi_compatible_data_types__rt_desc
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible, stkh_req__communication__extensible_external
   :status: valid

   The system shall provide a runtime-accessible type description for each data type defined for ABI compatibility.

.. feat_req:: Layout structural info
   :id: feat_req__abi_compatible_data_types__lay_inf
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible, stkh_req__communication__extensible_external
   :status: valid

   The type description shall contain sufficient structural information to interpret the in-memory layout of a data instance according to the ABI compatibility rules defined for supported target languages (C++17 and Rust 1.8x).

.. feat_req:: Versioned schemas
   :id: feat_req__abi_compatible_data_types__ver_sch
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible, stkh_req__communication__extensible_external
   :status: valid

   The type description format shall support versioning to allow evolution and backward compatibility of type schemas.

.. feat_req:: Schema-defined input
   :id: feat_req__abi_compatible_data_types__sch_inp
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible, stkh_req__communication__extensible_external
   :status: valid

   The system shall support a schema-defined type description as input to the build process to generate language-specific type definitions.

.. feat_req:: Native definitions input
   :id: feat_req__abi_compatible_data_types__nat_inp
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible, stkh_req__communication__extensible_external
   :status: valid

   The system shall support language-native type definitions as input, from which the type description is extracted during the build process.

.. feat_req:: Structured serialization
   :id: feat_req__abi_compatible_data_types__serial
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__abi_compatible, stkh_req__communication__extensible_external
   :status: valid

   The system shall support at least one structured serialization format (e.g., RON, JSON5, or equivalent) for the representation of type descriptions.

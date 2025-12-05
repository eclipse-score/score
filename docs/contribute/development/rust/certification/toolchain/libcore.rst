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

Certified libcore
#################

.. tool_req:: Rust libcore
   :id: tool_req__rust_libcore
   :safety: ASIL_B
   :security: NO
   :status: valid

   Rust `libcore` shall be certified at `ASIL-B` or higher for below list of modules:

   .. list-table::
      :header-rows: 1
      :widths: 15 10 60

      * - Module
        - Certification Available (Ferrocene)
        - Comment
      * - alloc
        - WIP
        - Memory allocation APIs
      * - any
        - ✅
        - Utilities for dynamic typing or type reflection.
      * - array
        - ✅
        - Utilities for the array primitive type.
      * - cell
        - ✅
        - Shareable mutable containers.
      * - clone
        - ✅
        - The Clone trait for types that cannot be ‘implicitly copied’.
      * - cmp
        - ✅
        - Utilities for comparing and ordering values.
      * - convert
        - ✅
        - Traits for conversions between types.
      * - default
        - ✅
        - The Default trait for types with a default value.
      * - f32
        - ✅
        - Constants for the f32 single-precision floating point type.
      * - f64
        - ✅
        - Constants for the f64 double-precision floating point type.
      * - fmt
        - WIP
        - Utilities for formatting and printing strings.
      * - hint
        - ✅
        - Hints to the compiler that affect how code is emitted or optimized.
      * - iter
        - ✅
        - Composable external iteration.
      * - marker
        - ✅
        - Primitive marker traits and types.
      * - mem
        - ✅
        - Basic functions for managing memory.
      * - num
        - ✅
        - Numeric traits and functions.
      * - ops
        - ✅
        - Overloadable operators.
      * - option
        - ✅
        - Optional values.
      * - panic
        - ✅
        - Panic support in the standard library.
      * - prelude
        - ✅
        - The core prelude.
      * - ptr
        - ✅
        - Raw pointer memory management.
      * - result
        - ✅
        - Error handling with the Result type.
      * - slice
        - ✅
        - Slice management and manipulation.
      * - str
        - ✅
        - String manipulation.
      * - sync
        - ✅
        - Synchronization primitives.
      * - time
        - ❓
        - Temporal quantification. Tracked via https://github.com/eclipse-score/score/issues/2248
      * - task
        - ❌
        - Types and Traits for working with asynchronous tasks. Tracked via https://github.com/eclipse-score/score/issues/2248
      * - pin
        - ❌
        - Types that pin data to a location in memory. Tracked via https://github.com/eclipse-score/score/issues/2248
      * - future
        - ❌
        - Asynchronous basic functionality. Tracked via https://github.com/eclipse-score/score/issues/2248
      * - ffi
        - ❌
        - Platform-specific types, as defined by C. Tracked via https://github.com/eclipse-score/score/issues/2248


.. tool_req:: Automatic checking of libcore usage
   :id: tool_req__rust_libcore_automatic_check
   :security: NO
   :safety: ASIL_B
   :status: valid

   The compiler or SCA tool shall automatically check that only certified modules from `libcore` are used in safety-critical components.

   .. note:: This requirement is satisfied via the Ferrocene toolchain integration in the build system. TO BE CONFIRMED!

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

futurecpp
#########

.. document:: FutureCPP Library
   :id: doc__futurecpp
   :status: draft
   :safety: ASIL_B
   :tags: baselibs_futurecpp
   :realizes: wp__cmpt_request
   :security: YES

.. toctree::
   :hidden:

Abstract
========

FutureCPP extends the C++ Standard Library with features from newer standards up to C++26 and selected proposals, offering an STL-like API.

Motivation and Rationale
========================

Adopting the latest C++ standards is often challenging in safety-critical environments, which can delay access to modern language and library features.
FutureCPP addresses this by providing forward-compatible extensions that mirror upcoming Standard Library capabilities, allowing developers to benefit
from modern APIs without waiting for full compiler support. This approach ensures smoother transitions to future standards.

Following components are provided by FutureCPP:

- **Containers library**: Provides data structures such as fixed-size circular buffers, multi-dimensional array views, and containers for optional or variant types.
- **Functional library**: Provides APIs for function wrappers and error handling.
- **Numeric and Math library**: Provides mathematical utilities such as angle conversions, safe numeric casts, interpolation, and angle wrapping.
- **Memory management library**: Provides polymorphic allocators and related utilities which allow flexible memory allocation.
- **Meta Programming**: Provides compile-time utilities for generic programming, enabling type-safe abstractions and reducing code duplication.
- **Threading Support**: Provides API for thread management.
- **Utilities library**: Provides APIs for type safe conversion.
- **String Utilities**: Provides APIs for managing string related functionality.

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

static_reflection_with_serialization
####################################

.. document:: Static Reflection With Serialization Library
   :id: doc__static_reflection_with_serialization
   :status: draft
   :safety: ASIL_B
   :tags: baselibs_static_reflection_with_serialization
   :realizes: wp__cmpt_request
   :security: YES

.. toctree::
   :hidden:

Abstract
=========

This component request proposes a static reflection with serialization library, which provides compile-time visitor pattern
mechanisms and binary serialization capabilities for the S-CORE software platform. The library enables type-safe object
traversal, struct introspection, and efficient data serialization or deserialization.

Motivation and Rationale
=========================

The static reflection with serialization library shall provide mechanism for:

- **Compile-time visitor pattern**: Type-safe traversal of heterogeneous data structures and their nested members using template metaprogramming.
- **Struct introspection**: Automatic field enumeration and metadata extraction for aggregate types.
- **Binary serialization**: Efficient serialization and deserialization of C++ objects with size calculation and type safety.
- **Extensible processing**: Custom visitor implementations for domain-specific operations (logging, IPC, persistence).

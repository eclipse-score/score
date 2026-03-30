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

Baselibs Module
###############

.. toctree::
   :titlesonly:
   :hidden:
   :glob:

   ./docs/index
   language/index
   ./*/docs/index

Components
==========

- :need:`doc__bitmanipulation`: Utilities for bit manipulation.
- :need:`doc__concurrency`: Provides a generic interface to execute any C++ callable in a parallel context,
  supporting various execution strategies (e.g., thread pool, timed execution), thread safety,
  interruption handling, and periodic/delayed task execution.
- :need:`doc__containers`: Offers a ``DynamicArray`` (fixed-size array with dynamic construction-time size)
  and an intrusive linked list implementation conforming to the
  `P0406R1 proposal <https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0406r1.html>`_.
- :need:`doc__json`: JSON abstraction layer that can switch between different parsers/serializers under the hood.
- :need:`doc__filesystem`: Filesystem manipulation library similar to ``std::filesystem``.
- :need:`doc__futurecpp`: Extends the C++17 Standard Library with features from newer C++ standards up to C++26,
  as well as selected proposals for the C++ Standard Library.
- :need:`doc__safecpp`: A collection of utilities that helps developers write safer C++ code, including
  overflow-safe arithmetic, scoped callable execution, abort-on-exception enforcement, atomic overflow
  prevention, null-terminated string view utilities, and coverage data preservation in GTest death tests.
- :need:`doc__memory`: Utility library for memory handling, including an abstraction layer for shared memory.
- :need:`doc__os`: OS Abstraction Layer (OSAL) to interface with different POSIX-like operating systems such
  as Linux and QNX.
- :need:`doc__result`: Provides a unified approach to error handling without exceptions, conforming to C++23
  ``std::expected``.
- :need:`doc__static_reflection_with_serialization`: A header-only library for binary serialization,
  deserialization, and compile-time type reflection of heterogenuous C++ data structures with focus
  on compile-time safety and efficiency of serialization, as well as efficiency of filtering by
  content during deserialization.
- *mw::log*: Logging frontend.
- :need:`doc__utils`: Provides a collection of small, reusable utilities that do not fit into the other
  base libraries.

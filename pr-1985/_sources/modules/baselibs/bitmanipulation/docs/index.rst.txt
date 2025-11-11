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

bitmanipulation
###############

.. document:: Bit Manipulation Library
   :id: doc__bitmanipulation
   :status: draft
   :safety: ASIL_B
   :tags: baselibs_bitmanipulation
   :realizes: wp__cmpt_request

.. toctree::
   :hidden:

   requirements/index.rst


Abstract
========

This component request proposes the integration of a safe Bit Manipulation library for constexpr bit operations and byte manipulation. It integrates a type-safe Bitmask Operator library.


Motivation and Rationale
========================

The Bit Manipulation library provides a type-safe mechanism to perform bitwise operations on integral types.
It enables safe and efficient bit operations and supports the development of safety-critical features by offering clear and reliable bit manipulation capabilities.
A Bit Manipulation library with constexpr operations is required in the S-CORE software platform to enable efficient, compile-time bit operations for embedded and automotive applications.
Typical use cases include setting control flags, extracting byte data from raw integers, and performing low-level bit operations with compile-time guarantees.
It integrates a type-safe Bitmask Operator library that extends enum class types to support standard bitmask operations ('|', '&', '^', '~', and their assignment forms).

Specification
=============

The following details and requirements describe the aspects of the current feature in the context of S-CORE.

General considerations
----------------------

The Bit Manipulation library should provide bit operation and byte extraction capabilities:

* :need:`comp_req__bitmanipulation__utilities`
* :need:`comp_req__bitmanipulation__bitmask_operators`
* :need:`comp_req__bitmanipulation__bounds_safety`
* :need:`comp_req__bitmanipulation__header_only`

The component should be extensible in the future to support richer error information and integration with other platform components.

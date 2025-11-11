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


.. _bitmanipulation_requirements:

Requirements
############

.. document:: Bit Manipulation Requirements
   :id: doc__bitmanipulation_requirements
   :status: draft
   :safety: ASIL_B
   :realizes: wp__requirements_comp
   :tags: requirements, bitmanipulation

Functional Requirements
=======================

.. comp_req:: Support for Bit Manipulation Utilities
   :id: comp_req__bitmanipulation__utilities
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__bitmanipulation, feat_req__baselibs__core_utilities
   :status: valid

   The bit manipulation component shall provide API for setting, clearing, toggling, and checking bits, as well as extracting bytes and manipulating half-bytes and bytes for any integral type up to 64 bits.

.. comp_req:: Support for Bitmask Operators for Enum Classes
   :id: comp_req__bitmanipulation__bitmask_operators
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__bitmanipulation, feat_req__baselibs__core_utilities
   :status: valid

   The bit manipulation library shall provide type-safe bitmask operations for scoped enumeration types.

.. comp_req:: Bounds and Safety Checks
   :id: comp_req__bitmanipulation__bounds_safety
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__bitmanipulation, feat_req__baselibs__safety
   :status: valid

   All bit manipulation functions shall validate input parameters and prevent data corruption.

Non-Functional Requirements
===========================

.. comp_req:: Header-only API
   :id: comp_req__bitmanipulation__header_only
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__bitmanipulation
   :status: valid

   The bit manipulation API shall be header-only and not require external dependencies.

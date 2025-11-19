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

JSON Component Architecture
===========================

.. document:: JSON Architecture
   :id: doc__json_architecture
   :status: draft
   :safety: ASIL_B
   :realizes: wp__component_arch

Overview
--------
The component JSON implements functionality for reading/parsing JSON data and also to write.
It provides currently only a C++ API.

Requirements Linked to Component Architecture
---------------------------------------------

See the "fulfils" links in static and dynamic architecture below.

Description
-----------

JSON provides an abstraction layer to underlying implementations, in first iteration there is only one
implementation provided. But generally there is a "Wrapper" and an "Implementation" lower-level component.

Design Decisions:

It was decided to use the nlohman_json OSS library (see `nlohman/json <https://github.com/nlohmann/json>`_). This decision still has to be documented (TBD).

JSON writing functionality is implemented in the "Wrapper", i.e. the nlohman_json OSS library is not used for this.
Reasoning is that this functionality is reused from an already qualified baselibs implementation.

Design Constraints:

The feature description states that this component provides a "JSON abstraction layer that can switch between different parsers/serializers under the hood."

Rationale Behind Architecture Decomposition
*******************************************

The decomposition in a wrapper and an implemetation component already comes from the feature definition,
the main driver is to re-use existing implementation(s), enable switch of implementation but providing a stable API.

Static Architecture
-------------------

.. comp_arc_sta:: JSON
   :id: comp_arc_sta__baselibs__json
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :implements: logic_arc_int__baselibs__json
   :includes: comp_arc_sta__baselibs__json_wrapper, comp_arc_sta__baselibs__nlohman_json
   :fulfils: comp_req__json__deserialization, comp_req__json__serialization, comp_req__json__user_format, comp_req__json__lang_idioms, comp_req__json__lang_infra, comp_req__json__type_compatibility, comp_req__json__full_testability, comp_req__json__asil

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}


Dynamic Architecture
--------------------

.. comp_arc_dyn:: JSON dynamic arch
   :id: comp_arc_dyn__baselibs__json_dynamic_view
   :security: YES
   :safety: ASIL_B
   :status: invalid
   :fulfils: comp_req__json__deserialization, comp_req__json__serialization, comp_req__json__user_format, comp_req__json__lang_idioms, comp_req__json__lang_infra, comp_req__json__type_compatibility, comp_req__json__full_testability, comp_req__json__asil

   put here a sequence diagram (TBD)


Interfaces
----------

.. logic_arc_int:: IJson
   :id: logic_arc_int__baselibs__json
   :security: YES
   :safety:  ASIL_B
   :status: valid

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: Parse
   :id: logic_arc_int_op__baselibs__parse
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__json

.. logic_arc_int_op:: Write
   :id: logic_arc_int_op__baselibs__write
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__json

Lower Level Components
----------------------

.. comp_arc_sta:: JSON-Wrapper
   :id: comp_arc_sta__baselibs__json_wrapper
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :implements: logic_arc_int__baselibs__json
   :fulfils: comp_req__json__user_format, comp_req__json__lang_idioms, comp_req__json__lang_infra, comp_req__json__type_compatibility, comp_req__json__full_testability, comp_req__json__serialization, comp_req__json__asil

.. comp_arc_sta:: nlohman-JSON
   :id: comp_arc_sta__baselibs__nlohman_json
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :fulfils: comp_req__json__deserialization, comp_req__json__asil

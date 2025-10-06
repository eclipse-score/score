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
***************************

.. comp_arc_sta:: JSON-Library
   :id: comp_arc_sta__baselibs__json
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :implements: logic_arc_int__baselibs__json
   :includes: comp_arc_sta__baselibs__json_wrapper, comp_arc_sta__baselibs__nlohman_json
   :fulfils: comp_req__json__validation, comp_req__json__deserialization, comp_req__json__serialization, comp_req__json__user_format, comp_req__json__lang_idioms, comp_req__json__lang_infra, comp_req__json__type_compatibility, comp_req__json__full_testability, comp_req__json__asil

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

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
   :id: logic_arc_int_op__baselibs__fromfile
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__json

.. logic_arc_int_op:: Check
   :id: logic_arc_int_op__baselibs__validate
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__json

.. logic_arc_int_op:: Dump
   :id: logic_arc_int_op__baselibs__tofile
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__json

.. comp_arc_sta:: JSON-Wrapper
   :id: comp_arc_sta__baselibs__json_wrapper
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :implements: logic_arc_int__baselibs__json
   :fulfils: comp_req__json__user_format, comp_req__json__lang_idioms, comp_req__json__lang_infra, comp_req__json__type_compatibility, comp_req__json__full_testability, comp_req__json__asil

.. comp_arc_sta:: nlohman-JSON
   :id: comp_arc_sta__baselibs__nlohman_json
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :fulfils: comp_req__json__validation, comp_req__json__deserialization, comp_req__json__serialization, comp_req__json__asil

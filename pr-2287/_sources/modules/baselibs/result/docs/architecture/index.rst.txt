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

Result Component Architecture
*****************************

.. document:: Result Architecture
   :id: doc__result_architecture
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__component_arch

Overview/Description
--------------------

see :need:`doc__result`

Static Architecture
-------------------

.. comp_arc_sta:: Result
   :id: comp_arc_sta__baselibs__result
   :security: YES
   :safety: ASIL_B
   :status: valid
   :tags: baselibs_result
   :implements: logic_arc_int__baselibs__result

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

Interfaces
----------

.. logic_arc_int:: Result
   :id: logic_arc_int__baselibs__result
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Set Result
   :id: logic_arc_int_op__baselibs__set_result
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__result

.. logic_arc_int_op:: Get Value
   :id: logic_arc_int_op__baselibs__get_value
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__result

.. logic_arc_int_op:: Get Error
   :id: logic_arc_int_op__baselibs__get_error
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__result

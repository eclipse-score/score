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

Container Component Architecture
********************************

.. document:: Container Architecture
   :id: doc__containers_architecture
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__component_arch

Overview/Description
--------------------

see :need:`doc__containers_architecture`

Static Architecture
-------------------

.. comp_arc_sta:: Containers
   :id: comp_arc_sta__baselibs__containers
   :security: YES
   :safety: ASIL_B
   :status: valid
   :tags: baselibs_containers
   :implements: logic_arc_int__baselibs__dynamic_array, logic_arc_int__baselibs__intrusive_list


    .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}


Interfaces
----------

.. logic_arc_int:: Dynamic Array
   :id: logic_arc_int__baselibs__dynamic_array
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Access
   :id: logic_arc_int_op__containers__dynarray_access
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__dynamic_array

.. logic_arc_int_op:: Iterate
   :id: logic_arc_int_op__containers__dynarray_itrate
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__dynamic_array

.. logic_arc_int_op:: Change
   :id: logic_arc_int_op__containers__dynarray_change
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__dynamic_array

.. logic_arc_int:: Intrusive List
   :id: logic_arc_int__baselibs__intrusive_list
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Insert
   :id: logic_arc_int_op__baselibs__intr_list_insert
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__intrusive_list

.. logic_arc_int_op:: Remove
   :id: logic_arc_int_op__baselibs__intr_list_remove
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__intrusive_list

.. logic_arc_int_op:: Iterate
   :id: logic_arc_int_op__baselibs__intr_list_iterate
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__intrusive_list

.. logic_arc_int_op:: Access
   :id: logic_arc_int_op__baselibs__intr_list_access
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__intrusive_list

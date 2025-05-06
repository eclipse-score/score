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

.. _definition_architectural_design:

Example model of architectural design
#####################################

This chapter only serves as an example how an architecture could be modeled in *Sphinx Needs*. All the needs are required to print the views which are displayed in the Static- and Interface Views. In the actual process this files would be split into multiple different files:

Feature Architecture File
=========================

.. feat_arc_sta:: Feature 1
   :id: feat_arc_sta__archdes_static
   :security: YES
   :safety: QM
   :status: valid
   :includes: logic_arc_int__archdes_logical_interface_1, logic_arc_int__archdes_logical_interface_2
   :fulfils: feat_req__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}

.. Logical Interfaces

.. logic_arc_int:: Logical Interface 2
   :id: logic_arc_int__archdes_logical_interface_2
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}


.. logic_arc_int:: Logical Interface 3
   :id: logic_arc_int__archdes_logical_interface_3
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__archdes_example_req


.. Logical Interface Operation

.. logic_arc_int_op:: Logical Operation 1
   :id: logic_arc_int_op__archdes_logical_operation_1
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__archdes_logical_interface_1

.. logic_arc_int_op:: Logical Operation 2
   :id: logic_arc_int_op__archdes_logical_operation_2
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__archdes_logical_interface_1

.. logic_arc_int_op:: Logical Operation 3
   :id: logic_arc_int_op__archdes_logical_operation_3
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__archdes_logical_interface_2

.. logic_arc_int_op:: Logical Operation 4
   :id: logic_arc_int_op__archdes_logical_operation_4
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__archdes_logical_interface_2

.. logic_arc_int_op:: Logical Operation 5
   :id: logic_arc_int_op__archdes_logical_operation_5
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__archdes_logical_interface_3

.. logic_arc_int_op:: Logical Operation 6
   :id: logic_arc_int_op__archdes_logical_operation_6
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__archdes_logical_interface_3

.. logic_arc_int_op:: Logical Operation 7
   :id: logic_arc_int_op__archdes_logical_operation_7
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__archdes_logical_interface_3

.. logic_arc_int_op:: Logical Operation 8
   :id: logic_arc_int_op__archdes_logical_operation_8
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__archdes_logical_interface_3


Module Viewpoint
================

.. mod_view_sta:: Module 1
   :id: mod_view_sta__archdes_1
   :includes: comp_arc_sta__archdes_component_1

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

.. mod_view_sta:: Module 2
   :id: mod_view_sta__archdes_2
   :includes: comp_arc_sta__archdes_component_3

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

Component Architecure File(s)
=============================

.. comp_arc_sta:: Component 1
   :id: comp_arc_sta__archdes_component_1
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: logic_arc_int__archdes_logical_interface_3
   :implements: logic_arc_int__archdes_logical_interface_1, logic_arc_int__archdes_logical_interface_2
   :fulfils: comp_req__archdes_example_req
   :includes: comp_arc_sta__archdes_sub_component_1, comp_arc_sta__archdes_sub_component_2, comp_arc_sta__archdes_sub_component_3

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. comp_arc_sta:: Component 3
   :id: comp_arc_sta__archdes_component_3
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: logic_arc_int__archdes_logical_interface_3
   :fulfils: comp_req__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. Subcomponents

.. comp_arc_sta:: Lower Level Component 1
   :id: comp_arc_sta__archdes_sub_component_1
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: logic_arc_int__archdes_logical_interface_3
   :implements: logic_arc_int__archdes_logical_interface_2
   :fulfils: comp_req__archdes_example_req

.. comp_arc_sta:: Lower Level Component 2
   :id: comp_arc_sta__archdes_sub_component_2
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: logic_arc_int__archdes_logical_interface_3
   :implements: logic_arc_int__archdes_logical_interface_2
   :fulfils: comp_req__archdes_example_req

.. comp_arc_sta:: Lower Level Component 3
   :id: comp_arc_sta__archdes_sub_component_3
   :status: valid
   :safety: QM
   :security: NO
   :implements: logic_arc_int__archdes_logical_interface_3
   :fulfils: comp_req__archdes_example_req

..
    Requirements

.. stkh_req:: Example Stkh Req
   :id: stkh_req__archdes_example_req
   :reqtype: Functional
   :safety: ASIL_B
   :rationale: needed for archdes example
   :status: valid

.. feat_req:: Example Feature Req
   :id: feat_req__archdes_example_req
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__archdes_example_req
   :status: valid

   The feature shall provide the functionality to ....

.. comp_req:: Example Component Req
   :id: comp_req__archdes_example_req
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__archdes_example_req
   :status: valid

   The component shall provide the Logical Operation 4 to get the ..

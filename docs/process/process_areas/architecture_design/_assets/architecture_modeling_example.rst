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
   :includes: feat_arc_int__archdes_logical_interface_1, feat_arc_int__archdes_logical_interface_2
   :fulfils: feat_req__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}

.. Logical Interfaces

.. feat_arc_int:: Logical Interface 2
   :id: feat_arc_int__archdes_logical_interface_2
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}


.. feat_arc_int:: Logical Interface 3
   :id: feat_arc_int__archdes_logical_interface_3
   :security: YES
   :safety: ASIL_B
   :status: valid
   :includes: feat_arc_int_op__archdes_logical_operation_7, feat_arc_int_op__archdes_logical_operation_8
   :fulfils: feat_req__archdes_example_req


.. Logical Interface Operation

.. feat_arc_int_op:: Logical Operation 1
   :id: feat_arc_int_op__archdes_logical_operation_1
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: feat_arc_int__archdes_logical_interface_1

.. feat_arc_int_op:: Logical Operation 2
   :id: feat_arc_int_op__archdes_logical_operation_2
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: feat_arc_int__archdes_logical_interface_1

.. feat_arc_int_op:: Logical Operation 3
   :id: feat_arc_int_op__archdes_logical_operation_3
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: feat_arc_int__archdes_logical_interface_2

.. feat_arc_int_op:: Logical Operation 4
   :id: feat_arc_int_op__archdes_logical_operation_4
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: feat_arc_int__archdes_logical_interface_2

.. feat_arc_int_op:: Logical Operation 5
   :id: feat_arc_int_op__archdes_logical_operation_5
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: feat_arc_int__archdes_logical_interface_3

.. feat_arc_int_op:: Logical Operation 6
   :id: feat_arc_int_op__archdes_logical_operation_6
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: feat_arc_int__archdes_logical_interface_3

.. feat_arc_int_op:: Logical Operation 7
   :id: feat_arc_int_op__archdes_logical_operation_7
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: feat_arc_int__archdes_logical_interface_3

.. feat_arc_int_op:: Logical Operation 8
   :id: feat_arc_int_op__archdes_logical_operation_8
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: feat_arc_int__archdes_logical_interface_3


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
   :uses: comp_arc_int__archdes_component_interface_3
   :implements: comp_arc_int__archdes_component_interface_1, comp_arc_int__archdes_component_interface_2
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
   :implements: comp_arc_int__archdes_component_interface_3
   :fulfils: comp_req__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. Component Interfaces

.. comp_arc_int:: Component Interface 2
   :id: comp_arc_int__archdes_component_interface_2
   :status: valid
   :safety: ASIL_B
   :security: NO
   :fulfils: comp_req__archdes_example_req
   :language: cpp

.. comp_arc_int:: Component Interface 3
   :id: comp_arc_int__archdes_component_interface_3
   :status: valid
   :safety: ASIL_B
   :security: NO
   :fulfils: comp_req__archdes_example_req
   :language: cpp

.. comp_arc_int:: Component Interface 4
   :id: comp_arc_int__archdes_component_interface_4
   :status: valid
   :safety: ASIL_B
   :security: NO
   :fulfils: comp_req__archdes_example_req
   :language: cpp

.. Subcomponents

.. comp_arc_sta:: Lower Level Component 1
   :id: comp_arc_sta__archdes_sub_component_1
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: comp_arc_int_op__archdes_real_operation_7
   :implements: comp_arc_int_op__archdes_real_operation_3
   :fulfils: comp_req__archdes_example_req

.. comp_arc_sta:: Lower Level Component 2
   :id: comp_arc_sta__archdes_sub_component_2
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: comp_arc_int_op__archdes_real_operation_8
   :implements: comp_arc_int_op__archdes_real_operation_4
   :fulfils: comp_req__archdes_example_req

.. comp_arc_sta:: Lower Level Component 3
   :id: comp_arc_sta__archdes_sub_component_3
   :status: valid
   :safety: QM
   :security: NO
   :implements: comp_arc_int_op__archdes_real_operation_7, comp_arc_int_op__archdes_real_operation_8
   :fulfils: comp_req__archdes_example_req

.. Component Interface Operations

.. comp_arc_int_op:: real operation 1
   :id: comp_arc_int_op__archdes_real_operation_1
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__archdes_component_interface_1

.. comp_arc_int_op:: real operation 2
   :id: comp_arc_int_op__archdes_real_operation_2
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_2
   :included_by: comp_arc_int__archdes_component_interface_1

.. comp_arc_int_op:: real operation 3
   :id: comp_arc_int_op__archdes_real_operation_3
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_3
   :included_by: comp_arc_int__archdes_component_interface_2

.. comp_arc_int_op:: real operation 4
   :id: comp_arc_int_op__archdes_real_operation_4
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_4
   :included_by: comp_arc_int__archdes_component_interface_2

.. comp_arc_int_op:: real operation 5
   :id: comp_arc_int_op__archdes_real_operation_5
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_5
   :included_by: comp_arc_int__archdes_component_interface_3

.. comp_arc_int_op:: real operation 6
   :id: comp_arc_int_op__archdes_real_operation_6
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_6
   :included_by: comp_arc_int__archdes_component_interface_3

.. comp_arc_int_op:: real operation 7
   :id: comp_arc_int_op__archdes_real_operation_7
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_7
   :included_by: comp_arc_int__archdes_component_interface_4

.. comp_arc_int_op:: real operation 8
   :id: comp_arc_int_op__archdes_real_operation_8
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_8
   :included_by: comp_arc_int__archdes_component_interface_4

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

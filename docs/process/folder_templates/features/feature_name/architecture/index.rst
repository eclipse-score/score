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

.. _feature_architecture_template:

Feature Architecture
====================

Overview
--------
Brief summary

Description
-----------

General Description

Design Decisions

Design Constraints

Requirements
------------

.. code-block:: none

   .. needtable:: Overview of Feature Requirements
      :style: table
      :columns: title;id
      :filter: search("feat_arch_sta__archdes$", "fulfils_back")
      :colwidths: 70,30


Rationale Behind Architecture Decomposition
*******************************************
mandatory: a motivation for the decomposition

.. note:: Common decisions across features / cross cutting concepts is at the high level.

Static Architecture
-------------------

.. feat_arc_sta:: Static View
   :id: feat_arc_sta__feature_name__static_view
   :security: YES
   :safety: ASIL_D
   :status: invalid
   :fulfils: feat_req__feature_name__some_title
   :includes: logic_arc_int__feature_name__interface_name

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}

Dynamic Architecture
--------------------

.. feat_arc_dyn:: Dynamic View
   :id: feat_arc_dyn__feature_name__dynamic_view
   :security: YES
   :safety: ASIL_D
   :status: invalid
   :fulfils: feat_req__feature_name__some_title

   put here a sequence diagram

Logical Interfaces
------------------

.. logic_arc_int:: Interface Name
   :id: logic_arc_int__feature_name__interface_name
   :security: YES
   :safety: ASIL_D
   :status: invalid

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: Operation
   :id: logic_arc_int_op__feature_name__operation
   :security: YES
   :safety: ASIL_D
   :status: invalid
   :included_by: logic_arc_int__feature_name__interface_name

Module Viewpoint
----------------

The following modules are needed to be defined to be able to draw the static feature view.
They will be replaced by linking the proper module definitions in the used module's repositories as soon as those exist.

.. mod_view_sta:: Module Name
   :id: mod_view_sta__feature_name_module_name
   :includes: comp_arc_sta__feature_name_component_name

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

Used Components
---------------

The following components are needed to be defined to be able to draw the static feature view.
They will be replaced by linking the proper SW component definitions in the used module's repositories as soon as those exist.

.. comp_arc_sta:: Component Name
   :id: comp_arc_sta__feature_name_component_name
   :safety: ASIL_D
   :security: YES
   :status: invalid
   :implements: logic_arc_int__feature_name__interface_name

.. note::
   Architecture can be split into multiple files, it is an High level architecture_design
   which can be shown without actual c++/rust interfaces and data types
   and there will be link to lower level architecture till code to get actual api descriptions.

.. needextend:: "feature_name/architecture" in docname
   :+tags: feature_name

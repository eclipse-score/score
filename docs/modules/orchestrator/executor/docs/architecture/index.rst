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

Component Architecture
======================

.. document:: Executor Architecture
   :id: doc__executor_architecture
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__component_arch
   :tags: orchestration, executor


Overview
--------
Brief summary

Requirements Linked to Component Architecture
---------------------------------------------

.. code-block:: none

   .. needtable:: Overview of Component Requirements
      :style: table
      :columns: title;id
      :filter: search("comp_arch_sta__archdes$", "fulfils_back")
      :colwidths: 70,30

Description
-----------

General Description

Design Decisions - For the documentation of the decision the :need:`gd_temp__change_decision_record` can be used.

Design Constraints

Rationale Behind Architecture Decomposition
*******************************************

Mandatory: a motivation for the decomposition or reason for not further splitting it into lower level components.

.. note:: Common decisions across components / cross cutting concepts is at the higher level.

Static Architecture
-------------------

The components are designed to cover the expectations from the feature architecture
(i.e. if already exists a definition it should be taken over and enriched).

.. comp_arc_sta:: Executor
   :id: comp_arc_sta__orch__executor
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :uses: logic_arc_int__logging__logging, logic_arc_int__tracing__tracing

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

Dynamic Architecture
--------------------

.. .. comp_arc_dyn:: Dynamic View
..    :id: comp_arc_dyn__component_name__dynamic_view
..    :security: YES
..    :safety: ASIL_B
..    :status: invalid
..    :fulfils: comp_req__component_name__some_title

..    put here a sequence diagram


Interfaces
----------

.. code-block:: rst

   .. real_arc_int:: <Title>
      :id: real_arc_int__<component>__<Title>
      :security: <YES|NO>
      :safety: <QM|ASIL_B>
      :fulfils: <link to component requirement id>
      :language: cpp

Lower Level Components
----------------------

.. .. comp_arc_sta:: Component Name 2
..    :id: comp_arc_sta__component_name__2
..    :status: invalid
..    :safety: ASIL_B
..    :security: YES
..    :fulfils: comp_req__component_name__some_title
..    :implements: logic_arc_int__feature_name__interface_name

..    no architecture but detailed design

.. .. note::
..    Architecture can be split into multiple files. At component level the public interfaces to be used by the user and tester to be shown.

.. .. attention::
..     The above directives must be updated according to your component architecture.

..     - Replace the example content by the real content (according to :need:`gd_guidl__arch_design`)
..     - Set the status to valid and start the review/merge process

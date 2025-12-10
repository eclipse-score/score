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

.. document:: Orchestrator Architecture
   :id: doc__orchestrator_architecture
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__component_arch
   :tags: orchestration, orchestrator


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





Component Architecture
=======================












Static Architecture
-------------------

The components are designed to cover the expectations from the feature architecture
(i.e. if already exists a definition it should be taken over and enriched).

.. comp_arc_sta:: Orchestrator
   :id: comp_arc_sta__orch__orchestrator
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :includes: comp_arc_sta__orch__design_impl, comp_arc_sta__orch__deployment_impl
   :implements: logic_arc_int__orchestration__user, logic_arc_int__orchestration__deployment, logic_arc_int__orchestration__design
   :uses: logic_arc_int__logging__logging, logic_arc_int__tracing__tracing, logic_arc_int__communication__user

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


.. logic_arc_int_op:: add_design
   :id: logic_arc_int_op__orch__add_design
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__user


.. logic_arc_int_op:: desing_done
   :id: logic_arc_int_op__orch__desing_done
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__user


.. logic_arc_int_op:: get_deployment_mut
   :id: logic_arc_int_op__orch__get_deployment_mut
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__user


.. logic_arc_int_op:: use_config
   :id: logic_arc_int_op__orch__use_config
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__user

.. logic_arc_int_op:: into_program_manager
   :id: logic_arc_int_op__orch__into_program_manager
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__user

.. logic_arc_int_op:: get_programs
   :id: logic_arc_int_op__orch__get_programs
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__user

.. logic_arc_int_op:: get_shutdown_notifier
   :id: logic_arc_int_op__orch__get_shutdown_notifier
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__user

.. Subcomponents

.. comp_arc_sta:: Design
   :id: comp_arc_sta__orch__design_impl
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: logic_arc_int__orchestration__design

.. comp_arc_sta:: Deployment
   :id: comp_arc_sta__orch__deployment_impl
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: logic_arc_int__orchestration__deployment

.. Operations


.. logic_arc_int_op:: register_invoke_fn
   :id: logic_arc_int_op__orch__register_invoke_fn
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__design

.. logic_arc_int_op:: register_invoke_method
   :id: logic_arc_int_op__orch__rim
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__design

.. logic_arc_int_op:: register_event
   :id: logic_arc_int_op__orch__register_event1
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__design

.. logic_arc_int_op:: register_if_else_condition
   :id: logic_arc_int_op__orch__register_if_else_cond
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__design

.. logic_arc_int_op:: add_program
   :id: logic_arc_int_op__orch__add_program1
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__design


.. logic_arc_int_op:: bind_events_as_global
   :id: logic_arc_int_op__orch__bind_events_as_global
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__deployment

.. logic_arc_int_op:: bind_events_as_local
   :id: logic_arc_int_op__orch__bind_events_as_local
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__deployment

.. logic_arc_int_op:: bind_events_as_timer
   :id: logic_arc_int_op__orch__bind_events_as_timer
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__deployment

.. logic_arc_int_op:: bind_invoke_to_worker
   :id: logic_arc_int_op__orch__bind_invoke_to_worker
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__deployment

.. logic_arc_int_op:: bind_shutdown_event_as_global
   :id: logic_arc_int_op__orch__bind_shutdown_event_g
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__deployment

.. logic_arc_int_op:: bind_shutdown_event_as_local
   :id: logic_arc_int_op__orch__bind_shutdown_event_l
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__deployment

.. .. code-block:: rst

..    .. real_arc_int:: <Title>
..       :id: real_arc_int__<component>__<Title>
..       :security: <YES|NO>
..       :safety: <QM|ASIL_B>
..       :fulfils: <link to component requirement id>
..       :language: cpp

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


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

Orchestration Component Architecture
************************************

.. comp_arc_sta:: orchestration
   :id: comp_arc_sta__orch__orchestration
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :includes: comp_arc_sta__orch__design_impl, comp_arc_sta__orch__deployment_impl
   :implements: logic_arc_int__orchestration__user, logic_arc_int__orchestration__deployment, logic_arc_int__orchestration__design
   :uses: logic_arc_int__logging__logging, logic_arc_int__tracing__tracing

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

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


.. logic_arc_int_op:: get_deployment
   :id: logic_arc_int_op__orch__get_deployment
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

.. logic_arc_int_op:: create_programs
   :id: logic_arc_int_op__orch__create_programs
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

.. logic_arc_int_op:: bind_shutdown_event
   :id: logic_arc_int_op__orch__bind_shutdown_event
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__deployment

.. toctree::
   :maxdepth: 1
   :titlesonly:

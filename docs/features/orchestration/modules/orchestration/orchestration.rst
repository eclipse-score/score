
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

Frontend Architecture
*********************

.. comp_arc_sta:: orchestration
   :id: comp_arc_sta__orch__orchestration
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :implements: logic_arc_int__orchestration__user
   :uses: logic_arc_int__logging__logging, logic_arc_int__tracing__tracing,logic_arc_int__baselibs__cont,logic_arc_int__baselibs__sync,logic_arc_int__communication__com

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. logic_arc_int_op:: register function
   :id: logic_arc_int_op__orch__register_func
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__user


.. logic_arc_int_op:: register event
   :id: logic_arc_int_op__orch__register_event
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__user


.. logic_arc_int_op:: add program
   :id: logic_arc_int_op__orch__add_program
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__orchestration__user

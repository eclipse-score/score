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

Frontend Component Architecture
*******************************

.. comp_arc_sta:: mw::com Frontend
   :id: comp_arc_sta__com__frontend
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :implements: logic_arc_int__communication__user
   :uses: logic_arc_int__logging__logging, logic_arc_int__tracing__tracing

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. logic_arc_int_op:: Initialize
   :id: logic_arc_int_op__com__initialize
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: Offer Service
   :id: logic_arc_int_op__com__offer_service
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: Update
   :id: logic_arc_int_op__com__update
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: Send
   :id: logic_arc_int_op__com__send
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: StartFindService
   :id: logic_arc_int_op__com__startfindserv
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: CreateProxy
   :id: logic_arc_int_op__com__createproxy
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: Subscribe
   :id: logic_arc_int_op__com__subscribe
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: GetNewSamples
   :id: logic_arc_int_op__com__getnewsamples
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__communication__user

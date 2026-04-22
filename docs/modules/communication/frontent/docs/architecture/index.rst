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

.. comp:: mw::com Frontend
   :id: comp__com_frontend
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :implements: logic_arc_int__communication__user
   :uses: logic_arc_int__logging__logging, logic_arc_int__tracing__tracing
   :belongs_to: feat__com_communication

.. comp_arc_sta:: mw::com Frontend Architecture
   :id: comp_arc_sta__com__frontend
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :uses: logic_arc_int__logging__logging, logic_arc_int__tracing__tracing
   :belongs_to: comp__com_frontend
   :fulfils: comp_req__communication__logging

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


Functional Requirements
=======================

.. comp_req:: Error logging
   :id: comp_req__communication__logging
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__com__event_type
   :status: valid
   :belongs_to: comp__com_frontend

   In case, that there is no related Event Type Info source provided in shared memory for a given Event enlisted in the deployment for the proxy, an ERROR message shall be logged.

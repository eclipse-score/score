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

Message Passing Component Architecture
**************************************

.. comp_arc_sta:: QNX::Message Passing
   :id: comp_arc_sta__os__message_passing
   :security: YES
   :safety: ASIL_B
   :status: valid
   :implements: logic_arc_int__os__message_passing

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. logic_arc_int:: OS::Message Passing
   :id: logic_arc_int__os__message_passing
   :security: YES
   :safety: ASIL_B
   :status: valid

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int:: OS::fork
   :id: logic_arc_int__os__fork
   :security: YES
   :safety: ASIL_B
   :status: valid

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: Reply
   :id: logic_arc_int_op__os__reply
   :security: YES
   :safety: QM
   :status: valid
   :included_by: logic_arc_int__os__message_passing

.. logic_arc_int_op:: Notify
   :id: logic_arc_int_op__os__notify
   :security: YES
   :safety: QM
   :status: valid
   :included_by: logic_arc_int__os__message_passing

.. logic_arc_int_op:: RequestDisconnect
   :id: logic_arc_int_op__os__requestdisconnect
   :security: YES
   :safety: QM
   :status: valid
   :included_by: logic_arc_int__os__message_passing

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

.. comp_arc_sta:: Message Passing
   :id: comp_arc_sta__baselibs__message_passing
   :security: YES
   :safety: ASIL_B
   :status: valid
   :implements: logic_arc_int__baselibs__message_passing
   :uses: logic_arc_int__os__message_passing

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}


.. logic_arc_int:: Message Passing
   :id: logic_arc_int__baselibs__message_passing
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Send Message
   :id: logic_arc_int_op__baselibs__mp_register
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__message_passing

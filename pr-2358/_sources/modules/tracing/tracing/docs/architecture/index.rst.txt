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

Tracing Component Architecture
******************************

.. comp_arc_sta:: Tracing
   :id: comp_arc_sta__tracing__tracing
   :security: YES
   :safety: ASIL_B
   :status: valid
   :implements: logic_arc_int__tracing__tracing

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. logic_arc_int:: Tracing
   :id: logic_arc_int__tracing__tracing
   :security: YES
   :safety: ASIL_B
   :status: valid

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: Trace
   :id: logic_arc_int_op__tracing__trace
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__tracing__tracing

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
**********************

.. comp_arc_sta:: Logging
   :id: comp_arc_sta__logging__logging
   :security: YES
   :safety: ASIL_B
   :status: valid
   :implements: logic_arc_int__logging__logging

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. logic_arc_int:: Logging
   :id: logic_arc_int__logging__logging
   :security: YES
   :safety:  ASIL_B
   :status: valid

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: Log
   :id: logic_arc_int_op__logging__isenabled
   :security: YES
   :safety: QM
   :status: valid
   :included_by: logic_arc_int__logging__logging

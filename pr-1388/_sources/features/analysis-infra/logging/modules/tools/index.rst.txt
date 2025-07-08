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

Tools Module
##############

.. mod_view_sta:: Tool
   :id: mod_view_sta__tool__tool
   :includes: comp_arc_sta__tool__tool

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

Component Architecture
----------------------

.. comp_arc_sta:: Tool
   :id: comp_arc_sta__tool__tool
   :security: YES
   :safety: ASIL_B
   :status: valid
   :uses: logic_arc_int__log__daemon
   :implements:

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

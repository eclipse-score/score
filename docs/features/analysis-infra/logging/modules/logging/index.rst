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

.. _definition_architectural_design:

Logging Module
##############

.. mod_view_sta:: Logging
   :id: mod_view_sta__log__logging
   :includes: comp_arc_sta__log__logging, comp_arc_sta__log__daemon

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

Component Architecture
----------------------

.. comp_arc_sta:: Logging API
   :id: comp_arc_sta__log__logging
   :security: YES
   :safety: ASIL_B
   :status: valid
   :uses: logic_arc_int__osal__osal
   :implements: logic_arc_int__log__logging

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. logic_arc_int:: Logging
   :id: logic_arc_int__log__logging
   :security: YES
   :safety:  ASIL_B
   :status: valid

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}


.. comp_arc_sta:: Logging Daemon
   :id: comp_arc_sta__log__daemon
   :security: YES
   :safety: ASIL_B
   :status: valid
   :uses: logic_arc_int__osal__osal, logic_arc_int__iam__iam
   :implements: logic_arc_int__log__daemon

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. logic_arc_int:: Logging Daemon
   :id: logic_arc_int__log__daemon
   :security: YES
   :safety:  ASIL_B
   :status: valid

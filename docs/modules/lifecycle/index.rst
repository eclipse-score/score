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

Lifecycle
=========


.. mod_view_sta:: Lifecycle
   :id: mod_view_sta__lifecycle__modules
   :includes: comp__lifecycle_launch_manager, comp__lifecycle_healthmonitor

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

.. comp:: Launch Manager
   :id: comp__lifecycle_launch_manager
   :status: valid
   :safety: ASIL_B
   :implements: logic_arc_int__lifecycle__controlif, logic_arc_int__lifecycle__alive_if
   :uses: logic_arc_int__logging__logging, logic_arc_int__baselibs__json, logic_arc_int__os__unistd, logic_arc_int__lifecycle__lifecycle_if
   :security: NO


.. comp_arc_sta:: Launch Manager Static View
   :id: comp_arc_sta__lifecycle__launch_manager
   :status: valid
   :safety: ASIL_B
   :security: NO

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. comp:: Health Monitor
   :id: comp__lifecycle_healthmonitor
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: logic_arc_int__lifecycle__deadline_monitor_if,logic_arc_int__lifecycle__logical_monitor_if
   :uses: logic_arc_int__lifecycle__alive_if

.. comp_arc_sta:: Health Monitor Static View
   :id: comp_arc_sta__lifecycle__healthmonitor
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: logic_arc_int__lifecycle__alive_if

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

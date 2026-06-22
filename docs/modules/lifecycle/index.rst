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

.. comp_req:: Lifecycle
   :id: comp_req__lifecycle__launch
   :reqtype: Functional
   :status: invalid
   :version: 1
   :security: NO
   :safety: ASIL_B
   :tags: lifecycle
   :derived_from: feat_req__lifecycle__launch_support[version==1]
   :belongs_to: comp__lifecycle_launch_manager[version==1]

   Dummy requirement

.. comp:: Launch Manager
   :id: comp__lifecycle_launch_manager
   :status: valid
   :version: 1
   :safety: ASIL_B
   :implements: logic_arc_int__lifecycle__controlif[version==1], logic_arc_int__lifecycle__alive_if[version==1]
   :uses: logic_arc_int__logging__logging[version==1], logic_arc_int__baselibs__json[version==1], logic_arc_int__os__unistd[version==1], logic_arc_int__lifecycle__lifecycle_if[version==1]
   :security: NO
   :belongs_to: feat__lifecycle[version==1]

.. comp_arc_sta:: Launch Manager Static View
   :id: comp_arc_sta__lifecycle__launch_manager
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: NO
   :belongs_to: comp__lifecycle_launch_manager[version==1]
   :fulfils: comp_req__lifecycle__launch[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. comp:: Health Monitor
   :id: comp__lifecycle_healthmonitor
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: NO
   :implements: logic_arc_int__lifecycle__deadline_monitor_if[version==1], logic_arc_int__lifecycle__logical_monitor_if[version==1]
   :uses: logic_arc_int__lifecycle__alive_if[version==1]
   :belongs_to: feat__lifecycle[version==1]

.. comp_arc_sta:: Health Monitor Static View
   :id: comp_arc_sta__lifecycle__healthmonitor
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: NO
   :uses: logic_arc_int__lifecycle__alive_if[version==1]
   :belongs_to: comp__lifecycle_healthmonitor[version==1]
   :fulfils: comp_req__lifecycle__launch[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

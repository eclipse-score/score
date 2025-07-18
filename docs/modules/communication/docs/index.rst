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

.. mod_view_sta:: Communication
   :id: mod_view_sta__com__communication
   :includes: comp_arc_sta__com__configuration, comp_arc_sta__com__ipc_binding, comp_arc_sta__com__mock_binding, comp_arc_sta__com__frontend

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}
      comp_arc_sta__com__ipc_binding -r[hidden]-> comp_arc_sta__com__frontend
      comp_arc_sta__com__frontend -r[hidden]-> comp_arc_sta__com__mock_binding
      comp_arc_sta__com__mock_binding -r[hidden]-> comp_arc_sta__com__configuration
      logic_arc_int__tracing__tracing -r[hidden]-> logic_arc_int__logging__logging


Module Documents
================

.. toctree::
   :maxdepth: 2
   :titlesonly:

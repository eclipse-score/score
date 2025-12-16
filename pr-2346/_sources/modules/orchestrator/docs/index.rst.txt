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

Module Documents Orchestrator
#############################


.. toctree::
   :maxdepth: 1
   :glob:

   manual/index.rst
   safety_mgt/index.rst
   verification/module_verification_report.rst
   release/release_note.rst



.. mod_view_sta:: Orchestrator
   :id: mod_view_sta__orch__orchestrator
   :includes: comp_arc_sta__orch__orchestrator, comp_arc_sta__orch__executor

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

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
=======================

.. document:: Executor Architecture
   :id: doc__executor_architecture
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__component_arch
   :tags: orchestration, executor

.. comp_arc_sta:: Executor
   :id: comp_arc_sta__orch__executor
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :uses: logic_arc_int__logging__logging, logic_arc_int__tracing__tracing

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. toctree::
   :maxdepth: 1
   :titlesonly:

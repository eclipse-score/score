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

Access Control Module
#####################

.. mod_view_sta:: Access Control
   :id: mod_view_sta__iam__iam
   :includes: comp_arc_sta__iam__iam

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

Component Architecture
----------------------

.. comp_arc_sta:: Access Control
   :id: comp_arc_sta__iam__iam
   :security: YES
   :safety: ASIL_B
   :status: valid
   :implements: logic_arc_int__iam__iam

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. logic_arc_int:: Access Control
   :id: logic_arc_int__iam__iam
   :security: YES
   :safety:  ASIL_B
   :status: valid

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

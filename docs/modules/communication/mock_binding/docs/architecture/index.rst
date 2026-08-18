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

Mock Binding Component Architecture
***********************************

.. comp:: Mock binding
   :id: comp__com_mock_binding
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :uses: logic_arc_int__logging__logging[version==1]
   :belongs_to: feat__com_communication[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

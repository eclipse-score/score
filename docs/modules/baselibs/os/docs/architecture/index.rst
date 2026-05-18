..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

OS Library Component Architecture
*********************************

.. document:: OS Library Architecture
   :id: doc__baselibs_os_architecture
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__component_arch

Overview/Description
--------------------

see :need:`doc__os`

Static Architecture
-------------------

.. comp:: OS Library
   :id: comp__baselibs_os
   :security: YES
   :safety: ASIL_B
   :status: valid
   :tags: baselibs_os

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

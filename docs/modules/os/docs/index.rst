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

.. mod:: OS
   :id: mod__os
   :status: valid
   :safety: ASIL_B
   :security: YES
   :includes: comp__os_libc, comp__os_message_passing

.. mod_view_sta:: OS
   :id: mod_view_sta__os__os
   :includes: comp__os_libc, comp__os_message_passing
   :belongs_to: mod__os

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

Module Documents
================

.. toctree::
   :maxdepth: 2
   :titlesonly:

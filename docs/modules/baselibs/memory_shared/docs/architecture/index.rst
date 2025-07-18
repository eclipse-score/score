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

Memory Shared Component Architecture
************************************

.. comp_arc_sta:: Memory Shared
   :id: comp_arc_sta__baselibs__memory_shared
   :security: YES
   :safety: ASIL_B
   :status: valid
   :implements: logic_arc_int__baselibs__memory_shared
   :uses: logic_arc_int__os__fcntl, logic_arc_int__os__stat, logic_arc_int__os__mmap

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. logic_arc_int:: Memory Shared
   :id: logic_arc_int__baselibs__memory_shared
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Open
   :id: logic_arc_int_op__baselibs__open
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__memory_shared

.. logic_arc_int_op:: Update
   :id: logic_arc_int_op__baselibs__update
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__memory_shared

.. logic_arc_int_op:: Lock
   :id: logic_arc_int_op__baselibs__lock
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__memory_shared

.. logic_arc_int_op:: Set Permissions
   :id: logic_arc_int_op__baselibs__set_perm
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__memory_shared

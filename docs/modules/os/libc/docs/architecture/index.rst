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

libc Component Architecture
***************************

.. comp:: libc
   :id: comp__os_libc
   :status: valid
   :safety: ASIL_B
   :implements: logic_arc_int__os__fcntl, logic_arc_int__os__stat, logic_arc_int__os__mmap, logic_arc_int__os__fork
   :security: NO

.. comp_arc_sta:: libc Static View
   :id: comp_arc_sta__os__libc
   :security: YES
   :safety: ASIL_B
   :status: valid
   :satisfies:

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. logic_arc_int:: fcntl
   :id: logic_arc_int__os__fcntl
   :security: YES
   :safety:  ASIL_B
   :status: valid

   File Control

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: Open
   :id: logic_arc_int_op__os__open
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__os__fcntl

.. logic_arc_int_op:: POSIX fallocate
   :id: logic_arc_int_op__os__fallocate
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__os__fcntl

.. logic_arc_int_op:: Flock
   :id: logic_arc_int_op__os__flock
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__os__fcntl

.. logic_arc_int:: mmap
   :id: logic_arc_int__os__mmap
   :security: YES
   :safety:  ASIL_B
   :status: valid

   Memory Mapping

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: SHM Open
   :id: logic_arc_int_op__os__shm_open
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__os__mmap

.. logic_arc_int_op:: SHM Unlink
   :id: logic_arc_int_op__os__shm_unlink
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__os__mmap

.. logic_arc_int:: stat
   :id: logic_arc_int__os__stat
   :security: YES
   :safety: ASIL_B
   :status: valid

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: fstat
   :id: logic_arc_int_op__os__fstat
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__os__stat

.. logic_arc_int_op:: mkdir
   :id: logic_arc_int_op__os__mkdir
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__os__stat

.. logic_arc_int_op:: chmod
   :id: logic_arc_int_op__os__chmod
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__os__stat

.. logic_arc_int_op:: fchmod
   :id: logic_arc_int_op__os__fchmod
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__os__stat

.. logic_arc_int_op:: umask
   :id: logic_arc_int_op__os__umask
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__os__stat

.. logic_arc_int_op:: fcomask
   :id: logic_arc_int_op__os__fcomask
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__os__stat

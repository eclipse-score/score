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

Filesystem Component Architecture
**********************************

.. document:: Filesystem Architecture
   :id: doc__filesystem_architecture
   :status: valid
   :security: YES
   :safety: ASIL_B
   :realizes: wp__component_arch

Overview/Description
--------------------
see :need:`doc__filesystem`

Static Architecture
-------------------

.. comp_arc_sta:: Filesystem
   :id: comp_arc_sta__baselibs__filesystem
   :security: YES
   :safety: ASIL_B
   :status: valid
   :tags: baselibs_filesystem
   :implements: logic_arc_int__baselibs__filesystem

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

Interfaces
----------

.. logic_arc_int:: Filesystem
   :id: logic_arc_int__baselibs__filesystem
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Path Canonicalization
   :id: logic_arc_int_op__baselibs__absolute
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: File/Directory Existence Check
   :id: logic_arc_int_op__baselibs__exists
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: File Type Detection
   :id: logic_arc_int_op__baselibs__file_type
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: File Status Query
   :id: logic_arc_int_op__baselibs__file_status
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Copy File
   :id: logic_arc_int_op__baselibs__copy_file
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Remove File or Directory
   :id: logic_arc_int_op__baselibs__remove
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Modify File Permissions
   :id: logic_arc_int_op__baselibs__permissions
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Create Directory
   :id: logic_arc_int_op__baselibs__create_directory
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Symlink Operations
   :id: logic_arc_int_op__baselibs__symlink_ops
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Hard Link Operations
   :id: logic_arc_int_op__baselibs__hardlink_ops
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Last Write Time
   :id: logic_arc_int_op__baselibs__last_write_time
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Current Path
   :id: logic_arc_int_op__baselibs__current_path
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Empty Check
   :id: logic_arc_int_op__baselibs__is_empty
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Directory Creation with Permissions
   :id: logic_arc_int_op__baselibs__create_dir_perms
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: File Content Comparison
   :id: logic_arc_int_op__baselibs__file_comparison
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Group Ownership Management
   :id: logic_arc_int_op__baselibs__change_group
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Group Validation
   :id: logic_arc_int_op__baselibs__validate_group
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Check Filesystem
   :id: logic_arc_int_op__baselibs__check_filesystem
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Repair Filesystem
   :id: logic_arc_int_op__baselibs__repair_filesystem
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Partition Formatting
   :id: logic_arc_int_op__baselibs__format_partition
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: QNX Compatibility Check
   :id: logic_arc_int_op__baselibs__qnx_compatible
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Directory Synchronization
   :id: logic_arc_int_op__baselibs__sync_directory
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

.. logic_arc_int_op:: Unique File Creation
   :id: logic_arc_int_op__baselibs__open_unique_file
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__filesystem

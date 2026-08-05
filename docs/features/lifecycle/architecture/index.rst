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

Architecture
============

.. document:: Lifecycle Architecture
   :id: doc__lifecycle_architecture
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feature_arch[version==1]

Lifecycle Feature
-----------------

.. feat:: Lifecycle
   :id: feat__lifecycle
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1


Interfaces
----------

**Lifecycle**

.. logic_arc_int:: Lifecycle Interface
   :id: logic_arc_int__lifecycle__lifecycle_if
   :included_by: feat__lifecycle
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__lifecycle__switch_run_targets[version==1], feat_req__lifecycle__liveliness_detection[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: run
   :id: logic_arc_int_op__lifecycle__run
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__lifecycle_if

.. logic_arc_int_op:: terminate
   :id: logic_arc_int_op__lifecycle__terminate
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__lifecycle_if

**Alive**

.. logic_arc_int:: Alive API
   :id: logic_arc_int__lifecycle__alive_if
   :included_by: feat__lifecycle
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__com__interfaces[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: report_health_status
   :id: logic_arc_int_op__lifecycle__report_health
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__alive_if

**Control**

.. logic_arc_int:: Control Interface
   :id: logic_arc_int__lifecycle__controlif
   :included_by: feat__lifecycle
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__com__interfaces[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: Activate Run Target
   :id: logic_arc_int_op__lifecycle__activate_target
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__controlif

**Deadline**

.. logic_arc_int:: Deadline Monitor API
   :id: logic_arc_int__lifecycle__deadline_monitor_if
   :included_by: feat__lifecycle
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__com__interfaces[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: configure_minimum_time
   :id: logic_arc_int_op__lifecycle__min_time
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: configure_maximum_time
   :id: logic_arc_int_op__lifecycle__max_time
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: link_condition
   :id: logic_arc_int_op__lifecycle__link_cond_dl
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: mark_start
   :id: logic_arc_int_op__lifecycle__start
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: mark_end
   :id: logic_arc_int_op__lifecycle__end
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: on_timer_expiry
   :id: logic_arc_int_op__lifecycle__timer_expiry
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: enable_monitoring
   :id: logic_arc_int_op__lifecycle__enable_mon
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: disable_monitoring
   :id: logic_arc_int_op__lifecycle__disable_mon
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: check_configuration
   :id: logic_arc_int_op__lifecycle__check_cfg
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

**Logical**

.. logic_arc_int:: Logical Monitor API
   :id: logic_arc_int__lifecycle__logical_monitor_if
   :included_by: feat__lifecycle
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__com__interfaces[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: add_entry_point
   :id: logic_arc_int_op__lifecycle__entry_point
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: add_exit_point
   :id: logic_arc_int_op__lifecycle__exit_point
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: add_allowed_transition
   :id: logic_arc_int_op__lifecycle__allowed_trans
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: link_condition
   :id: logic_arc_int_op__lifecycle__link_cond_lg
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: record_checkpoint
   :id: logic_arc_int_op__lifecycle__rec_checkpoint
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: enable
   :id: logic_arc_int_op__lifecycle__enable
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: disable
   :id: logic_arc_int_op__lifecycle__disable
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: verify
   :id: logic_arc_int_op__lifecycle__verify
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

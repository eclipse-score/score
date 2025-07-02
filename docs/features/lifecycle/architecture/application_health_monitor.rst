..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

Application Health Monitor
##########################


Static Architecture
===================


.. comp_arc_sta:: <<library>\nHealth Monitor
   :id: comp_arc_sta__lifecycle__healthmonitor
   :status: valid
   :safety: ASIL_B
   :implements: logic_arc_int__lifecycle__health_monitor_if
   :uses: logic_arc_int__lifecycle__alive_if
   :security: NO
   :includes: 
   :fulfils:

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}


.. logic_arc_int:: Health Monitor API
   :id: logic_arc_int__lifecycle__health_monitor_if
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces


.. logic_arc_int:: Deadline Monitor API
   :id: logic_arc_int__lifecycle__deadline_monitor_if
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces



.. logic_arc_int_op:: configure_minimum_time
   :id: logic_arc_int_op__lifecycle__min_time
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__health_monitor_if

.. logic_arc_int_op:: configure_maximum_time
   :id: logic_arc_int_op__lifecycle__max_time
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: link_condition
   :id: logic_arc_int_op__lifecycle__link_cond
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: mark_start
   :id: logic_arc_int_op__lifecycle__start
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: mark_end
   :id: logic_arc_int_op__lifecycle__end
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: on_timer_expiry
   :id: logic_arc_int_op__lifecycle__timer_expiry
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: enable_monitoring
   :id: logic_arc_int_op__lifecycle__enable_mon
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: disable_monitoring
   :id: logic_arc_int_op__lifecycle__disable_mon
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if

.. logic_arc_int_op:: check_configuration
   :id: logic_arc_int_op__lifecycle__check_cfg
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__deadline_monitor_if



.. logic_arc_int:: Logical Monitor API
   :id: logic_arc_int__lifecycle__logical_monitor_if
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces



.. logic_arc_int_op:: add_entry_point
   :id: logic_arc_int_op__lifecycle__entry_point
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: add_exit_point
   :id: logic_arc_int_op__lifecycle__exit_point
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: add_allowed_transition
   :id: logic_arc_int_op__lifecycle__allowed_trans
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: link_condition
   :id: logic_arc_int_op__lifecycle__link_cond
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: record_checkpoint
   :id: logic_arc_int_op__lifecycle__rec_checkpoint
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: enable
   :id: logic_arc_int_op__lifecycle__enable
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: disable
   :id: logic_arc_int_op__lifecycle__disable
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__logical_monitor_if

.. logic_arc_int_op:: verify
   :id: logic_arc_int_op__lifecycle__verify
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__logical_monitor_if




Dynamic Architecture
====================

 .. feat_arc_dyn:: Application health monitoring
   :id: feat_arc_dyn__lifecycle__app_health_moni
   :security: YES
   :status: invalid
   :safety: ASIL_B
   :fulfils: feat_req__lifecycle__process_monitoring

   .. uml:: _assets/application_health_monitoring_dynamic.puml
      :scale: 50
      :align: center

The most important interactions are the following:

.. list-table:: Sequence diagram Description
   :widths: 10 90
   :header-rows: 1

   * - Sequence number
     - Description
   * - 001 
     - `Launch manager` configuration for the alive monitoring of the `Monitored application` is parsed. This contains for example, what is the expected interval of alive notifications,
       how long grace period is given before failing to a missed (never received) alive notification etc. 
   * - 002
     - Start the startup grace period timer to allow the application to startup, before timing out to a missed alive notification
   * - 003
     - The `Monitored application` is started. (To simplify, no startup checks drawn here)
   * - 004
     - The `Monitored application` instantiate and configure the HealthMonitor
   * - 006
     - Cyclic reporting aliveness to the monitor.
   * - 007
     - HealthMonitor waking up and checking if the checkpoint(s) have been called
   * - 008
     - Report aliveness to the LM's application specific supervision, observing the health of the HealthMonitor itself
   * - 009
     - Checkpoint sent, but not on time
   * - 010
     - Wake up and check if the checkpoint(s) have been triggered. In this case it was not, and thus actions 011 and 012 are triggered.
   * - 011
     - Trigger a failure event to the Launch Manager. This event allows the monitor react faster than waiting for the timeout to expire.
   * - 012
     - Additionally, triggering alive must be stopped
  

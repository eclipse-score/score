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

Lifecycle Architecture
======================

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

.. logic_arc_int:: Lifecycle
   :id: logic_arc_int__lifecycle__lifecycle_if
   :included_by: feat__lifecycle
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__lifecycle__monitor_processes[version==1]

   The lifecycle interface supports the initialization, execution, and termination phases of the application.
   It registers the necessary signal handler for termination signals.
   It calls the Initialize() and Run() methods in sequence which need to be implemented by the user.

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: Initialize
   :id: logic_arc_int_op__lifecycle__initialize
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__lifecycle_if

   Initialize() method shall be implemented by the user to perform the initialization of the application.

   Input:
      - Application context (e.g. CLI arguments)

   Output:
      - Integer indicating whether the initialization was successful or not.

   Upon successful initialization, the Run() method is invoked next.

.. logic_arc_int_op:: Run
   :id: logic_arc_int_op__lifecycle__run
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__lifecycle_if

   Run() method shall be implemented by the user to perform the main execution of the application.

   Input:
      - Shutdown flag indicating whether the application received the request to terminate.

   Output:
      - Integer indicating whether the execution was successful or not.


**Report Running**

.. logic_arc_int:: Report Running
   :id: logic_arc_int__lifecycle__report_running_if
   :included_by: feat__lifecycle
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__lifecycle__monitor_processes[version==1]

   The report running interface allows the application to report to the Launch Manager that it finished its initialization phase.
   The interface only offers a simple function without the sourrounding framework of the full Lifecycle interface.

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: ReportRunning
   :id: logic_arc_int_op__lifecycle__report_running
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__report_running_if

   Input:
      - None

   Output:
      - None

   The operation does not indicate the success or failure of the reporting.
   Failure to report would eventually result in an activation timeout and forced termination of the application process by the Launch Manager.

**Alive**

.. logic_arc_int:: Alive
   :id: logic_arc_int__lifecycle__alive_if
   :included_by: feat__lifecycle
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__com__interfaces[version==1]

   The alive interface allows the application to periodically report its liveness to the Launch Manager or escalate failures.

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: ReportAlive
   :id: logic_arc_int_op__lifecycle__report_alive
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__alive_if

   ReportAlive() operation is used by the application to cyclically indicate that it is still alive.

   Input:
      - None

   Output:
      - None

.. logic_arc_int_op:: ReportFailure
   :id: logic_arc_int_op__lifecycle__report_failure
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__alive_if

   ReportFailure() operation is used by the application to indicate that it has encountered a failure condition.

   Input:
      - None

   Output:
      - None

**Control**

.. logic_arc_int:: Control
   :id: logic_arc_int__lifecycle__controlif
   :included_by: feat__lifecycle
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__com__interfaces[version==1]

   The Control interface is used by a State Manager application to control which components shall be active at any given time through the activation run targets.

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: ActivateRunTarget
   :id: logic_arc_int_op__lifecycle__activate_target
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__controlif

   ActivateRunTarget() operation is used by the application to request the activation of a specific run target.

   Input:
      - Run target to be activated
      - Force flag indicating whether to cancel any ongoing activation of a different run target or queue the request

   Output:
      - Boolean indicating whether the request was accepted or not

   The successful execution of the request is returned asynchronously by the callback registered via RegisterActivationCallback().

.. logic_arc_int_op:: GetActiveRunTarget
   :id: logic_arc_int_op__lifecycle__get_act_target
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__controlif

   GetActiveRunTarget() operation is used by the application to query the currently active run target.

   Input:
      - None

   Output:
      - Currently active run target or error if no run target is currently active

.. logic_arc_int_op:: RegisterActivationCallback
   :id: logic_arc_int_op__lifecycle__reg_callback
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__lifecycle__controlif

   RegisterActivationCallback() operation is used by the application to register a callback that will be invoked upon the successful execution of a Run Target activation.

   Input:
      - Callback function to be registered. The callback will be invoked with the name of the newly activated Run Target and the reason for activating it.

   Output:
      - None


**Deadline**

.. logic_arc_int:: Deadline Monitor
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

.. logic_arc_int:: Logical Monitor
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

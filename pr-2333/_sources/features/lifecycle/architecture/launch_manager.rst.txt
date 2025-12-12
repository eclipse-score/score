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

Launch manager
##############

The :term:`Launch Manager` is a component that provides a framework for managing
the lifecycle of processes in the S-CORE platform. It allows for launching,
monitoring, and controlling processes based on defined configurations and
requirements. As such, it is a central part of the lifecycle management in
S-CORE and knows about the state of all processes in the system.

It's foreseen ECU projects will need a custom state management to fulfill ECU-project specific requirements.  The S-CORE stack will offer a framework to control application lifecycle, but will not specify the State Manager.

Overview
========

The functionality of the :term:`Launch Manager` is defined by configuration data, which spawns a directed acyclic graph (DAG) of :term:`Components <Component>` and so called :term:`Run Targets <Run Target>`.
The :term:`Run Targets <Run Target>` are virtual nodes in the DAG and represent :term:`Run States <Run State>` of the system.
The :term:`Launch Manager` is responsible for starting and stopping the processes in the correct order, based on the dependencies defined in the configuration data.

E.g. the configuration below consists of three :term:`Run Targets <Run Target>` managing 9 components. If the user selects e.g. the :term:`Run Target` "debug" the :term:`Launch Manager` will start the components in the following order defined by the dependencies.

1. flash driver
2. filesystem
3. setup filesystems
4. networking
5. ssh

.. uml:: _assets/launch_manager_target_tree.puml
   :scale: 50
   :align: center

The :need:`comp_arc_sta__lifecycle__launch_manager` implements the following interfaces,for the selection of :term:`Run Target` s, starting and stopping of components and monitoring of the processes.

Switching between Run Targets
-----------------------------

The :term:`Launch Manager` allows switching between different :term:`Run Targets <Run Target>`. When a switch is requested, the :term:`Launch Manager` evaluates the current state and the target state,
determining which components need to be started or stopped based on their dependencies.

When a component is started the :term:`Launch Manager` will start the corresponding process and monitor its state via :term:`Ready Conditions <Ready Condition>`.

:term:`Ready Conditions <Ready Condition>` are essential mechanisms that determine when a component has successfully completed its startup phase and is ready to fulfill its intended role in the system. These conditions provide flexibility in defining what constitutes a "ready" state for different types of components. For SCORE applications, components can actively report their readiness through the Lifecycle Interface by signaling specific states or custom conditions. For native applications, the :term:`Launch Manager` relies on external indicators such as process existence, file creation, network socket availability, or successful process termination. This dual approach ensures that both modern SCORE-aware applications and legacy native applications can participate in the dependency management system, allowing the :term:`Launch Manager` to orchestrate complex startup sequences where components depend on each other's readiness rather than just their launch order.


Control Interface
=================

This interface provides control functionality for activating and managing run targets.It allows users to trigger execution of configured :term:`Run targets <Run target>` through a standardized activation mechanism.

Static architecture
-------------------

.. logic_arc_int:: Control Interface
   :id: logic_arc_int__lifecycle__controlif
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces

**Operations**

.. logic_arc_int_op:: Activate Run Target
   :id: logic_arc_int_op__lifecycle__activate_target
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__controlif


The :term:`Launch Manager` shall provide an interface, which allows an external State Manager application to request the :term:`Launch Manager` to start, stop or restart applications or groups of applications,
which allows the implementation of a state management applications to support dynamic state control.



Dynamic architecture
--------------------

The following use cases are supported by the `ControlInterface` provided by the :term:`Launch Manager`.

**Activating a Run Target**

When a request to activate a run target is received via the `ControlInterface`, the :term:`Launch Manager` shall perform the following operations:

1. **Validation**: Evaluate if the conditions are correct for activating the requested run target:
   - The run target exists in the configuration
   - All dependencies for the run target are resolvable
   - Required resources are available

2. **Transition Logic**: Determine the transition from the current state to the target state:
   - If a different run target is active, perform a switch operation (stop current, start requested)
   - If the same run target is already active, verify its state and potentially restart failed components

3. **Execution**: Execute the transition in the correct dependency order:
   - Stop components that are not part of the new run target
   - Start components that are required for the new run target
   - Respect dependency relationships during both stop and start operations

4. **Response**: Return status to the caller:
   - Success if all components transitioned correctly
   - Failure with detailed error information if any component failed to transition

This unified approach allows external state managers to request any run target activation without needing to know the current system state, as the :term:`Launch Manager` handles the transition logic internally.


.. feat_arc_dyn:: Control interface dynamic architecture activate run target
   :id: feat_arc_dyn__lifecycle__control_if_activate
   :security: YES
   :status: valid
   :safety: ASIL_B
   :fulfils: feat_req__lifecycle__control_commands, feat_req__lifecycle__request_run_target_start, feat_req__lifecycle__switch_run_targets
   :includes:

   .. uml:: _assets/control_interface_start_sequence.puml
      :scale: 50
      :align: center



Requirements
------------

- :need:`feat_req__lifecycle__control_commands`
- :need:`feat_req__lifecycle__request_run_target_start`
- :need:`feat_req__lifecycle__switch_run_targets`



Lifecycle Interface
===================


The :term:`Launch Manager` provides interfaces for communication with launched applications, supporting two distinct application types:

1. **SCORE Applications**: Implement the full Lifecycle Interface for bidirectional communication with state reporting, liveliness indication, and conditional signaling
2. **Native Applications**: Controlled exclusively via POSIX signals (SIGTERM, SIGKILL, etc.) without direct API communication

This dual approach enables the :term:`Launch Manager` to manage both legacy native applications and SCORE-aware applications within the same system.

The Lifecycle Interface serves as the communication channel between applications and the :term:`Launch Manager`:

**For SCORE Applications:**
- Application state reporting (started, running, stopped)
- Conditional signaling for application dependencies

**For Native Applications:**
- Process lifecycle control via POSIX signals
- Basic process monitoring (PID-based status checking)
- Exit code evaluation for failure detection

Static architecture
-------------------

.. logic_arc_int:: Lifecycle Interface
   :id: logic_arc_int__lifecycle__lifecycle_if
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__lifecycle__process_state_comm, feat_req__lifecycle__liveliness_detection
   :includes: logic_arc_int_op__lifecycle__run, logic_arc_int_op__lifecycle__terminate,

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: run
   :id: logic_arc_int_op__lifecycle__run
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__lifecycle_if

.. logic_arc_int_op:: terminate
   :id: logic_arc_int_op__lifecycle__terminate
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__lifecycle_if


The following use cases are supported by the Lifecycle Interface, with different capabilities depending on the application type.

**SCORE Application State Communication**

SCORE applications implementing the Lifecycle Interface can communicate their internal state to the :term:`Launch Manager`. The state information includes:

- **Started**: Application has successfully initialized and is ready to operate
- **Running**: Application is actively executing its main functionality
- **Stopped**: Application has terminated or is in the process of shutting down

The :term:`Launch Manager` uses this state information for:

- Dependency resolution for other applications
- Recovery action decisions
- Status reporting to external state managers via the Control Interface


**SCORE Application Conditional Signaling**

SCORE applications can signal custom conditions to the :term:`Launch Manager` via the Alive Interface. This enables:

- Complex dependency management beyond simple process startup
- Coordination between interdependent applications

Custom conditions can be used by other applications as launch dependencies, allowing for sophisticated startup orchestration.

**Native Application Control**

Native applications that do not implement the Lifecycle Interface are controlled through POSIX signals:

- **SIGTERM**: Graceful shutdown request
- **SIGKILL**: Forced termination (after timeout)
- **SIGUSR1/SIGUSR2**: Application-specific signals (if configured)

The :term:`Launch Manager` monitors native applications through:

- Process ID (PID) tracking
- Exit code evaluation
- Resource usage monitoring via OS facilities
- Timeout-based failure detection

For native applications, the :term:`Launch Manager` provides:

- Basic lifecycle control (start/stop)
- Simple dependency management based on process existence
- Configurable startup/shutdown timeouts
- Exit code-based success/failure determination


Dynamic Architecture
--------------------

.. feat_arc_dyn:: Lifecyle Interface
   :id: feat_arc_dyn__lifecycle__state_machine
   :security: YES
   :status: valid
   :safety: ASIL_B
   :fulfils: feat_req__lifecycle__control_commands, feat_req__lifecycle__request_run_target_start, feat_req__lifecycle__switch_run_targets
   :includes:

   .. uml:: _assets/lifecycle_state_machine.puml
      :scale: 50
      :align: center

Requirements
------------

- :need:`feat_req__lifecycle__process_state_comm`
- :need:`feat_req__lifecycle__custom_cond_support`
- :need:`feat_req__lifecycle__smart_watchdog_config`
- :need:`feat_req__lifecycle__process_monitoring`
- :need:`feat_req__lifecycle__process_termination`
- :need:`feat_req__lifecycle__shutdown_signal`
- :need:`feat_req__lifecycle__launch_support`
- :need:`feat_req__lifecycle__process_ordering`
- :need:`feat_req__lifecycle__parallel_launch_support`
- :need:`feat_req__lifecycle__waitfor_support`
- :need:`feat_req__lifecycle__process_input_output`
- :need:`feat_req__lifecycle__process_launch_args`
- :need:`feat_req__lifecycle__uid_gid_support`
- :need:`feat_req__lifecycle__total_wait_time_support`
- :need:`feat_req__lifecycle__polling_interval`
- :need:`feat_req__lifecycle__launch_priority_support`
- :need:`feat_req__lifecycle__cwd_support`
- :need:`feat_req__lifecycle__terminal_support`
- :need:`feat_req__lifecycle__std_handle_redir`
- :need:`feat_req__lifecycle__secpol_non_root`
- :need:`feat_req__lifecycle__retries_configurable`
- :need:`feat_req__lifecycle__fd_inheritance`
- :need:`feat_req__lifecycle__support_secpol_type`
- :need:`feat_req__lifecycle__supplementary_groups`
- :need:`feat_req__lifecycle__scheduling_policy`
- :need:`feat_req__lifecycle__runmask_support`
- :need:`feat_req__lifecycle__aslr_support`
- :need:`feat_req__lifecycle__process_rlimit_support`
- :need:`feat_req__lifecycle__detach_parent_process`
- :need:`feat_req__lifecycle__running_processes`
- :need:`feat_req__lifecycle__drop_supervsion`
- :need:`feat_req__lifecycle__multi_start_support`
- :need:`feat_req__lifecycle__validate_conditions`
- :need:`feat_req__lifecycle__validation_conditions`
- :need:`feat_req__lifecycle__consistent_dependencies`
- :need:`feat_req__lifecycle__stop_process_dependents`
- :need:`feat_req__lifecycle__stop_order_spec`
- :need:`feat_req__lifecycle__oci_compliant`



Alive Interface
===============
The Alive Interface provides a basic watchdog functionality interface that delivers essential monitoring capabilities for system health and responsiveness tracking.
It implements core watchdog operations including heartbeat signals to ensure reliable operation and automatic recovery from unresponsive states.

**SCORE Application Liveliness Reporting**

SCORE applications can periodically signal their liveliness to the :term:`Launch Manager` through the Alive Interface. This mechanism allows the :term:`Launch Manager` to:

- Detect application failures or hangs
- Trigger recovery actions when liveliness is lost
- Maintain accurate process health status

The liveliness mechanism includes:

- Configurable heartbeat intervals per application
- Timeout detection and failure handling

Static architecture
-------------------

.. logic_arc_int:: Alive API
   :id: logic_arc_int__lifecycle__alive_if
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

**Operations**

.. logic_arc_int_op:: report_health_status
   :id: logic_arc_int_op__lifecycle__report_health
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__lifecycle__alive_if


Dynamic architecture
--------------------

.. feat_arc_dyn:: Alive Monitoring
   :id: feat_arc_dyn__lifecycle__alive_monitoring
   :security: YES
   :status: valid
   :safety: ASIL_B
   :fulfils: feat_req__lifecycle__monitoring_processes, feat_req__lifecycle__polling_interval,, feat_req__lifecycle__failure_detect
   :includes:

   .. uml:: _assets/alive_monitoring_dynamic.puml
      :scale: 50
      :align: center

Requirements
------------
- :need:`feat_req__lifecycle__monitoring_processes`
- :need:`feat_req__lifecycle__polling_interval`
- :need:`feat_req__lifecycle__failure_detect`
- :need:`feat_req__lifecycle__liveliness_detection`

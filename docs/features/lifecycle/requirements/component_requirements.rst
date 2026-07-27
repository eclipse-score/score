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


Component Requirements
======================

Launching Processes
-------------------

.. comp_req:: Forward process information
    :id: comp_req__lifecycle__process_input_output
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support to pass the output of one or
    multiple :term:`Processes <Process>` as input arguments to another process.

.. comp_req:: Handling process args
    :id: comp_req__lifecycle__process_launch_args
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a process with a
    given set of arguments.

.. comp_req:: Launching process in debug mode
    :id: comp_req__lifecycle__debug_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching process with a
    given set of debug arguments in debug mode.

.. comp_req:: Launching process in state waiting for a debugger connection
    :id: comp_req__lifecycle__support_held_state
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a process in a state
    waiting for a debugger connection.

.. comp_req:: Process user, group IDs support
    :id: comp_req__lifecycle__uid_gid_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a process with a
    given :term:`UID`/:term:`GID` (user name/Group Identifier).

.. comp_req:: Process priority support
    :id: comp_req__lifecycle__launch_priority_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a process with a
    given priority.

.. comp_req:: CWD support
    :id: comp_req__lifecycle__cwd_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a process with a
    given :term:`Working Directory`.

.. comp_req:: Launching terminal
    :id: comp_req__lifecycle__terminal_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a terminal or a
    session leader.

.. comp_req:: Standard handle redirection
    :id: comp_req__lifecycle__std_handle_redir
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for stdin, stdout, stderr
    redirection.

.. comp_req:: Non-root support
    :id: comp_req__lifecycle__secpol_non_root
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support to be started with security
    policy as non-root.

.. comp_req:: Configurable amount of retries
    :id: comp_req__lifecycle__retries_configurable
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall support a configurable amount of retries in
    case error occurs during startup of a component (e.g. file not available) occurs.

.. comp_req:: Process capability support
    :id: comp_req__lifecycle__capability_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching :term:`Processes <Process>`
    with configured OS-specific capabilities and privileges.

.. comp_req:: File descriptor inheritance support
    :id: comp_req__lifecycle__fd_inheritance
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a process with
    given :term:`File Descriptor` inheritance restrictions.

.. comp_req:: Security policy support
    :id: comp_req__lifecycle__support_secpol_type
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a process with a
    given security policy.

.. comp_req:: Supplementary group support
    :id: comp_req__lifecycle__supplementary_groups
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a process with a
    given set of supplementary groups.

.. comp_req:: Scheduling support
    :id: comp_req__lifecycle__scheduling_policy
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a process with
    certain scheduling policy.

.. comp_req:: CPU runmask support
    :id: comp_req__lifecycle__runmask_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a process with a
    given runmask.

.. comp_req:: ASLR support
    :id: comp_req__lifecycle__aslr_support
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching process with
    :term:`ASLR` (Address Space Layout Randomization).

.. comp_req:: Resource limit support
    :id: comp_req__lifecycle__process_rlimit_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a process with a
    given set of system resource limits (rlimit).

.. comp_req:: Process detach from parent support
    :id: comp_req__lifecycle__detach_parent_process
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__custom_cond_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for launching a process to
    detach from parent.

Conditional Launching
---------------------

.. comp_req:: Conditionally launch of processes
    :id: comp_req__lifecycle__cond_process_start
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support to conditionally start a process
    or process group based on the return value of a single or multiple :term:`Processes <Process>`
    executed before.

.. comp_req:: Condition timeout
    :id: comp_req__lifecycle__total_wait_time_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for per condition configurable
    total wait time for launch conditions to be satisfied.

.. comp_req:: Conditional launch polling interval
    :id: comp_req__lifecycle__polling_interval
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for per condition configurable
    :term:`Polling Interval` for launch conditions to be checked.

.. comp_req:: Pre-start validation
    :id: comp_req__lifecycle__validate_conditions
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall be able to validate the pre-start conditions of the executable using the conditions.

.. comp_req:: post-start validation
    :id: comp_req__lifecycle__validation_conditions
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall be able to validate the start of the executable using the conditions.

.. comp_req:: Launched Process status
    :id: comp_req__lifecycle__launcher_status_storage
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide a way to store the status of the launched process.

.. comp_req:: Condition check based on status
    :id: comp_req__lifecycle__condition_check_method
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide a method for condition check based on process state.

.. comp_req:: Configuration of action based on condition evaluation
    :id: comp_req__lifecycle__config_actions_cond
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide a way to configure actions based on condition evaluation i.e. to be able to configure SUCCESS and FAILURE case.

.. comp_req:: Condition check based on path
    :id: comp_req__lifecycle__path_condition_check
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide a method for condition check for a path.

.. comp_req:: Condition check based on ENV
    :id: comp_req__lifecycle__env_variable_cond_check
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide a method for condition check for environment variable.

.. comp_req:: Condition check based on all dependency
    :id: comp_req__lifecycle__dependency_check
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide a method to check if all dependencies have been executed.

.. comp_req:: Condition check based on at least one dependency
    :id: comp_req__lifecycle__check_dependency_exec
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide a method to check if at least one dependency has been executed.

.. comp_req:: Condition check for each SWC its dependencies
    :id: comp_req__lifecycle__define_swc_dependencies
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide a way to define for each :term:`SWC` (Software Components), its dependencies.

Process Management
------------------

.. comp_req:: Dropping process responsibility
    :id: comp_req__lifecycle__drop_supervsion
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__running_processes[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support to dropping all surveillance
    and failure reaction activities of :term:`Processes <Process>`.

.. comp_req:: Multiple instance of executable
    :id: comp_req__lifecycle__multi_start_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__running_processes[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall permit an executable to be launched more than once.

.. comp_req:: Invalid dependency
    :id: comp_req__lifecycle__consistent_dependencies
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__running_processes[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall reject an inconsistent definition of set of executables dependencies.

.. comp_req:: Dangling dependency
    :id: comp_req__lifecycle__stop_process_dependents
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__running_processes[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall be able to stop a process when all it's dependents are stopped if specified in the set of executables.

.. comp_req:: Coordination stop dependency
    :id: comp_req__lifecycle__stop_order_spec
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__running_processes[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall permit the stop order of non-dependent processes to be specified.

Run targets
-----------

.. comp_req:: Process state
    :id: comp_req__lifecycle__process_state_comm
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__switch_run_targets[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall have a means for the launched :term:`Processes <Process>`
    to communicate a state, which represents the launched processes' internal state,
    to the launcher.

Terminating Processes
---------------------

.. comp_req:: Stop timeout
    :id: comp_req__lifecycle__configurable_timeout
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__switch_run_targets[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for configurable timeout
    :term:`Interval` to wait for the process to be stopped.

.. comp_req:: Configurable delay between SIGTERM and SIGKILL
    :id: comp_req__lifecycle__time_to_wait_config
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__terminationn_dependency[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall offer a configuration of the time to wait before
    SIGKILL is sent. In case "0" is stated, the SIGKILL shall be sent immediately.

.. comp_req:: Normal shutdown
    :id: comp_req__lifecycle__launch_manager_shutdown
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__terminationn_dependency[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall support normal shutdown by terminating all
    process in the dependency order.

.. comp_req:: Fast shutdown
    :id: comp_req__lifecycle__fast_shutdown_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__terminationn_dependency[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall support fast shutdown by terminating itself
    without considering the started :term:`Processes <Process>`.

.. comp_req:: Launch Manager shutdown
    :id: comp_req__lifecycle__launcher_exit_shutdown
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__terminationn_dependency[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall exit after performing shutdown operation by
    stopping all the :term:`Processes <Process>` it owns in the dependency order when requested.

.. comp_req:: Shutdown signal handling
    :id: comp_req__lifecycle__shutdown_signal
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__terminationn_dependency[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall implement a shutdown by sending a SIGTERM to
    the process. In case the process does not terminate itself, a SIGKILL shall be sent.

Monitoring, Notification and Recovery
-------------------------------------

.. comp_req:: Process state notification
    :id: comp_req__lifecycle__ext_monitor_notify
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__monitor_abnormal_term[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for external monitors to get
    notified on process life status.

.. comp_req:: Monitoring and recovery: recovery wait time
    :id: comp_req__lifecycle__configurable_wait_time
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__conditional_startup[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for configurable wait time
    that shall elapse before repeating :term:`Recovery Action`.

.. comp_req:: Monitoring and recovery: adopted process monitoring
    :id: comp_req__lifecycle__monitoring_processes
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__liveliness_detection[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for monitoring adopted
    :term:`Processes <Process>`.

.. comp_req:: Process launch monitoring
    :id: comp_req__lifecycle__failure_detect
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__switch_run_targets[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall be able to detect and react to failure of the
    process launch.

.. comp_req:: Recovery
    :id: comp_req__lifecycle__process_failure_react
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__liveliness_detection[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall be able to react to a process failure by
    optionally performing one of relaunching the process, stopping the process,
    stopping the process and starting another process, or triggering :term:`QNX`
    :term:`Operating System` (:term:`QOS`) Device Safe State (:term:`DSS`).

.. comp_req:: Launch manager external watchdog notification
    :id: comp_req__lifecycle__lm_ext_watchdog_notify
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__lm_self_health_check[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall trigger a notification to an external
    :term:`Watchdog` for each successful self monitoring test execution.

.. comp_req:: Launch manager external watchdog notification - failed test
    :id: comp_req__lifecycle__lm_ext_wdg_failed_test
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__lm_self_health_check[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall not trigger an external :term:`Watchdog`
    notification if an internal health check failed.

.. comp_req:: Launch manager external monitoring configuration
    :id: comp_req__lifecycle__lm_ext_watchdog_cfg
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__lm_self_health_check[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall support configuring the :term:`Interval` of
    the internal health check executions.

Logging
-------

.. comp_req:: Logging slog2 and file support
    :id: comp_req__lifecycle__slog2_logging
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__logging_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall support OS specific logging facilities to analyze the early
    boot sequence.

.. comp_req:: Logging state transitions
    :id: comp_req__lifecycle__process_logging_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__logging_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide support for logging process launches,
    :term:`Processes <Process>` exit/recovery, internal tasks, and interaction with external monitor.

.. comp_req:: Logging timestamp
    :id: comp_req__lifecycle__log_timestamp
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__logging_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` logs shall contain timestamp information.

.. comp_req:: Logging DAG
    :id: comp_req__lifecycle__dag_logging_controlif
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__logging_support[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall provide the possibility to log the :term:`DAG`
    in a human readable format, triggered via :term:`Control Interface`.

.. comp_req:: Configuration dependency view
    :id: comp_req__lifecycle__dependency_visu
    :reqtype: Functional
    :security: NO
    :safety: QM
    :derived_from: feat_req__lifecycle__deps_visualization[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall have the means to log the current dependencies in a format that can be visualized when requested.

Configuration file
------------------

.. comp_req:: Configuration file support
    :id: comp_req__lifecycle__modular_config_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__config_file_support[version==1]
    :status: valid
    :version: 1

    The launch manager shall provide modular configuration file support to configure process attributes.

.. comp_req:: Runtime configuration compliance
    :id: comp_req__lifecycle__runtime_config_compat
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__config_file_support[version==1]
    :status: valid
    :version: 1

    The launch manager shall provide modular configuration files support for configurations coming from `OCI runtime configuration<https://github.com/opencontainers/runtime-spec/blob/v1.2.0/config.md>`.

.. comp_req:: Global process properties
    :id: comp_req__lifecycle__central_default_defines
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__component_group_config[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall be able to centrally define defaults for specific properties for the set of executables.

.. comp_req:: Lazy check of configured commands
    :id: comp_req__lifecycle__lazy_check
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: feat_req__lifecycle__component_group_config[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall check availability of executables in the filesystem only when the executable shall required to be executed.

.. comp_req:: Configuration Verification tool
    :id: comp_req__lifecycle__offline_config_valid
    :reqtype: Functional
    :security: NO
    :safety: QM
    :derived_from: feat_req__lifecycle__deps_visualization[version==1]
    :status: valid
    :version: 1

    The :term:`Launch Manager` shall have a means to validate the configuration offline.

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

Requirements
============

.. document:: Lifecycle Requirements
   :id: doc__lifecycle_requirements
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_feat[version==1]

Launching Processes
-------------------

.. feat_req:: Support for launching processes
    :id: feat_req__lifecycle__launch_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall provide support for launching :term:`Processes <Process>`.

.. feat_req:: Process dependency handling
    :id: feat_req__lifecycle__process_ordering
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall provide support for ordering the launching of
    :term:`Processes <Process>` based on the dependencies.


.. feat_req:: Launching processes in parallel
    :id: feat_req__lifecycle__parallel_launch_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall provide support for launching :term:`Processes <Process>`
    in parallel.

.. feat_req:: Control interface support
    :id: feat_req__lifecycle__custom_cond_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall provide support to wait for configurable custom
    conditions, which can be signaled from applications via :term:`Control Interface`.


Conditional Launching
---------------------

.. feat_req:: Conditional launching
    :id: feat_req__lifecycle__conditional_startup
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall provide launching processes based on conditions.


Process Management
------------------

.. feat_req:: Process adoption
    :id: feat_req__lifecycle__running_processes
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall be able to control already running :term:`Processes <Process>`.


.. feat_req:: OCI Compliant
    :id: feat_req__lifecycle__oci_compliant
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0
    :derived_from: stkh_req__overall_goals__enable_cooperation[version==1]

    The :term:`Lifecycle Feature` shall be compliant to the `OCI Specification v1.2.0 <https://github.com/opencontainers/runtime-spec/releases/tag/v1.2.0>`__.


Run targets
-----------

.. feat_req:: Run target support
    :id: feat_req__lifecycle__run_target_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall provide support for :term:`run targets <Run target>` to define
    collections of :term:`Processes <Process>` that can be launched together.

.. feat_req:: Launching run target
    :id: feat_req__lifecycle__start_named_run_target
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall be able to start a named :term:`Run target`.

.. feat_req:: Switch between run targets
    :id: feat_req__lifecycle__switch_run_targets
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall be able to switch between different :term:`run targets <Run target>`.


Terminating Processes
---------------------

.. feat_req:: Terminating process
    :id: feat_req__lifecycle__process_termination
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall provide support for terminating :term:`Processes <Process>`.

.. feat_req:: Handling process dependency in termination
    :id: feat_req__lifecycle__terminationn_dependency
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall terminate the :term:`Processes <Process>` based on the
    dependency order.


Control Interface
-----------------

.. feat_req:: Control commands
    :id: feat_req__lifecycle__control_commands
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall provide support for run-target selection.

.. feat_req:: Query commands
    :id: feat_req__lifecycle__query_commands
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall provide support for commands to query component
    states.


.. feat_req:: Report "started/running/degraded"
    :id: feat_req__lifecycle__controlif_status
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall be able to report status on components via the
    :term:`Control Interface`.

    Note: status can be "started/running/degraded" - refer to documentation for details

.. feat_req:: Request run target launch
    :id: feat_req__lifecycle__request_run_target_start
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall be able to start a named :term:`Run target` respecting the
    dependencies when requested.


Monitoring, Notification and Recovery
-------------------------------------

.. feat_req:: Process crash monitoring
    :id: feat_req__lifecycle__monitor_abnormal_term
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall provide support for monitoring abnormal
    termination of :term:`Processes <Process>`.


.. feat_req:: Recovery action
    :id: feat_req__lifecycle__recovery_action_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall support :term:`Recovery Action` for the
    abnormally terminated :term:`Processes <Process>`.

.. feat_req:: Run target switch as recovery action
    :id: feat_req__lifecycle__recov_run_target_switch
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall support switching to a different :term:`Run target` as
    recovery action in case a single process terminated abnormally or lost its
    :term:`Liveliness`.

.. feat_req:: Monitoring and recovery: watchdog support
    :id: feat_req__lifecycle__smart_watchdog_config
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall support a smart :term:`Watchdog`, configurable
    per process.


.. feat_req:: Process liveliness detection
    :id: feat_req__lifecycle__liveliness_detection
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall be able to detect and react to loss of
    :term:`Liveliness` of the :term:`Processes <Process>` it owns, by monitoring
    the state of the :term:`Processes <Process>` as specified by the set of
    executables.


.. feat_req:: Multi-instance
    :id: feat_req__lifecycle__multi_instance_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v2.0.0

    The :term:`Lifecycle Feature` shall be able to run in multiple instances with its
    own configurations on a system.

.. feat_req:: Launch manager self health check
    :id: feat_req__lifecycle__lm_self_health_check
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1], stkh_req__dependability__safety_features_1[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall implement time based cyclical monitoring of itself.

.. feat_req:: Lifecycle programing language support
    :id: feat_req__lifecycle__prog_lang
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__dependability__safety_features_1[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall support Rust and C++ programming languages.

.. feat_req:: Health Monitor deadline supervision
    :id: feat_req__lifecycle__hm_deadline
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__dependability__safety_features_1[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall support deadline supervision to allow
    monitoring timely execution within applications to detect timing violations.

.. feat_req:: Health Monitor logical supervision
    :id: feat_req__lifecycle__hm_logical
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__dependability__safety_features_1[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall support logical supervision to allow
    monitoring execution flow within applications to detect logical errors.

.. feat_req:: Health Monitor checkpoint supervision
    :id: feat_req__lifecycle__hm_checkpoint
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__dependability__safety_features_1[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall support checkpoint supervision to allow
    monitoring periodic execution within applications to detect failures.

Logging
-------

.. feat_req:: Logging support
    :id: feat_req__lifecycle__logging_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall support logging of process launch, monitoring,
    and configuration activities.


Configuration file
------------------

.. feat_req:: Configuration file support
    :id: feat_req__lifecycle__config_file_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__functional_req__file_based[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall support modular configuration files to
    configure process attributes, including configurations coming from
    external formats such as OCI runtime configuration.

.. feat_req:: Updating configuration
    :id: feat_req__lifecycle__session_extension
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__functional_req__file_based[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall provide support for extending already running
    session with additional new configuration file.

.. feat_req:: Component grouping configuration
    :id: feat_req__lifecycle__component_group_config
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :derived_from: stkh_req__functional_req__file_based[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall provide support for grouping sets of
    :term:`Components <Component>` to share configuration.

.. feat_req:: Configuration Dependency view
    :id: feat_req__lifecycle__deps_visualization
    :reqtype: Functional
    :security: NO
    :safety: QM
    :derived_from: stkh_req__execution_model__processes[version==1]
    :satisfied_by: feat__lifecycle[version==1]
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The :term:`Lifecycle Feature` shall have the means to generate the specified dependencies in a format that can be visualized.

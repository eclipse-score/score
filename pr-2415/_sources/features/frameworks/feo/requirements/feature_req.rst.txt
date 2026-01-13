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

.. document:: FEO Feature Requirements
   :id: doc__frameworks_feo_feat_reqs
   :status: valid
   :security: NO
   :safety: ASIL_B
   :realizes: wp__requirements_feat

FEO Feature Requirements
========================


Definitions
===========

.. feat_req:: Definition: Application
    :id: feat_req__feo__application
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data
    :status: valid

    An application consists of one or more activities.

    An application consists of one or more operating system processes.
    In particular it consists of the primary process which handles the lifecycle, configuration and execution management.
    It may optionally consist of one or more secondary processes.
    The purpose of secondary processes is to run code in separate address spaces (Freedom From Interference) for safety reasons.
    Each process (primary and secondary) belongs to exactly one application.
    Each process contains one ore more operating system threads.

.. feat_req:: Definition: Activity
    :id: feat_req__feo__activity
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data
    :status: valid

    Activities are mapped to threads within primary or secondary processes.
    Each activity is mapped to exactly one thread and provides the following functions:

    * `init`: Initialization of the activity.
    * `step`: Execution of the activity.
    * `shutdown`: Shutdown of the activity.

    The mapping is done in a configuration file and cannot be changed at runtime.

.. feat_req:: Definition: Task Chain
    :id: feat_req__feo__task_chain
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data, stkh_req__execution_model__processes
    :status: valid

    All activities within an application are arranged within a `Task Chain`.
    There is exactly one task chain per application.

    The task chain configuration defines the execution order of the activities.
    In particular it defines when the task chain is activated (typically in a cyclic manner) and in which order the activities will run.

    Every task chain may have one or multiple input service activities which will run in the beginning.
    The purpose of an input service activity is to collect external input signals and provide them to the other activities during task chain execution.
    Every task may have one or more output service activities which will run in the end.
    The purpose of an output service activity is to collect signals produced by activities within the task chain and send them to external entities.

.. feat_req:: Definition: Service Activity
    :id: feat_req__feo__service_activity
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data
    :status: valid

    * Service activities are a means to interact with the outside world, e.g. via
      network communication, direct sensor input or direct actuator output
    * Service activities may also use APIs external to the framework
      (e.g. networking APIs, reading from external sensor devices, writing HW I/O, etc.)

.. feat_req:: Definition: Agent
    :id: feat_req__feo__agent
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data
    :status: valid

    In order to execute activities in secondary processes, the executor makes
    use of an `Agent` for each secondary process and possibly also the primary process.
    The agent receives commands from the executor, invokes actions on
    activities within its process and reports back to the executor.

    Each Activity that is part of the task chain is associated with an
    Agent, which takes over the task to wait for a trigger from its
    corresponding Executor. When the Agent gets a step request from the
    Executor, it calls the Step function of the Activity There is exactly
    one agent for each secondary process. The primary can but doesn't have to be
    associated with an agent.

Dynamic Architecture
====================

.. feat_req:: The lifecycle of an `Application` consists of 3 phases: Init, Run and Shutdown.
    :id: feat_req__feo__application_lifecycle
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data, stkh_req__execution_model__processes
    :status: valid

    The Application Lifecycle consists of 3 phases: Init, Run and Shutdown.

.. feat_req:: Initialization of activities
    :id: feat_req__feo__activity_init
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data, stkh_req__execution_model__processes
    :status: valid

    Initialization of activities is done during application initialization.

    Each activity is initialized by a call to its `init` function.

    The `init` function will be invoked in the thread to which the activity is mapped.
    Note that `init`, `step` and `shutdown` functions will be run in the same thread.

.. feat_req:: Stepping of activities
    :id: feat_req__feo__activitiy_step
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data, stkh_req__execution_model__processes
    :status: valid

    Each activity is stepped once within each execution of the task chain they belong to.

    Stepping is done by a call to an activity's `step` function.

.. feat_req:: Shutdown of activities
    :id: feat_req__feo__activity_shutdown
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data, stkh_req__execution_model__processes
    :status: valid

    Shutdown of activities is done during application shutdown.

    Each activity is shut down by a call to its `shutdown` function.

    The `shutdown` function will be invoked in the thread to which the activity is mapped.

Supervision
===========

.. feat_req:: Alive supervision
    :id: feat_req__feo__alive_supervision
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__dependability__safety_features, stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data
    :status: valid

    The framework shall provide the functionality to enable the reporting of
    alive supervision checkpoint to an external health management system
    (e.g. watchdog)

.. feat_req:: Support of deadline supervision checkpoints
    :id: feat_req__feo__deadline_supervision
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__dependability__safety_features, stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data
    :status: valid

    The framework shall provide the functionality to enable the reporting of
    deadline supervision checkpoints to an external health management system
    (e.g. watchdog)

.. feat_req:: Support of logical supervision
    :id: feat_req__feo__logical_supervision
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__dependability__safety_features, stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data
    :status: valid

    The framework shall provide the functionality to enable the reporting of
    logical supervision checkpoints to an external health management system
    (e.g. watchdog)

.. feat_req:: Trustable computation
    :id: feat_req__feo__trustable_computation
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: stkh_req__dependability__safety_features, stkh_req__app_architectures__support_time, stkh_req__app_architectures__support_data
    :status: valid

    The framework shall provide mechanisms to check after the computation of
    an Activity if the result is trustable.
    This can be done e.g. via evaluation of floating point exceptions,
    checking of hardware registers or status information of the
    software platform.


Error Handling for S-CORE v0.5
==============================

.. feat_req:: Response to termination request
    :id: feat_req__feo__response_term_request
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: stkh_req__dependability__safety_features, stkh_req__dependability__availability, stkh_req__execution_model__processes
    :status: valid

    If the primary process receives a termination signal, it shall call the shutdown
    function of all remaining activities in arbitrary sequence and terminate itself.

    If a secondary process receives a termination signal, it shall terminate itself.


.. feat_req:: Secondary connection timeout
    :id: feat_req__feo__secondary_conn_timeout
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: stkh_req__dependability__safety_features, stkh_req__dependability__availability, stkh_req__execution_model__processes
    :status: valid

    If not all secondary processes connect to the primary in time, the primary shall terminate itself.
    The startup functions shall not be triggered.


.. feat_req:: Activity startup error
    :id: feat_req__feo__act_startup_error
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: stkh_req__dependability__safety_features, stkh_req__dependability__availability, stkh_req__execution_model__processes
    :status: valid

    If an error occurs during the execution of a startup function, the primary process shall abort calling
    startup functions and terminate itself. For all of the activities
    whose startup functions have already been called successfully, the corresponding shutdown functions shall be
    executed in arbitrary sequence.


.. feat_req:: Activity resource allocation error
    :id: feat_req__feo__act_alloc_error
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: stkh_req__dependability__safety_features, stkh_req__dependability__availability, stkh_req__execution_model__processes
    :status: valid

    During initialization (i.e. in the startup function of an activity), activities shall check for resource allocation
    and report an error to the executor in case of failure.


.. feat_req:: Activity timeout
    :id: feat_req__feo__act_timeout
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: stkh_req__dependability__safety_features, stkh_req__dependability__availability, stkh_req__execution_model__processes
    :status: valid

    If a timeout occurs during startup, stepping or shutdown of an activity, the primary process shall shutdown all
    successfully started activities in arbitrary sequence and terminate itself.


.. feat_req:: Startup timeout
    :id: feat_req__feo__startup_timeout
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: stkh_req__dependability__safety_features, stkh_req__dependability__availability, stkh_req__execution_model__processes
    :status: valid

    If not all activities reach their initialized state within a certain period of time (startup timeout),
    the primary process shall shutdown all successfully started activities in arbitrary sequence and terminate itself.


.. feat_req:: Activity stepping error
    :id: feat_req__feo__act_stepping_error
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: stkh_req__dependability__safety_features, stkh_req__dependability__availability, stkh_req__execution_model__processes
    :status: valid

    If an activity fails in the step function, the primary process shall call shutdown for all activities
    in arbitrary sequence and terminate itself.


.. feat_req:: Activity shutdown error
    :id: feat_req__feo__act_shutdown_error
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: stkh_req__dependability__safety_features, stkh_req__dependability__availability, stkh_req__execution_model__processes
    :status: valid

    If an activity fails in the shutdown function, the primary process shall shutdown all remaining activities
    in arbitrary sequence and terminate itself.

.. needextend:: docname is not None and "frameworks/feo/requirements" in docname
   :+tags: frameworks_feo

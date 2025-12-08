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

.. document:: FEO Component Requirements
   :id: doc__component_feo_requirements
   :status: draft
   :security: NO
   :safety: ASIL_B
   :realizes: wp__requirements_comp
   :tags: component_feo

FEO Component Requirements
==========================

.. comp_req:: Application Processes
    :id: comp_req__feo__application
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__application
    :status: valid

    An application consists of one or more activities executed in one or multiple operating system processes.

    In particular it consists of the primary process which handles the lifecycle, configuration and execution management.
    It may optionally consist of one or more secondary processes.
    The purpose of secondary processes is to run code in separate address spaces (Freedom From Interference) for safety reasons.
    Each process (primary and secondary) belongs to exactly one application.
    Each process contains one ore more operating system threads.


.. comp_req:: Activity
    :id: comp_req__feo__activity
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__activity
    :status: valid

    Each activitiy is mapped to exactly one thread within the primary or one of the secondary processes.
    Each activity provides the following functions:

    * `init`: Initialization of the activity.
    * `step`: Execution of the activity.
    * `shutdown`: Shutdown of the activity.


.. comp_req:: Task Chain
    :id: comp_req__feo__task_chain
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__task_chain
    :status: valid

    All activities within an application are arranged within a `Task Chain`.
    There is exactly one task chain per application.

    The task chain configuration defines the execution order of the activities.
    In particular it defines when the task chain is activated (typically in a cyclic manner) and in which order the activities will run.

    Every task chain may have one or multiple input service activities which will run in the beginning.
    The purpose of an input service activity is to collect external input signals and provide them to the other activities during task chain execution.
    Every task may have one or more output service activities which will run in the end.
    The purpose of an output service activity is to collect signals produced by activities within the task chain and send them to external entities.


.. comp_req:: Scheduler aka Executor
    :id: comp_req__feo__scheduler
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__application, feat_req__feo__agent
    :status: valid

    The component shall implement a scheduler (aka executor) that manages the execution of activities in correct order.


.. comp_req:: Service Activity
    :id: comp_req__feo__service_activity
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__service_activity
    :status: valid

    The component shall enable the implementation and execution of Service Activities, which are a means to interact
    with the outside world, e.g. via network communication, direct sensor input or direct actuator output.

    A Service Activity shall be enabled to use APIs external to the framework (e.g. networking APIs, reading from
    external sensor devices, writing HW I/O, etc.)


.. comp_req:: Agent
    :id: comp_req__feo__agent
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__agent
    :status: valid

    In order to execute activities in secondary processes, the Scheduler shall use agents running in the secondary
    processes. There shall be exactly one agent for each secondary process.

    The Agent in a secondary process shall receive commands from the Scheduler, invoke actions on Activities within its
    process and report back to the Scheduler. Each Activity that is part of the task chain in a secondary process shall
    be associated with an Agent, which takes over the task to wait for a trigger from the Scheduler. When the Agent
    gets a step request from the Scheduler, it calls the Step function of the Activity.


.. comp_req:: Mapping of Activities to threads
    :id: comp_req__feo__activitiy_thread
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__activity_init, feat_req__feo__activitiy_step, feat_req__feo__activity_shutdown, feat_req__feo__activity
    :status: valid

    Each activity shall be mapped to one thread. The mapping cannot be changed at runtime.
    Each activity's `init`, `step` and `shutdown` functions shall be executed in the assigned thread.


.. comp_req:: Application Lifecycle Phases
    :id: comp_req__feo__application_lifecycle
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__application_lifecycle
    :status: valid

    The Application Lifecycle shall consists of 3 phases: Init, Run and Shutdown.


.. comp_req:: Initialization of Activities
    :id: comp_req__feo__activity_init
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__activity_init
    :status: valid

    Initialization of Activities shall be done during application initialization.

    Each Activity shall be initialized by a call to its `init` function.
    The `init` function shall be invoked in the thread to which the activity is mapped.


.. comp_req:: Stepping of Activities
    :id: comp_req__feo__activitiy_step
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__activitiy_step, feat_req__feo__activity_init, feat_req__feo__activity
    :status: valid

    Each Activity shall be stepped once within each execution of the Task Chain they belong to.
    Stepping is done by a call to an activity's `step` function. The `step` function shall be invoked
    in the thread to which the activity is mapped.


.. comp_req:: Shutdown of activities
    :id: comp_req__feo__activity_shutdown
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__activity_shutdown
    :status: valid

    Shutdown of activities shall be done during application shutdown.

    Each activity shall be shut down by a call to its `shutdown` function. The `shutdown` function shall be invoked
    in the thread to which the activity is mapped.


.. comp_req:: Component Configuration
    :id: comp_req__feo__comp_cfg
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__activity, feat_req__feo__task_chain
    :status: valid

    The component shall provide a configuration mechanism that supports configuring

    - the mapping of activities to threads
    - the execution order of activities
    - when the task chain is activated (e.g. a cycle time for cyclic execution)


.. comp_req:: Component Configuration from File
    :id: comp_req__feo__comp_cfg_file
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__activity
    :status: valid

    It shall be possible to define the component configuration in a pre-defined configuration file.


.. comp_req:: Activity Mapping Configuration
    :id: comp_req__feo__act_map_cfg
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__activity
    :status: valid

    The mapping of activities to threads is done in the component configuration and cannot be changed at runtime.


.. comp_req:: Alive supervision
    :id: comp_req__feo__alive_supervision
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__alive_supervision
    :status: valid

    The component shall provide the functionality to enable the reporting of
    alive supervision checkpoint to an external health management system
    (e.g. watchdog)


.. comp_req:: Support of deadline supervision checkpoints
    :id: comp_req__feo__deadline_supervision
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__deadline_supervision
    :status: valid

    The component shall provide the functionality to enable the reporting of
    deadline supervision checkpoints to an external health management system
    (e.g. watchdog)


.. comp_req:: Support of logical supervision
    :id: comp_req__feo__logical_supervision
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__logical_supervision
    :status: valid

    The component shall provide the functionality to enable the reporting of
    logical supervision checkpoints to an external health management system
    (e.g. watchdog)


.. comp_req:: Trustable computation
    :id: comp_req__feo__trustable_computation
    :reqtype: Functional
    :security: NO
    :safety: ASIL_B
    :satisfies: feat_req__feo__trustable_computation
    :status: valid

    The component shall provide mechanisms to check after the computation of
    an Activity if the result is trustable.
    This can be done e.g. via evaluation of floating point exceptions,
    checking of hardware registers or status information of the
    software platform.

Error Handling for S-CORE v0.5
==============================

.. comp_req:: Response to termination request
    :id: comp_req__feo__response_term_request
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: feat_req__feo__response_term_request
    :status: valid

    If the primary process receives a termination signal, it shall call the shutdown
    function of all remaining activities in arbitrary sequence and terminate itself.

    If a secondary process receives a termination signal, it shall terminate itself.


.. comp_req:: Secondary connection timeout
    :id: comp_req__feo__secondary_conn_timeout
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: feat_req__feo__secondary_conn_timeout
    :status: valid

    If not all secondary processes connect to the primary in time, the primary shall terminate itself.
    The startup functions shall not be triggered.


.. comp_req:: Activity startup error
    :id: comp_req__feo__act_startup_error
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: feat_req__feo__act_startup_error
    :status: valid

    If an error occurs during the execution of a startup function, the primary process shall abort calling
    startup functions and terminate itself. For all of the activities
    whose startup functions have already been called successfully, the corresponding shutdown functions shall be
    executed in arbitrary sequence.


.. comp_req:: Activity resource allocation error
    :id: comp_req__feo__act_alloc_error
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: feat_req__feo__act_alloc_error
    :status: valid

    During initialization (i.e. in the startup function of an activity), activities shall check for resource allocation
    and report an error to the executor in case of failure.


.. comp_req:: Activity timeout
    :id: comp_req__feo__act_timeout
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: feat_req__feo__act_timeout
    :status: valid

    If a timeout occurs during startup, stepping or shutdown of an activity, the primary process shall shutdown all
    successfully started activities in arbitrary sequence and terminate itself.


.. comp_req:: Startup timeout
    :id: comp_req__feo__startup_timeout
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: feat_req__feo__startup_timeout
    :status: valid

    If not all activities reach their initialized state within a certain period of time (startup timeout),
    the primary process shall shutdown all successfully started activities in arbitrary sequence and terminate itself.


.. comp_req:: Activity stepping error
    :id: comp_req__feo__act_stepping_error
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: feat_req__feo__act_stepping_error
    :status: valid

    If an activity fails in the step function, the primary process shall call shutdown for all activities
    in arbitrary sequence and terminate itself.


.. comp_req:: Activity shutdown error
    :id: comp_req__feo__act_shutdown_error
    :reqtype: Functional
    :security: YES
    :safety: ASIL_B
    :satisfies: feat_req__feo__act_shutdown_error
    :status: valid

    If an activity fails in the shutdown function, the primary process shall shutdown all remaining activities
    in arbitrary sequence and terminate itself.

.. needextend:: docname is not None and "feo/docs/requirements" in docname
   :+tags: component_feo

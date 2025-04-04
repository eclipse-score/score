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

Requirements
############


Definitions
===========

.. feat_req:: Definition: Application
    :id: FEAT_REQ__feo__application
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: STKH_REQ__282
    :status: valid

    An application consists of one or more activities.

    An application consists of one or more operating system processes.
    In particular it consists of the primary process which handles the lifecycle, configuration and execution management.
    It may optionally consist of one or more Secondary processes.
    The purpose of secondary processes is to run code in separate address spaces (Freedom From Interference) for safety reasons.
    Each process (primary and secondary) belongs to exactly one application.
    Each process contains one ore more operating system threads.

.. feat_req:: Definition: Activity
    :id: FEAT_REQ__feo__activity
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: STKH_REQ__282
    :status: valid

    Activities are mapped to threads within primary or secondary processes.
    Each activity is mapped to exactly one thread and provides the following functions:

    * `init`: Initialization of the activity.
    * `step`: Execution of the activity.
    * `shutdown`: Shutdown of the activity.

    The mapping is done in a configuration file and cannot be changed at runtime.

.. feat_req:: Definition: Task Chain
    :id: FEAT_REQ__feo__task_chain
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: STKH_REQ__282
    :status: valid

    All activities within an application are arranged within a `Task Chain`.
    There is exactly one task chain per application.

    The task chain configuration defines the execution order of the activities.
    In particular it defines when the task chain is activated (typically in a cyclic manner) and in which order the activities will run.

    Every task chain has exactly one `receiver` activity which will run in the beginning.
    The purpose of the receiver activity is to collect external input signals and provide them to the other activities during task chain execution.
    Every task chain has exactly one `sender` activity which will run in the end.
    The purpose of the sender activity is to collect signals produced by activities within the task chain and send them to external entities.

.. feat_req:: Definition: Service Activity
    :id: FEAT_REQ__feo__service_activity
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: STKH_REQ__282
    :status: valid

    * Service activities are a means to interact with the outside world, e.g. via
      network communication, direct sensor input or direct actuator output
    * Service activities may also use APIs external to the framework
      (e.g. networking APIs, reading from external sensor devices, writing HW I/O, etc.)

  .. feat_req:: Definition: Agent
    :id: FEAT_REQ__feo_agent
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: STKH_REQ__282
    :status: valid

    In order to execute activities in secondary processes, the executor makes 
    use of an `Agent` for each secondary process.
    The agent receives commands from the executor, invokes actions on 
    activities within its process and reports back to the executor.

    Each Activity that is part of the task chain is associated with an
    Agent, which takes over the task to wait for a trigger from its 
    corresponding Executor. When the Agent gets a step request from the 
    Executor, it calls the Step function of the Activity There is exactly 
    one agent for each secondary process.The primary can but doesn't have to be 
    associated with an agent.

Dynamic Architecture
====================

.. feat_req:: The lifecycle of an `Application` consists of 3 phases: Init, Run and Shutdown.
    :id: FEAT_REQ__application_lifecycle
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: STKH_REQ__282
    :status: valid

    The Application Lifecycle consists of 3 phases: Init, Run and Shutdown.

.. feat_req:: Initialization of activities
    :id: FEAT_REQ__feo__activity_init
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: STKH_REQ__282
    :status: valid

    Initialization of activities is done during application initialization.

    Each activity is initialized by a call to its `init` function.

    The `init` function will be invoked in the thread to which the activity is mapped.
    Note that `init`, `step` and `shutdown` functions will be run in the same thread.

.. feat_req:: Stepping of activities
    :id: FEAT_REQ__feo__activitiy_step
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: STKH_REQ__282
    :status: valid

    Each activity is stepped once within each execution of the task chain they belong to.

    Stepping is done by a call to an activity's `step` function.

.. feat_req:: Shutdown of activities
    :id: FEAT_REQ__feo__activity_shutdown
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: STKH_REQ__282
    :status: valid

    Shutdown of activities is done during application shutdown.

    Each activity is shut down by a call to its `shutdown` function.

    The `shutdown` function will be invoked in the thread to which the activity is mapped.

Supervision
===========

.. feat_req:: Alive supervision
    :id: FEAT_REQ__feo__alive_supervision
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: STKH_REQ__282
    :status: valid

    The framework shall provide the functionality to enable the reporting of 
    alive supervision checkpoint to an external health management system 
    (e.g. watchdog) 

.. feat_req:: Support of deadline supervision checkpoints
    :id: FEAT_REQ__feo__deadline_supervision
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: STKH_REQ__282
    :status: valid

    The framework shall provide the functionality to enable the reporting of 
    deadline supervision checkpoints to an external health management system 
    (e.g. watchdog) 

.. feat_req:: Support of logical supervision
    :id: FEAT_REQ__feo__logical_supervision
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: STKH_REQ__282
    :status: valid

    The framework shall provide the functionality to enable the reporting of 
    logical supervision checkpoints to an external health management system 
    (e.g. watchdog) 

.. feat_req:: Trustable computation
    :id: FEAT_REQ__feo__trustable_computation
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: STKH_REQ__282
    :status: valid

    The framework shall provide mechanisms to check after the computation of 
    an Activity if the result is trustable.
    This can be done e.g. via evaluation of floating point exceptions, 
    checking of hardware registers or status information of the
    software platform.


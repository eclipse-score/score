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
#############

.. evaluate following sth requirements:
.. com driven:
.. stkh_req__app_architectures__support_time
.. stkh_req__app_architectures__support_data
.. stkh_req__app_architectures__support_request

.. stkh_req__communication__service_quality

.. compute driven:
.. stkh_req__execution_model__processes
.. stkh_req__dev_experience__tracing_of_exec

.. safety:
.. stkh_req__dependability__automotive_safety
.. stkh_req__functional_req__safe_comput

.. security:
.. stkh_req__dependability__security_features

.. accelerators:
.. stkh_req__functional_req__hardware_comput
.. stkh_req__functional_req__comp_subsystem

.. feat_req:: User Level Scheduling
   :id: feat_req__orchestration__user_level
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: invalid

   The system **SHALL** implement user-level scheduling for task management so that task switches occur in the nanosecond range.

   *Rationale:* Minimizes overhead compared to conventional thread-based approaches.

   *Verification:* Benchmarking task switching performance.

.. feat_req:: Cooperative Multi Tasking
   :id: feat_req__orchestration__cooperative_multi
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: invalid

   The system **SHALL** support cooperative multi-tasking, allowing multiple concurrent tasks to share the same OS thread.

   *Rationale:* Reduces the number of threads and associated context-switch overhead.

   *Verification:* Analysis of thread usage and context-switch statistics.

.. feat_req:: Configurable Thread Pool
   :id: feat_req__orchestration__configurable_thread
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: invalid

   The system **SHALL** provide a configurable thread pool for executing concurrent tasks. Additional thread pools **MAY** be introduced only when necessary (e.g., when tasks differ in criticality or require separation by process boundaries).

   *Rationale:* Optimizes resource utilization and enables parallel execution.

   *Verification:* Configuration tests and runtime profiling.

.. feat_req:: Deterministic and Expressive Programming Framework
   :id: feat_req__orchestration__deterministic_and
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: invalid

   The programming framework **SHALL** allow developers to express concurrent and sequential dependencies, conditional branching, timing constraints, and error handling paths while abstracting explicit thread management and complex synchronization.

   *Rationale:* Provides a user-friendly, transparent, and deterministic interface that aids debugging and control flow analysis.

   *Verification:* Code reviews and simulated execution scenarios.

.. feat_req:: Resource Independent Algorithm Design
   :id: feat_req__orchestration__resource
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: invalid

   The system **SHALL** decouple algorithm design from deployment specifics, allowing dynamic updates, upgrades, and new deployments.

   *Rationale:* Facilitates integration of applications from distributed teams without binding to a fixed runtime configuration.

   *Verification:* Integration tests in simulated deployment environments.

.. feat_req:: Tracing and Profiling
   :id: feat_req__orchestration__tracing_and
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes, stkh_req__dev_experience__tracing_of_exec
   :status: invalid

   The system **SHALL** provide hooks for tracing and profiling task execution to verify behavior and control flow of the integrated system.

   *Rationale:* Enables effective debugging and validation of the orchestration framework.

   *Verification:* Trace logs analysis and profiling test cases.

.. security impact

.. feat_req:: Trusted Intra Process Code Assumption
   :id: feat_req__orchestration__trusted_intra
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__execution_model__processes, stkh_req__dependability__security_features
   :status: invalid

   The orchestration feature **SHALL** assume that all code executing within a process is trusted.

   *Rationale:* Reduces the attack surface by focusing security on inter-process interactions.

   *Verification:* Security reviews and threat modeling.

.. security and safety impact

.. feat_req:: Exclusive Use of IPC Feature for Inter Process Synchronization
   :id: feat_req__orchestration__exclusive_use_of_ipc
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__dependability__security_features, stkh_req__communication__inter_process
   :status: invalid

   The system **SHALL** use the approved IPC feature exclusively for all inter-process synchronization.

   *Rationale:* Minimizes the attack surface and leverages a pre-evaluated secure mechanism.

   *Verification:* Code audits and configuration checks.

.. safety impact

.. feat_req:: Homogeneous ASIL Levels Within a Process
   :id: feat_req__orchestration__homogeneous_asil
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__dependability__automotive_safety
   :status: invalid

   All tasks within a single process **SHALL** share the same ASIL level.

   *Rationale:* Prevents mixing of safety-critical and non-safety-critical operations.

   *Verification:* ASIL compliance testing and system safety reviews.

.. feat_req:: Configurable Error Handling Mechanisms
   :id: feat_req__orchestration__configurable_error
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__dependability__automotive_safety
   :status: invalid

   The orchestration feature **SHALL** include configurable error handling mechanisms that are insulated from the effects of misbehaving tasks (e.g., tasks in an infinite loop).

   *Rationale:* Ensures that system stability is maintained even under error conditions.

   *Verification:* Error injection testing and robustness analysis.

.. feat_req:: External Supervision Hooks
   :id: feat_req__orchestration__external_supervision
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__dependability__automotive_safety
   :status: invalid

   The system **SHALL** expose hooks for external supervision (e.g., integration with a watchdog) without directly coupling to the watchdog mechanism.

   *Rationale:* Enables integration with external safety monitors while maintaining modularity.

   *Verification:* Integration tests with simulated watchdog behavior.

.. feat_req:: Enforcement of Homogeneous Criticality in Thread Pools
   :id: feat_req__orchestration__enforcement_of
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__dependability__automotive_safety
   :status: invalid

   The system **SHALL** enforce that all tasks within a thread pool have the same criticality level. Lower-criticality tasks **SHALL NOT** influence the timing behavior of higher-criticality tasks.

   *Rationale:* Prevents interference across criticality levels, ensuring reliable performance in safety-critical applications.

   *Verification:* Criticality isolation tests and scheduling verification.

.. feat_req:: Priority Based Preemption Between Thread Pools
   :id: feat_req__orchestration__priority_based
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__dependability__automotive_safety
   :status: invalid

   The system **SHALL** implement priority-based preemption between thread pools to ensure that lower-priority programs cannot interfere with higher-priority programs.

   *Rationale:* Maintains deterministic timing behavior for high-criticality tasks.

   *Verification:* Priority scheduling tests and timing analysis.

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
############

.. document:: Orchestration Requirements
   :id: doc__orchestration_requirements
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_feat
   :tags: orchestration

Executor
========

Task Management
---------------

.. TODO: set invalid requirements to valid once bug regarding tracing ASIL and QM sth req is solved

.. feat_req:: Async Cooperative Task Runtime
   :id: feat_req__orchestration__exec_async_rt
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   The executor shall provide a cooperative task runtime for async programming based on the definition of Rust's async model (see `Asynchronous Programming in Rust <https://rust-lang.github.io/async-book>`).

.. feat_req:: Yielding Guidelines for Long Operations
   :id: feat_req__orchestration__exec_yielding
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   The executor shall provide guidelines for dividing long-running operations into smaller, cooperatively yielding segments.

.. feat_req:: Dedicated Threads for Blocking Operations
   :id: feat_req__orchestration__exec_block_threads
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   The system shall support execution of tasks containing blocking calls on dedicated OS threads isolated from cooperative scheduling.

Special Tasks and Preemption
----------------------------

.. feat_req:: Preemptive Scheduling for Safety Tasks
   :id: feat_req__orchestration__exec_preempt_safety
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__dependability__automotive_safety
   :status: invalid

   The Executor shall support preemptive scheduling of special safety-critical tasks, guaranteeing their execution.

.. feat_req:: Separate Priority for Safety Tasks
   :id: feat_req__orchestration__exec_safe_task_prio
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__dependability__automotive_safety
   :status: invalid

   Safety-critical tasks shall be prioritized separately from standard cooperative tasks.

Thread Pool Configuration
--------------------------

.. feat_req:: Fixed-Size Thread Pool
   :id: feat_req__orchestration__exec_fixed_pool
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Executor instances shall run tasks on a statically configured thread pool with a fixed thread count.

.. feat_req:: Uniform OS Priority for Non-Safety Threads
   :id: feat_req__orchestration__exec_os_prio
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Threads within an Executor not involved in safety-critical tasks shall share identical OS-level priority.

.. feat_req:: Configurable Thread Affinity
   :id: feat_req__orchestration__exec_thread_aff
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Thread affinity to CPU cores shall be configurable per Executor instance.

.. feat_req:: Isolated Thread Pools
   :id: feat_req__orchestration__exec_pool_isolation
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Executor instances shall isolate their thread pools from each other.

Task Scheduling
---------------

.. feat_req:: No Internal Priorities for Cooperative Tasks
   :id: feat_req__orchestration__exec_no_int_prios
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Cooperative tasks within an Executor shall execute without internal priority distinctions.

.. feat_req:: FIFO or Fairness Scheduling
   :id: feat_req__orchestration__exec_fifo_fair_sched
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   The Executor shall support FIFO or fairness-based scheduling among cooperative tasks.

.. feat_req:: Scale via Additional Executors
   :id: feat_req__orchestration__exec_scale_instances
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Scaling of Executor resources shall be achieved through additional Executor instances rather than dynamic thread scaling.

Orchestrator Requirements
=========================

Program Definition
------------------

.. feat_req:: Static Program Execution Graphs
   :id: feat_req__orchestration__orch_static_graphs
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__app_architectures__support_time
   :status: valid

   The Orchestrator shall provide a runtime-static Program abstraction representing computation logic as execution graphs.

.. feat_req:: Explicit Control Flows and Timing
   :id: feat_req__orchestration__orch_ctrl_flows
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__app_architectures__support_time
   :status: valid

   Programs shall explicitly define sequential, parallel, conditional execution flows, loops, and timing contracts.

.. feat_req:: Event-Based Synchronization
   :id: feat_req__orchestration__orch_event_sync
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__app_architectures__support_time
   :status: valid

   Programs shall support explicit event-based synchronization and trigger conditions.

.. feat_req:: Fault-Handling and Monitors
   :id: feat_req__orchestration__orch_fault_mon
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__app_architectures__support_time
   :status: valid

   Programs shall contain integrated fault-handling logic and execution monitors to enforce timing constraints.

API Design
----------

.. feat_req:: Code-First Integration API
   :id: feat_req__orchestration__orch_code_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__app_architectures__support_time
   :status: valid

   The Orchestrator shall offer a code-first API to integrate directly with application logic without external DSL/IDL.

Execution Model
---------------

.. feat_req:: Single-Executor Deployment
   :id: feat_req__orchestration__orch_single_deploy
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__app_architectures__support_time
   :status: valid

   Each Program shall be deployed exclusively on a single Executor instance.

.. feat_req:: Multi-Program Support per Executor
   :id: feat_req__orchestration__orch_multi_prog
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__app_architectures__support_time
   :status: valid

   Executors may host multiple Programs to support resource sharing.

.. feat_req:: Event-Only Communication
   :id: feat_req__orchestration__orch_event_comm
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__app_architectures__support_time
   :status: valid

   Programs shall communicate exclusively through explicitly defined events.

Special Safety Task Integration
-------------------------------

.. feat_req:: Safety Tasks in Programs
   :id: feat_req__orchestration__orch_safety_tasks
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__dependability__automotive_safety
   :status: invalid

   Critical timing or safety paths within Programs shall be executed via preemptive special tasks provided by the Executor.

Observability Requirements
==========================

.. feat_req:: Trace Correlation Points
   :id: feat_req__orchestration__obsv_trace_corr
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes, stkh_req__dev_experience__tracing_of_exec
   :status: valid

   The Executor and Orchestrator shall expose structured tracing points correlating user-space task scheduling with OS-level scheduling.

.. feat_req:: Task Lifecycle and Queue Metrics
   :id: feat_req__orchestration__obsv_lifecycle_qm
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes, stkh_req__dev_experience__tracing_of_exec
   :status: valid

   Observability shall capture task lifecycle events, Executor queue metrics, and mapping of user-space tasks to OS threads.

.. feat_req:: Program Flow and Timing Visibility
   :id: feat_req__orchestration__obsv_flow_vis
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes, stkh_req__dev_experience__tracing_of_exec
   :status: valid

   Observability shall provide visibility into Program execution flow, event synchronization points, and timing violations.

.. feat_req:: Integration with Tracing Frameworks
   :id: feat_req__orchestration__obsv_fw_integ
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes, stkh_req__dev_experience__tracing_of_exec
   :status: valid

   Tracing points shall integrate seamlessly with established tracing frameworks like Perfetto and LTTng.

External Supervision Requirements
=================================

.. feat_req:: Health Indicators Export
   :id: feat_req__orchestration__ext_health_inds
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Executor and Orchestrator frameworks shall expose health indicators for integration with external supervisory systems.

.. feat_req:: Internal Task Health Verification
   :id: feat_req__orchestration__ext_task_health
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Frameworks shall internally verify task-level health status based on timing constraints and fault-handling execution.

General Constraints
===================

.. feat_req:: Determinism and Scalability
   :id: feat_req__orchestration__gen_det_scale
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   The Executor and Orchestrator shall maintain determinism and scalability suitable for mixed-criticality environments.

.. feat_req:: Explicit Preemption Activation
   :id: feat_req__orchestration__gen_preempt_act
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__dependability__automotive_safety
   :status: invalid

   Preemptive scheduling shall only be activated explicitly for tasks with safety or critical timing constraints.

.. feat_req:: Exclusive Use of IPC Feature for Inter Process Synchronization
   :id: feat_req__orchestration__gen_excl_ipc
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes, stkh_req__dependability__automotive_safety, stkh_req__dependability__security_features, stkh_req__communication__inter_process
   :status: invalid

   The system shall use the approved IPC feature exclusively for all inter-process synchronization.

.. needextend:: docname is not None and "orchestration/requirements" in docname
   :+tags: orchestration

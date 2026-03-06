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

.. _vso_requirements:

Requirements
############

Workload Lifecycle Management
==============================

.. feat_req:: Standard Container Command Set
   :id: feat_req__vso__standard_commands
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__vso__workload_control
   :status: valid

   The orchestrator shall support seven essential workload commands: create, start, pause, resume, stop, restart, and delete. All commands shall be delivered via remote procedure calls and follow a standardized response format.

.. feat_req:: Container State Model
   :id: feat_req__vso__state_model
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__vso__workload_control
   :status: valid

   The system shall manage containers across five main states: Created, Running, Paused, Exited, and Restarting. State transitions shall follow strict rules and be tracked by the StateManager component.

Scenario-Based Automation
==========================

.. feat_req:: Conditional Execution Engine
   :id: feat_req__vso__conditional_execution
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__vso__vehicle_state_awareness
   :status: valid

   The orchestrator shall automatically control services based on changes in vehicle state. Scenario information shall be retrieved from a distributed key-value store, and corresponding actions shall be executed automatically when conditions are met.

Resource Management and Isolation
==================================

.. feat_req:: Container Security Isolation
   :id: feat_req__vso__security_isolation
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__security_features,stkh_req__vso__security_isolation
   :status: valid

   User identifiers, group permissions, and Linux capabilities are strictly controlled according to the principle of least privilege. Restricting privileged mode and applying security contexts strengthens system-level protection.

.. feat_req:: Performance Optimization
   :id: feat_req__vso__perf_optimization
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   Processor and memory usage are tracked in real time, allowing early detection of resource shortages. Parallel container creation, asynchronous processing, and automatic scaling optimize startup times and maximize efficiency.

Monitoring and Recovery
========================

.. feat_req:: State Monitoring
   :id: feat_req__vso__state_monitoring
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__automotive_safety
   :status: valid

   Comprehensive health checks continuously monitor process status, port connectivity, and application-level health. Changes in status are detected immediately, ensuring consistency across the entire system.

.. feat_req:: Automatic Recovery Mechanisms
   :id: feat_req__vso__auto_recovery
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__automotive_safety,stkh_req__vso__fault_tolerance
   :status: valid

   Failure recovery is automated according to restart policies. Failed containers are automatically restarted, and state-based corrective actions minimize operational downtime. Customized recovery logic is applied depending on the error type.

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

.. _vso_requirements:

Requirements
############

VSO Contract API
================

.. feat_req:: VSO Scenario Contract Definition
   :id: feat_req__vso__contract_api
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__vso__scenario_evidence
   :status: valid

   The system shall provide APIs to identify roles, capabilities, real-time health, workload policy configuration information of node such as placement, movement, starting and stopping with pipeline dependencies. All APIs shall be delivered via remote procedure calls and follow a standardized response format.

VSO Evidence Aggregation
=========================

.. feat_req:: VSO Evidence Aggregation and Correlation
   :id: feat_req__vso__evidence_aggregation
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__vso__scenario_evidence
   :status: valid

   The system shall correlate runtime, diagnostic, fault, health, log, and resource signals by scenario_run_id.
   
   Evidence aggregation shall:
   
   - Collect runtime timing and deadline events
   - Collect diagnostic logs and fault status
   - Collect platform resource metrics (CPU, memory, node health)
   - Correlate all signals using scenario_run_id as the reference
   - Support pipeline chain tracking
   - Maintain temporal ordering of events across nodes

VSO Evidence Quality
=====================

.. feat_req:: VSO Evidence Quality Metrics
   :id: feat_req__vso__evidence_quality
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__vso__scenario_evidence
   :status: valid

   The system shall attach freshness, completeness, and confidence to all evidence packages. Evidence packages marked INCOMPLETE shall indicate missing signals and affected nodes.
   
   Quality metrics shall include:
   
   - **Freshness:** Timestamp and age of evidence data
   - **Completeness:** Percentage of required signals successfully collected
   - **Confidence:** Classification confidence level (HIGH, MEDIUM, LOW)
   - **Source Health:** Health status of data sources

VSO Response Management
========================

.. feat_req:: VSO Observability Escalation and Response
   :id: feat_req__vso__response_management
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__vso__observability, stkh_req__vso__fault_detection, stkh_req__vso__events_visibility
   :status: valid

   The system shall support observability escalation, snapshot freeze, handoff, event publication, notification, and recovery.
   
   Response actions per evidence state:
   
   - **OK:** NORMAL observability, no action
   - **WATCH:** Optional light observation, monitoring only
   - **WARN:** FOCUSED_DEBUG (30s), pre-snapshot collection, package + condRef handoff, Dashboard WARN notification
   - **VIOLATED:** INTENSIVE_DIAG (60s), freeze snapshot, package + condRef + quality handoff, event publication + Dashboard ERROR notification
   - **INCOMPLETE:** Source health report, mark incomplete, package with LOW confidence, Dashboard WARN notification
   - **RECOVERED:** NORMAL observability, archive snapshot, recovery package, Dashboard INFO notification


VSO Evidence Package Model
=================================

.. feat_req:: VSO Evidence Package Model
   :id: feat_req__vso__evidence_package_model
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__vso__state_manager_integration
   :status: valid

   The system shall deliver the generated evidence packages and conditionRefs without forcing target states.
   
   Evidence package shall include:
   
   - scenario_run_id (unique identifier for this scenario execution)
   - pipeline_id (identifier for the pipeline chain)
   - affected_nodes (list of nodes involved in the violation)
   - violation_type (timing, resource, ordering, diagnostic)
   - confidence (HIGH, MEDIUM, LOW)
   - conditionRefs (references to conditions for execution adaptation)
   - timestamp and evidence quality metrics
   
   VSO shall NOT:
   
   - Force specific Function Group States
   - Execute lifecycle transitions
   - Make safety decisions
   - Control application execution directly

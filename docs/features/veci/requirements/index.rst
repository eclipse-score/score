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

.. _veci_requirements:

Requirements
============

.. feat_req:: Current State Publication
   :id: feat_req__veci__state_publication
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The platform shall publish selected runtime state, configuration status, and health indicators in a
   structured, versioned, and timestamped model, supporting both pull and event-driven update patterns.
   Only explicitly exposed signals and metadata shall be made available to external systems.

.. feat_req:: Desired State Interface
   :id: feat_req__veci__desired_state_interface
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The platform shall provide standardized desired state endpoints for platform components and
   applications. Desired state updates shall represent target conditions rather than direct low-level
   actuation commands, and shall be versioned, typed, and associated with explicit preconditions.

.. feat_req:: State Schema and Semantics per Domain
   :id: feat_req__veci__state_schema
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   Each VECI state domain shall define an expected desired/current state schema, semantic constraints,
   admission preconditions, safety gates, and convergence acknowledgement/completion semantics.

.. feat_req:: Desired State Acquisition and Freshness
   :id: feat_req__veci__desired_state_acquisition
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The vehicle shall retrieve desired state at its own pace, and shall apply freshness checks based on
   versioning and timestamps to prevent reconciliation against stale desired state.

.. feat_req:: Policy and Constraint Injection
   :id: feat_req__veci__policy_injection
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The platform shall accept desired constraints and policy inputs from external systems as proposals
   only. Injected policies shall pass local policy checks before activation, and shall support explicit
   validity windows and scoped applicability.

.. feat_req:: Validation and Enforcement Pipeline
   :id: feat_req__veci__validation_pipeline
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   Every desired state update shall pass through authentication, authorization, schema validation,
   semantic validation, and policy compliance checks before reconciliation. Reconciliation shall be
   admitted only if local rules, safety constraints, and current system state permit it. Rejected
   updates shall produce explicit status codes and diagnostic context.

.. feat_req:: Vehicle-Side Decision Authority
   :id: feat_req__veci__vehicle_authority
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__safe_state
   :status: valid

   Final admission and execution decisions for any externally provided desired state update or policy
   shall remain with the vehicle and shall not be delegated to external orchestrators.

.. feat_req:: Reconciliation Execution
   :id: feat_req__veci__reconciliation_execution
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   Accepted desired state updates shall be realized through existing platform lifecycle and
   orchestration mechanisms, without introducing parallel execution paths.

.. feat_req:: Convergence Status Reporting
   :id: feat_req__veci__convergence_reporting
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The platform shall report structured reconciliation status including accepted, progressing,
   converged, partially converged, rejected, and failed outcomes, along with diagnostic context.

.. feat_req:: Configurable Reconciliation Mode
   :id: feat_req__veci__reconciliation_mode
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The platform shall support both on-demand (vehicle-initiated) reconciliation per desired state
   version and continuous reconciliation/monitoring until convergence criteria are met. The active
   reconciliation mode shall be configurable per vehicle, per state domain, or per deployment profile.

.. feat_req:: Push-Triggered Reconciliation
   :id: feat_req__veci__push_triggered_reconciliation
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The platform shall support orchestrator-initiated notifications signalling that a new desired state
   version is available, and shall treat such notifications as triggers to retrieve and reconcile the
   referenced desired state version subject to local trust, safety, and policy checks.

.. feat_req:: Deterministic Execution
   :id: feat_req__veci__deterministic_execution
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__runtime_determinism
   :status: valid

   Reconciliation execution shall remain deterministic for predefined operating scenarios and shall
   degrade gracefully in error conditions.

.. feat_req:: Bounded Failure Handling
   :id: feat_req__veci__bounded_failure_handling
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__error_reaction
   :status: valid

   The platform shall handle communication loss, invalid policies, reconciliation timeouts, and
   reconciliation failures through bounded error handling, including rollback or fallback behavior
   where applicable.

.. feat_req:: Safe State Protection
   :id: feat_req__veci__safe_state_protection
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__safe_state
   :status: valid

   Desired state reconciliation shall not be allowed to bypass local safety constraints or lifecycle
   guards.

.. feat_req:: Endpoint Authentication
   :id: feat_req__veci__endpoint_authentication
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   All external endpoints interacting via VECI shall be strongly authenticated prior to interaction,
   using credentials that are revocable and bound to scoped permissions.

.. feat_req:: Authorization and Least Privilege
   :id: feat_req__veci__authorization
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   External desired state updates shall be authorized per capability, context, and policy. Access
   shall be limited to the explicitly exposed state and policy surfaces.

.. feat_req:: Message Integrity and Replay Protection
   :id: feat_req__veci__message_integrity
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__communication__secure
   :status: valid

   All VECI interface messages shall be integrity-protected and freshness-validated to prevent
   tampering and replay attacks.

.. feat_req:: Trust Management
   :id: feat_req__veci__trust_management
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The platform shall manage trust relationships with external systems through verifiable identities
   and revocable credentials, supporting runtime revocation and trust re-establishment without
   requiring a platform restart.

.. feat_req:: Auditability of Security-Relevant Actions
   :id: feat_req__veci__auditability
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   Security-relevant actions shall be auditable end-to-end, recording requester identity, policy
   context, validation outcomes, and decision results to support post-event analysis and compliance
   evidence.

.. feat_req:: State Reconciliation Semantics
   :id: feat_req__veci__reconciliation_semantics
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The platform shall implement explicit reconciliation semantics including desired state versioning
   with monotonic update handling, conflict handling between concurrent updates, partial convergence
   reporting, and stable final states for accepted or rejected reconciliation attempts.

.. feat_req:: Transport-Agnostic Interface
   :id: feat_req__veci__transport_agnostic
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__extensible_external
   :status: valid

   The VECI interface shall be transport-agnostic and shall operate across vehicle-to-cloud,
   vehicle-to-edge, and hybrid deployment profiles without changes to protocol-level behavior.

.. feat_req:: Interface Versioning and Compatibility
   :id: feat_req__veci__versioning
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__extensible_external
   :status: valid

   VECI interface contracts and data models shall be versioned to support incremental evolution.
   Backward-compatible extensions shall be preferred; breaking changes shall require explicit version
   transitions.

.. feat_req:: Additive Integration with Existing Modules
   :id: feat_req__veci__additive_integration
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__overall_goals__reuse_of_app_soft
   :status: valid

   VECI shall augment existing S-CORE modules through additive integration points (lifecycle,
   communication/IPC abstractions, and platform security services) without replacing existing
   in-vehicle lifecycle, orchestration, or IPC mechanisms.

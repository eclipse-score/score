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

.. _veci_feature:

VECI
####

.. document:: VECI
   :id: doc__veci
   :status: draft
   :safety: QM
   :security: YES
   :tags: feature_request
   :realizes: wp__feat_request

.. toctree::
   :maxdepth: 1
   :glob:
   :titlesonly:
   :hidden:

   */index

Feature flag
============

To activate this feature, use the following feature flag:

``experimental_veci``

Abstract
========

This proposal introduces the Vehicle External Control Interface (VECI), a standardized vehicle-side interface layer
for interaction with external management systems such as cloud or on-premises orchestrators. VECI enables vehicles to
expose selected runtime state, accept externally requested target state, and reconcile desired state under local
validation and enforcement.

VECI defines an end-to-end interaction model including current state publication, desired state acquisition,
vehicle-side reconciliation, and convergence monitoring. It further establishes constraints and guarantees such as
vehicle-side decision authority, deterministic enforcement paths, secure communication, and auditability.

The interface is designed to be extensible and transport-agnostic, enabling integration with diverse deployment
environments while preserving existing in-vehicle architecture and autonomy.

Motivation
==========

As S-CORE adoption scales from individual vehicles to fleet-level deployments, a consistent mechanism for system updates
and configuration management across heterogeneous vehicle platforms becomes necessary.
Today, integration with external orchestration systems is often implementation-specific,
which leads to fragmented interfaces and difficult cross-vehicle operability.

Cross-Vehicle Operability
-------------------------

In current projects, externally managed vehicle functions are often exposed through custom APIs and integration adapters.
This creates incompatible state models and observability semantics across vehicle programs, even when platform capabilities are similar.

A common vehicle-side interface is required to make external state orchestration portable across deployments and suppliers.

Operational Observability at Scale
----------------------------------

Fleet operations require consistent insight into vehicle runtime state, feature activation status, and health signals.
Without a standardized reporting model, diagnostics and governance workflows become tightly coupled to implementation details.

S-CORE already provides key observability building blocks through Lifecycle health supervision,
analysis-infra logging, and tracing capabilities.

VECI does not introduce a separate observability stack. Instead, it standardizes how orchestrator-relevant state is exposed
and correlated with these existing platform signals, so external systems can reason about vehicle behavior in a comparable
and machine-processable way.

Safe External Influence
-----------------------

External systems often need to provide desired constraints, rollout directives, or policy updates.
Without a standardized safety and policy validation path, these interactions can bypass local assumptions and increase risk.

VECI establishes controlled injection points and a strict vehicle-side validation pipeline so external influence remains bounded,
auditable, and aligned with local safety/security constraints.

Without a standardized interface, systems cannot reliably:

* expose orchestratable platform state in a common form,
* report runtime and health state in a consistent and machine-readable way,
* accept desired state and enforce convergence under local safety and security rules.

VECI addresses this gap by defining a standardized, vehicle-side interaction contract that enables scalable observability,
control, and policy governance across heterogeneous fleets while preserving local authority.


Rationale
=========

VECI is designed as a state-oriented semantic interface on top of existing S-CORE runtime capabilities. Traditional
integration approaches rely on proprietary adapters and ad-hoc APIs, which are difficult to scale and validate across
vendors and deployments. By introducing a common model for state, control, and policy exchange, VECI enables
interoperable external interaction without requiring fundamental changes to core modules.

The vehicle remains the final authority for all externally requested actions. Inputs from external systems are validated
against local constraints, trust settings, and safety policies before being accepted or applied.

This design was selected to keep core platform behavior deterministic while still enabling dynamic external coordination.
Rather than introducing a new orchestration runtime, VECI reuses existing lifecycle, communication, and policy mechanisms
through stable integration hooks.


Scope Overview
--------------

In scope:

- Standardized vehicle-side desired state interface for selected capabilities
- Structured state publication for observability and fleet operations
- Policy and constraint injection with local validation and enforcement
- State convergence visibility (accepted, progressing, converged, rejected)
- Integration with existing S-CORE modules through additive interfaces

Out of scope:

- Definition or implementation of cloud-side orchestration systems
- OEM-specific decision-making strategies for optimization or planning
- Direct remote actuation paths that bypass vehicle-side policy checks
- Replacement of existing in-vehicle lifecycle, orchestration, or IPC mechanisms


Specification
=============

VECI defines a standardized vehicle-side interaction model for external orchestrators based on state-seeking.
The interface is structured around desired state exchange and reconciliation safeguards.
A vehicle-side coordination component is responsible for mediating all external interactions.

Interaction Model
_________________

VECI follows a state-oriented interaction pattern:

1. The vehicle publishes selected current state and exposed state schema.
2. An external orchestrator provides desired target state and/or policy constraints. Desired state may be submitted directly or staged at an accessible location for vehicle retrieval.
   The orchestrator may optionally send a notification that a new desired state version is available.
3. The vehicle retrieves the desired state at its own pace and applies freshness checks to prevent stale reconciliation.
4. The vehicle validates each desired state update against trust, schema, semantic, policy, and runtime gates.
5. Accepted desired state is reconciled via existing platform mechanisms and reported with structured convergence status and diagnostics.
   Continuous reconciliation/monitoring is optional and can be enabled or disabled by vehicle-side configuration or policy.

This flow ensures external intent can be expressed as target state while preserving vehicle-side authority over
admission, reconciliation strategy, and execution boundaries.

State Exposure and Observability
________________________________

The vehicle publishes selected runtime state, configuration status, and health indicators in a structured model.
State publication supports both pull and event-driven update patterns.
Only explicitly exposed signals and metadata are made available to external systems.

State data is versioned and timestamped to support consistency checks, traceability, and replay-safe processing.

Desired State Interface
_______________________

VECI provides standardized desired state endpoints for platform components and applications.
Desired state updates represent target conditions instead of direct low-level actuation commands.
All desired state updates are versioned, typed, and associated with explicit preconditions.

Each state domain defines:

- expected desired/current state schema and semantic constraints,
- admission preconditions and safety gates,
- convergence acknowledgement and completion semantics.

Policy and Constraint Injection
_______________________________

External systems may submit desired constraints or policy inputs, such as execution limits, feature activation constraints,
or operating envelopes.
Injected policies are treated as proposals and must pass local policy checks before activation.
Policy priority and conflict resolution rules are defined by the vehicle-side runtime.

Policy activation supports explicit validity windows and scoped applicability to avoid unintended global side effects.

Validation and Enforcement Pipeline
___________________________________

Every desired state update passes through authentication, authorization, schema validation, semantic validation,
and policy compliance checks before reconciliation.
Reconciliation is admitted only if local rules, safety constraints, and current system state permit it.
Rejected updates produce explicit status codes and diagnostic context.

Validation outcomes are recorded to support post-event analysis and compliance evidence.

Execution and Monitoring
________________________

Accepted desired state updates are realized through existing lifecycle and orchestration mechanisms.
VECI provides reconciliation status, progress, and converged/failed outcomes for observability.
Timeout handling and rollback or fallback behavior are supported for bounded fault handling.

The vehicle runtime may operate in either mode:

- on-demand reconciliation per desired state version (vehicle-initiated), or
- continuous reconciliation/monitoring until convergence criteria are met.

Continuous reconciliation is optional and can be switched on or off by vehicle-side configuration or policy.

Execution must remain deterministic for predefined operating scenarios and degrade gracefully in error conditions.

Security and Trust
__________________

All interactions must be authenticated and integrity-protected.
Trust relationships with external systems are managed through verifiable identities and revocable credentials.
The interface supports runtime revocation and trust re-establishment without requiring platform restart.

Security-relevant actions must be auditable end-to-end, including requester identity, policy context, and decision outcome.

State Reconciliation Semantics
______________________________

VECI defines explicit semantics for state reconciliation:

- desired state versioning and monotonic update handling,
- conflict handling between concurrent desired state updates,
- configurable reconciliation mode (one-shot or continuous),
- partial convergence reporting when some state domains cannot be fulfilled,
- stable final states for accepted or rejected reconciliation attempts.

The reconciliation strategy is local to the vehicle runtime and is not controlled by the external orchestrator.

Reconciliation Paradigms and Application Scenarios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VECI supports the following reconciliation paradigms. The selected paradigm can be configured per vehicle,
per state domain, or per deployment profile.

1. Continuous reconciliation

The vehicle continuously evaluates current state against desired state and keeps driving convergence while conditions change.

Typical scenarios:

- safety- or availability-relevant states that must stay within a target envelope,
- long-running state goals that can drift due to environment or resource contention,
- closed-loop fleet operations requiring near-real-time convergence supervision.

2. On-demand reconciliation (vehicle-initiated)

The vehicle decides when to fetch/evaluate desired state and performs reconciliation in discrete cycles.

Typical scenarios:

- bandwidth-constrained or intermittently connected environments,
- energy-sensitive platforms where periodic reconciliation is preferred over continuous processing,
- maintenance windows or scheduled update campaigns.

3. Push-triggered reconciliation (orchestrator-initiated, vehicle subscribes)

The orchestrator emits a new desired-state notification; subscribed vehicles treat this as a trigger to retrieve and
reconcile the referenced desired state version.

Typical scenarios:

- event-driven fleet rollouts requiring faster reaction than periodic pull,
- coordinated policy changes across many vehicles,
- staged desired-state publication where notification and payload distribution are decoupled.

In all paradigms, final admission and execution remain vehicle-side decisions subject to local trust, safety,
and policy checks.

Integration Boundaries
______________________

VECI augments existing S-CORE modules through well-defined integration points, including lifecycle management,
communication/IPC abstractions, and platform security services.
The interface does not define any external orchestration backend and does not mandate cloud architecture choices.


Deployment Profiles
___________________

The VECI model supports multiple deployment profiles:

- vehicle-to-cloud fleet management,
- vehicle-to-edge control within local infrastructure,
- hybrid deployments combining cloud governance with edge-local execution.

The protocol-level behavior remains consistent across profiles; only transport and deployment topology vary.


Versioning and Compatibility
____________________________

Interface contracts and data models are versioned to support incremental evolution.
Backward-compatible extensions are preferred; breaking changes require explicit version transitions.


Requirements
____________

See :ref:`veci_requirements` for the list of feature requirements derived from this specification.


Open Topics
===========

The following topics are expected to be refined in subsequent requirements and architecture work:

- canonical state taxonomy and data model definitions,
- desired state conflict resolution strategy across concurrent external authorities,
- audit log retention and evidence requirements for regulated deployments,
- conformance profiles for different connectivity and security environments.


Backwards Compatibility
=======================

VECI is an incremental extension and does not replace existing in-vehicle lifecycle or communication mechanisms.
Integration is achieved through additive interfaces and hooks, preserving established module responsibilities and
runtime behavior.


Security Impact
===============

VECI introduces security-sensitive interaction paths between external systems and in-vehicle runtime functions.
The following non-complete list highlights key security considerations:

- Endpoint Authentication
   - All external endpoints must be strongly authenticated before interaction
   - Credentials must be revocable and bound to scoped permissions
- Authorization and Least Privilege
   - External desired state updates must be authorized per capability, context, and policy
   - Access must be minimized to explicitly exposed state and policy surfaces
- Message Integrity and Replay Protection
   - All interface messages must be integrity-protected and freshness-validated
- Policy Integrity
   - Injected constraints must be validated, versioned, and auditable
   - Unauthorized or conflicting policy changes must be rejected


Safety Impact
=============

VECI can influence execution behavior through externally provided inputs and therefore requires strict vehicle-side safety guardrails.
The following list gives an idea of safety considerations and is not complete. An in-depth safety analysis must be conducted in the future.

- Vehicle-side Authority
   - Final decision authority for any desired state update remains on the vehicle
- Safe State Protection
   - Desired state reconciliation must not bypass local safety constraints or lifecycle guards
- Bounded Failure Handling
   - Communication loss, invalid policies, and reconciliation failures must degrade gracefully


License Impact
==============

VECI is expected to be implemented primarily using Free and Open Source Software (FOSS), in alignment with the Eclipse Foundation's licensing principles.

- All new components developed under this feature shall be licensed under the Apache 2.0 License
- No additional licensing constraints are introduced by this feature request beyond those already adopted in S-CORE


How to Teach This
=================

The following sources are recommended for onboarding:

- This feature request document and its linked requirements
- The S-CORE platform documentation for related features such as AI Platform, Communication, Lifecycle, and Security/Crypto
- Feature Request issue discussion for VECI (#2751) and related VACP context (#2752)


References
==========

- VECI Feature Request issue: https://github.com/eclipse-score/score/issues/2751
- VACP Feature Request issue (related context): https://github.com/eclipse-score/score/issues/2752
- AI Platform Feature Request PR (format and process reference): https://github.com/eclipse-score/score/pull/1258

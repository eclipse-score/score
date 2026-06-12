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

.. _vacp_requirements:

Requirements
============

.. feat_req:: Intention Establishment
   :id: feat_req__vacp__intention_establishment
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The platform shall provide a mechanism to establish an unambiguous, self-contained, and verifiable
   user intention, supporting various input modalities including natural language, deterministic UI
   interactions, and rule-based triggers.

.. feat_req:: Collaborative Planning
   :id: feat_req__vacp__collaborative_planning
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The Vehicle Coordination Agent (VCA) shall create a fulfillment plan for an established intention,
   defining the sequence and assignment of actions across collaborating agents, including fallback
   strategies and contingency handling. The platform shall support both pre-defined deterministic
   plans and dynamically generated plans.

.. feat_req:: Capability Discovery
   :id: feat_req__vacp__capability_discovery
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The platform shall provide a transport-agnostic mechanism for the VCA to discover capabilities
   offered by vehicle on-board and infrastructure-based agents, supporting broadcast, registry-based,
   and direct query discovery patterns.

.. feat_req:: Capability Exchange and Evaluation
   :id: feat_req__vacp__capability_exchange
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The platform shall allow agents to respond to capability requests with offers describing functional
   and non-functional attributes, and shall enable the VCA to evaluate offers based on availability,
   trustworthiness, and compatibility with the fulfillment plan.

.. feat_req:: Plan Execution and Monitoring
   :id: feat_req__vacp__plan_execution
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The VCA shall coordinate execution of the fulfillment plan across the assigned agents, monitor
   execution progress, detect faults or deviations, and trigger contingency plans as required.

.. feat_req:: Deterministic Execution
   :id: feat_req__vacp__deterministic_execution
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__runtime_determinism
   :status: valid

   Fulfillment plans designated as safety-relevant shall be executable in a deterministic and
   reproducible manner to support safety analysis.

.. feat_req:: Human-in-the-Loop Approval
   :id: feat_req__vacp__human_in_the_loop
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__safe_state
   :status: valid

   The protocol shall provide approval and intervention checkpoints that require explicit human
   confirmation for safety-critical actions, and shall allow humans to override or abort an
   in-progress fulfillment plan.

.. feat_req:: Fault Handling
   :id: feat_req__vacp__fault_handling
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__error_reaction
   :status: valid

   The protocol shall handle agent failures, communication losses, and plan deviations gracefully
   without compromising the safety of the overall system.

.. feat_req:: Agent Authentication
   :id: feat_req__vacp__agent_authentication
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   All agents participating in a VACP collaboration session shall be authenticated prior to
   participation, using credentials that can be verified and revoked at runtime.

.. feat_req:: Message Integrity
   :id: feat_req__vacp__message_integrity
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__secure
   :status: valid

   All VACP protocol messages shall be integrity-protected to prevent tampering and replay attacks.

.. feat_req:: Trust Management
   :id: feat_req__vacp__trust_management
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The protocol shall support explicit establishment, continuous validation, revocation, and
   re-establishment of trust relationships between collaborating agents at runtime, including the
   detection and isolation of compromised agents.

.. feat_req:: Contextual Awareness
   :id: feat_req__vacp__contextual_awareness
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   Agents shall maintain and share contextual information relevant to the collaboration, such as
   environmental conditions, vehicle state, and infrastructure status. Shared context shall be
   timestamped and validated to ensure consistency across collaborating agents.

.. feat_req:: Transport-Agnostic Communication
   :id: feat_req__vacp__transport_agnostic
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__extensible_external
   :status: valid

   The protocol shall be transport-agnostic and capable of operating over diverse underlying
   communication channels without imposing constraints on the underlying infrastructure.

.. feat_req:: Extensibility
   :id: feat_req__vacp__extensibility
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__extensible_external
   :status: valid

   The protocol shall be extensible to accommodate new agent capabilities, message types, and
   collaboration patterns without breaking backward compatibility with existing agents.

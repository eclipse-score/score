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

.. _vacp_feature:

VACP
####

.. document:: VACP
   :id: doc__vacp
   :status: draft
   :safety: ASIL_B
   :security: NO
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

``experimental_vacp``

Abstract
========

This proposal introduces the Vehicle Agent Collaboration Protocol (VACP), a standardized framework for secure and interoperable
collaboration between vehicle on-board agents and infrastructure-based agents. The protocol enables agents to collaboratively
fulfill user intentions by discovering, negotiating, and orchestrating capabilities across vehicles and intelligent infrastructure.
VACP defines an end-to-end workflow including intention establishment, capability discovery and exchange, collaborative planning, and
execution of fulfillment plans. It further specifies constraints and guarantees such as deterministic execution, contextual awareness,
human-in-the-loop approval and intervention, and robust security and trust mechanisms.

The protocol is designed to be extensible and transport-agnostic, allowing it to operate over various underlying communication channels.
Unlike traditional rule-based coordination systems, VACP is purpose-built for agentic systems, where autonomous agents dynamically reason,
plan, and adapt to achieve goals.

Motivation
==========

As the automotive and infrastructure ecosystems increasingly adopt AI-driven capabilities, there is a growing need for standardized collaboration
mechanisms between distributed intelligent agents. Today’s systems remain largely siloed:

* vehicles operate independently with limited coordination,
* infrastructure provides static or reactive services,
and cross-domain orchestration is minimal or proprietary.

This limits the realization of advanced scenarios such as: dynamically coordinated traffic systems, autonomous valet and parking ecosystems,
and collaborative safety response across vehicles and road infrastructure. VACP addresses this gap by enabling intent-driven, cross-entity
collaboration, allowing agents to jointly reason about goals and coordinate actions in real time.


Rationale
=========

VACP is designed as a purpose-built semantic layer for agentic collaboration on top of existing service-oriented communication standards.
Traditional approaches rely on predefined message sets and static coordination rules, which are insufficient for the dynamic reasoning and adaptive
planning required by autonomous agents. By introducing a semantic layer with explicit phases for intention establishment, capability discovery,
collaborative planning, and execution, VACP enables flexible and extensible agent interactions. The transport-agnostic design ensures that VACP can
operate over diverse communication channels without imposing constraints on the underlying infrastructure.

Specification
=============

VACP defines a standardized end-to-end workflow for agent collaboration across vehicle and infrastructure boundaries. The protocol is structured around the
following core phases and components. An on-vehicle coordination agent (VCA) is responsible to drive the protocol execution.

Intention Establishment
_______________________

An intention can be expressed in various form, ranging from natural language expressions to determinstic UI interactions (such as clicking on a specific menu),
to rule-based triggers. Hence, a sophsicated intention parsing and establishment mechanism, such as through generative AI, is not always required. However, an intention must be unambiguous,
self-contained, and verifiable.

Collaborative Planning
______________________

Once an intention is established, the VCA plans for fulfillment of the intention by creating a fulfillment plan. The plan defines the sequence
and assignment of actions across agents, including fallback strategies and contingency handling. Note that VACP doesn't mandate intelligent, dynamic planning,
which allows the whole fulfillment process to be fully determinstic. This allows common scenarios to be solidified and optimized in an offline planning process,
while still allowing for dynamic reasoning and adaptation in more complex scenarios.

Capability Discovery and Exchange
_________________________________

As the fulfillment plan is established, the VCA identifies and assembles required capabilities to fullfill the plan. VCA initiate capability discovery by
broadcasting a capability request or querying a registry. Participating agents respond with capability offers that match the requested criteria, including
both functional and non-functional attributes. VCA evaluates offers based on criteria such as availability, trustworthiness, and compatibility with the
fulfillment plan.
Note the broadcasting is not necessarily implemented as a network broadcast, but can be implemented as a direct request to known registry services with a location-based scope,
or a direct request to known agents in the vicinity. The exact discovery mechanism is not mandated by VACP and can be adapted to the deployment context.

Execution and Monitoring
________________________

VCA exeutes the fulfillment plan by coordinating the involved agents to perform their assigned actions. The protocol includes mechanisms for monitoring execution progress,
detecting faults or deviations, and triggering contingency plans as needed. Human-in-the-loop approval and intervention mechanisms allow for safety-critical actions to
require explicit human approval, and for humans to override or abort.

Security and Trust
__________________

All agent interactions must be authenticated and integrity-protected.
Trust relationships between agents are established through verifiable credentials and attestation mechanisms.
The protocol must support revocation and re-establishment of trust at runtime.

Contextual Awareness
____________________

Agents must maintain and share contextual information relevant to the collaboration, such as environmental conditions,
vehicle state, and infrastructure status.
Context must be timestamped and validated to ensure consistency across collaborating agents.


Requirements
____________

.. note::

   Requirements for this feature are under development.


Backwards Compatibility
=======================

VACP is a new protocol and does not replace existing V2X or service-oriented communication mechanisms.
Integration with existing systems is ensured by the transport-agnostic design, allowing VACP messages to be carried over established communication channels.


Security Impact
===============

VACP introduces new attack surfaces related to inter-agent communication and collaborative decision-making.
The following non-complete list highlights security considerations:

- Agent Authentication
   - All agents must be authenticated before participation in a collaboration session
   - Credentials must be verified and revocable at runtime
- Message Integrity
   - All protocol messages must be integrity-protected to prevent tampering or replay attacks
- Trust Management
   - Trust relationships must be explicitly established and continuously validated
   - Compromised agents must be detectable and isolatable


Safety Impact
=============

VACP is designed to support safety-relevant collaborative scenarios up to ASIL-B.
The following list gives an idea of safety considerations and is not complete. An in-depth safety analysis must be conducted in the future.

- Deterministic Execution
   - Fulfillment plans must be deterministic and reproducible to support safety analysis
- Human-in-the-Loop
   - Safety-critical actions must include human approval and intervention checkpoints
- Fault Handling
   - The protocol must handle agent failures, communication losses, and plan deviations gracefully without compromising safety

License Impact
==============

VACP is expected to be implemented primarily using Free and Open Source Software (FOSS), in alignment with the Eclipse Foundation's licensing principles.

- All new components developed under this feature shall be licensed under the Apache 2.0 License
- No additional licensing constraints are introduced by this feature request beyond those already adopted in S-CORE

How to Teach This
=================

The following sources are recommended for onboarding:

- This feature request document and its linked requirements
- The S-CORE platform documentation for related features such as Communication and AI Platform

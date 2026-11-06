..
   *******************************************************************************
   Copyright (c) 2026 Contributors to the Eclipse Foundation
   *
   * See the NOTICE file(s) distributed with this work for additional
   * information regarding copyright ownership.
   *
   * This program and the accompanying materials are made available under the
   * terms of the Apache License Version 2.0 which is available at
   * https://www.apache.org/licenses/LICENSE-2.0
   *
   * SPDX-License-Identifier: Apache-2.0
   *******************************************************************************

.. _dds_binding_gateway_use_cases:

DDS Binding and Gateway Use Cases
#################################

Supported Use Cases
===================

Direct DDS Binding
------------------

An ``mw::com`` application is deployed with the DDS Binding.

The application uses the standard ``mw::com`` API while the DDS Binding maps
configured events to DDS communication routes.

The DDS stack executes in the DDS Communication Daemon.

Native DDS Interoperability
---------------------------

An ``mw::com`` publisher or subscriber communicates with a compatible native
DDS participant.

Both sides use compatible DDS Domain, Topic, type, and QoS information.

Endpoint-based availability may be used when the native DDS participant does
not provide explicit service-instance state.

LoLa-to-DDS Gateway
-------------------

An existing LoLa producer is connected to DDS through the DDS Gateway.

The Gateway consumes the configured LoLa event using a Generic Proxy,
serializes the sample, and forwards it through runtime IPC to the DDS
Communication Daemon.

DDS-to-LoLa Gateway
-------------------

A DDS sample is received by the DDS Communication Daemon and forwarded through
runtime IPC to the DDS Gateway.

The Gateway deserializes the sample and provides it locally using a Generic
Skeleton.

LoLa-to-LoLa Communication over DDS
-----------------------------------

A LoLa application on one ECU communicates with a LoLa application on another
ECU through DDS Gateways and DDS Communication Daemons.

The applications remain unaware of DDS.

Configure an Existing mw::com Event for DDS
-------------------------------------------

An integrator extends the existing ``mw::com`` deployment information for an
event with the DDS information required to establish communication.

The existing service type, service version, service instance, event, provider,
and consumer information is reused.

DDS-specific deployment information supplements it with:

* DDS Domain selection;
* DDS Topic mapping;
* DDS type information;
* communication direction;
* DDS QoS; and
* service-availability policy where required.

The configured route may be consumed by a DDS Binding deployment or a DDS
Gateway deployment.

Deterministic DDS Topic Mapping
-------------------------------

A configured ``mw::com`` event is mapped unambiguously to a DDS Topic.

The Topic name may be explicitly configured or deterministically derived from
deployment information.

The mapping distinguishes routes where required by service type, version,
instance, event, Domain, or type.

The mapping avoids unintended Topic collisions and ensures that communicating
endpoints use compatible Topic identities.

Externally Defined DDS Topic
----------------------------

A deployment maps an ``mw::com`` event to a DDS Topic whose identity is already
defined by an external DDS system.

The Topic name is explicitly configured rather than derived.

The ``mw::com`` application remains unchanged.

Runtime DDS Type
----------------

A DDS route is created using runtime type information rather than a
DDS-generated interface linked into the application.

The configured type information is sufficient for DDS entity creation,
serialization, deserialization, validation, and interoperability.

Per-Route DDS QoS
-----------------

An integrator assigns DDS QoS to a configured communication route.

Different events or service instances may use different QoS profiles according
to their communication requirements.

The application continues to use the standard ``mw::com`` API and remains
unaware of the DDS QoS configuration.

Reusable DDS QoS Profile
------------------------

Multiple DDS routes refer to the same configured QoS profile.

This allows consistent QoS deployment without repeating policy values for every
route.

Multiple DDS Domains
--------------------

Different configured DDS routes use different DDS Domains.

This enables communication isolation according to deployment needs while
preserving the same ``mw::com`` programming model.

Multiple Applications per Daemon
--------------------------------

A DDS Communication Daemon serves multiple applications using DDS Bindings,
or DDS Gateways.

Each runtime IPC message is associated with a preconfigured communication
route.

Component-Specific Configuration
--------------------------------

A deployment process produces separate, mutually consistent configuration
artifacts for the DDS Binding, DDS Gateway, and DDS Communication Daemon.

Each component receives the information required for its own responsibilities.

Configuration is not distributed through runtime IPC.

DDS Route-State Propagation to Binding
--------------------------------------

The DDS Communication Daemon detects a change in the operational state of a
configured DDS communication route.

The resulting route state is communicated to the DDS Binding.

The DDS Binding evaluates the configured service-availability policy and updates
the corresponding ``mw::com`` availability state.

DDS Route-State Propagation through Gateway
-------------------------------------------

The DDS Communication Daemon detects changes in the operational state of the
DDS communication routes associated with a configured remote service.

The resulting route state is communicated to the DDS Gateway.

The DDS Gateway evaluates the configured service-availability policy and offers
or withdraws the corresponding local LoLa service.

Explicit Service-State Propagation
----------------------------------

A locally provided ``mw::com`` service is offered or withdrawn.

Where explicit service-state propagation is configured, the DDS Binding or DDS
Gateway forwards the local service state to the DDS Communication Daemon.

The daemon propagates this state through a configured DDS communication route.

The receiving side uses the state as an input to its configured
service-availability policy.

Configurable Service-Availability Policy
----------------------------------------

A deployment defines how the availability of a mapped ``mw::com`` service
instance is determined.

The configured policy may use:

* DDS communication-route state;
* explicit service-instance state; or
* both.

For endpoint-based evaluation, the policy identifies the communication routes
that are required before the service instance is considered available.

Configured E2E with Direct Binding
----------------------------------

The DDS Binding applies the configured E2E processing to a DDS route while
exposing binding-independent E2E result semantics to the application.

Configured E2E with Gateway
---------------------------

The DDS Gateway applies the configured E2E processing to the network route.

LoLa E2E processing is disabled for the internal Gateway leg when the Gateway
owns the same E2E profile.

Daemon Restart and Recovery
---------------------------

The DDS Communication Daemon is restarted independently from the application or
Gateway process.

Configured DDS entities and runtime availability are restored according to the
deployment lifecycle and availability policies.

Implementation-Dependent Use Cases
==================================

Dynamic DDS Instances
---------------------

Runtime selection or creation of previously unconfined DDS instances may be
supported by an implementation but is not required by this feature.

Payload Transformation
----------------------

Semantic transformation between different application data models is not
required.

The required use case is representation conversion for compatible configured
types.

Out of Scope
============

The following are outside the scope of this feature request:

* one mandatory DDS Topic naming formula;
* one mandatory representation for explicit service state;
* one mandatory JSON schema;
* runtime modification of DDS deployment configuration through IPC;
* semantic payload transformation;
* automatic universal QoS mapping;
* one IPC connection per Topic;
* one worker or queue per route;
* DDS Security configuration;
* network-layer security;
* TSN configuration;
* application-specific safety decisions; and
* certification of a particular DDS stack.

Rejected or Invalid Configurations
==================================

A DDS route shall not become operational when required configuration is missing,
ambiguous, inconsistent, or unsupported.

Examples include:

* an unknown service type, instance, or event;
* missing DDS type information;
* an event type incompatible with the DDS type;
* an invalid DDS Domain;
* an unsupported QoS policy;
* duplicate or ambiguous Topic mappings;
* conflicting communication directions;
* inconsistent Binding, Gateway, and Daemon route identities;
* a missing external Topic mapping where derivation is disabled;
* an availability policy referencing an unknown communication route; or
* inconsistent availability policies between configured components.

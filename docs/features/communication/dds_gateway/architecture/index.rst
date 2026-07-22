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

.. _dds_binding_gateway_architecture:

DDS Binding and Gateway Architecture
####################################

Overview
========

This feature introduces two DDS integration concepts:

* a DDS Binding beneath ``mw::com``; and
* a DDS Gateway between LoLa and DDS.

The DDS Binding is used when DDS is selected as the communication binding of an
``mw::com`` application.

The DDS Gateway is used when an existing application remains on LoLa and
configured LoLa services shall be forwarded to or received from DDS.

Both deployment concepts reuse the same DDS Communication Daemon.

The DDS Communication Daemon contains the DDS network-facing functionality,
including the selected DDS stack, DDS discovery, DDS Domains, Topics,
DataReaders, DataWriters, and QoS handling.

The DDS Binding and DDS Gateway communicate with the DDS Communication Daemon
through runtime inter-process communication.

This process boundary allows the DDS stack to remain outside the
application-facing process. This is especially relevant when the DDS Binding or
DDS Gateway executes in an ASIL context while the selected DDS stack is
available as a QM component.

Context View
============

The feature supports:

#. Direct DDS Binding deployment.
#. LoLa application with DDS Gateway deployment.

The DDS Gateway is not an additional ``mw::com`` binding.

It is a separately deployed process that communicates with local applications
through LoLa and with the DDS Communication Daemon through runtime IPC.

Direct DDS Binding Deployment
=============================

In this deployment, DDS is selected as the ``mw::com`` communication binding.

The application continues to use the standard ``mw::com`` API.

The DDS Binding performs the application-side adaptation between ``mw::com``
and DDS. The DDS stack remains in the separately deployed DDS Communication
Daemon.

::

   ==============================
               ECU
   ==============================

   +------------------------------------------------+
   | Application Process                            |
   |                                                |
   |  +------------------------------------------+  |
   |  | mw::com Application                      |  |
   |  +--------------------+---------------------+  |
   |                       |                        |
   |                   mw::com API                  |
   |                       |                        |
   |  +--------------------v---------------------+  |
   |  | DDS Binding                              |  |
   |  |                                          |  |
   |  | - mw::com service adaptation             |  |
   |  | - Runtime type handling                  |  |
   |  | - Serialization / deserialization        |  |
   |  | - Route mapping                          |  |
   |  | - Availability-policy evaluation         |  |
   |  | - Configured E2E processing              |  |
   |  +--------------------+---------------------+  |
   +-----------------------|------------------------+
                           |
                           | Runtime IPC
                           v
   +------------------------------------------------+
   | DDS Communication Daemon Process               |
   |                                                |
   | - DDS discovery and endpoint matching          |
   | - Route-state tracking                         |
   | - DDS Domains and Topics                       |
   | - DataReaders / DataWriters                    |
   | - DDS QoS                                      |
   | - DDS stack processing and RTPS message handling                 |
   | - DDS stack abstraction                        |
   | - DDS stack                                    |
   +-----------------------+------------------------+
                           |
                       DDS / RTPS
                           |
                      DDS Network

Direct DDS Binding Responsibilities
-----------------------------------

The DDS Binding is responsible for:

* exposing the standard ``mw::com`` programming model;
* mapping configured ``mw::com`` events to DDS communication routes;
* runtime type handling;
* conversion and serialization between ``mw::com`` samples and the configured
  DDS serialized representation;
* configured E2E Protect and E2E Check processing;
* runtime communication-route handling;
* evaluation of the configured service-availability policy; and
* propagation of the resulting state into the ``mw::com`` availability model.

Gateway Deployment
==================

In this deployment, the application remains configured with the LoLa Binding.

The DDS Gateway is deployed as a separate process.

The Gateway communicates with local applications through LoLa IPC and with the
DDS Communication Daemon through runtime IPC.

::

   ==============================
               ECU
   ==============================

   +------------------------------------------------+
   | Application Process                            |
   |                                                |
   |  +------------------------------------------+  |
   |  | mw::com Application                      |  |
   |  +--------------------+---------------------+  |
   |                       |                        |
   |                   mw::com API                  |
   |                       |                        |
   |  +--------------------v---------------------+  |
   |  | LoLa Binding                             |  |
   |  +--------------------+---------------------+  |
   +-----------------------|------------------------+
                           |
                           | LoLa IPC
                           v
   +------------------------------------------------+
   | DDS Gateway Process                            |
   |                                                |
   | - Generic Proxy / Generic Skeleton             |
   | - LoLa service interaction                     |
   | - Route translation                            |
   | - Runtime type handling                        |
   | - Serialization / deserialization              |
   | - Availability-policy evaluation               |
   | - Configured E2E processing                    |
   +-----------------------+------------------------+
                           |
                           | Runtime IPC
                           v
   +------------------------------------------------+
   | DDS Communication Daemon Process               |
   |                                                |
   | - DDS discovery and endpoint matching          |
   | - Route-state tracking                         |
   | - DDS Domains and Topics                       |
   | - DataReaders / DataWriters                    |
   | - DDS QoS                                      |
   | - DDS stack abstraction and DDS stack          |
   +-----------------------+------------------------+
                           |
                       DDS / RTPS
                           |
                      DDS Network

Gateway Responsibilities
------------------------

The DDS Gateway is responsible for:

* discovering configured local LoLa services;
* creating Generic Proxies for locally provided services;
* creating Generic Skeletons for remotely provided DDS services;
* mapping configured LoLa events to DDS route identifiers;
* mapping received DDS route identifiers to LoLa events;
* runtime type handling;
* conversion and serialization between LoLa samples and the configured DDS
  serialized representation;
* configured E2E Protect and E2E Check processing;
* evaluation of the configured service-availability policy;
* offering or withdrawing mapped local services; and
* forwarding runtime data between LoLa and the DDS Communication Daemon.

Relationship Between DDS Binding and DDS Gateway
================================================

The DDS Binding and DDS Gateway serve different deployment scenarios.

The DDS Binding is part of an application process when DDS is selected as the
application's ``mw::com`` binding.

The DDS Gateway is a separate process used when the application remains on
LoLa.

Both communicate with the same DDS Communication Daemon through runtime IPC.

::

                         +-----------------------------+
                         | DDS Communication Daemon    |
                         |                             |
                         | DDS stack and DDS runtime   |
                         +-------------+---------------+
                                       ^
                                       |
                       IPC             |             IPC
                                       |
                  +--------------------+--------------------+
                  |                                         |
          +-------+--------+                       +--------+-------+
          | DDS Binding    |                       | DDS Gateway    |
          |                |                       |                |
          | Application    |                       | Separate       |
          | process        |                       | process        |
          +----------------+                       +----------------+

The DDS Binding and DDS Gateway may reuse common application-facing
infrastructure, including:

* the daemon communication protocol;
* the route-identification model;
* the serialized data-transfer mechanism;
* runtime type and serialization utilities; and
* the discovery and availability-notification model.

DDS DomainParticipants, Topics, DataReaders, DataWriters, QoS, and the selected
DDS stack are owned and managed only by the DDS Communication Daemon.

DDS Communication Daemon
========================

The DDS Communication Daemon is responsible for:

* integration of the selected DDS stack;
* creation and management of DDS DomainParticipants;
* creation and management of DDS Topics;
* creation and management of DDS DataReaders and DataWriters;
* DDS participant and endpoint discovery;
* DDS endpoint matching;
* tracking configured communication-route state;
* transmission and reception of explicit service state where configured;
* DDS QoS handling;
* submission and reception of serialized DDS samples;
* runtime IPC notifications;
* resource management; and
* reporting DDS-related runtime errors.
The DDS Communication Daemon may serve:

* multiple applications using the DDS Binding;
* the DDS Gateway process; or
* a combination of DDS Binding applications and the DDS Gateway.

::

   Application A / DDS Binding --\
                                  \
   Application B / DDS Binding ----+--> DDS Communication Daemon
                                  /
   DDS Gateway -------------------/

Configuration Model
===================

The DDS integration extends the existing ``mw::com`` deployment configuration
model.

Existing ``mw::com`` service-type and service-instance information remains the
basis of the application-facing model.

DDS-specific deployment information supplements it with:

* DDS Domain;
* DDS Topic;
* DDS data type;
* communication direction;
* DDS QoS;
* service-availability policy; and
* optional E2E information.

The DDS Binding, DDS Gateway, and DDS Communication Daemon may consume separate
but mutually consistent configuration artifacts.

Configuration is not exchanged through runtime IPC.

DDS Communication Route
-----------------------

A configured DDS communication route associates an existing ``mw::com`` event
with the corresponding DDS communication information.

The configuration shall provide sufficient information to identify:

* the ``mw::com`` service type;
* the service version;
* the service instance;
* the event;
* the DDS Domain;
* the DDS Topic;
* the DDS data type;
* the communication direction; and
* the applicable DDS QoS.

The configuration may additionally provide information for service-availability
evaluation, explicit service-state communication, E2E handling, and
communication prioritization.

Event-to-Topic Mapping
----------------------

Each ``mw::com`` event configured for DDS communication is mapped to a DDS
Topic.

The mapping shall be deterministic and unambiguous.

The Topic name may be explicitly configured or derived according to an
implementation-defined deterministic convention.

This feature request does not prescribe one mandatory Topic naming convention.

DDS Type Configuration
----------------------

Each DDS-enabled ``mw::com`` event shall reference sufficient runtime type
information for:

* DDS entity creation;
* serialization;
* deserialization;
* compatibility validation; and
* native DDS interoperability.

The ``mw::com`` application itself is not required to use a DDS-generated API.

DDS Domain Configuration
------------------------

Each DDS communication route shall be associated with a DDS Domain identifier.

Different configured routes may use different DDS Domains.

DDS QoS Configuration
---------------------

The DDS deployment information shall provide the QoS required by each
configured communication route.

The supported QoS policies depend on the selected DDS stack and implementation.

Component-Specific Configuration
--------------------------------

The DDS Binding may require:

* application-facing event-to-route mapping;
* runtime type information;
* serialization and deserialization information;
* route identification;
* service-availability policy;
* E2E configuration; and
* application-facing availability mapping.

The DDS Gateway may require:

* LoLa-to-DDS and DDS-to-LoLa routes;
* Generic Proxy and Generic Skeleton deployment information;
* runtime type information;
* route identification;
* service-availability policy and mapping; and
* E2E configuration.

The DDS Communication Daemon may require:

* DDS Domain configuration;
* DDS Topic identities;
* DDS type information;
* endpoint direction;
* QoS configuration;
* explicit service-state route information where configured; and
* identifiers associating IPC traffic with configured DDS entities.

Configuration Validation
------------------------

Invalid or inconsistent deployment information shall be detected before the
affected route or availability policy becomes operational.

Validation shall include, where applicable:

* unresolved service types, instances, or events;
* missing or incompatible DDS type information;
* invalid DDS Domain or QoS configuration;
* duplicate or ambiguous Topic mappings;
* conflicting route definitions;
* missing communication direction;
* invalid service-availability policies;
* references to unknown availability routes; and
* inconsistent component-specific configuration.

Runtime IPC
===========

Runtime IPC carries:

* serialized DDS payloads;
* communication-route identifiers;
* communication-route state notifications;
* local and remote service-instance state;
* lifecycle notifications; and
* runtime errors.

Runtime IPC does not carry deployment configuration.

The IPC protocol, message format, buffer mechanism, and IPC technology are
implementation-specific.

Why IPC Is Used
===============

The DDS Binding or DDS Gateway may execute in an ASIL context while the selected
DDS stack is available as a QM component.

The DDS Communication Daemon creates a process boundary between the
application-facing communication component and the DDS stack.

The complete freedom-from-interference argument remains deployment-specific.

Data Flow Overview
==================

DDS Binding Publish
-------------------

::

   mw::com Application
          |
          v
   DDS Binding
          |
          | conversion and serialization
          | configured E2E Protect
          v
   Runtime IPC
          |
          v
   DDS Communication Daemon
          |
          v
      DDS Network

DDS Binding Receive
-------------------

::

      DDS Network
          |
          v
   DDS Communication Daemon
          |
          v
   Runtime IPC
          |
          v
   DDS Binding
          |
          | configured E2E Check
          | deserialization
          v
   mw::com Application

Gateway Publish
---------------

::

   Local mw::com Producer
          |
          v
   DDS Gateway Generic Proxy
          |
          | conversion and serialization
          | configured E2E Protect
          v
   Runtime IPC
          |
          v
   DDS Communication Daemon
          |
          v
      DDS Network

Gateway Receive
---------------

::

      DDS Network
          |
          v
   DDS Communication Daemon
          |
          v
   Runtime IPC
          |
          v
   DDS Gateway
          |
          | configured E2E Check
          | deserialization
          v
   Generic Skeleton / LoLa IPC
          |
          v
   Local mw::com Consumer

Discovery and Availability
==========================

DDS discovery is performed only by the DDS Communication Daemon through the DDS
stack.

The daemon tracks configured DDS communication-route state and communicates
relevant changes through runtime IPC.

The DDS Binding or DDS Gateway evaluates the configured service-availability
policy.

The policy may use route state, explicit service-instance state, or both.

Detailed behavior is defined in
:ref:`dds_binding_gateway_service_discovery`.

E2E Considerations
==================

The DDS Binding or DDS Gateway performs configured application-level E2E
processing on the serialized application-data representation.

The DDS Communication Daemon transports the serialized payload and does not
perform E2E Protect, E2E Check, or application-specific acceptance decisions.

Detailed E2E behavior is defined in
:ref:`dds_binding_gateway_e2e`.

Implementation Considerations
=============================

This architecture does not prescribe:

* the internal IPC protocol;
* the number of IPC channels;
* the queue or worker model;
* the shared-memory layout;
* the buffer-allocation strategy;
* the configuration-file format;
* the configuration-generation mechanism;
* the Topic naming convention;
* one mandatory representation for explicit service state;
* DDS entity-creation time; or
* the selected DDS stack.

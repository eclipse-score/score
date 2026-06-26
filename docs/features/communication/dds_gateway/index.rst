..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

DDS Binding and Gateway
=======================

.. document:: DDS-Gateway
   :id: doc__dds_gateway
   :status: valid
   :safety: ASIL_B
   :tags: contribution_request, feature_request
   :security: YES
   :realizes: wp__feat_request


Overview
--------
This feature introduces DDS communication support for ``mw::com`` and a
reference DDS Gateway implementation.

DDS communication is provided as a binding beneath ``mw::com``. This allows
applications to use the ``mw::com`` abstraction while the communication is
transported over a DDS network, based on the service and deployment
configuration selected by the integrator.

In addition, the DDS Gateway provides a reference translation concept between
local ``mw::com (LoLa)`` communication and DDS-based inter-ECU communication.
It enables controlled and configurable data exchange between intra-ECU
``mw::com (LoLa)`` participants and DDS-based systems while preserving
existing application implementations.

Architecture Concept
--------------------

The DDS feature supports two integration concepts:

- Direct DDS binding usage beneath ``mw::com``
- Reference DDS Gateway based translation

Direct DDS Binding Concept
~~~~~~~~~~~~~~~~~~~~~~~~~~
In this concept, an application uses the regular ``mw::com`` API and service
definition. The integrator selects DDS as the communication binding through
the service/deployment configuration. The application does not directly use
DDS APIs, but its communication is transported over the DDS network.

::

   ==============================        ==============================
              ECU 1                              ECU 2
   ==============================        ==============================

   +-------------------------+           +-------------------------+
   |     Application A       |           |     Application B       |
   |        (mw::com)        |           |        (mw::com)        |
   +-----------+-------------+           +-----------+-------------+
               |                                     ^
               | mw::com API                         | mw::com API
               v                                     |
       +---------------------+               +---------------------+
       |   DDS Binding       |               |   DDS Binding       |
       | beneath mw::com     |               | beneath mw::com     |
       +----------+----------+               +----------+----------+
                  |                                     ^
                  | DDS                                 | DDS
                  v                                     |
         ===================   DDS NETWORK   ===================

The DDS binding provides the DDS communication layer beneath ``mw::com``.
It is responsible for runtime type handling, runtime serialization and
deserialization, creation of DDS communication entities, conversion between
``mw::com`` samples and DDS runtime data representation, DDS communication
routing, QoS configuration, and interaction with the underlying DDS stack.

In DDS, a Topic represents a named communication channel associated with a
specific data type.The DDS binding maps ``mw::com`` events to DDS Topics and creates the
required DDS Topics, DataReaders and DataWriters from the deployment
configuration. DDS Domains provide communication isolation and may be used to separate
communication routes (for example, QM and ASIL communication).

Applications continue to use the standard ``mw::com`` programming model,
while the selected binding transports the data over DDS.
The application programming model remains unchanged. Publishers and subscribers
continue to allocate and populate typed ``mw::com`` samples, while the DDS
binding performs the conversion to the DDS data representation and interacts
with the underlying DDS stack.

Reference DDS Gateway Concept
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The DDS Gateway is a reference implementation that demonstrates one possible
translation concept between local ``mw::com (LoLa)`` communication and DDS
domains. In this concept, the applications continue to use ``mw::com (LoLa)``
locally, while the gateway performs the translation and routing to DDS.

::

   ==============================        ==============================
              ECU 1                              ECU 2
   ==============================        ==============================

   +-------------------------+           +-------------------------+
   |     Application A       |           |     Application B       |
   |   (mw::com LoLa)        |           |   (mw::com LoLa)        |
   +-----------+-------------+           +-----------+-------------+
               |                                     ^
               |  mw::com (LoLa - IPC)               | mw::com (LoLa - IPC)
               v                                     |
       +---------------------+               +---------------------+
       |     DDS Gateway     |               |     DDS Gateway     |
       |       (ECU 1)       |               |       (ECU 2)       |
       +----------+----------+               +----------+----------+
                  |                                     ^
                  |                                     |
                  v                                     |
         ===================   DDS NETWORK   ===================
                  |                                     ^
      ==============================                    |
               ECU 3                                    |
      ==============================                    |
                  |                                     |
                  v                                     |
       +---------------------+                          |
       |   DDS Application   |--------------------------+
       |     (optional)      |
       +---------------------+

The reference DDS Gateway is one such implementation built on top of the 
DDS communication binding. The binding architecture also supports deployment 
solutions without an explicit gateway process.

Each DDS Gateway instance connects to:

- Local ``mw::com (LoLa)`` participants (IPC binding)
- A DDS domain for inter-ECU communication

The gateway is responsible for:

- Translating between ``mw::com (LoLa)`` and DDS communication
- Managing configurable translation routes
- Applying End-to-End (E2E) protection
- Scheduling translation through configurable worker queues (e.g., Mailbox and Queue policies)

Scope
-----

This feature provides:

DDS Communication Binding
~~~~~~~~~~~~~~~~~~~~~~~~~

The DDS communication binding provides DDS communication beneath ``mw::com``.

It provides:

- Communication between ``mw::com`` applications over DDS using the standard
  ``mw::com`` programming model

- Configuration-driven mapping between ``mw::com`` and DDS:

  - Each ``mw::com`` event is mapped to one DDS Topic
  - DDS Topic data is mapped back to the corresponding ``mw::com`` event
  - DDS deployment configuration extends the ``mw::com`` deployment
    configuration with DDS-specific attributes such as runtime type references,
    QoS policies and DDS Domain IDs
  - Standard DDS endpoint discovery is used to determine the availability of
    configured DDS endpoints and map this to the ``mw::com`` availability model

- Support for configurable DDS domain-based routing
- Runtime type definition via configuration (e.g. JSON) or dynamic library
- Runtime creation of DDS entities (Topics, DataReaders and DataWriters)
- Runtime conversion between ``mw::com`` raw memory samples and the DDS runtime
data representation using runtime type definitions
- Runtime serialization and deserialization performed by the DDS binding using
configured runtime type definitions
- Support for standard DDS serialization encodings (e.g. XCDR1 and XCDR2)
- True zero-generation workflow with no dependency on DDS IDL generation
- Per-route DDS Quality of Service (QoS) configuration
- Pluggable DDS stack implementations via defined abstract interfaces,
  isolating DDS-stack-specific APIs from the DDS communication binding

Reference DDS Gateway
~~~~~~~~~~~~~~~~~~~~~

The DDS Gateway is the reference implementation for translating between
``mw::com (LoLa)`` and DDS.

It provides:

- Bridging between ``mw::com (LoLa)`` and DDS:
   - ``mw::com (LoLa)`` → DDS GW → ``mw::com (LoLa)``
   - ``mw::com (LoLa)`` → DDS GW → DDS applications
   - DDS applications → DDS GW → ``mw::com (LoLa)``

- End-to-End (E2E) protection:
  - The translation layer performs generation and validation of Counter, CRC, and DataID
  - Independent of the underlying DDS stack implementation
  - Validation and protection configurable per route

- Execution and performance model:

  - Asynchronous processing using internal worker queues
  - Support for configurable priority-based routing
  - High-priority routes can be processed with dedicated queues and worker pools
  - Normal-priority routes are handled via standard processing queues


Motivation
----------

S-CORE currently focuses on local communication via ``mw::com (LoLa)`` but does
not provide a standardized mechanism for inter-ECU communication using DDS-based
systems.

In mixed middleware environments:

- ``mw::com`` does not provide a standardized DDS communication binding
- Different projects implement DDS integration using project-specific solutions
- Integration with DDS requires project-specific bindings or adapters
- Applications may need to embed DDS-specific logic, reducing abstraction
- Communication with native DDS applications is not standardized
- Inter-ECU communication between ``mw::com`` participants via DDS is not standardized
- Multi-domain DDS deployments are difficult to configure consistently


This feature addresses these challenges by introducing a reusable DDS
communication binding beneath ``mw::com`` together with a reference DDS
Gateway implementation.

The DDS binding provides standardized DDS communication for ``mw::com``
applications, while the reference gateway demonstrates one possible approach
for translating between local ``mw::com (LoLa)`` communication and DDS-based
communication.

Key Value
---------

- Standardized DDS communication support through an ``mw::com`` binding
- Reference DDS Gateway implementation for ``mw::com (LoLa)`` to DDS translation
- Supports multiple integration concepts through a common DDS communication layer
- DDS-stack-independent runtime type handling through a common abstraction layer
- Direct interoperability with native DDS applications
- Standardized inter-ECU communication between ``mw::com`` participants via DDS

- Performance and determinism:

  - Low-latency processing for high-priority data flows
  - Controlled execution via configurable worker queues
  - Predictable behavior for mixed criticality communication

- Interoperability across heterogeneous systems:

  - Enables communication between systems with different architectures
    (e.g., 32-bit / 64-bit, different endianness)
  - Ensures consistent data representation via Dynamic Type handling

- End-to-End (E2E) protection:
  - The translation layer performs generation and validation of Counter, CRC, and DataID
  - Independent of the underlying DDS stack implementation
  - Validation and protection configurable per route

Reference
---------

The detailed Feature Request is available here:

- DDS Gateway Feature Request: https://github.com/eclipse-score/score/issues/2726

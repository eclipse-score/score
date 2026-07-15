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
In this concept, an application uses the regular ``mw::com`` API.The integrator selects DDS as 
the communication binding through the service/deployment configuration. 
The application does not directly use DDS APIs, but its communication is transported over the DDS network.

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

Communication is established by mapping mw::com events to DDS Topics.
In DDS, a Topic represents a named communication channel associated with a
specific data type.Based on the deployment configuration, the DDS binding
creates the required DDS Topics, DataReaders and DataWriters. DDS Domains
provide communication isolation and may be used to separate communication
routes (for example, QM and ASIL communication).

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

The DDS Gateway is a reference deployment concept for translating between
local ``mw::com (LoLa)`` communication and DDS-based communication.

A gateway deployment may separate the functionality responsible for local
``mw::com`` interaction from the functionality responsible for DDS stack
interaction.

::

   +-------------------------+
   | Local mw::com           |
   | Applications            |
   +------------+------------+
                |
                | mw::com (LoLa)
                v
   +--------------------------------------------+
   | Gateway Component                          |
   |                                            |
   | - Local service model                      |
   | - Runtime type handling                    |
   | - Runtime Serialization / Deserialization  |
   | - E2E processing                           |
   +------------+-------------------------------+
                |
                | IPC
                v
   +--------------------------------+
   | DDS Communication              |
   | Component                      |
   |                                |
   | - DDS discovery                |
   | - DDS Topics                   |
   | - DDS QoS                      |
   | - DDS Stack interaction        |
   | - DDS publication and          |
   |    subscription of serialized  |
   |    payloads                    |
   +------------+-------------------+
                |
                | DDS
                v
        ==================
           DDS NETWORK
        ==================

This separation allows deployments where DDS stack interaction is isolated
from local application interaction while preserving the standard
``mw::com (LoLa)`` programming model for local applications.

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
- DDS endpoint and service discovery:
     - Standard DDS discovery mechanisms are used to discover matching
       DDS endpoints.
     - Service availability is derived from the DDS endpoints associated
       with a configured service instance.
     - DDS endpoint availability is mapped to the corresponding
       ``mw::com`` availability model.
     - Availability changes resulting from DDS participant join, leave,
       restart, or recovery are propagated through the ``mw::com`` availability model.
- Support for configurable DDS domain-based routing
- Runtime type definition via configuration (e.g. JSON) or dynamic library
- Runtime creation of DDS entities (Topics, DataReaders and DataWriters)
- Runtime conversion between ``mw::com`` raw memory samples and the DDS runtime data representation using runtime type definitions
- Runtime serialization and deserialization performed by the DDS binding usingconfigured runtime type definitions
- Support for standard DDS serialization encodings (e.g. XCDR1 and XCDR2)
- No dependency on DDS-stack-specific IDL-generated application interfaces
- Runtime type definitions and E2E-related configuration may be generated
  or manually maintained as part of the deployment configuration
- Per-route DDS Quality of Service (QoS) configuration
- Pluggable DDS stack implementations via defined abstract interfaces,isolating DDS-stack-specific APIs from the DDS communication binding

Reference DDS Gateway
~~~~~~~~~~~~~~~~~~~~~

The DDS Gateway is the reference implementation for translating between
``mw::com (LoLa)`` and DDS.

It provides:

- Bridging between ``mw::com (LoLa)`` and DDS:
   - ``mw::com (LoLa)`` → DDS GW → ``mw::com (LoLa)``
   - ``mw::com (LoLa)`` → DDS GW → DDS applications
   - DDS applications → DDS GW → ``mw::com (LoLa)``

- Service availability propagation:

  - DDS endpoint discovery is performed by ``DDS Communication Component`` for the DDS Topics
    associated with a configured service route.

  - The gateway configuration maps the discovered DDS Topics and endpoints to
    the events of the corresponding ``mw::com`` service instance.

  - Service availability is derived from the configured DDS Topics associated
    with the service instance.

  - Once the endpoints required for all configured DDS Topics are available,
    ``DDS Communication Component`` exposes the corresponding inter-daemon route to ``Gateway Component``.

  - ``Gateway Component`` offers the corresponding local ``mw::com`` service only after
    the inter-daemon route and the required DDS communication path are
    available.

  - Loss of a required DDS endpoint causes ``DDS Communication Component`` to withdraw the
    inter-daemon route. ``Gateway Component`` then withdraws the corresponding local
    ``mw::com`` service availability.

  - Availability is restored automatically when the required DDS endpoints
    and the inter-daemon communication route become available again.

::

   +------------------------------------------------------------+
   |                       DDS NETWORK                          |
   +------------------------------------------------------------+
          |                    |                    |
          | Topic A            | Topic B            | Topic C
          | discovered         | discovered         | discovered
          v                    v                    v

   +------------------------------------------------------------+
   |              DDS Communication Component                   |
   |                                                            |
   |  DDS endpoint discovery                                    |
   |  Topic-to-service mapping                                  |
   |                                                            |
   |  All configured service events available?                  |
   +--------------------------+---------------------------------+
                              |
                              | Yes
                              |
                              | Offer inter-daemon route
                              v

   ==================== mw::com (LoLa IPC) =====================

   +------------------------------------------------------------+
   |                       Gateway Component                    |
   |                                                            |
   |  Discover inter-daemon route                               |
   |  Establish event subscriptions                             |
   |                                                            |
   |  Offer local mw::com service                               |
   +--------------------------+---------------------------------+
                              |
                              |
                              v

   +------------------------------------------------------------+
   |              Local mw::com Application                     |
   +------------------------------------------------------------+

   Availability loss propagates in the reverse direction:

   DDS endpoint lost
        -> DDS Communication Component withdraws route
        -> Gateway Component StopOfferService()
        -> local service unavailable
- End-to-End (E2E) protection:

  - E2E protection is implemented by the gateway translation layer and is
    independent of the selected DDS stack implementation.

  - E2E generation and validation are performed by ``Gateway Component``.
    ``DDS Communication Component`` and the DDS stack transport the resulting payload without
    interpreting the E2E protection information.

  - E2E protection is configurable per communication route.

  - Routes may be configured with or without E2E protection according to
    deployment requirements.

  - E2E protection information, including Counter, CRC, and DataID related
    information, is associated with the application payload representation used for translation and is independent of DDS or RTPS transport headers.

  - The E2E representation is defined through configuration associated with
    the runtime type description of the mapped ``mw::com`` event and DDS Topic.

  - Runtime type information may be provided through configuration or a
    dynamically loaded type description.

  - No DDS-stack-specific IDL generated application interfaces are required
    for E2E processing.

- For outgoing communication:

  - ``Gateway Component`` reads the sample using the configured runtime type.

  - ``Gateway Component`` updates Counter, CRC, DataID and other configured
    E2E elements.

  - ``Gateway Component`` serializes the payload using the configured runtime
    type representation.

  - The serialized payload is forwarded to the
    ``DDS Communication Component``.

  - The ``DDS Communication Component`` publishes the serialized payload
    through the DDS stack.

- For incoming communication:

  - The ``DDS Communication Component`` receives the serialized DDS payload.

  - The serialized payload is forwarded to the
    ``Gateway Component``.

  - ``Gateway Component`` performs deserialization using the configured
    runtime type representation.

  - ``Gateway Component`` validates the configured E2E information before
    delivering the sample to the local application.

  - Samples failing E2E validation are handled according to the configured
    route policy.

::

    Outgoing direction

    +----------------------------+
    | Local mw::com Sample       |
    +-------------+--------------+
                  |
                  v
    +----------------------------+
    | Gateway Component          |
    |                            |
    | Runtime type handling      |
    | Update Counter             |
    | Update CRC                 |
    | Update DataID              |
    | Serialize payload          |
    +-------------+--------------+
                  |
                  | Serialized payload
                  v

    ================= LoLa IPC =================

                  |
                  v

    +-------------------------------+
    | DDS Communication Component   |
    |                               |
    | DDS discovery                 |
    | DDS Topics                    |
    | DDS write_cdr()               |
    +-------------+-----------------+
                  |
                  v

              DDS NETWORK


    Incoming direction

              DDS NETWORK
                  |
                  v

    +-------------------------------+
    | DDS Communication Component   |
    |                               |
    | DDS read_cdr()                |
    +-------------+-----------------+
                  |
                  | Serialized payload
                  v

    ================= LoLa IPC =================

                  |
                  v

    +----------------------------+
    | Gateway Component          |
    |                            |
    | Deserialize payload        |
    | Validate Counter           |
    | Validate CRC               |
    | Validate DataID            |
    +-------------+--------------+
                  |
                  v

    +----------------------------+
    | Local mw::com Sample       |
    +----------------------------+

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


Reference
---------

The detailed Feature Request is available here:

- DDS Gateway Feature Request: https://github.com/eclipse-score/score/issues/2726

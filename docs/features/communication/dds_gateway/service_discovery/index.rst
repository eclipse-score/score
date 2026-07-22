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

.. _dds_binding_gateway_service_discovery:

DDS Service Discovery and Availability
######################################

Overview
========

DDS and ``mw::com`` provide different communication abstractions.

DDS discovers communication participants and compatible communication
endpoints (DataReaders and DataWriters). Applications using ``mw::com``,
however, interact with service instances rather than individual DDS endpoints.

A mapped ``mw::com`` service instance may contain multiple events, where each
event is mapped to an independent DDS communication route. Consequently, the
availability of a service instance cannot always be inferred directly from the
discovery state of a single DDS endpoint.

To bridge this semantic difference, this feature defines how DDS runtime
information is mapped to the ``mw::com`` service-availability model.

The feature introduces configurable service-availability policies that derive
the availability of a mapped ``mw::com`` service instance from DDS runtime
information while preserving standard DDS discovery.

The resulting service availability is then exposed to applications through the
standard ``mw::com`` programming model.

Service-Availability Policy
===========================

DDS endpoint discovery and ``mw::com`` service availability are distinct
concepts.

DDS discovery provides runtime information about DDS communication endpoints.

The DDS Binding or DDS Gateway derives the availability of each mapped
``mw::com`` service instance according to a configured availability policy.

This specification defines the following availability policies:

* Endpoint-Based Availability
* Explicit Service Availability

Future specifications may define additional availability policies without
changing the DDS discovery mechanism described by this feature.

Availability policies derive application-level service availability. They do
not introduce an additional DDS discovery mechanism.

Endpoint-Based Availability
---------------------------

Endpoint-Based Availability derives the availability of a mapped
``mw::com`` service instance from the operational state of its configured DDS
communication routes.

A DDS communication route represents one configured communication path between
an ``mw::com`` event and a DDS Topic. A mapped ``mw::com`` service instance may
therefore depend on multiple DDS communication routes.

The DDS Communication Daemon performs standard DDS participant and endpoint
discovery through the selected DDS stack. For every configured communication
route, the daemon determines whether the required compatible remote DDS
endpoint is discovered and matched.

A communication route becomes operational when the required compatible remote
DDS endpoint is discovered and matched. It becomes non-operational when, for
example:

* the corresponding remote DataWriter or DataReader is removed;
* the remote DDS participant disappears;
* a previously matched endpoint becomes unmatched; or
* another configured DDS runtime condition invalidates the route.

The DDS Communication Daemon reports every communication-route state change to
the DDS Binding or DDS Gateway through runtime IPC.

The DDS Binding or DDS Gateway maintains the current operational state of all
routes associated with each mapped ``mw::com`` service instance. Whenever a
route state changes, the Endpoint-Based Availability policy is evaluated using
the current state of all required routes.

During initial discovery, routes may become operational one by one. The mapped
service remains unavailable until all routes required by the configured policy
are operational. No withdrawal action is performed while the service is already
unavailable.

When all required routes become operational, the service state changes from
unavailable to available. The DDS Binding or DDS Gateway exposes the mapped
service through the standard ``mw::com`` service-discovery mechanism.

After the service has become available, if any required route becomes
non-operational, the service state changes from available to unavailable. The
DDS Binding or DDS Gateway withdraws the mapped service through the standard
``mw::com`` service-discovery mechanism.

Endpoint-Based Availability with DDS Binding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following diagram shows the transition from unavailable to available after
all required DDS communication routes have been discovered and matched.

::

       Remote DDS Application
       ----------------------
       Topic A       Topic B       Topic C
          |             |             |
          | DDS endpoint discovery and matching
          v             v             v
       +-----------------------------------+
       |     DDS Communication Daemon      |
       |-----------------------------------|
       | Route A: operational              |
       | Route B: operational              |
       | Route C: operational              |
       +-----------------+-----------------+
                         |
                         | route-state changes
                         | through runtime IPC
                         v
       +-----------------------------------+
       |           DDS Binding             |
       |-----------------------------------|
       | Current state for Service X       |
       |                                   |
       | Route A: operational              |
       | Route B: operational              |
       | Route C: operational              |
       +-----------------+-----------------+
                         |
                         | evaluate Endpoint-Based
                         | Availability policy
                         v
       +-----------------------------------+
       | All required routes operational   |
       |                                   |
       | Service state transition:         |
       | UNAVAILABLE -> AVAILABLE          |
       +-----------------+-----------------+
                         |
                         | expose mapped service through
                         | mw::com service discovery
                         v
       +-----------------------------------+
       |        mw::com Application        |
       |-----------------------------------|
       |           Service available       |
       |                                   |
       +-----------------------------------+

The following diagram shows the transition from available to unavailable when
a previously operational required route disappears or becomes unmatched.

::

       Remote DDS Application
       ----------------------
       Topic A       Topic B       Topic C
          |             X             |
          |       Topic B removed     |
          |       or endpoint lost    |
          v                           v
       +-----------------------------------+
       |     DDS Communication Daemon      |
       |-----------------------------------|
       | Route A: operational              |
       | Route B: non-operational          |
       | Route C: operational              |
       +-----------------+-----------------+
                         |
                         | Route B state changed:
                         | operational -> non-operational
                         | through runtime IPC
                         v
       +-----------------------------------+
       |           DDS Binding             |
       |-----------------------------------|
       | Current state for Service X       |
       |                                   |
       | Route A: operational              |
       | Route B: non-operational          |
       | Route C: operational              |
       +-----------------+-----------------+
                         |
                         | re-evaluate Endpoint-Based
                         | Availability policy
                         v
       +-----------------------------------+
       | A required route is unavailable   |
       |                                   |
       | Service state transition:         |
       | AVAILABLE -> UNAVAILABLE          |
       +-----------------+-----------------+
                         |
                         | withdraw mapped service from
                         | mw::com service discovery
                         v
       +-----------------------------------+
       |        mw::com Application        |
       |-----------------------------------|
       |         service unavailable       |
       |                                   |
       +-----------------------------------+

Endpoint-Based Availability with DDS Gateway
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following diagram shows the transition from unavailable to available after
all required DDS communication routes have been discovered and matched.

::

       Remote DDS Application
       ----------------------
       Topic A       Topic B       Topic C
          |             |             |
          | DDS endpoint discovery and matching
          v             v             v
       +-----------------------------------+
       |     DDS Communication Daemon      |
       |-----------------------------------|
       | Route A: operational              |
       | Route B: operational              |
       | Route C: operational              |
       +-----------------+-----------------+
                         |
                         | route-state changes
                         | through runtime IPC
                         v
       +-----------------------------------+
       |           DDS Gateway             |
       |-----------------------------------|
       | Current state for Service X       |
       |                                   |
       | Route A: operational              |
       | Route B: operational              |
       | Route C: operational              |
       +-----------------+-----------------+
                         |
                         | evaluate Endpoint-Based
                         | Availability policy
                         v
       +-----------------------------------+
       | All required routes operational   |
       |                                   |
       | Service state transition:         |
       | UNAVAILABLE -> AVAILABLE          |
       +-----------------+-----------------+
                         |
                         | Generic Skeleton
                         | OfferService()
                         v
       +-----------------------------------+
       |        mw::com Application        |
       |-----------------------------------|
       |           Service available       |
       |                                   |
       +-----------------------------------+

The following diagram shows the transition from available to unavailable when
a previously operational required route disappears or becomes unmatched.

::

       Remote DDS Application
       ----------------------
       Topic A       Topic B       Topic C
          |             X             |
          |       Topic B removed     |
          |       or endpoint lost    |
          v                           v
       +-----------------------------------+
       |     DDS Communication Daemon      |
       |-----------------------------------|
       | Route A: operational              |
       | Route B: non-operational          |
       | Route C: operational              |
       +-----------------+-----------------+
                         |
                         | Route B state changed:
                         | operational -> non-operational
                         | through runtime IPC
                         v
       +-----------------------------------+
       |           DDS Gateway             |
       |-----------------------------------|
       | Current state for Service X       |
       |                                   |
       | Route A: operational              |
       | Route B: non-operational          |
       | Route C: operational              |
       +-----------------+-----------------+
                         |
                         | re-evaluate Endpoint-Based
                         | Availability policy
                         v
       +-----------------------------------+
       | A required route is unavailable   |
       |                                   |
       | Service state transition:         |
       | AVAILABLE -> UNAVAILABLE          |
       +-----------------+-----------------+
                         |
                         | Generic Skeleton
                         | StopOfferService()
                         v
       +-----------------------------------+
       |        mw::com Application        |
       |-----------------------------------|
       |                                   |
       |         service unavailable       |
       +-----------------------------------+


Explicit Service Availability
-----------------------------

Explicit Service Availability derives the availability of a mapped
``mw::com`` service instance from an explicit availability indication
provided by a remote DDS Binding or DDS Gateway.

Unlike Endpoint-Based Availability, this policy does not derive
application-level availability only from the discovery state of DDS
communication endpoints.

Instead, the explicit availability indication represents the lifecycle state
of the remotely provided ``mw::com`` service instance.

For example, the indication may represent that the remotely provided service
has become available or unavailable.

The mechanism used to exchange the explicit availability indication is
implementation-specific.

The following details are therefore not prescribed by this feature:

* the DDS Topic used to carry the indication;
* the data representation;
* the DDS QoS;
* the mapping between service instances and availability indications;
* the runtime IPC representation; and
* the internal availability state machine.

The DDS Communication Daemon receives the explicit availability indication and
reports the resulting availability change to the DDS Binding or DDS Gateway
through runtime IPC.

The DDS Binding or DDS Gateway then exposes or withdraws the corresponding
mapped service through the standard ``mw::com`` service-discovery mechanism.

This policy allows ``mw::com`` service availability to follow the lifecycle of
the remote provider independently of the discovery state of the DDS data
endpoints.

Explicit Service Availability with DDS Binding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a service is provided through a DDS Binding, the provider-side Binding
observes the lifecycle of the locally provided ``mw::com`` service instance.

When the local service becomes available or unavailable, the provider-side
Binding propagates the corresponding explicit availability indication through
the DDS Communication Daemon.

The receiving DDS Communication Daemon reports the indication to the
consumer-side DDS Binding.

The consumer-side DDS Binding then exposes or withdraws the corresponding
mapped ``mw::com`` service instance.

The consuming application observes the resulting availability change through
the standard ``mw::com`` service-discovery mechanism.

::

       Provider ECU                              Consumer ECU
       ============                              ============

 +--------------------------+             +--------------------------+
 | Provider mw::com         |             | Consumer mw::com         |
 | Application              |             | Application              |
 |                          |             |                          |
 | Local service lifecycle  |             | Observes mapped service  |
 | state                    |             | availability             |
 +------------+-------------+             +-------------^------------+
              |                                             |
              | local mw::com service                       |
              | lifecycle                                   |
              v                                             |
 +--------------------------+             +--------------------------+
 | Provider DDS Binding     |             | Consumer DDS Binding     |
 +------------+-------------+             +-------------^------------+
              |                                             |
              | explicit availability                       |
              | state through runtime IPC                   |
              v                                             |
 +--------------------------+             +--------------------------+
 | DDS Communication Daemon |             | DDS Communication Daemon |
 +------------+-------------+             +-------------^------------+
              |                                             |
              | implementation-specific explicit            |
              | service-availability mechanism              |
              +---------------- DDS ------------------------+
                                                            |
                                                            |
                                            expose or withdraw mapped
                                            mw::com service instance

The explicit availability indication and the DDS event data may use
independent communication mechanisms and independent DDS Topics.

Explicit Service Availability with DDS Gateway
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a locally provided ``mw::com`` service is forwarded through a DDS Gateway,
the provider-side Gateway observes the lifecycle of the local service through
its Generic Proxy.

When the local service becomes available or unavailable, the provider-side
Gateway forwards the corresponding explicit availability indication to the DDS
Communication Daemon.

On the receiving ECU, the DDS Communication Daemon reports the explicit
availability indication to the consumer-side DDS Gateway.

The consumer-side DDS Gateway then exposes or withdraws the corresponding
mapped service through its Generic Skeleton.

The consuming application observes the resulting availability change through
the standard ``mw::com`` service-discovery mechanism.

::

       Provider ECU                              Consumer ECU
       ============                              ============

 +--------------------------+             +--------------------------+
 | Provider mw::com         |             | Consumer mw::com         |
 | Application              |             | Application              |
 |                          |             |                          |
 | Local service lifecycle  |             | Observes mapped service  |
 | state                    |             | availability             |
 +------------+-------------+             +-------------^------------+
              |                                             |
              | local mw::com communication                 |
              v                                             |
 +--------------------------+             +--------------------------+
 | DDS Gateway              |             | DDS Gateway              |
 |                          |             |                          |
 | Generic Proxy observes   |             | Generic Skeleton exposes |
 | local service lifecycle  |             | or withdraws mapped      |
 |                          |             | service instance         |
 +------------+-------------+             +-------------^------------+
              |                                             |
              | explicit availability                       |
              | state through runtime IPC                   |
              v                                             |
 +--------------------------+             +--------------------------+
 | DDS Communication Daemon |             | DDS Communication Daemon |
 +------------+-------------+             +-------------^------------+
              |                                             |
              | implementation-specific explicit            |
              | service-availability mechanism              |
              +---------------- DDS ------------------------+

The consuming application therefore observes the lifecycle of the remote
provider through the standard ``mw::com`` service-discovery mechanism.

Native DDS Interoperability
===========================

Native DDS applications typically participate only in standard DDS endpoint
discovery and do not provide application-level service-availability
information.

Endpoint-Based Availability enables interoperability with native DDS
applications by deriving ``mw::com`` service availability from standard DDS
endpoint discovery without requiring an additional DDS protocol or
application-level availability information.

Responsibility Split
====================

DDS Communication Daemon
------------------------

The DDS Communication Daemon is responsible for:

* performing DDS participant and endpoint discovery;
* creating and managing the required DDS communication entities;
* maintaining the runtime state of configured DDS communication routes;
* mapping DDS endpoint state to configured communication-route identifiers;
* receiving and transmitting explicit service-availability indications, where
  configured;
* reporting communication-route and explicit availability changes through
  runtime IPC; and
* restoring DDS runtime state following restart or communication recovery.

The DDS Communication Daemon does not expose ``mw::com`` services directly to
applications.

DDS Binding
-----------

The DDS Binding is responsible for:

* associating daemon notifications with configured ``mw::com`` service
  instances;
* evaluating the configured availability policy;
* offering or withdrawing the mapped ``mw::com`` service instance;
* exposing the resulting availability through the standard ``mw::com``
  service-discovery API;
* observing the lifecycle of locally provided ``mw::com`` services; and
* forwarding local service-availability changes where Explicit Service
  Availability is configured.

Applications using the DDS Binding continue to use the standard ``mw::com``
API.

DDS Gateway
-----------

The DDS Gateway is responsible for:

* associating daemon notifications with configured Generic Skeleton service
  instances;
* evaluating the configured availability policy;
* calling ``OfferService()`` or ``StopOfferService()`` on the corresponding
  Generic Skeleton;
* observing locally provided services through the corresponding Generic Proxy;
  and
* forwarding local service-availability changes where Explicit Service
  Availability is configured.

The DDS Gateway exposes remotely provided DDS services to local applications
through the standard LoLa and ``mw::com`` service-discovery mechanisms.

Configuration
=============

The deployment configuration shall provide sufficient information to determine
the availability behavior of every mapped ``mw::com`` service instance.

This may include:

* the mapped service type and service instance;
* the DDS communication routes associated with the service instance;
* the availability policy associated with the mapped service instance;
* the communication routes participating in the availability decision;
* the communication routes used to exchange Explicit Service Availability,
  where configured; and
* deployment-specific policy parameters.

The DDS Communication Daemon, DDS Binding and DDS Gateway may consume separate
configuration artifacts.

These artifacts shall define mutually consistent communication-route
identifiers and availability policies.

The exact configuration schema is implementation-specific.

Startup and Data Handling
=========================

DDS communication may become operational before the corresponding local
application-facing communication path is ready.

The implementation shall define bounded handling for samples received during
this interval.

Possible strategies include:

* delaying DDS reception;
* bounded buffering;
* retaining only the latest sample;
* using configured DDS durability and history;
* dropping samples until the local communication path becomes available; or
* another bounded deployment-specific strategy.

Unlimited buffering is not required.

Implementation Considerations
=============================

This feature request does not prescribe:

* one mandatory availability policy;
* one mandatory DDS Topic for Explicit Service Availability;
* the binary representation of Explicit Service Availability;
* the QoS associated with Explicit Service Availability;
* DDS entity creation time;
* the runtime IPC protocol;
* the internal state-machine representation;
* polling versus callback-based implementations;
* one startup buffering strategy; or
* fixed discovery or availability timeout values.

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

   # #914 Feature Request for SOME/IP Gateway

.. _some_ip_gateway_feature:

SOME/IP-Gateway
###########################

.. document:: SOME_IP-Gateway
   :id: doc__some_ip_gateway
   :status: valid
   :safety: ASIL_B
   :tags: contribution_request, feature_request


.. toctree::
   :hidden:

   architecture/index.rst
   requirements/index.rst
   service_discovery/index.rst


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_some-ip-gateway``

Abstract
========

This contribution describes how data-exchange that is outside the scope of internal communication (IPC) shall be handled in modules that service data-input and data-output to a platform.
Services handling data in this context can be considered as gateways.
The focus is on a gateway to handle SOME/IP communication with external devices or counterparts, therefore this feature request is called: SOME/IP-Gateway

This feature request includes:
  - A description of how a SOME/IP gateway service (or data broker) shall be implemented
  - How the SOME/IP gateway services shall integrate with the zero-copy communication from IPC
  - How data shall be mapped or translated between SOME/IP protocol and IPC communication
  - How service discovery should be integrated, also for services that are offered by IPC-Clients
  - How End-to-End protection and checking shall be realized

.. _Motivation:

Motivation
==========

S-CORE is targeting high-performance automotive systems with safety impact. Applications integrated on S-CORE will be distributed across multiple processes and frameworks (like FEO)
that schedule software components (i.e. activities) with the need to exchange data.
For data-exchange between applications the IPC feature is providing high-speed communication capabilities, but when it comes to communication with applications outside the scope of
the S-CORE platform, services are required that will handle protocols for communication with both side. This is for instance the case when communication with rest of vehicle or sensors
needs to be realized with the SOME/IP protocol.

For software component developers it should be unrecognized that data is originated from a SOME/IP communication channel, the data should be provided with the same API as in IPC.
Nonetheless integrators and architects will have to configure the system to receive or send data over SOME/IP.


.. _Rationale:

Rationale
==========

SOME/IP and IPC use different mechanisms and data representations to communicate. Therefor it's not only a task of this gateway
to adapt the communication, but also to transform from one representation to another. This includes changing data layout, filling in missing data, filtering traffic, error handling, service discovery and further steps.

Hence the gateway shall be a transparent bridge between IPC and SOME/IP. On the one side it should act as a participant in IPC and fulfill all requirements to this accordingly, where providing data or consuming it.
Whereas on the other side it shall participate in SOME/IP communication acting as a SOME/IP service and client fulfilling all SOME/IP requirements and defined communication.
Between these two contexts developers shall be able to create signal or data mappings and translate the different data-types and representations of the two contexts.


This module shall fulfill the following requirements:
 - Multi-Binding support - :need:`feat_req__com__multi_binding_support`
 - binding agnostic API - :need:`feat_req__com__binding_agnostic_api`
 - deployment configuration - :need:`feat_req__com__multi_binding_depl`


.. _Specification:

Specification
=============

The requirements from Communication generally apply to the SOME/IP Gateway.


SOME/IP protocol implementation
-------------------------------

The protocol implementation shall be fully compatible and complying with the SOME/IP specification from AUTOSAR Adaptive. (:need:`feat_req__some_ip_gateway__someip_protocol`)
Specifically the SOME/IP specification from AUTOSAR release R24-11 shall be supported by the SOME/IP Gateway. This shall guarantee that systems integrated with the SOME/IP gateway can be used in according
automotive E/E-architectures.
Protocol implementations shall be wrapped in an abstraction API, that stays stable and allows implementations may be exchanged, potentially even by binary only libraries.

The SOME/IP Gateway shall support SOME/IP Events, Fields and Methods and shall map these accordingly into IPC.

The SOME/IP Gateway shall support SOME/IP Service Discovery. Please refer to the Service Discovery page for detailed discussions on how SD shall be realized with IPC-Clients.

..
   # fix #1424 SOME/IP Gateway in lifecycle-management

SOME/IP Gateway processes and life cycle management
---------------------------------------------------

The implementation of a gateway likely requires using one or multiple processes. Startup of processes for the gateway, as with any other
process in the S-CORE system, need to be put under the control of lifecycle-management (see feature Lifecycle).
Hence the SOME/IP Gateway must not start any processes on its own, but configure the lifecycle launch and health-monitoring accordingly.
Specifically for the integration of the SOME/IP Stack "plug-in", which is expected to be QM, whereas the rest of the gateway is ASIL-B,
if one or more additional processes need to be spawned and additional executables need to be involved with the implementation,
all need to go into launch control in health monitoring and must not be setup (fork()) by the gateway.



SOME/IP Gateway Security Goals
------------------------------

The security approach for SOME/IP gateway shall achieve the following security goals:

- access control (:need:`feat_req__com__acl_per_service_instance`)

The SOME/IP Gateway service instance shall be defined in the deployment configuration.

- :need:`ACL Placement <feat_req__com__acl_placement>`


Backwards Compatibility
=======================

As there is currently no previous solution for gateways in S-CORE, no backwards compatibility is required.
Subsequent changes to the SOME/IP gateway module shall keep the API stable where possible and introduce breaking APIs only with approval from tech lead circle.
Applications shall stay stable on API layer, need to recompile is acceptable.

Security Impact
===============

Be aware, communication with SOME/IP generally is considered to be not secure. Integrators may apply measures that are outside the
scope of the SOME/IP gateway to secure the communication (IPsec, MACsec, ...).

.. note::
   it is expected that a feature request for crypto and security will cover the necessary measures.
   `Feature Request for Security & Crypto <https://github.com/eclipse-score/score/issues/905>`_


Access Control List (ACL)
-------------------------

The gateway shall only forward selective service instances originating from IP addresses configured in an allow-list.
The logic required for this is protocol specific and therefore part of this feature request.

Be aware that an additional security mechanism may be necessary that ensures that IP addresses are not forged. This mechanism is out of scope of this feature.

An access control mechanism is part of a firewall solution, which states that only the traffic defined in the security policy is allowed onto the network and all other traffic must be silently dropped.
Access Control acts on OSI Layer 5-7. It shall fulfill the following:

- What SOME/IP service instances to forward
- What IP address is allowed to offer a SOME/IP service instance
- Configuration of ACL is done at deployment
- Versioning of services
- ACL, or single parameters of it, shall be able to be switched on/off
- It shall be possible to persistently log ACL drop actions

.. note::
  - Checking SOME/IP-SD messages with the ACL is optional because no functional data is transported.
  - SOME/IP-SD messages are not protected as per AUTOSAR Adaptive specification.


.. uml::
   :name: doc__acl_activity_diagram
   :scale: 80
   :align: center
   :caption: Simplified Access Control Activity Diagram

   !include assets/puml-theme-score.puml

   start

   :Ingress SOME/IP;
   :ACL Check;

   if (Packet matches ACL entry?) then (Yes)
      :Process Packet;
   else (No)
      :Log Event;
      if (ACL is active?) then (Yes)
         :Drop Packet;
      else (No)
         :Process Packet;
      endif
   endif

   stop


Safety Impact
=============

SOME/IP stack and underlying OS network stacks are typically QM only. Freedom from interference needs to be respected between the
safety classified IPC component (mw::com) and the SOME/IP stack which is part of the gateway. The SOME/IP communication itself needs
to be properly protected by E2E to maintain a safe communication via the grey SOME/IP channel.

End-to-End (E2E) protection with CRC and counters
-------------------------------------------------

Applications communicating over the network may have to protect data with end-to-end protection (E2E), which may involve
CRC-protection and checks, and message counters.

There are several E2E (= End-to-End) profiles, which utilize various CRC routines as part of AUTOSAR E2E Protocol Specification, that shall be supported with the SOME/IP Gateway.

Though the implementation of the SOME/IP protocol itself is likely not going to be ASIL-B compliant and have a safety consideration of QM rather,
E2E-checks and protection need to happen in an ASIL-B context. The gateway may perform the CRC routines as a central service.
All communication channels (IPC) to this central service must be qualified for ASIL-B, and protected against data loss / loss of samples.

SOME/IP Events, Methods, and Fields need to be supported with E2E protection.

Please refer to the SOME/IP Gateway architecture for further details.

References

- `AUTOSAR_FO_PRS_E2EProtocol <https://www.autosar.org/fileadmin/standards/R24-11/FO/AUTOSAR_FO_PRS_E2EProtocol.pdf>`_
- `AUTOSAR_FO_RS_E2E <https://www.autosar.org/fileadmin/standards/R24-11/FO/AUTOSAR_FO_RS_E2E.pdf>`_

License Impact
==============

[How could the copyright impacted by the license of the new contribution?]

Since SOME/IP is a protocol, including applied E2E protection and the according profile (polynom, etc.),
defined by AUTOSAR and published under the license of AUTOSAR, the gateway implementation shall carefully distinguish between the SOME/IP communication stack,
the E2E protection of data, and the integration into S-CORE mw::com. Breach of foreign licenses must be avoided.

Anybody using SOME/IP Gateway needs to make sure to follow the license conditions and rules of AUTOSAR.

How to Teach This
=================

TBD

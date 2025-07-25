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
  - How the SOME/IP gateway services shall integrate with the zero-copy communication from IPC (which might become a general description of how services plug-in to the IPC context)
  - How data shall be mapped or translated between SOME/IP protocol and IPC communication

.. _Motivation:

Motivation
==========

S-CORE is targeting high-performance automotive systems with safety impact. Applications integrated on S-CORE will be distributed across multiple processes and frameworks (like FEO)
that schedule software components (i.e. activities) with the need to exchange data.
For data-exchange between applications the IPC feature is providing high-speed communication capabilities, but when it comes to communication with applications outside the scope of
the S-CORE platform, services are required that will handle protocols for communication with both side. This is for instance the case when communication with rest of vehicle or sensors
needs to be realized with the SOME/IP protocol.

For software component developers it should be unrecognized that data is originated from a SOME/IP communication channel, the data should be provided with the same API as in IPC.
Nonetheless integrators and architects will have to configure the system to receive or send data over SOME/IP, hence provide it as a SOME/IP service.


.. _Rationale:

Rationale
==========

SOME/IP and IPC use different mechanisms to communicate on different channels. Applications integrating on S-CORE platform may have certain requirements to data-input that is not directly supported with SOME/IP and vice versa
SOME/IP definition may have requirements that cannot directly be supported by the application providing data on IPC. Therefor it's not only a task of this gateway
to adapt the communication, but also to translate data between the two communication channels and probably even fill data, i.e. when applications require new data that has not be received on SOME/IP or vice versa.

Hence the gateway on the one side should act as a participant in IPC and fulfill all requirements to this accordingly, whereas on the other side it shall participate in SOME/IP communication
acting as a SOME/IP service fulfilling all SOME/IP requirements and defined communication. Between these two contexts developers shall be able to create signal or data mappings and
translate the different data-types and representations of the two contexts.

The SOME/IP side shall, where possible, use an existing SOME/IP stack that is fully compatible and complying with the SOME/IP specification from AUTOSAR Adaptive.

This module shall fulfill the following requirements:
 - Multi-Binding support - :need:`feat_req__com__multi_binding_support`
 - agnostic binding - :need:`feat_req__com__binding_agnostic_api`
 - deployment configuration - :need:`feat_req__com__multi_binding_depl`


.. _Specification:

Specification
=============

SOME/IP Gateway protocol implementation
---------------------------------------

The protocol implementation shall be fully compatible and complying with the SOME/IP specification from AUTOSAR Adaptive.
Specifically the SOME/IP specification from AUTOSAR release 24-11 shall be supported by the SOME/IP Gateway. This shall guarantee that systems integrated with the SOME/IP gateway can be used in
Protocol implementations shall be wrapped in an abstraction API, that stays stable and allows implementations may be exchanged, potentially even by binary only libraries.



SOME/IP Gateway Security Goals
------------------------------

As with IPC generally, the security approach for SOME/IP gateway shall achieve the following security goals:

- confidentiality (:need:`feat_req__ipc__confidentiality`)
- integrity (:need:`feat_req__ipc__integrity`)
- availability (per criticality-level) (:need:`feat_req__ipc__availability`)


Backwards Compatibility
=======================

As there is currently no previous solution for communication in S-CORE, no backwards compatibility is required.
Subsequent changes to the SOME/IP gateway module shall keep the API stable where possible and introduce breaking APIs only with approval from tech lead circle.
Applications shall stay stable on API layer, need to recompile is acceptable.

Security Impact
===============

As the SOME/IP gateway will open direct communication channels on the SOME/IP channels, the SOME/IP implementation shall comply with standard security requirements.

Safety Impact
=============

SOME/IP stack and underlying OS network stacks are typically QM only. Freedom from interference needs to be respected between the
safty classified IPC component (mw::com) and the SOME/IP stack which is part of the gateway. The SOME/IP communication itself needs
to be properly protected by E2E to maintain a safe communication via the grey SOME/IP channel.

License Impact
==============

[How could the copyright impacted by the license of the new contribution?]


How to Teach This
=================

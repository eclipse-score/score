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
- secure communication (:need:`feat_req__some_ip_gateway__secure_com`)
- access control (:need:`feat_req__some_ip_gateway__access_control`)


Backwards Compatibility
=======================

As there is currently no previous solution for communication in S-CORE, no backwards compatibility is required.
Subsequent changes to the SOME/IP gateway module shall keep the API stable where possible and introduce breaking APIs only with approval from tech lead circle.
Applications shall stay stable on API layer, need to recompile is acceptable.

Security Impact
===============

There are multiple protocols targeting secure communication. In general a holistic security concept for a vehicle will not apply all together.

.. figure:: assets/some_ip_gateway_sec_protocols.drawio.svg
   :align: center
   :name: some_ip_gateway_sec_protocols_

   Secure communication protocols


.. note::
   Access Control List (ACL) is not a security protocol, but a mechanism to restrict access to the SOME/IP Gateway services and tylically allocated within the stateful packet inspection firewall.

Scope
-----

As the SOME/IP gateway will open direct communication channels via SOME/IP, where the SOME/IP implementation shall comply with standard security requirements.

Since SOME/IP is a protocol relies on the security of the underlying transport layer, the SOME/IP gateway makes use of the security features relevant for it. This includes:

- VLAN (= Virtual Local Area Network): A virtual interface that separates ethernet network packets identified by a VLAN ID
- MACsec: Provides L2 data Integrity, Authenticity and optionally Confidentiality for point-to-point communication.
- IPsec: A network layer protocol suite that secures network connections by encrypting and/or authenticating IP packets.
- TLS (= Transport Layer Security): Authentication, integrity, confidentiality of TCP channels -> Protection for one to one communication.
- DTLS (= Datagram Transport Layer Security): Authentication, integrity, confidentiality of UDP packets -> Protection for multicast communication.
- ACL (= Access Control List): A filter mechanism to ensure that only allowed SOME/IP communication can take place.

Features included `Feature Request for Security & Crypto <https://github.com/eclipse-score/score/issues/905>`_ e.g cryptographic algorithms, symmetric-, asymmetric encryption, Signature functionality, Certificate management, certificate management, entropy generation, data integrity, key management, are out of scope.


Access Control List
-------------------

An access control mechanism is part of a firewall solution, which states that only the traffic defined in the security policy is allowed onto the network and all other traffic must be silently dropped.
Access Control acts on OSI Layer 5-7. It shall fulfill following:

- Whitelisting of SOME/IP services and methods based on IP addresses and therefore IP address authenticity.
- A static list which could be updated via OTA (= Over-The-Air) updates.
- Versioning
- ACL shall be able to be switched on/off to allow bypassing in an secured environment e.g. engineering mode or repair shop.
- ACL drop actions shall be logged persistently via a DTC (= Diagnostic Trouble Code) including needed environment data to clearly understand the context of the drop, including the sender, timestamp, Service ID and Instance ID.
- To avoid code injection attacks, into services of the system, only authenticated and authorized communication partners are allowed to write or delete entries into the **Service Registry**.

.. note::
  - Checking SOME/IP-SD messages with the ACL is optional because no functional data is transported.
  - SOME/IP-SD messages are not protected as per AUTSAR Adaptive specification.


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


E2E and CRC (Informal Notes)
----------------------------

There are several E2E (= End-to-End) profiles, which utilize various CRC routines as part of AUTOSAR E2E Protocol Specification:

- CRC8 (SAEJ1850)
- CRC8H2F (0x2F polynomial)
- CRC16 (also known as CCITT-FALSE 16-bit CRC)
- CRC32 (also known as IEEE 802.3 Ethernet 32-bit CRC)
- CRC32P4 (0xF4ACFB13 polynomial)
- CRC64 (CRC-64-ECMA)
- CRC32_J1939 (0x6938392D polynomial) (used by Profile 76).

These routines can be implemented using different calculation methods:

- Table based calculation for faster execution, but requiring a larger code size due to ROM tables.
- Runtime calculation for smaller code size (no ROM table), but resulting in slower execution.
- Hardware supported CRC calculation (device-specific) for fast execution and less CPU time.

The E2E Library itself does not provide CRC routine implementations, instead, it calls the CRC routines from a dedicated CRC library.
It is also a requirement that the CRC used in an E2E profile must be different from the CRC used by the underlying physical communication protocol.

All E2E profiles can be used in combination with SOME/IP, although specific profiles may have limitations regarding maximum data length or being restricted to fixed-length messages.

For E2E protection with SOME/IP, the CRC is calculated over specific parts of the serialized SOME/IP message:

- For profiles 1, 2, 4, 5, 6, 7, 11, and 22, which are typically used for signal-based or periodic event-based communication, the E2E CRC should be calculated over the following elements of the serialized SOME/IP message:

  - Request ID (Client ID / Session ID)
  - Protocol Version
  - Interface Version
  - Message Type
  -  Return Code
  - Payload

- For profiles 4m, 7m, 8m, and 44m, which are designed for method-based (client-server) communication, the E2E CRC shall be calculated over specific parts of the serialized SOME/IP message. These method-specific profiles incorporate additional fields like Message Type and Message Result within their E2E headers to distinguish between request and response messages and their outcomes.

The E2E communication protection process involves the sender adding control fields, including the CRC, to the transmitted data, and the receiver then evaluating these fields upon reception.
The middleware, is responsible for determining parameters like DataID, Message Type, Message Result, and SourceID from the exchanged information and then invoking the E2E functions.
The CRC is calculated over the entire E2E header (excluding the CRC bytes themselves) and the user data.
For some profiles (e.g., Profile 5, 6, 22), the Data ID is included as an extension at the end of the user data for CRC calculation, even if it is not explicitly transmitted.


References

- `AUTOSAR_FO_PRS_E2EProtocol <https://www.autosar.org/fileadmin/standards/R24-11/FO/AUTOSAR_FO_PRS_E2EProtocol.pdf>`_
- `AUTOSAR_FO_RS_E2E <https://www.autosar.org/fileadmin/standards/R24-11/FO/AUTOSAR_FO_RS_E2E.pdf>`_

SecOC (Informal Notes)
----------------------

- The SecOC protocol provides a mechanism to verify the authenticity and integrity but lacks of confidentiality.
- SecOC (= Secured Onboard Communication) does not offer encryption support by design.
- In contrast to SecOC, TLS can protect all payload of an AUTOSAR PDU including the AUTOSAR PDU header used which overlaps with the SOME/IP message header.
- In case of SOME/IP protocol, the SOME/IP message id can not be protected by SecOC, because it is stripped before SecO is invoked.


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

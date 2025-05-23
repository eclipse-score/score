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

.. _diagnostics_feature:

Diagnostic and Fault Management
###############################

.. document:: Diagnostics
   :id: doc__diagnostics
   :status: draft
   :safety: QM
   :tags: feature_request


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_diagnostics``


Abstract
========

We propose adding support for Vehicle Diagnostics via Service-Oriented Vehicle Diagnostics (SOVD) within S-CORE.
SOVD offers a service-oriented, self-descriptive interface based on standardized RESTful APIs,
eliminating the need for manually modeling diagnostic interfaces as required in UDS.
This significantly reduces integration overhead and simplifies the onboarding of new ECUs.
Additionally, SOVD enables scalable, secure, and cloud-ready diagnostics with real-time fault access and
advanced data handling across platforms. Integrating SOVD into S-CORE will enhance developer efficiency,
improve system maintainability, and support future-proof diagnostic workflows.

The intent of this feature request is to define a high-level architecture for the diagnostic system.
The components listed throughout this document require detailed feature requests in the future respectively.


Motivation
==========

Currently there is no solution for vehicle diagnostics in S-CORE.
Diagnostic is a core capability of automotive platform stacks and is required for various use-cases
such as field troubleshooting, quality assurance, after sales, production, development and more.


Rationale
=========

SOVD was chosen as the foundation for the diagnostic architecture because it offers a modern,
service-oriented approach that aligns with the industry's shift toward Ethernet-based communication and scalable software-defined vehicle platforms.
It provides a standardized and extensible interface that enables better interoperability across ECUs, testers, and external tools.


Specification
=============


Architecture
------------

The proposed concept consists of three main parts:

1.	A framework agnostic library to aggregate faults and integrate the diagnostic system into S-CORE
2.	A SOVD based diagnostic system
3.	Components to interface the diagnostic system with the outside – e.g. Tester or UDS based ECUs

The diagram below shows the entire concept with the three subgroups connected.

.. image:: _assets/score-diagnostics-draft.drawio.svg
   :alt: Diagnostic stack component architecture


In scope components
-------------------

The following components are considered in scope of this feature request.

Fault Library

- Provides a framework agnostic interface for apps or FEO activities to report faults - called "Fault API" in the S-CORE architecture.
- Relays faults via IPC to central Diagnostic Fault Manager.
- Enables domain-specific error logic (e.g. debouncing) by exposing a configuration interface
- Reporting of faults additionally results in a log entry.
- The interface needs to be specified further but will likely include: Fault ID (FID), time, ENUM fault type (like DLT ENUMs), optional meta data.
- Fault lib is the base for activity specific, custom fault handling.

Diagnostic Fault Manager

- Aggregates and manages diagnostic fault data from Fault libs across the system.
- Provides centralized fault status to the SOVD Server.
- Interfaces with the Diagnostic DB (persistency) to store and retrieve data.
- Stores (persistently) central configuration (e.g. for debouncing thresholds) which can be loaded during startup by Fault libs.

Diagnostic DB

- Stores static and runtime diagnostic data
- Is considered in scope due to the domain specific data format but internally uses S-CORE::Persistency.
- The data format needs to be specified further but will likely include:
- Diagnostic Trouble Code (DTC): OEM specific code, relevant for end-user.
- Fault ID (FID): ECU specific ID to uniquely identify every fault.
- Count: occurrence count of DTC/fault.
- Meta data: meta data related to fault occurrence.

SOVD Server

- Central entry point for all diagnostic requests via SOVD.
- Implements the SOVD API and dispatches requests to services, DB, and fault manager.
- Manages authentication, configuration, and data access via IPC.

Service App

- Is a base concept to extend the system with system-specific diagnostic services/routines (e.g. DTC clear, ECU reset, Flash Master).
- Interfaces with the SOVD Server via IPC.

SOVD Gateway

- Forwards SOVD requests to appropriate backend targets (e.g. adapters, proxies, clients).
- Acts as a router between clients and distributed SOVD components.
- Supports multi-ECU SOVD communication.

SOVD Client

- Off-board, on-board or cloud client that initiates diagnostics via SOVD protocol.
- Can be used by developers, testers, ECUs or cloud services; should be deployment agnostic.
- Handles access control on the client side – e.g. by providing relevant certificates.

Classic Diagnostic Adapter

- Translates SOVD service calls to UDS commands.
- Enables backward compatibility with legacy ECUs that only support UDS.
- Configured via ODX files describing ECU-specific UDS expectations.

UDS2SOVD Proxy

- Exposes selected SOVD functionality via UDS for backward-compatible testers.
- Acts as a local translation layer between UDS clients and SOVD stack.
- Configured via ODX files to define what is exposed.


Out of scope components
-----------------------

The following components are out of scope for this feature request but are included for context.
Each one is briefly described to illustrate its role within the overall system architecture and
to highlight any resulting requirements or constraints imposed by the diagnostic system design.

Logging

- Enables the Fault Library to log fault events.

Configuration Manager

- Provides configuration data to the SOVD Server (e.g. ECU layout, variant, parameters).
- Enables parametrization of applications.

Authentication Manager

- Manages authentication and authorization for incoming SOVD requests.
- Ensures only valid users or clients can access services.

Crypto

- Provides cryptographic services – e.g. securely store and retrieve diagnostic certificates.
- Used by Authentication Manager.

Persistency

- Provides persistent data storage.

Flash Service App

- Specialized extension of the Service App to handle ECU flashing.
- Provides routines for software update/bootloader access via diagnostics.

Rest of Vehicle UDS

- Represents legacy ECUs in the vehicle that only speak UDS.
- Interact via the Classic Diagnostic Adapter (SOVD2UDS).

Rest of Vehicle SOVD

- Other ECUs in the vehicle that already support SOVD natively.
- Can communicate directly with the SOVD Gateway.

UDS Tester

- Traditional diagnostics tester that uses UDS protocol.
- Communicates with the UDS2SOVD Proxy for limited diagnostics access.


Requirements
------------

The following section includes unordered and incomplete feature requirements.

.. feat_req:: SOVD Standard
   :id: feat_req__diagnostics__sovd_std
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__dtc_read_sovd
   :status: valid

   The SOVD implementation shall conform to the SOVD standard as defined in ISO/DIS 17978 (or the latest available draft or final publication).

.. feat_req:: OEM Diagnostic Plug In
   :id: feat_req__diagnostics__oem_plugin
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__dtc_read_sovd
   :status: valid

   The diagnostic system shall provide a plug-in mechanism to include OEM-specific features.

.. feat_req:: Diagnostic system internal communication
   :id: feat_req__diagnostics__internal_com
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__dtc_read_sovd
   :status: valid

   All internal communication between diagnostic components that do not use UDS or SOVD protocols shall be implemented using the S-CORE::COM middleware.


Backwards Compatibility
=======================

UDS2SOVD Proxy and Classic Diagnostic Adapter (SOVD2UDS) ensure compatibility with legacy UDS systems.
ODX as a standardized exchange format further ensures compatibility with proprietary diagnostic data models.


Security Impact
===============

The introduction of a SOVD based diagnostic stack has significant security implications due to its capabilities and network-based communication model.
Diagnostics inherently allow access to system information, state manipulation, coding, and software updates - all of which pose risks if accessed by unauthorized actors.
SOVD, based on REST, includes modern security features such as HTTPS and token-based authentication,
but also introduces a broader attack surface compared to traditional UDS, which relies on more isolated, session-based access.
If improperly secured, diagnostic interfaces could be exploited to trigger unauthorized routines or inject malicious software.
This may enable new threat scenarios and attack paths, particularly over external or less trusted networks.
To mitigate these risks, the diagnostic stack shall enforce secure communication via HTTPS,
authenticate endpoints using certificates (see architecture diagram), and implement strict access control mechanisms.
While diagnostics do not directly impact functional safety, a successful attack could indirectly influence safety-relevant functions
- for example by setting the system into a different state.
Therefore, the overall security architecture must be revisited in detail to assess and mitigate potential risks introduced by the SOVD integration.


Safety Impact
=============

At this point in time no direct safety impact is foreseen. The expected ASIL level is QM.
Configuration Management could have a safety impact but is handled in another feature request and out of scope of this document.
As pointed out in "Security Impact", a breach in the diagnostic system could theoretically effect safety-relevant functions
- for example by setting the system into a different state.


License Impact
==============

There are no license restrictions preventing the implementation of an open-source SOVD stack at this time.
While SOVD is currently in the ISO standardization process (ISO/DIS 17978) [#s1]_, the relevant parts - especially Part 3,
which defines the API - are already publicly available for purchase as Draft International Standards (DIS).
These drafts are considered stable and are typically subject only to minor editorial changes before final publication.
As such, referencing the current DIS versions is sufficient for implementation purposes, and does not pose any legal or license-related risk.
Once the final ISO standard is published, the delta to the current drafts is expected to be minimal and can be easily addressed.

The license impact regarding publication of XML schemata to handle/convert ODX files as per ISO 22901 needs to be evaluated.


How to Teach This
=================

A good starting point to get an overview of SOVD is the overview pages provided by ISO [#s1]_ and ASAM [#s2]_.


Rejected Ideas
==============

An UDS first based diagnostic system was considered but rejected.
The current market trend clearly indicates the move towards SOVD.
Additionally, there a multiple well established proprietary UDS stacks and tools available.
Because no FOSS SOVD stack exists currently, it presents an opportunity for S-CORE to provide value and increase adoption.


Open Issues
===========

-	Interfacing concept with Autosar Adaptive Diagnostic Stack for mixed stacks and/or a transitional phase
-	Investigate synergies between Configuration Manager and central diagnostic configuration file in Diagnostic Fault Manager
-	Evaluate publication of XML schemata to handle/convert ODX files as per ISO 22901


Footnotes
=========

.. [#s1] "SOVD Standard ISO/DIS 17978", ISO, https://www.iso.org/standard/85133.html.
.. [#s2] "ASAM SOVD Overview", ASAM, https://www.asam.net/standards/detail/sovd.

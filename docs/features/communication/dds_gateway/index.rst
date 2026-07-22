..
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

.. _dds_binding_gateway_feature:

DDS Binding and Gateway
#######################

.. document:: DDS Binding and Gateway
   :id: doc__dds_binding_gateway
   :status: valid
   :safety: ASIL_B
   :tags: contribution_request, feature_request
   :security: YES
   :realizes: wp__feat_request


.. toctree::
   :hidden:

   architecture/index.rst
   requirements/index.rst
   service_discovery/index.rst
   e2e/index.rst
   use_cases/index.rst


Feature Flag
============

To activate this feature, use the implementation-specific DDS Binding or DDS
Gateway feature configuration.


Abstract
========

This feature introduces DDS communication into the ``mw::com`` ecosystem
through two complementary deployment concepts:

* DDS Binding beneath ``mw::com``; and
* DDS Gateway between LoLa and DDS.

The DDS Binding allows applications to use DDS while preserving the standard
``mw::com`` concepts.

The DDS Gateway enables existing LoLa-based applications to communicate with
DDS without changing their application-facing API.

Both deployment concepts reuse a common DDS Communication Daemon containing the
selected DDS stack and DDS network-facing functionality.

The DDS Binding or DDS Gateway communicates with the DDS Communication Daemon
through runtime IPC, allowing deployments where the application-facing
communication component executes in an ASIL context while the DDS stack remains
a QM component.


Motivation
==========

DDS is widely used in automotive systems requiring scalable publish-subscribe
communication, configurable Quality of Service (QoS), runtime discovery, and
interoperability with native DDS participants.

Applications using ``mw::com`` shall remain independent of the selected
communication technology.

This feature therefore introduces DDS support while preserving the existing
``mw::com`` programming model.

The feature provides:

* DDS Binding beneath ``mw::com``;
* DDS Gateway for existing LoLa applications;
* runtime DDS type handling;
* configuration-driven mapping between ``mw::com`` events and DDS Topics;
* configurable DDS Domains and QoS;
* configurable service availability mapping;
* configurable End-to-End (E2E) processing; and
* architectural separation between the application-facing communication
  component and the DDS stack where required by the deployment safety concept.


Rationale
=========

DDS Binding and DDS Gateway address different deployment scenarios.

The DDS Binding provides native DDS communication beneath ``mw::com`` while
preserving the existing application programming model.

The DDS Gateway enables existing LoLa deployments to communicate with DDS
and vice-versa where DDS application communicate with LoLa applications
without changing their configured communication binding.

Both deployment concepts reuse the same DDS Communication Daemon and DDS stack
integration.

DDS-specific deployment information extends the existing ``mw::com`` deployment
model with DDS Topics, runtime type information, Domains, QoS, communication
routes, availability policies, and E2E configuration.


Specification
=============

The DDS Binding and DDS Gateway specification consists of the following
chapters.

Architecture
------------

The Architecture chapter describes:

* DDS Binding deployment;
* DDS Gateway deployment;
* DDS Communication Daemon;
* configuration model;
* communication routes;
* Topic mapping;
* runtime type handling;
* QoS configuration; and
* runtime data flow.

Requirements
------------

The Requirements chapter defines the requirements for the DDS
Binding, DDS Gateway, DDS Communication Daemon, deployment configuration,
runtime behavior, interoperability, and safety aspects.

Service Discovery and Availability
----------------------------------

The Service Discovery chapter describes:

* DDS endpoint discovery;
* communication-route state;
* configurable service-availability policies;
* route-based availability;
* explicit service-state propagation;
* startup behavior; and
* recovery behavior.

End-to-End Protection
---------------------

The E2E chapter describes:

* ownership of E2E processing;
* E2E Protect and E2E Check;
* Binding deployment;
* Gateway deployment;
* interaction with the DDS Communication Daemon; and
* application-facing E2E semantics.

Use Cases
---------

The Use Cases chapter illustrates supported deployment scenarios and expected
runtime behavior.


Backwards Compatibility
=======================

Existing ``mw::com`` applications continue to use the standard ``mw::com`` API.

Existing LoLa application's deployment remain unchanged unless DDS Gateway communication is
explicitly configured for this application requiring communication over DDS network.


Security Impact
===============

DDS communication may interact with other systems for which security is needed.

Validation of received data, deployment of DDS Security, credential management,
network protection, and platform hardening remain deployment-specific unless
covered by another SCORE feature.


Safety Impact
=============

DDS stacks are typically available as QM software components.

Deployments requiring ASIL/QM separation may execute the DDS Binding or DDS
Gateway in an ASIL context while placing the DDS stack inside a separate DDS
Communication Daemon.

The runtime IPC boundary provides architectural separation between the
application-facing communication component and the DDS stack.

The complete freedom-from-interference argument remains deployment-specific.

Refer to the Architecture and E2E chapters for further details.


License Impact
==============

DDS is an open communication standard supported by multiple implementations.

The implementation shall comply with the license terms of the selected DDS
implementation while preserving the stable application-facing abstraction
defined by this feature.


How to Teach This
=================

Application developers continue to use the standard ``mw::com`` API and are not
required to understand deeply DDS programming/concept.

System integrators configure DDS deployment information, including Topics,
runtime types, Domains, QoS, communication routes, availability policies, and
E2E settings.

Developers implementing the communication infrastructure should additionally
understand the DDS Binding architecture, DDS Gateway architecture, DDS
Communication Daemon, service discovery, communication routes, and E2E
processing.

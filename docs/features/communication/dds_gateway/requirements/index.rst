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

.. _dds_binding_gateway_requirements:

DDS Binding and Gateway Requirements
####################################

Architecture Requirements
=========================

.. req:: Direct DDS Binding deployment
   :id: feat_req__dds__direct_binding
   :status: valid

   The feature shall support deployment of a DDS Binding beneath ``mw::com``.

.. req:: DDS Gateway deployment
   :id: feat_req__dds__gateway
   :status: valid

   The feature shall support deployment of a DDS Gateway between LoLa and DDS.

.. req:: Common DDS Communication Daemon
   :id: feat_req__dds__common_daemon
   :status: valid

   The DDS Binding and DDS Gateway shall be able to reuse the same DDS
   Communication Daemon capability.

.. req:: DDS stack outside ASIL-facing process
   :id: feat_req__dds__stack_process_separation
   :status: valid

   A deployment requiring ASIL/QM separation shall support placing the DDS
   stack in a DDS Communication Daemon process outside the DDS Binding or DDS
   Gateway process.

.. req:: Runtime IPC
   :id: feat_req__dds__runtime_ipc
   :status: valid

   The DDS Binding and DDS Gateway shall communicate with the DDS Communication
   Daemon through runtime IPC.

Configuration Requirements
==========================

.. req:: Extend mw::com deployment for DDS
   :id: feat_req__dds__extend_mwcom_deployment
   :status: valid

   The DDS integration shall extend the existing ``mw::com`` deployment model
   with the DDS-specific information required to establish configured DDS
   communication routes.

.. req:: Reuse mw::com service model
   :id: feat_req__dds__reuse_mwcom_service_model
   :status: valid

   DDS configuration shall reuse the existing ``mw::com`` service type,
   version, service instance, and event identities.

.. req:: DDS communication route information
   :id: feat_req__dds__route_information
   :status: valid

   A configured DDS communication route shall identify the corresponding
   ``mw::com`` event, DDS Domain, DDS Topic, DDS type, communication direction,
   and applicable DDS QoS configuration.

.. req:: Component-specific configuration
   :id: feat_req__dds__component_specific_configuration
   :status: valid

   The DDS Binding, DDS Gateway, and DDS Communication Daemon may consume
   separate configuration artifacts according to their respective
   responsibilities.

.. req:: Configuration consistency
   :id: feat_req__dds__configuration_consistency
   :status: valid

   Configuration artifacts used by the DDS Binding, DDS Gateway, and DDS
   Communication Daemon shall be mutually consistent for every configured
   route and availability policy.

.. req:: Configuration outside runtime IPC
   :id: feat_req__dds__configuration_outside_runtime_ipc
   :status: valid

   DDS deployment configuration shall not be exchanged through the runtime IPC
   between the DDS Binding or DDS Gateway and the DDS Communication Daemon.

.. req:: Configuration validation
   :id: feat_req__dds__configuration_validation
   :status: valid

   The implementation shall not activate a DDS route or service-availability
   policy whose required configuration is missing, inconsistent, ambiguous,
   invalid, or unsupported.

Topic Mapping Requirements
==========================

.. req:: Event-to-Topic mapping
   :id: feat_req__dds__event_topic_mapping
   :status: valid

   Each ``mw::com`` event configured for DDS communication shall be mapped
   unambiguously to a DDS Topic.

.. req:: Deterministic Topic identity
   :id: feat_req__dds__deterministic_topic_identity
   :status: valid

   A configured or derived DDS Topic identity shall be deterministic.

.. req:: Prevent unintended Topic collision
   :id: feat_req__dds__topic_collision_prevention
   :status: valid

   The event-to-Topic mapping shall prevent different DDS communication routes
   from unintentionally resolving to the same DDS Topic identity.

.. req:: Explicit or derived Topic name
   :id: feat_req__dds__topic_name_selection
   :status: valid

   The deployment shall support a Topic identity that is either explicitly
   configured or derived according to an implementation-defined deterministic
   convention.

.. req:: Compatible Topic definition
   :id: feat_req__dds__compatible_topic_definition
   :status: valid

   Communicating publishers and subscribers shall use compatible DDS Domain,
   Topic, type, and QoS information.

DDS Type Requirements
=====================

.. req:: DDS type configuration
   :id: feat_req__dds__type_configuration
   :status: valid

   Each DDS-enabled ``mw::com`` event shall be associated with sufficient DDS
   type information to create the DDS Topic and corresponding endpoint.

.. req:: Runtime serialization information
   :id: feat_req__dds__runtime_serialization_information
   :status: valid

   The configured type information shall be sufficient to serialize and
   deserialize the event payload at runtime.

.. req:: No generated DDS application interface
   :id: feat_req__dds__no_generated_application_interface
   :status: valid

   The DDS integration shall not require the ``mw::com`` application to use or
   link a DDS-generated application interface.

.. req:: Type compatibility validation
   :id: feat_req__dds__type_compatibility_validation
   :status: valid

   The implementation shall validate compatibility between the configured
   ``mw::com`` event type and DDS type before activating the route.

DDS Domain Requirements
=======================

.. req:: DDS Domain configuration
   :id: feat_req__dds__domain_configuration
   :status: valid

   Each DDS communication route shall be associated with a DDS Domain.

.. req:: Multiple DDS Domains
   :id: feat_req__dds__multiple_domains
   :status: valid

   The deployment model shall allow different configured routes to use
   different DDS Domains.

DDS QoS Requirements
====================

.. req:: DDS QoS configuration
   :id: feat_req__dds__qos_configuration
   :status: valid

   The DDS deployment information shall provide the DDS QoS required for each
   configured communication route.

.. req:: Reusable QoS profiles
   :id: feat_req__dds__reusable_qos_profiles
   :status: valid

   An implementation may allow multiple routes to refer to a reusable DDS QoS
   profile.

.. req:: Explicit QoS configuration
   :id: feat_req__dds__explicit_qos_configuration
   :status: valid

   The implementation shall not assume an automatic one-to-one mapping between
   LoLa communication properties and DDS QoS policies.

Binding Requirements
====================

.. req:: Binding-independent application API
   :id: feat_req__dds__binding_independent_api
   :status: valid

   An application using the DDS Binding shall continue to use the standard
   ``mw::com`` API.

.. req:: Binding runtime type handling
   :id: feat_req__dds__binding_runtime_types
   :status: valid

   The DDS Binding shall use the configured runtime type information required
   for its routes.

.. req:: Binding serialization
   :id: feat_req__dds__binding_serialization
   :status: valid

   The DDS Binding shall convert between ``mw::com`` samples and the configured
   serialized DDS representation.

Gateway Requirements
====================

.. req:: Generic Proxy
   :id: feat_req__dds__generic_proxy
   :status: valid

   The DDS Gateway shall be able to consume configured locally provided LoLa
   events through a Generic Proxy.

.. req:: Generic Skeleton
   :id: feat_req__dds__generic_skeleton
   :status: valid

   The DDS Gateway shall be able to provide configured remotely received DDS
   events through a Generic Skeleton.

.. req:: Bidirectional Gateway routes
   :id: feat_req__dds__bidirectional_gateway
   :status: valid

   The DDS Gateway shall support configured LoLa-to-DDS and DDS-to-LoLa event
   routes.

Daemon Requirements
===================

.. req:: DDS entity creation
   :id: feat_req__dds__daemon_entity_creation
   :status: valid

   The DDS Communication Daemon shall create the configured DDS Domains, Topics,
   DataReaders, and DataWriters according to the deployment lifecycle policy.

.. req:: Serialized DDS write
   :id: feat_req__dds__serialized_write
   :status: valid

   The DDS Communication Daemon shall publish serialized DDS samples received
   for configured writer routes.

.. req:: Serialized DDS read
   :id: feat_req__dds__serialized_read
   :status: valid

   The DDS Communication Daemon shall deliver serialized DDS samples received
   on configured reader routes through runtime IPC.

.. req:: Multiplex configured routes
   :id: feat_req__dds__multiplex_routes
   :status: valid

   The runtime IPC shall support multiple configured communication routes
   without requiring one IPC connection per Topic, service, or event.

Discovery and Availability Requirements
=======================================

.. req:: DDS endpoint discovery
   :id: feat_req__dds__endpoint_discovery
   :status: valid

   The DDS Communication Daemon shall use DDS participant and endpoint
   discovery for configured DDS communication routes.

.. req:: Communication-route state
   :id: feat_req__dds__route_operational_state
   :status: valid

   The DDS Communication Daemon shall evaluate the operational state of each
   configured DDS communication route.

.. req:: Route-state notification
   :id: feat_req__dds__endpoint_status_notification
   :status: valid

   The DDS Communication Daemon shall communicate relevant communication-route
   state changes to the DDS Binding or DDS Gateway through runtime IPC.

.. req:: Configurable service-availability policy
   :id: feat_req__dds__availability_policy
   :status: valid

   The deployment configuration shall define how availability of each mapped
   ``mw::com`` service instance is determined.

.. req:: Availability-policy inputs
   :id: feat_req__dds__availability_sources
   :status: valid

   The service-availability policy shall support using:

   * DDS communication-route state;
   * explicit service-instance state;

.. req:: Required communication routes
   :id: feat_req__dds__required_availability_routes
   :status: valid

   For route-based availability, the deployment configuration shall identify
   the DDS communication routes that participate in the service-availability
   decision.

.. req:: Explicit service-state propagation
   :id: feat_req__dds__explicit_service_availability
   :status: valid

   The architecture shall support propagation of explicit service-instance
   state through a configured DDS communication route.


.. req:: Binding availability propagation
   :id: feat_req__dds__binding_availability
   :status: valid

   The DDS Binding shall apply the configured service-availability policy and
   update the corresponding ``mw::com`` availability state.

.. req:: Gateway availability propagation
   :id: feat_req__dds__gateway_availability
   :status: valid

   The DDS Gateway shall apply the configured service-availability policy and
   offer or withdraw the corresponding local LoLa service.

.. req:: Native DDS route-based availability
   :id: feat_req__dds__native_endpoint_availability
   :status: valid

   A compatible native DDS participant that does not provide explicit
   service-instance state shall be supportable through a route-based
   availability policy.

.. req:: Availability recovery
   :id: feat_req__dds__availability_recovery
   :status: valid

   Following DDS communication or DDS Communication Daemon recovery, service
   availability shall be restored only after the configured availability
   conditions are fulfilled again.

.. req:: Bounded startup data handling
   :id: feat_req__dds__bounded_startup_handling
   :status: valid

   The implementation shall define bounded behavior for DDS samples received
   before the corresponding local application-facing communication path is
   ready.

E2E Requirements
================

.. req:: Binding-independent E2E API
   :id: feat_req__dds__e2e_binding_independent_api
   :status: valid

   An application shall use the same ``mw::com`` E2E-facing API when deployed
   with the DDS Binding or LoLa Binding.

.. req:: Single E2E owner
   :id: feat_req__dds__single_e2e_owner
   :status: valid

   A protected communication route shall have one configured owner for E2E
   protection and one configured owner for E2E checking.

.. req:: Disable duplicate LoLa E2E
   :id: feat_req__dds__disable_duplicate_lola_e2e
   :status: valid

   LoLa-side E2E processing shall be disabled for an internal DDS Gateway leg
   when the DDS Gateway owns the same configured E2E profile.

.. req:: Gateway E2E result forwarding
   :id: feat_req__dds__gateway_e2e_forwarding
   :status: valid

   For incoming DDS Gateway routes, the Gateway shall forward the payload and
   produced E2E result to the local ``mw::com`` consumer without repeating the
   same E2E check in LoLa.

Safety Requirements
===================

.. req:: ASIL/QM process boundary
   :id: feat_req__dds__asil_qm_boundary
   :status: valid

   A deployment requiring separation between an ASIL-facing communication
   component and a QM DDS stack shall use the DDS Communication Daemon process
   boundary.

.. req:: Deployment-specific IPC suitability
   :id: feat_req__dds__ipc_suitability
   :status: valid

   The selected runtime IPC mechanism shall be suitable for the requirements of
   the deployment safety concept.

Interoperability Requirements
=============================

.. req:: Native DDS interoperability
   :id: feat_req__dds__native_interoperability
   :status: valid

   A configured route shall be able to interoperate with a compatible native
   DDS participant using matching Domain, Topic, type, and QoS information.

.. req:: DDS stack abstraction
   :id: feat_req__dds__stack_abstraction
   :status: valid

   Application-facing components shall not depend directly on one
   vendor-specific DDS API.

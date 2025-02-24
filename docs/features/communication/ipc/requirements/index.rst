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

Requirements
############

High cohesion and loose coupling
================================

.. feat_req:: Support for Time-based Architecture
   :id: feat_req__ipc__time_based_arch
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process,stkh_req__app_architectures__support_time
   :status: valid

   The communication framework shall provide API to support a time-based architecture.

.. feat_req:: Support for Data-driven Architecture
   :id: feat_req__ipc__data_driven_arch
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process,stkh_req__app_architectures__support_data
   :status: valid

   The communication framework shall provide API to support a data-driven architecture.

.. feat_req:: Support for Request-driven Architecture
   :id: feat_req__ipc__request_driven_arch
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process,stkh_req__app_architectures__support_data
   :status: valid

   The communication framework shall provide API to support a request-driven architecture.

.. feat_req:: Communication Interfaces
   :id: feat_req__ipc__interfaces
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process,stkh_req__app_architectures__support_data,stkh_req__app_architectures__support_request
   :status: valid

   A communication interface consists of a combination of any number of the following elements:

   - Event-Types
   - Methods
   - Signals

.. feat_req:: Event Type
   :id: feat_req__ipc__event_type
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process,stkh_req__app_architectures__support_data
   :status: valid

   An event-type is part of a communication interface and has:

   - a name
   - a data type

   The producer can assign a value to it.
   Consumers can subscribe to value-changed events of the element or poll unseen, cached events.

.. feat_req:: Method
   :id: feat_req__ipc__method
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process,stkh_req__app_architectures__support_request
   :status: valid

   A method is part of a communication interface and has:

   - a name
   - a specified application routine with a given set of parameters and a return type

   When a communication partner issues a call to the method with the required parameters:

   1. it shall invoke the application routine with the provided parameters, and
   2. return its result to the communication partner

   A method call shall be possible both synchronously and asynchronously.

.. feat_req:: Signal
   :id: feat_req__ipc__signal
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process,stkh_req__app_architectures__support_time
   :status: valid

   A signal is part of a communication interface and has:

   - a name

   A client can trigger the signal.
   The service instance offering the trigger can:

   - wait for the signal to be triggered
   - check if the signal was triggered

   Note: Signals can not transport data. They are meant to be fast synchronization mechanism with low setup cost.
   Thus, depending on the location of the communication partners primitives like Linux Signals or QNX Pulses or
   Hypervisor Signalling APIs may be chosen.

.. feat_req:: Producer-Consumer Pattern
   :id: feat_req__ipc__producer_consumer
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process,stkh_req__app_architectures__support_time
   :status: valid

   Communication shall be cached based on the producer-consumer pattern.

.. feat_req:: Service Instance
   :id: feat_req__ipc__service_instance
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   A communication interface that is offered to consumers is called a service instance.

   Multiple service instances shall be able to offer the same interface.

.. feat_req:: Service Instance Names
   :id: feat_req__ipc__service_instance_names
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   A service instance is offered under one or more unique names by which it can be discovered.
   Names follow a POSIX path style.

   Note: The resolution from a service instance name to the protocol-specific identifier is handled by the service
   discovery.


.. feat_req:: Versioning
   :id: feat_req__ipc__versioning
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The communication framework shall support versioning of service instances.
   Version information of a service instance is binding-specific.
   Version information is provided in the deployment configuration.

   Note:
   Multiple service instances can have the same interface and version.

.. feat_req:: Service location transparency
   :id: feat_req__ipc__service_location_transparency
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The interface to access service instances is agnostic to the binding used to communicate with the service.
   Note: Deployment information may require manual changes based on where the service is located.

.. feat_req:: Stateless communication
   :id: feat_req__ipc__stateless_communication
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The communication framework shall support stateless communication.
   Note:
   - In case of events, the producer is not aware of its consumers.
   - In case of RPC, the skeleton is not aware of the proxy, this request originated from.

.. feat_req:: Service instance_granularity
   :id: feat_req__ipc__service_instance_granularity
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The communication framework shall support multiple service instances per software architecture element.
   Note: A software architecture element is for example an application, activity, proces, ...

.. feat_req:: Service discovery
   :id: feat_req__ipc__service_discovery
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The communication framework shall provide service discovery to find available services during runtime.
   Service discovery shall consider version compatibility.
   Service discovery shall be handled implicitly (where possible).
   Note: The service discovery may be restricted/impacted by availability of deployment information.

Mixed-Criticality safety systems
================================

.. feat_req:: Safe communication over criticality levels
   :id: feat_req__ipc__safe_communication
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The communication framework shall support safe communication involving communication partners on the same or multiple
   criticality levels.

.. feat_req:: Data Corruption
   :id: feat_req__ipc__data_corruption
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   Consumers with lower criticality shall not be able to corrupt data consumed by partners with higher criticality.

.. feat_req:: Data Reordering
   :id: feat_req__ipc__data_reordering
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   Consumers with lower criticality shall not be able to modify the order of data consumed by partners with higher
   criticality.

.. feat_req:: Data Repetition
   :id: feat_req__ipc__data_repetition
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   Consumers with lower criticality shall not be able to duplicate data consumed by other communication partners with
   higher criticality.

.. feat_req:: Data Loss
   :id: feat_req__ipc__data_loss
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   Consumers with lower criticality shall not be able to drop data before it is consumed by partners with higher
   criticality.

Performance
===========

.. feat_req:: Zero-Copy IPC
   :id: feat_req__ipc__zero_copy
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process,stkh_req__app_architectures__support_data
   :status: valid

   IPC communication shall be possible without copying to-be-transferred data.

User friendly API for information exchange
==========================================

.. feat_req:: Support for multiple programming languages
   :id: feat_req__ipc__multi_lang
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__prog_languages
   :status: valid

   The communication framework shall provide a public API for each supported programming language of SCORE.

.. feat_req:: Support for programming language idioms
   :id: feat_req__ipc__lang_idioms
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__prog_languages
   :status: valid

   Each public API shall support the idioms of the programming language it is written in.

.. feat_req:: Use programming language infrastructure
   :id: feat_req__ipc__lang_infra
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__prog_languages
   :status: valid

   Each public API shall use core infrastructure of its programming language and accompanying standard libraries,
   whenever possible and meaningful.

   Note: This includes error handling.

Full testability for the user facing API
========================================

.. feat_req:: Fully mockable public API
   :id: feat_req__ipc__testability_mock_api
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The public API shall be fully mockable.

.. feat_req:: Fake binding
   :id: feat_req__ipc__testability_fake_binding
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The communication framework shall provide a fake binding.

Multi-binding support
=====================

.. feat_req:: Multi-binding support
   :id: feat_req__ipc__multi_binding_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The communication framework shall support multiple bindings.

   Note:
   A binding performs the conversion of user communication to the respective communication protocol.
   It does this either directly or via a gateway approach.

.. feat_req:: Binding-agnostic public API
   :id: feat_req__ipc__binding_agnostic_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The public API of the communication framework shall be binding-agnostic.

   Note:
   Binding-agnostic in this context means, that the public API is independent of the binding underneath. E.g., if the
   binding is exchanged, the public API remains syntactically and semantically unchanged.

.. feat_req:: Multi-binding deployment configuration
   :id: feat_req__ipc__multi_binding_depl
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The association of a service instance and the appropriate binding shall be specified in the deployment configuration.

Dynamic deployment at runtime
=============================

.. feat_req:: Deployment configuration at runtime
   :id: feat_req__ipc__depl_config_runtime
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   Deployment configuration shall be read from an integrity-checked configuration file at runtime.

Tracing
=======

.. feat_req:: Support for Tracing
   :id: feat_req__ipc__tracing
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dev_experience__tracing_of_comm
   :status: valid

   The communication framework shall provide infrastructure to enable binding-agnostic, zero-copy, read-only tracing of
   communication.

Security Impact
===============

.. feat_req:: Access Control List Placement
   :id: feat_req__ipc__acl_placement
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The communication framework shall support an Access Control Lists in the deployment configuration.

.. feat_req:: Access Control List per service instance
   :id: feat_req__ipc__acl_per_service_instance
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The communication framework shall support an Access Control List per service instance.

.. feat_req:: Access Control List for producer
   :id: feat_req__ipc__acl_for_producer
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The communication framework shall support an Access Control List for the communication partner offering a service
   instance (producer).
   An entry in the ACL corresponds to an allowed consumer.

.. feat_req:: Access Control List for consumer
   :id: feat_req__ipc__acl_for_consumer
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The communication framework shall support an Access Control List for the communication partner consuming a service
   instance.
   An entry in the ACL corresponds to an allowed producer.

.. feat_req:: IPC Confidentiality
   :id: feat_req__ipc__confidentiality
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The IPC binding shall ensure confidentiality of its communication.

.. feat_req:: IPC Integrity
   :id: feat_req__ipc__integrity
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The IPC binding shall ensure integrity of its communication.

.. feat_req:: IPC Availability
   :id: feat_req__ipc__availability
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The IPC binding shall ensure availability of its communication, so that the availability is independent per
   criticality level.

Safety Impact
=============

.. feat_req:: IPC ASIL level
   :id: feat_req__ipc__asil
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The communication framework shall support safe communication up to ASIL-B.

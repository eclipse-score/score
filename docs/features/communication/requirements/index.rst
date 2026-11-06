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

.. _com_requirements:

Communication Requirements
==========================

.. document:: Communication Requirements
   :id: doc__communication_requirements
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_feat[version==1]

.. feat_req:: Support for Time-based Architecture
   :id: feat_req__com__time_based_arch
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_time[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall provide API to support a time-based architecture.

.. feat_req:: Support for Data-driven Architecture
   :id: feat_req__com__data_driven_arch
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_data[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall provide API to support a data-driven architecture.

.. feat_req:: Support for Request-driven Architecture
   :id: feat_req__com__request_driven_arch
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_request[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall provide API to support a request-driven architecture.

.. feat_req:: Communication Interfaces
   :id: feat_req__com__interfaces
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_data[version==1], stkh_req__app_architectures__support_time[version==1], stkh_req__communication__safe[version==1], stkh_req__app_architectures__support_request[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   A communication interface consists of a combination of any number of the following elements:

   - Events
   - Methods
   - Fields

.. feat_req:: Event Type Structure
   :id: feat_req__com__event_type_structure
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_time[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   An event-type shall be a named element of a communication interface with an associated data type.

.. feat_req:: Event Access
   :id: feat_req__com__event_type_access
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_time[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   An event-type shall allow its producer to assign a value and its consumers to either subscribe to value-changed events or poll unseen, cached events.

.. feat_req:: Method Structure
   :id: feat_req__com__method_structure
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_request[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   A method shall be defined by a name, a specified application routine with a given set of parameters, and a return type.

.. feat_req:: Method Invocation
   :id: feat_req__com__method_invocation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_request[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   When a communication partner calls a method with the required parameters, the method shall invoke
   its application routine with those parameters, return the result to the caller,
   and support both synchronous and asynchronous invocation.

.. feat_req:: Field Structure
   :id: feat_req__com__field_structure
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_request[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   A field shall be defined by a name, a data type, and dedicated getter and setter methods.

.. feat_req:: Field Invocation
   :id: feat_req__com__field_invocation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_request[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   A field shall allow its producer to assign a value, and shall allow its consumers to subscribe
   to value-changed notifications, poll unseen cached values, or retrieve and update the value via its getter and setter methods.

.. feat_req:: Producer-Consumer Pattern
   :id: feat_req__com__producer_consumer
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_time[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Communication shall be cached based on the producer-consumer pattern.

.. feat_req:: Service Instance
   :id: feat_req__com__service_instance
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The communication framework shall support offering multiple service instances for the same interface.

.. feat_req:: Service Instance Names
   :id: feat_req__com__service_instance_names
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   A service instance shall be offered and discoverable under one unique name.

.. feat_req:: Versioning
   :id: feat_req__com__versioning
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: invalid
   :version: 1

   The communication framework shall support versioning of service instances:

   - Version information of a service instance is binding-specific.
   - Version information is provided in the deployment configuration.

   .. note::
      Multiple service instances can have the same interface and version.

.. feat_req:: Service location transparency
   :id: feat_req__com__service_location_transparency
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The interface to access service instances shall be agnostic to the binding used to communicate with the service.

   .. note::
      Deployment information may require manual changes based on where the service is located.

.. feat_req:: Stateless communication
   :id: feat_req__com__stateless_communication
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall support stateless communication.

   .. note::
      - In case of events, the producer is not aware of its consumers.
      - In case of RPC, the skeleton is not aware of the proxy, this request originated from.

.. feat_req:: Service instance_granularity
   :id: feat_req__com__service_instance_granularity
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall support multiple service instances per software architecture element.

   .. note::
      A software architecture element is for example an application, activity, proces, ...

.. feat_req:: Service discovery
   :id: feat_req__com__service_discovery
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The communication framework shall provide service discovery that considers version compatibility to find available services during runtime.


Mixed-Criticality safety systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. feat_req:: Safe communication over criticality levels
   :id: feat_req__com__safe_communication
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall support safe communication involving communication partners on the same or multiple
   criticality levels.

.. feat_req:: Data Corruption
   :id: feat_req__com__data_corruption
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Consumers with lower criticality shall not be able to corrupt data consumed by partners with higher criticality.

.. feat_req:: Data Reordering
   :id: feat_req__com__data_reordering
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Consumers with lower criticality shall not be able to modify the order of data consumed by partners with higher
   criticality.

.. feat_req:: Data Repetition
   :id: feat_req__com__data_repetition
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Consumers with lower criticality shall not be able to duplicate data consumed by other communication partners with
   higher criticality.

.. feat_req:: Data Loss
   :id: feat_req__com__data_loss
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Consumers with lower criticality shall not be able to drop data before it is consumed by partners with higher
   criticality.


Performance
^^^^^^^^^^^

.. feat_req:: Zero-Copy Approach
   :id: feat_req__com__zero_copy
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_data[version==1], stkh_req__app_architectures__support_request[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall enable Zero-Copy communication without copying to-be-transferred data.

   .. note::
      It has to be evaluated on binding level if a Zero-Copy approach is applicable for the respective binding.

User friendly API for information exchange
------------------------------------------

.. feat_req:: Support for multiple programming languages
   :id: feat_req__com__multi_lang
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__dev_experience__prog_languages[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall provide a public API for each supported programming language of S-CORE.

.. feat_req:: Support for programming language idioms
   :id: feat_req__com__lang_idioms
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__dev_experience__prog_languages[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Each public API shall support the idioms of the programming language it is written in.

.. feat_req:: Use programming language infrastructure
   :id: feat_req__com__lang_infra
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__dev_experience__prog_languages[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Each public API shall use core infrastructure of its programming language and accompanying standard libraries,
   whenever possible and meaningful.

   .. note::
      This includes error handling.

Full testability for the user facing API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. feat_req:: Fully mockable public API
   :id: feat_req__com__testability_mock_api
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The public API shall be fully mockable.

.. feat_req:: Fake binding
   :id: feat_req__com__testability_fake_binding
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall provide a fake binding.


Multi-binding support
^^^^^^^^^^^^^^^^^^^^^

.. feat_req:: Multi-binding support
   :id: feat_req__com__multi_binding_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall support multiple bindings.

   .. note::
      A binding performs the conversion of user communication to the respective communication protocol. It does this either directly or via a gateway approach.

.. feat_req:: Binding-agnostic public API
   :id: feat_req__com__binding_agnostic_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The public API of the communication framework shall be binding-agnostic.

   .. note::
      Binding-agnostic in this context means, that the public API is independent of the binding underneath. E.g., if the binding is exchanged, the public API remains syntactically and semantically unchanged.

.. feat_req:: Multi-binding deployment configuration
   :id: feat_req__com__multi_binding_depl
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The association of a service instance and the appropriate binding shall be specified in the deployment configuration.

Cross-VM Extensions
^^^^^^^^^^^^^^^^^^^
.. feat_req:: One-way data sharing into a VM
   :id: feat_req__com__one_way_sharing
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The system shall support one-way data sharing into a Virtual Machine (VM) for vehicle state read-only for the VM (snapshot state).

.. feat_req:: Read-only access for VM
   :id: feat_req__com__readonly_vm
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The consumer (VM) shall have read-only access to the shared data.

.. feat_req:: Consistent data-sets
   :id: feat_req__com__consistent_data
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The system shall support consistent data-sets, allowing the consumer to obtain a consistent version of related data items.

.. feat_req:: Lock-free access
   :id: feat_req__com__lock_free_access
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Consistent access to data must be lock-free.

.. feat_req:: Producer time stamps
   :id: feat_req__com__producer_timestamps
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Producer time stamps shall be available for related data-sets.

.. feat_req:: Streamed data based on shared queues
   :id: feat_req__com__streamed_data
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The system shall support streamed data based on shared queues (stream of events or data).

.. feat_req:: Configurable queues
   :id: feat_req__com__configurable_queues
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Queues shall be configurable by the client (VM), including the number of elements and buffer allocation.

.. feat_req:: Lock-free queue access
   :id: feat_req__com__lock_free_queue
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Queues shall support lock-free access to data elements.

.. feat_req:: Bi-directional communication
   :id: feat_req__com__bi_directional_comm
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The system shall support bi-directional communication via writable data elements by the client.

.. feat_req:: Asynchronous support
   :id: feat_req__com__async_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The system shall provide asynchronous bi-directional support via multiple queues.

.. feat_req:: Shared memory chunks
   :id: feat_req__com__shared_memory
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The system shall support multiple chunks of shared memory to allow required access control.

.. feat_req:: Data update notifications
   :id: feat_req__com__data_notifications
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Notifications for data updates shall be available (virtual IRQs in a VM).

.. feat_req:: Configurable notifications
   :id: feat_req__com__config_notifications
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Notifications shall be configurable by consumers of data (using flags or watermarks in shared memory from client to producer).


Dynamic deployment at runtime
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. feat_req:: Deployment configuration at runtime
   :id: feat_req__com__depl_config_runtime
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   Deployment configuration shall be read from an integrity-checked configuration file at runtime.

Tracing
-------

.. feat_req:: Support for Tracing
   :id: feat_req__com__tracing
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__dev_experience__tracing_of_comm[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall provide infrastructure to enable binding-agnostic, zero-copy, read-only tracing of
   communication.

Security Impact
---------------

.. feat_req:: Access Control List Placement
   :id: feat_req__com__acl_placement
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__dependability__security_features[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall support an Access Control Lists in the deployment configuration.

.. feat_req:: Access Control List per service instance
   :id: feat_req__com__acl_per_service_instance
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__dependability__security_features[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall support an Access Control List per service instance.

.. feat_req:: Access Control List for producer
   :id: feat_req__com__acl_for_producer
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__dependability__security_features[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall support an Access Control List for the communication partner offering a service
   instance (producer).
   An entry in the ACL corresponds to an allowed consumer.

.. feat_req:: Access Control List for consumer
   :id: feat_req__com__acl_for_consumer
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__dependability__security_features[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall support an Access Control List for the communication partner consuming a service
   instance.
   An entry in the ACL corresponds to an allowed producer.

Safety Impact
-------------

.. feat_req:: Communication ASIL level
   :id: feat_req__com__asil
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__communication__safe[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The communication framework shall support safe communication up to ASIL-B.

.. needextend:: c.this_doc() and is_external == False and "__com_" in id
   :+tags: com

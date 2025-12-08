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


.. _feature_requirements_PersistencyKvs:

Requirements
############

.. document:: Persistency KVS Feature Requirements
   :id: doc__persistency_requirements
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__requirements_feat
   :tags: persistency

.. feat_req:: C++ & Rust Interoperability
   :id: feat_req__persistency__cpp_rust_interop
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__prog_languages
   :status: valid

   The Key-Value-Storage shall provide access through both C++ and Rust
   interfaces.

.. feat_req:: Maximum Size
   :id: feat_req__persistency__maximum_size
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The Key-Value-Storage shall support specification of its maximum size at
   compile time.

.. feat_req:: Multiple KVS per Software Architecture Element
   :id: feat_req__persistency__multiple_kvs
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The Key-Value-Storage shall allow instantiating multiple independent stores
   per software architecture element.

.. feat_req:: Supported Datatypes (Keys)
   :id: feat_req__persistency__support_datatype_keys
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The Key-Value-Storage shall support UTF-8 encoded strings as valid key
   types.

.. feat_req:: Supported Datatypes (Values)
   :id: feat_req__persistency__support_datatype_value
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid
   :tags: persistency

   The Key-Value-Storage shall support storing both primitive and non-primitive
   datatypes as values. The supported datatypes shall match those used by the
   IPC feature.

.. feat_req:: Default Values
   :id: feat_req__persistency__default_values
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The Key-Value-Storage shall support predefined default values for keys.

.. feat_req:: Default Value Retrieval
   :id: feat_req__persistency__default_value_get
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The Key-Value-Storage shall support retrieving the default value associated
   with a key.

.. feat_req:: Default Value Reset
   :id: feat_req__persistency__default_value_reset
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The Key-Value-Storage shall support resetting a single key or all keys to
   their respective default values.

.. feat_req:: Persistency
   :id: feat_req__persistency__persistency
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The Key-Value-Storage shall persist stored data and provide an API to
   explicitly trigger persistence.

.. feat_req:: Integrity Check
   :id: feat_req__persistency__integrity_check
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The Key-Value-Storage shall detect and report data corruption.
   Note: Implementation depends on AoUs.

.. feat_req:: Versioning
   :id: feat_req__persistency__versioning
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The Key-Value-Storage shall support versioning for different layout
   configurations.

.. feat_req:: Update Mechanism
   :id: feat_req__persistency__update_mechanism
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The Key-Value-Storage shall implement mechanisms to upgrade from one version
   to another, including multi-version jumps.

.. feat_req:: Snapshots
   :id: feat_req__persistency__snapshots
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The Key-Value-Storage shall support explicit creation of snapshots
   identified by unique IDs and allow rollback to previous snapshots. Snapshots
   shall also be deletable.

.. feat_req:: Tooling
   :id: feat_req__persistency__tooling
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The Key-Value-Storage shall provide tooling support for viewing and
   modifying key-value pairs during development and debugging.

.. feat_req:: Variant management support
   :id: feat_req__persistency__variant_management
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__overall_goals__variant_management
   :status: valid

   The Key-Value-Storage shall ensure compatibility across different
   architectures and versions.

.. feat_req:: Set default key values via file
   :id: feat_req__persistency__default_value_file
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   The Key-Value-Storage shall support the configuration of default key values
   using an external file.

.. feat_req:: Configure limits via file
   :id: feat_req__persistency__config_file
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   The Key-Value-Storage shall support the configuration of memory and other
   resource limits via a configuration file.

.. feat_req:: Store persistent data
   :id: feat_req__persistency__persist_data
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__data_persistency
   :status: valid

   The Key-Value-Storage shall support storing and loading its data to and from
   persistent storage.

.. feat_req:: Support engineering mode
   :id: feat_req__persistency__eng_mode
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__safety_features
   :status: valid

   The Key-Value-Storage shall an engineering (developer) mode.
   The engineering mode shall allow unrestricted data access.

.. feat_req:: Support field mode
   :id: feat_req__persistency__field_mode
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__safety_features
   :status: valid

   The Key-Value-Storage shall a field mode.
   The field mode should enforce the most restrictive data access controls feasible.

.. feat_req:: Provide an async API
   :id: feat_req__persistency__async_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__availability, stkh_req__app_architectures__support_request
   :status: valid

   The Key-Value-Storage shall provide an asynchronous API for accessing and
   manipulating data.

.. feat_req:: Separate data stores
   :id: feat_req__persistency__access_control
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The Key-Value-Storage shall ensure that only authorized components can
   access individual data stores.

.. feat_req:: Data-change events
   :id: feat_req__persistency__events
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__app_architectures__support_data
   :status: valid

   The Key-Value-Storage shall provide an API that allows for the registration
   of callback functions. These callbacks shall be invoked in response to
   specific events, such as when keys are changed or removed.

.. feat_req:: Fast access
   :id: feat_req__persistency__fast_access
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__short_app_cycles
   :status: valid

   The Key-Value-Storage shall ensure that key operations are completed within
   5 milliseconds.

.. feat_req:: Intra-Process Data Access
   :id: feat_req__persistency__intra_process_comm
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__intra_process
   :status: valid

   The Key-Value-Storage shall support concurrent intra-process data access.

.. needextend:: docname is not None and "persistency/kvs/requirements" in docname
   :+tags: persistency

AoU Requirements
################

.. aou_req:: Persistency Error handling
   :id: aou_req__persistency__error_handling
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: environment

   The application shall handle if the feature persistency is not available.

.. aou_req:: Application deadlock
   :id: aou_req__persistency__appl_design
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: environment

   The application shall be designed in a way that deadlocks are avoided.

.. aou_req:: Application execution
   :id: aou_req__persistency__appl_exec
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: environment

   The execution of persistency shall not be blocked by the application.

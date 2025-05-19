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

Requirements
############

.. feat_req:: C++ & Rust Interoperability
   :id: feat_req__kvs__cpp_rust_interoperability
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__prog_languages
   :status: valid

   The KVS system shall provide access through both C++ and Rust interfaces.

.. feat_req:: Maximum Size
   :id: feat_req__kvs__maximum_size
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: invalid

   The KVS system shall support specification of its maximum capacity at compile time.

.. feat_req:: Multiple KVS per Software Architecture Element
   :id: feat_req__kvs__multiple_kvs
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The KVS system shall allow instantiating multiple independent stores per software architecture element.

.. feat_req:: Supported Datatypes (Keys)
   :id: feat_req__kvs__supported_datatypes_keys
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The KVS system shall support UTF-8 encoded strings as valid key types.

.. feat_req:: Supported Datatypes (Values)
   :id: feat_req__kvs__supported_datatypes_values
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The KVS system shall support storing both primitive and non-primitive datatypes as values.
   The supported datatypes shall match those used by the IPC feature.

.. feat_req:: Default Values
   :id: feat_req__kvs__default_values
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The KVS system shall support predefined default values for keys.

.. feat_req:: Default Value Retrieval
   :id: feat_req__kvs__default_value_retrieval
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The KVS system shall support retrieving the default value associated with a key.

.. feat_req:: Default Value Reset
   :id: feat_req__kvs__default_value_reset
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The KVS system shall support resetting a single key or all keys to their respective default values.

.. feat_req:: Persistency
   :id: feat_req__kvs__persistency
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The KVS system shall persist stored data and provide an API to explicitly trigger persistence.

.. feat_req:: Integrity Check
   :id: feat_req__kvs__integrity_check
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The KVS system shall detect and report data corruption.
   Note: Implementation depends on AoUs.

.. feat_req:: Versioning
   :id: feat_req__kvs__versioning
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The KVS system shall support versioning for different layout configurations.

.. feat_req:: Update Mechanism
   :id: feat_req__kvs__update_mechanism
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The KVS system shall implement mechanisms to upgrade from one version to another, including multi-version jumps.

.. feat_req:: Snapshots
   :id: feat_req__kvs__snapshots
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The KVS system shall support explicit creation of snapshots identified by unique IDs and allow rollback to previous snapshots.
   Snapshots shall also be deletable.

.. feat_req:: Tooling
   :id: feat_req__kvs__tooling
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The KVS system shall provide tooling support for viewing and modifying key-value pairs during development and debugging.

.. feat_req:: Stable APIs
   :id: feat_req__kvs__stable_api
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__stable_app_inter
   :status: valid

   The KVS API shall remain stable throughout its lifecycle while enabling the addition of new functionalities.

.. feat_req:: Variant management support
   :id: feat_req__kvs__variant_management
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__overall_goals__variant_management
   :status: valid

   The KVS shall ensure compatibility across different architectures and versions.

.. feat_req:: Set default key values via file
   :id: feat_req__kvs__default_value_file
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   The KVS shall support the configuration of default key values using an external file.

.. feat_req:: Configure limits via file
   :id: feat_req__kvs__config_file
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   The KVS shall support the configuration of memory and other resource limits via a configuration file.

.. feat_req:: Store persistent data
   :id: feat_req__kvs__persist_data
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__data_persistency
   :status: valid

   The KVS shall support storing and loading its data to and from persistent storage.

.. feat_req:: Support engineering and field mode
   :id: feat_req__kvs__dev_mode
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__safety_features
   :status: valid

   The KVS shall provide both engineering (developer) and field modes.
   The engineering mode shall allow unrestricted data access.

.. feat_req:: Provide an async API
   :id: feat_req__kvs__async_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dependability__availability, stkh_req__app_architectures__support_request
   :status: valid

   The KVS shall provide an asynchronous API for accessing and manipulating data.

.. feat_req:: Separate data stores
   :id: feat_req__kvs__access_control
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The KVS shall ensure that only authorized components can access individual data stores.

.. feat_req:: Data-change events
   :id: feat_req__kvs__events
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__app_architectures__support_data
   :status: valid

   The KVS shall provide an API that allows for the registration of callback
   functions. These callbacks shall be invoked in response to specific events,
   such as when keys are changed or removed.

.. feat_req:: Fast access
   :id: feat_req__kvs__fast_access
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__short_app_cycles
   :status: valid

   The KVS shall ensure that key operations are typically completed within 5 milliseconds.

.. feat_req:: Intra-Process Data Access
   :id: feat_req__kvs__intra_process_comm
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__intra_process
   :status: valid

   The KVS shall support concurrent intra-process data access.

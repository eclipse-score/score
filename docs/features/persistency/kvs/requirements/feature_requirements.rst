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

Feature Requirements
####################

.. feat_req:: C++ & Rust Interoperability
   :id: feat_req__kvs__cpp_rust_interoperability
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__prog_languages
   :status: valid

   The key-value storage shall allow concurrent access via C++ and Rust interfaces.

.. feat_req:: Maximum Size
   :id: feat_req__kvs__maximum_size
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall have a maximum size defined at compile time.

.. feat_req:: Thread Safety
   :id: feat_req__kvs__thread_safety
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow thread safe access per key.

.. feat_req:: Multiple KVS per Software Architecture Element
   :id: feat_req__kvs__multiple_kvs
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow to instantiate multiple key-value storages per software architecture element.

.. feat_req:: Supported Datatypes (Keys)
   :id: feat_req__kvs__supported_datatypes_keys
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow only UTF-8 encoded strings as keys.

.. feat_req:: Supported Datatypes (Values)
   :id: feat_req__kvs__supported_datatypes_values
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow the storage of primitive and non-primitive datatypes as values.
   The allowed datatypes shall be identical to the ones in the IPC feature.

.. feat_req:: Default Values
   :id: feat_req__kvs__default_values
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall support default values for each key.
   The default values shall be pre-defined in a configuration file.

   Note: Not each key does require a default value.

.. feat_req:: Default Value Retrieval
   :id: feat_req__kvs__default_value_retrieval
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow the retrieval of a key's default value.

.. feat_req:: Default Value Reset
   :id: feat_req__kvs__default_value_reset
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow the reset of a specific key or all keys to its/their default value(s).

.. feat_req:: Persistency
   :id: feat_req__kvs__persistency
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall store the data persistent. It shall provide an API to trigger the persistency.

.. feat_req:: Integrity Check
   :id: feat_req__kvs__integrity_check
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall detect data corruption. TODO: Dependent on AoUs.

.. feat_req:: Versioning
   :id: feat_req__kvs__versioning
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall support the versioning of different layouts.

.. feat_req:: Update Mechanism
   :id: feat_req__kvs__update_mechanism
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall implement a mechanism to support the update from one version to another version.
   In addition, multiple version jumps at once shall be supported.

.. feat_req:: Snapshots
   :id: feat_req__kvs__snapshots
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow the explicit creation of snapshots of a specific version and
   shall support the roll-back to previous snapshots, e.g. in case the integrity check fails or an rolled-back update.
   The snapshots shall be associated with an unique ID to be referenced.

   The key-value storage shall allow the deletion of snapshots.

.. feat_req:: Tooling
   :id: feat_req__kvs__tooling
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall support tooling to view and modify key-value pairs for development and debugging purposes.

.. feat_req:: Stable APIs
   :id: feat_req__kvs__stable_api
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__stable_app_inter
   :status: valid

   The KVS API will be designed to provide a stable interface over the
   lifecylcle without preventing new functionality from beeing implemented.

.. feat_req:: Variant management support
   :id: feat_req__kvs__variant_management
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__overall_goals__variant_management
   :status: valid

   The KVS ensures compatibilty between architectures and versions.

.. feat_req:: Set default key values via file
   :id: feat_req__kvs__default_value_file
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   The KVS allows to configure default key values by using a file.

.. feat_req:: Configure limits via file
   :id: feat_req__kvs__config_file
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   The KVS allows to configure memory and other limits by using a config file.

.. feat_req:: Store persistent data
   :id: feat_req__kvs__persist_data
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__data_persistency
   :status: valid

   The KVS must be able to store and load its data to/from a persistent
   storage.

.. feat_req:: Support ASIL-B
   :id: feat_req__kvs__safety_asil_b
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__automotive_safety
   :status: valid

   The KVS must support at least ASIL-B.

.. feat_req:: Support engineering and field mode
   :id: feat_req__kvs__dev_mode
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__safety_features
   :status: valid

   The KVS must support an engineering (developer) and a field mode. The
   engineering must provide a way to to access all data without restrictions.

.. feat_req:: Provide an async API
   :id: feat_req__kvs__async_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dependability__availability, stkh_req__app_architectures__support_request
   :status: valid

   The KVS must provide an async API.

.. feat_req:: Separate data stores
   :id: feat_req__kvs__access_control
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The KVS must make sure that data stores can only be accessed by allowed components.

.. feat_req:: Data-change events
   :id: feat_req__kvs__events
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__app_architectures__support_data
   :status: valid

   The KVS must provide an API to register callbacks which will be called for
   several events like keys are changed or removed.

.. feat_req:: Fast access
   :id: feat_req__kvs__fast_access
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__short_app_cycles
   :status: valid

   The KVS must ensure that operations are usually done in under 5 ms.

.. feat_req:: Fast startup
   :id: feat_req__kvs__fast_startup
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__startup_perf
   :status: valid

   The KVS must ensure that the startup time, besides the time that is needed
   to read the files from the filesystem, must be very short in terms of
   initial parsing and hash checking.

.. feat_req:: Intra-process communication
   :id: feat_req__kvs__intra_process_comm
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__intra_process
   :status: valid

   The KVS must support concurrent access to the data.

.. feat_req:: Multi-architecture support
   :id: feat_req__kvs__multi_arch
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__hardware_support__chipset_support
   :status: valid

   The KVS must run on all S-CORE platforms.

.. feat_req:: Logging and tracing
   :id: feat_req__kvs__log_trace
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The KVS must use the provided S-CORE logging and tracing framework.

.. feat_req:: Development steering
   :id: feat_req__kvs__dev_steering
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__re_requirements__traceability
   :status: valid

   Requirements must be linked to top-level (Stakeholder) requirements.

.. feat_req:: Document requirements as code
   :id: feat_req__kvs__req_as_code
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__requirements__as_code
   :status: valid

   Requirements must be documented as code.

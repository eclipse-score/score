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

.. _feature_persistency_requirements:

Requirements
############

.. document:: Persistency Requirements
   :id: doc__feature_persistency_requirements
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feat_request
   :tags: persistency

.. feat_req:: C++ and Rust language support
   :id: feat_req__persistency__cpp_rust
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__prog_languages
   :status: valid

   The Persistency shall provide native API support for both C++ and Rust programming languages.

.. feat_req:: Operating system agnostic implementation
   :id: feat_req__persistency__os_agnostic
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__operating_system
   :status: valid

   The Persistency shall be operating system agnostic.

.. feat_req:: Variant management support
   :id: feat_req__persistency__variant_management
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__overall_goals__variant_management
   :status: valid

   The Persistency shall ensure compatibility across different SW versions.

.. feat_req:: Dynamic memory allocation during runtime
   :id: feat_req__persistency__dynamic_memory_alloc
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall not allocate dynamic memory during runtime. All required dynamic memory shall be allocated during initialization.

   .. note::

      Dynamic memory allocation violates freedom from interference as the `HEAP` is a shared resource on OS process level.
      Additionally, fragmentation of the `HEAP` can lead to non-deterministic behavior of the application.

.. feat_req:: Multiple KVS per application
   :id: feat_req__persistency__multiple_kvs
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__data_persistency
   :status: valid

   The Persistency shall support multiple independent storages per application.

.. feat_req:: Access from multiple applications
   :id: feat_req__persistency__multiple_app
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall prevent access to a single KVS instance from multiple OS processes.

   .. note::
      Access from multiple OS processes violates freedom from interference, as applications can modify the same data concurrently.

.. feat_req:: Separate data stores
   :id: feat_req__persistency__access_control
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The Persistency shall ensure that only authorized applications can access individual data stores.

   .. note::
      Access control is essential to prevent unauthorized access and modification of sensitive data.
      The Persistency shall implement mechanisms to enforce access control policies based on user roles and permissions.

.. feat_req:: Configuration
   :id: feat_req__persistency__cfg
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__file_based
   :status: valid
   :tags: config

   The Persistency shall support configuration via a configuration file.
   The configuration shall include:

   - Global settings:
      - Maximum number of KVS instances
      - Maximum size of a key

   - Settings for KVS instance:
      - Instance identifier
      - Storage URI
      - Maximum number of Key-Value pairs
      - Maximum number of snapshots
      - Maximum consumed storage size (Including all metadata and redundant data)
      - Security settings
      - Redundancy settings
      - Backend specific settings

   Configuration file shall be optional and all configuration attributes shall have sensible default values defined at compile time.

   .. note::
      To improve the user experience during rapid prototyping, the Persistency shall also be able to operate without a configuration file.

.. feat_req:: Supported datatypes (Keys)
   :id: feat_req__persistency__support_datatype_keys
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall support UTF-8 encoded strings as valid key types.

.. feat_req:: Supported datatypes (Values)
   :id: feat_req__persistency__support_datatype_value
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid
   :tags: persistency

   The Persistency shall support storing both primitive and non-primitive (composite) datatypes as values.

.. feat_req:: Default values
   :id: feat_req__persistency__default_values
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall support predefined default values for keys.

.. feat_req:: Provisioning of default values via external file
   :id: feat_req__persistency__default_value_file
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   The Persistency shall support import of default values using an external file.

   .. note::
      Default values are read-only and cannot be modified at runtime. This requirement addresses the provisioning of default values
      during initial deployment. See :need:`feat_req__persistency__tooling`.

.. feat_req:: Retrieval of default values
   :id: feat_req__persistency__default_value_get
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall support retrieval of the default value associated with a key.

.. feat_req:: Reset to default values
   :id: feat_req__persistency__reset_to_default
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall support reset of individual key or all keys to their default values.
   This is only applicable for existing keys that have a predefined default value.

.. feat_req:: Store persistent data
   :id: feat_req__persistency__store_data
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__data_persistency
   :status: valid

   The Persistency shall support storing of key-value pairs to persistent storage.

.. feat_req:: Reset resistant storage
   :id: feat_req__persistency__reset_resistant
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall ensure that write operations are reset resistant to prevent data corruption in case of expected or unexpected interruption.

   .. note::
      As the constant power supply can not be guaranteed in embedded systems, it is essential to ensure that write operations are completed
      successfully, or rolled back to the previous state in case of any kind of interruption.

.. feat_req:: Recovery from reset
   :id: feat_req__persistency__recovery_from_reset
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall recover to a consistent state after reset.

   .. note::
      After a reset, the Persistency shall ensure that all key-value pairs are in a consistent state, reflecting either the last successful write operation or the previous consistent state.

.. feat_req:: Atomic store operation
   :id: feat_req__persistency__atomic_store
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall support atomic write operation for entire storage to ensure data consistency.

   .. note::

      Atomic write operation guarantee that either all key-value pairs are written, or no changes are made at all.
      This is required to prevent malfunctions when individual key-value pairs are dependent on each other.

.. feat_req:: Write amplification minimization
   :id: feat_req__persistency__write_amplification
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__app_architectures__support_data
   :status: valid

   The Persistency shall minimize the write amplification during data storage operations to enhance performance and prolong the lifespan of the underlying storage medium.

   .. note::
      Write amplification refers to the phenomenon where the amount of data written to the storage medium exceeds the amount of user data intended to be written.
      Minimizing write amplification is crucial for optimizing performance and reducing wear on storage devices, especially in embedded systems with limited number of program-erase cycles.

.. feat_req:: Load persistent data
   :id: feat_req__persistency__load_data
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__data_persistency
   :status: valid

   The Persistency shall support loading of key-value pairs from persistent storage.

.. feat_req:: Cached access
   :id: feat_req__persistency__cached_access
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall support caching mechanisms to improve access times for frequently accessed key-value pairs.

.. feat_req:: Direct access
   :id: feat_req__persistency__direct_access
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__availability
   :status: valid

   The Persistency shall support direct access to key-value pairs without the necessity to load the entire storage to RAM in advance.

   .. note::
      Direct access improves availability of data and reduces memory consumption for large data sets.

.. feat_req:: Integrity check
   :id: feat_req__persistency__integrity_check
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall detect and report data integrity issues.

.. feat_req:: Confidential storage
   :id: feat_req__persistency__confidential_storage
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__functional_req__data_persistency
   :status: valid

   The Persistency shall support confidential storage of key-value pairs using encryption mechanisms.

   .. note::
      Confidential storage is essential to protect sensitive data from unauthorized access, especially in scenarios where the storage medium may be exposed to potential threats.

.. feat_req:: Multiple storage backends
   :id: feat_req__persistency__storage_backends
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall support multiple storage backends.
   More than one storage backend of the same type shall be optionally supported for the sake of redundancy.
   The storage backends shall be compile time configurable for each KVS instance.

   .. note::
      Storage backend represents an abstraction for the underlying storage format and mechanism.
      Configurable storage backends allow the user to select the most suitable solution for their specific use case (Performance, easy of use, resource consumption, ...).

.. feat_req:: Asynchronous operation
   :id: feat_req__persistency__async_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__availability, stkh_req__app_architectures__support_request
   :status: valid

   The Persistency shall provide an asynchronous API for time consuming operations like loading and storing of data.

.. feat_req:: Signalling completion of asynchronous operation
   :id: feat_req__persistency__async_completion
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__app_architectures__support_data
   :status: valid

   The Persistency shall provide a mechanism to signal the completion of an asynchronous operations to the application.

.. feat_req:: Snapshot create
   :id: feat_req__persistency__snapshot_create
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall support explicit creation of snapshots. Snapshots are identified by unique IDs.
   Snapshots shall also include the version of the data layout. See :need:`feat_req__persistency__versioning`.

   .. note::
      Snapshots are point-in-time, read-only view on all key-value pairs at moment of snapshot creation. They are typically used for backup and rollback purposes.
      Implicit snapshots (e.g. created during store operation) shall be prevented to reduce storage consumption.

.. feat_req:: Snapshot restore
   :id: feat_req__persistency__snapshot_restore
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall support explicit restoration of snapshots.

.. feat_req:: Snapshot remove
   :id: feat_req__persistency__snapshot_remove
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall support explicit removal of snapshots.

.. feat_req:: Intra-Process data access
   :id: feat_req__persistency__concurrency
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__intra_process
   :status: valid

   The Persistency shall support concurrent access to key-value pairs from multiple threads within the same process.

.. feat_req:: Versioning
   :id: feat_req__persistency__versioning
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall support versioning for different data representation of KVS.

   .. note::
      Versioning is essential to ensure compatibility between different versions of the Persistency and the stored data.
      Each version shall be uniquely identifiable and include information of the data layout and structure.

.. feat_req:: Update Mechanism
   :id: feat_req__persistency__update_mechanism
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__overall_goals__variant_management
   :status: valid

   The Persistency shall implement mechanisms to upgrade from one version to another, including multi-version jumps.

.. feat_req:: Random access time
   :id: feat_req__persistency__fast_access
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__execution_model__short_app_cycles
   :status: valid

   The Persistency shall ensure that random read access for key-value pair is completed with constant or logarithmic time complexity relative to the number of stored key-value pairs.

.. feat_req:: Tooling
   :id: feat_req__persistency__tooling
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__support_of_store
   :status: valid

   The Persistency shall provide tooling support for:

   - viewing and modifying key-value pairs during development, testing and debugging
   - provisioning of default values via external file

.. feat_req:: Support development mode
   :id: feat_req__persistency__dev_mode
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__safety_features
   :status: valid

   The Persistency shall support the development mode.
   The development mode shall allow unrestricted data access and bypass security policies.

.. feat_req:: Support production mode
   :id: feat_req__persistency__prod_mode
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__safety_features
   :status: valid

   The Persistency shall support the production mode.
   The production mode should enforce the most restrictive data access controls feasible.

.. needextend:: docname is not None and "persistency/requirements" in docname
   :+tags: persistency


.. _feature_persistency_requirements_aou:

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

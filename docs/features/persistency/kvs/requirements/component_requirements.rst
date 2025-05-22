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

Component Requirements
######################

.. comp_req:: Key Handling
   :id: comp_req__kvs__key_handling
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__supported_datatypes_keys
   :status: valid

   The component shall accept keys that consist solely of alphanumeric characters, underscores, or dashes.
   The component shall encode each key as valid UTF-8.
   The component shall guarantee that each key is unique.
   The component shall limit the maximum length of a key to 32 bytes.

.. comp_req:: Value Handling
   :id: comp_req__kvs__value_handling
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__supported_datatypes_values,feat_req__kvs__default_values
   :status: valid

   The component shall accept only values of the following data types: Number, String, Null, Array[Value], or Dictionary{Key:Value}.
   The component shall serialize and deserialize all values to and from JSON.
   The component shall limit the maximum length of a value to 1024 bytes.
   The component shall support unset values and shall provide a default value when a value is unset.
   The component shall allow resetting a value to its default if a default is defined.

.. comp_req:: Default Value Handling
   :id: comp_req__kvs__default_value_handling
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__default_values,feat_req__kvs__default_value_retrieval,feat_req__kvs__default_value_reset,feat_req__kvs__default_value_file
   :status: valid

   The component shall accept default values of only permitted value data types.
   The component shall provide an API to retrieve default values.
   The component shall allow configuration of default values in code or in a separate configuration file.
   The component shall secure the configuration file for default values with an associated checksum file when default values are stored in a file.

.. comp_req:: Constraint Configuration
   :id: comp_req__kvs__constraints
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__config_file
   :status: valid

   The component shall allow configuration of KVS constraints at compile-time using source code constants or at runtime using a configuration file.

.. comp_req:: Language Agnostic
   :id: comp_req__kvs__language_agnostic
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__cpp_rust_interoperability
   :status: valid

   The component shall provide an API that supports bindings to other languages or shall use a storage and memory exchange format that is adaptable to other languages.

.. comp_req:: Concurrency
   :id: comp_req__kvs__concurrency
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__intra_process_comm
   :status: valid

   The component shall implement thread-safe mechanisms to enable concurrent access to data without data races.

.. comp_req:: Multi-Instance
   :id: comp_req__kvs__multi_instance
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__multiple_kvs
   :status: valid

   The component shall manage all runtime variables within an instance to enable creation and use of multiple KVS instances concurrently within a single software architecture element.

.. comp_req:: Persistent Data Storage
   :id: comp_req__kvs__persistent_data_storage
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__persistency,feat_req__kvs__integrity_check,feat_req__kvs__persist_data
   :status: valid

   The component shall use the file API and the JSON data format to persist data.
   The component shall generate a checksum for each data file and shall store it alongside the data.
   The component shall verify the checksum when loading data.

.. comp_req:: Persistent Data Schema Handling
   :id: comp_req__kvs__persistent_data_schema
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__versioning,feat_req__kvs__update_mechanism
   :status: valid

   The component shall not provide built-in versioning.
   The component shall use a JSON file storage format that enables the application to implement versioning, including upgrade and downgrade paths, as needed.

.. comp_req:: Snapshots
   :id: comp_req__kvs__snapshots
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__snapshots
   :status: valid

   The component shall create a snapshot each time data is stored.
   The component shall maintain a configurable maximum number of snapshots.
   The component shall assign the ID 1 to the newest snapshot and shall increment the IDs of older snapshots accordingly.
   The component shall rotate and delete the oldest snapshot when the maximum number is reached.
   The component shall allow restoration of a snapshot by its ID.
   The component shall allow deletion of individual snapshots.

.. comp_req:: Develop Mode
   :id: comp_req__kvs__dev_mode
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__dev_mode
   :status: valid

   The component shall provide a developer mode that can be enabled during build time to display debugging and internal information.

.. comp_req:: Async API
   :id: comp_req__kvs__async_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__async_api
   :status: valid

   The component shall provide an asynchronous API in addition to the standard API.

.. comp_req:: Permission Handling
   :id: comp_req__kvs__permission_handling
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__access_control
   :status: valid

   The component shall rely on the underlying filesystem for access and permission management and shall not implement its own access or permission controls.
   The component shall report any access or permission errors encountered at the filesystem level to the application.

.. comp_req:: Callback Support
   :id: comp_req__kvs__callback_support
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__events
   :status: valid

   The component shall provide an API for registering callbacks that are triggered by data change events.

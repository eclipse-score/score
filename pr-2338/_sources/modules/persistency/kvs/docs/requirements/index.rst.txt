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

.. document:: Persistency KVS Requirements
   :id: doc__persistency_kvs_requirements
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__requirements_comp

.. comp_req:: Key Naming
   :id: comp_req__persistency__key_naming
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__support_datatype_keys
   :status: valid

   The component shall accept keys that consist solely of alphanumeric characters, underscores, or dashes.

.. comp_req:: Key Encoding
   :id: comp_req__persistency__key_encoding
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__support_datatype_keys
   :status: valid

   The component shall encode each key as valid UTF-8.

.. comp_req:: Key Uniqueness
   :id: comp_req__persistency__key_uniqueness
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__support_datatype_keys
   :status: valid

   The component shall guarantee that each key is unique.

.. comp_req:: Key Length
   :id: comp_req__persistency__key_length
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__support_datatype_keys
   :status: valid

   The component shall limit the maximum length of a key to 32 bytes.

.. comp_req:: Value Data Types
   :id: comp_req__persistency__value_data_types
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__support_datatype_value
   :status: valid

   The component shall accept only values of the following data types: Number,
   String, Null, Array[Value], or Dictionary{Key:Value}.

.. comp_req:: Value Serialization
   :id: comp_req__persistency__value_serialize
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__support_datatype_value
   :status: valid

   The component shall serialize and deserialize all values to and from JSON.

.. comp_req:: Value Length
   :id: comp_req__persistency__value_length
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__support_datatype_value
   :status: valid

   The component shall limit the maximum length of a value to 1024 bytes.

.. comp_req:: Value Default
   :id: comp_req__persistency__value_default
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__support_datatype_value,feat_req__persistency__default_values
   :status: valid

   The component shall support unset values and shall provide a default value
   when a value is unset.

.. comp_req:: Value Reset
   :id: comp_req__persistency__value_reset
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__support_datatype_value,feat_req__persistency__default_values
   :status: valid

   The component shall allow resetting a value to its default if a default is
   defined.

.. comp_req:: Default Value Datatypes
   :id: comp_req__persistency__default_value_types
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__default_values,feat_req__persistency__default_value_get,feat_req__persistency__reset_to_default,feat_req__persistency__default_value_file
   :status: valid

   The component shall accept default values of only permitted value data
   types.

.. comp_req:: Default Value Query
   :id: comp_req__persistency__default_value_query
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__default_values,feat_req__persistency__default_value_get,feat_req__persistency__reset_to_default,feat_req__persistency__default_value_file
   :status: valid

   The component shall provide an API to retrieve default values.

.. comp_req:: Default Value Config
   :id: comp_req__persistency__default_value_config
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__default_values,feat_req__persistency__default_value_get,feat_req__persistency__reset_to_default,feat_req__persistency__default_value_file
   :status: valid

   The component shall allow configuration of default values in code or in a
   separate configuration file.

.. comp_req:: Default Value Checksum
   :id: comp_req__persistency__default_value_checksum
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__default_values,feat_req__persistency__default_value_get,feat_req__persistency__reset_to_default,feat_req__persistency__default_value_file
   :status: valid

   The component shall secure the configuration file for default values with an
   associated checksum file when default values are stored in a file.

.. comp_req:: Constraint Configuration
   :id: comp_req__persistency__constraints
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__cfg
   :status: valid

   The component shall allow configuration of KVS constraints at compile-time
   using source code constants or at runtime using a configuration file.

.. comp_req:: Concurrency
   :id: comp_req__persistency__concurrency
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__concurrency
   :status: valid

   The component shall implement thread-safe mechanisms to enable concurrent
   access to data without data races.

.. comp_req:: Multi-Instance
   :id: comp_req__persistency__multi_instance
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__multiple_kvs
   :status: valid

   The component shall manage all runtime variables within an instance to
   enable creation and use of multiple KVS instances concurrently within a
   single software architecture element.

.. comp_req:: Persistent Data Storage Components
   :id: comp_req__persistency__persist_data_store_com
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__integrity_check,feat_req__persistency__store_data
   :status: valid

   The component shall use the file API and the JSON data format to persist data.

.. comp_req:: Persistent Data Storage Checksum Write
   :id: comp_req__persistency__pers_data_csum_write
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__integrity_check,feat_req__persistency__store_data
   :status: valid

   The component shall generate a checksum for each data file and shall store
   it alongside the data.

.. comp_req:: Persistent Data Storage Checksum Verify
   :id: comp_req__persistency__pers_data_csum_verify
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__integrity_check,feat_req__persistency__load_data
   :status: valid

   The component shall verify the checksum when loading data.

.. comp_req:: Persistent Data Storage Backend
   :id: comp_req__persistency__pers_data_store_bend
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__integrity_check,feat_req__persistency__store_data
   :status: valid

   The component shall use the file API to persist data.

.. comp_req:: Persistent Data Storage Format
   :id: comp_req__persistency__pers_data_store_fmt
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__integrity_check,feat_req__persistency__store_data
   :status: valid

   The component shall use the JSON data format to persist data.

.. comp_req:: Persistent Data Versioning
   :id: comp_req__persistency__pers_data_version
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__versioning,feat_req__persistency__update_mechanism
   :status: valid

   The component shall not provide built-in versioning.

.. comp_req:: Persistent Data Schema
   :id: comp_req__persistency__pers_data_schema
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__versioning,feat_req__persistency__update_mechanism
   :status: valid

   The component shall use a JSON file storage format that enables the
   application to implement versioning, including upgrade and downgrade paths,
   as needed.

.. comp_req:: Snapshot Creation
   :id: comp_req__persistency__snapshot_creation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__snapshot_create
   :status: valid

   The component shall create a snapshot each time data is stored.

.. comp_req:: Snapshot Maximum Number
   :id: comp_req__persistency__snapshot_max_num
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__cfg
   :status: valid

   The component shall maintain a configurable maximum number of snapshots.

.. comp_req:: Snapshot IDs
   :id: comp_req__persistency__snapshot_id
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__snapshot_create
   :status: valid

   The component shall assign the ID 1 to the newest snapshot and shall increment the IDs of older snapshots accordingly.

.. comp_req:: Snapshot Rotation
   :id: comp_req__persistency__snapshot_rotate
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__snapshot_remove, feat_req__persistency__snapshot_restore
   :status: valid

   The component shall rotate and delete the oldest snapshot when the maximum number is reached.

.. comp_req:: Snapshot Restore
   :id: comp_req__persistency__snapshot_restore
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__snapshot_restore
   :status: valid

   The component shall allow restoration of a snapshot by its ID.

.. comp_req:: Snapshot Deletion
   :id: comp_req__persistency__snapshot_delete
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__snapshot_remove
   :status: valid

   The component shall allow deletion of individual snapshots.

.. comp_req:: Engineering Mode
   :id: comp_req__persistency__eng_mode
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__dev_mode
   :status: valid

   The component shall provide an engineering mode that can be enabled during
   build time to display debugging and internal information.

.. comp_req:: Field Mode
   :id: comp_req__persistency__field_mode
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__prod_mode
   :status: valid

   The component shall provide a field mode that can be enabled during build
   time to restrict access as much as possible.

.. comp_req:: Async API
   :id: comp_req__persistency__async_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__async_api
   :status: valid

   The component shall provide an asynchronous API in addition to the standard API.

.. comp_req:: Permission Control
   :id: comp_req__persistency__permission_control
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__access_control
   :status: valid

   The component shall rely on the underlying filesystem for access and
   permission management and shall not implement its own access or permission
   controls.

.. comp_req:: Permission Error Handling
   :id: comp_req__persistency__permission_err_handle
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__access_control
   :status: valid

   The component shall report any access or permission errors encountered at
   the filesystem level to the application.

.. comp_req:: Callback Support
   :id: comp_req__persistency__callback_support
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__persistency__async_api, feat_req__persistency__async_completion
   :status: valid

   The component shall provide an API for registering callbacks that are triggered by data change events.

.. needextend:: docname is not None and "persistency/kvs/docs/requirements" in docname
   :+tags: kvs

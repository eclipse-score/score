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

   The key must contain only alphanumerical characters, underscores and dashes.
   The key must be valid UTF-8.
   The key must be unique.
   The key must have a maximum length of 32 bytes.

.. comp_req:: Value Handling
   :id: comp_req__kvs__value_handling
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__supported_datatypes_values,feat_req__kvs__default_values
   :status: valid

   The value must have one of these datatypes: Number, String, Null, Array[Value], Dictionary{Key:Value}.
   The value must be serializeable and deserializeable to JSON.
   The value must have a maximum length of 1024 bytes.
   The value can be no-set and provide a default value for this case.
   If the value has a default value assigned it must be resetable to the default value.

.. comp_req:: Default Value Handling
   :id: comp_req__kvs__default_value_handling
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__default_values,feat_req__kvs__default_value_retrieval,feat_req__kvs__default_value_reset,feat_req__kvs__default_value_file
   :status: valid

   The default value can be available.
   The default value must contain any of the valid value datatypes.
   The default value must be retrieval through an extra API.
   The default value must be configurable either in code or in a separate file.
   If the default value is stored in a file the file must be secured by a checksum file.

.. comp_req:: Constraint Configuration
   :id: comp_req__kvs__constraints
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__maximum_size,feat_req__kvs__config_file
   :status: valid

   The key-value-storage constraints must be configurable at compile-time
   through source code constants or dynamically at runtime with a config file.

.. comp_req:: Language Agnostic
   :id: comp_req__kvs__language_agnostic
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__cpp_rust_interoperability
   :status: valid

   The key-value-storage must either provide an API that can be bind to other
   languages or use a storage and memory exchange-format that can be adapted to
   other languages.

.. comp_req:: Concurrency
   :id: comp_req__kvs__concurrency
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__thread_safety,feat_req__kvs__intra_process_comm
   :status: valid

   The key-value-storage must implement thread-safe mechanisms to allow
   concurrent access to the data without data races.

.. comp_req:: Multi-Instance
   :id: comp_req__kvs__multi_instance
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__multiple_kvs
   :status: valid

   The key-value-storage must manage all runtime variables in an instance so
   that multiple instances with different key-value-stores can be spawned and
   used at the same time per software architecture element.

.. comp_req:: Persistent Data Storage
   :id: comp_req__kvs__persistent_data_storage
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__persistency,feat_req__kvs__integrity_check,feat_req__kvs__persist_data
   :status: valid

   The key-value-storage must use the file API and the JSON data format for
   persistent data storage.
   A checksum must be build over the data file and stored next to the data.
   On data load the checksum must be verified.

.. comp_req:: Persistent Data Schema Handling
   :id: comp_req__kvs__persistent_data_schema
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__versioning,feat_req__kvs__update_mechanism
   :status: valid

   The key-value-storage doesn't support versioning directly.
   The used JSON file storage format allows the application to implement
   versioning, including up- and down-paths, by itself.

.. comp_req:: Snapshots
   :id: comp_req__kvs__snapshots
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__snapshots
   :status: valid

   The key-value-storage must write a snapshot whenever the data is stored.
   It must maintain a configurable maximum number of snapshots.
   Each new snapshot has id 1 and all older snapshots get their id increased..
   After the maximum snapshot number is reached the snapshots are rotated and the oldest snapshot is dropped.
   Each snapshot can be restored by it's id.
   Snapshots must be deletable.

.. comp_req:: Develop Mode
   :id: comp_req__kvs__dev_mode
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__dev_mode
   :status: valid

   The key-value-storage must provide a developer mode which can be enabled
   during build time. This mode can be used to show debug and other internal
   information.

.. comp_req:: Async API
   :id: comp_req__kvs__async_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__async_api
   :status: valid

   Additional to the normal API the key-value-storage must provide an Async
   API.

.. comp_req:: Permission Handling
   :id: comp_req__kvs__permission_handling
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__access_control
   :status: valid

   The key-value-storage must not implement access and permission handling.
   This is left to the underlying filesystem implementation.
   The key-value-storage must report access and permission errors that are
   thrown by the filesystem to the application.

.. comp_req:: Callback Support
   :id: comp_req__kvs__callback_support
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__events
   :status: valid

   The key-value-storage must provide an API to register callbacks for
   data-change events.

.. comp_req:: Logging & Tracing
   :id: comp_req__kvs__log_trace
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__log_trace
   :status: valid

   The key-value-storage must use the S-CORE provided logging and tracing
   framework.

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

.. _feature_architecture_PersistencyKvs:

Architecture
============

.. document:: Persistency KVS Feature Architecture
   :id: doc__persistency_architecture
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__feature_arch
   :tags: persistency

Overview
--------

The Key-Value-Storage (kvs) provides the capability to efficiently store,
retrieve, and manage key-value pairs in a persistent storage system.

Description
-----------

- kvs organize data as pairs, where each unique key is associated with a specific value.
  The key acts as a unique identifier for getting the value.
- The data is persisted in JSON format to the file system, providing a human-readable,
  and widely supported way to store and manage key-value pairs.
- The JSON data persisted is according to RFC-8259.

Rationale Behind Architecture Decomposition
*******************************************

- The architecture is decomposed to include a dedicated JSON parser component (json) to facilitate the persistent storage of data in JSON format.
- The architecture is decomposed to include a FileStorage component (fs) to read and write to the file system.


Glossary
--------

- User: Program code that is written by a person that initiates the given
  functionality call or receives a callback.


Static Architecture
-------------------

.. feat_arc_sta:: Static Architecture
   :id: feat_arc_sta__persistency__static
   :security: YES
   :safety: ASIL_B
   :includes: logic_arc_int__persistency__interface
   :fulfils: feat_req__persistency__default_value_get,feat_req__persistency__default_values,feat_req__persistency__events,feat_req__persistency__integrity_check,feat_req__persistency__persist_data,feat_req__persistency__persistency,feat_req__persistency__snapshots,feat_req__persistency__support_datatype_keys,feat_req__persistency__support_datatype_value,feat_req__persistency__variant_management,feat_req__persistency__default_value_file,feat_req__persistency__config_file,feat_req__persistency__async_api,feat_req__persistency__access_control,feat_req__persistency__intra_process_comm
   :status: valid

   .. uml:: _assets/kvs_static_view.puml

Dynamic Architecture
--------------------
.. feat_arc_dyn:: Check if key contains default value
   :id: feat_arc_dyn__persistency__check_key_default
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__persistency__default_values,feat_req__persistency__default_value_get
   :status: valid

   .. uml:: _assets/kvs_dyn_check_value_default.puml

.. feat_arc_dyn:: Delete key from KVS instance
   :id: feat_arc_dyn__persistency__delete_key
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__persistency__events
   :status: valid

   .. uml:: _assets/kvs_dyn_delete_data_key.puml

.. feat_arc_dyn:: Flush to permanent storage
   :id: feat_arc_dyn__persistency__flush
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__persistency__persist_data,feat_req__persistency__persistency,feat_req__persistency__snapshots,feat_req__persistency__integrity_check,feat_req__persistency__snapshots
   :status: valid

   .. uml:: _assets/kvs_dyn_flush_local_repr_to_file.puml

.. feat_arc_dyn:: Read key value
   :id: feat_arc_dyn__persistency__read_key
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__persistency__support_datatype_keys,feat_req__persistency__support_datatype_value,feat_req__persistency__default_values,feat_req__persistency__default_value_get
   :status: valid

   .. uml:: _assets/kvs_dyn_read_data_key.puml

.. feat_arc_dyn:: Read data from permanent storage
   :id: feat_arc_dyn__persistency__read_from_storage
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__persistency__persist_data,feat_req__persistency__persistency,feat_req__persistency__integrity_check,feat_req__persistency__snapshots
   :status: valid

   .. uml:: _assets/kvs_dyn_read_file_into_local_repr.puml

.. feat_arc_dyn:: Write value to key
   :id: feat_arc_dyn__persistency__write_key
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__persistency__support_datatype_keys,feat_req__persistency__support_datatype_value
   :status: valid

   .. uml:: _assets/kvs_dyn_write_data_key.puml

.. feat_arc_dyn:: Restore snapshot
   :id: feat_arc_dyn__persistency__snapshot_restore
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__persistency__snapshots,feat_req__persistency__persist_data,feat_req__persistency__persistency
   :status: valid

   .. uml:: _assets/kvs_dyn_restore_snapshot.puml


Logical Interfaces
------------------

.. logic_arc_int:: Ikvs
   :id: logic_arc_int__persistency__interface
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__persistency__async_api
   :status: valid

   .. uml:: _assets/kvs_interface.puml

.. needextend:: docname is not None and "persistency/kvs/architecture" in docname
   :+tags: persistency

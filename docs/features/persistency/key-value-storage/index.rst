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

Key-value Storage
#################

.. document:: Key-Value Storage
   :id: DOC__KVS
   :status: draft
   :safety: ASIL_B
   :tags: contribution_request, feature_request

Feature flag
============

To activate this feature, use the following feature flag:

``experimental_kvs``

Abstract
========

This feature describes a key-value storage to be used within applications of the Eclipse S-CORE project,
independent of the used application framework. It shall enable applications to access and store persistent
data (primitive & non-primitive datatypes) associated with an unique key.


Motivation
==========

A key-value storage is used within many applications to store e.g. configuration data and is therefore
seen crucial for the Eclipse S-CORE platform.


Rationale
=========

n/a


Specification
=============

.. feat_req:: C++ & Rust Interoperability
   :id: FEAT_REQ__KVS__cpp_rust_interoperability
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__260, STKH_REQ__350
   :status: valid

   The key-value storage shall allow concurrent access via C++ and Rust interfaces.

.. feat_req:: Maximum Size
   :id: FEAT_REQ__KVS__maximum_size
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall have a maximum size defined at compile time.

.. feat_req:: Thread Safety
   :id: FEAT_REQ__KVS__thread_safety
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall allow thread safe access per key.

.. feat_req:: Multiple KVS per Software Architecture Element
   :id: FEAT_REQ__KVS__multiple_kvs
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall allow to instantiate multiple key-value storages per software architecture element.

.. feat_req:: Supported Datatypes (Keys)
   :id: FEAT_REQ__KVS__supported_datatypes_keys
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall allow only UTF-8 encoded strings as keys.

.. feat_req:: Supported Datatypes (Values)
   :id: FEAT_REQ__KVS__supported_datatypes_values
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall allow the storage of primitive and non-primitive datatypes as values.
   The allowed datatypes shall be identical to the ones in the IPC feature.

.. feat_req:: Default Values
   :id: FEAT_REQ__KVS__default_values
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall support default values for each key.
   The default values shall be pre-defined in a configuration file.

   Note: Not each key does require a default value.

.. feat_req:: Default Value Retrieval
   :id: FEAT_REQ__KVS__default_value_retrieval
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall allow the retrieval of a key's default value.

.. feat_req:: Default Value Reset
   :id: FEAT_REQ__KVS__default_value_reset
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall allow the reset of a specific key or all keys to its/their default value(s).

.. feat_req:: Persistency
   :id: FEAT_REQ__KVS__persistency
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall store the data persistent. It shall provide an API to trigger the persistency.

.. feat_req:: Integrity Check
   :id: FEAT_REQ__KVS__integrity_check
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall detect data corruption. TODO: Dependent on AoUs.

.. feat_req:: Versioning
   :id: FEAT_REQ__KVS__versioning
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall support the versioning of different layouts.

.. feat_req:: Update Mechanism
   :id: FEAT_REQ__KVS__update_mechanism
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall implement a mechanism to support the update from one version to another version.
   In addition, multiple version jumps at once shall be supported.

.. feat_req:: Snapshots
   :id: FEAT_REQ__KVS__snapshots
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall allow the explicit creation of snapshots of a specific version and
   shall support the roll-back to previous snapshots, e.g. in case the integrity check fails or an rolled-back update.
   The snapshots shall be associated with an unique ID to be referenced.

   The key-value storage shall allow the deletion of snapshots.

.. feat_req:: Tooling
   :id: FEAT_REQ__KVS__tooling
   :reqtype: Non-Functional
   :security: no
   :safety: ASIL_B
   :satisfies: STKH_REQ__350
   :status: valid

   The key-value storage shall support tooling to view and modify key-value pairs for development and debugging purposes.


Backwards Compatibility
=======================

[Describe potential impact (especially including safety and security impacts) and severity on pre-existing platform/project elements.]


Security Impact
===============

[How could a malicious user take advantage of this new feature?]

   .. note::
      If there are security concerns in relation to the Feature Request, those concerns should be explicitly written out to make sure reviewers of the Feature Request are aware of them.



Safety Impact
=============

Notes:
  - One key-value storage should not be used within different processes (freedom from interference) -> To be added to AoUs?

[How could the safety be impacted by the new feature?]

   .. note::
      If there are safety concerns in relation to the Feature Request, those concerns should be explicitly written out to make sure reviewers of the Feature Request are aware of them.
      ToDo - Link to the Safety Impact Method

[What is the expected ASIL level?]
[What is the expected classification of the contribution?]

   .. note::
      Use the component classification method here to classfiy your component, if it shall to be used in a safety context: (TODO: add link to component classification).


License Impact
==============

[How could the copyright impacted by the license of the new contribution?]


How to Teach This
=================

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

Key-Value-Storage
#################

.. document:: Persistency Key-Value-Storage
   :id: doc__persistency_kvs
   :status: draft
   :safety: ASIL_B
   :tags: contribution_request, feature_request

.. toctree::
   :hidden:

   requirements/index.rst


Feature flag
============

To activate this feature, use the following feature flag:

``persistency_kvs``


Abstract
========

This feature request describes the key-value storage (KVS) that is needed by
applications to store either temporary or permanent data in an easy way that
conforms to most programming languages that provide a hash, hashmap, dictionary
or similar data structure. Access to the KVS is possible from any support
language through language specific interfaces.


Motivation
==========

The current solutions available mostly don't meet the specific needs of the
S-CORE project like storing specific datatypes without a BASE64 conversation or
having no rollback/replay feature. Also the integration into analysis tools is
simpler when the solution grows with the needs instead having to adapt existing
data structures through wrapppers. Especially in the focus of security it will
be possible to build a system that integrates the layers from scratch and
provide them as API to any language whilst still using Rust as the backend.

A main USP of the solution will be the integration of a tracing framework that
allows to understand how events also in the context of other events interact.

A key-value storage is used within many applications to store e.g.
configuration data and is therefore seen crucial for the Eclipse S-CORE
platform.


Rationale
=========

1. There are multiple key-value storages allowed per application.

To allow for data separation and different levels of security, each application
is allowed to have multiple KVS.

2. There must be an update mechanism from different versions of a KVS to another version.

Staying compatible through updates and rollbacks is a main requirement for the
project.

3. The same KVS should be read/writable from C++ & Rust and any other language.

Having a flexible interface allows to focus on solutions where the language
fits the needs.

4. KVS should store default values.

If possible, all keys should return a configurable default value or the access
should return an error if the key needs to be written first.

5. KVS should use a simple data representation.

The KVS should use a data representation that supports versioned up- and
downgrading like JSON or Cap'n Proto and is easily debuggable by the developer.

6. Integrity of the KVS should be checked.

The KVS is always be in a consistent state that either provides the currently
stored data or if not possible the previous snapshot.


Backwards Compatibility
=======================

The API for the specific language tries to represent the language specific
implementation like hashmaps or dictionaries to be mostly backwards compatible
to already existing key-value-storage usage cases. Access without a safe error
handling path, like the array-operator in Rust which can panic, must be
avoided.


Security Impact
===============

Access to the key-value-storage would allow a malicious user to control the
behaviour of the device so it needs to be secured as much as possible, like
only providing debug access when a debug firmware image is installed.


Safety Impact
=============

   .. note::
      One key-value storage should not be used within different processes (freedom from interference) -> To be added to AoUs?

[How could the safety be impacted by the new feature?]

   .. note::
      If there are safety concerns in relation to the Feature Request, those concerns should be explicitly written out to make sure reviewers of the Feature Request are aware of them.
      ToDo - Link to the Safety Impact Method

[What is the expected ASIL level?]
[What is the expected classification of the contribution?]

   .. note::
      Use the component classification method here to classify your component, if it shall to be used in a safety context: (TODO: add link to component classification).


License Impact
==============

   .. note::
      The key-value storage itself uses the Apache-2.0 license. Licenses of
      used libraries are need to be checked.


How to Teach This
=================

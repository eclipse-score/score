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

Persistency (v0.5 alpha)
########################

.. document:: Persistency
   :id: doc__persistency
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__feat_request
   :tags: feature_request, persistency

.. toctree::
   architecture/index.rst
   architecture/chklst_arc_inspection.rst
   requirements/index.rst
   requirements/chklst_req_inspection.rst
   safety_analysis/fmea.rst
   safety_analysis/dfa.rst
   safety_planning/index.rst


Feature flag
============

To activate this feature, use the following feature flag:

``persistency``


Abstract
========

Persistency is a critical feature that ensures the long-term storage and
retrieval of data within S-CORE. It provides a reliable mechanism for
preserving information, allowing the application to maintain its state and data
integrity over time. This feature is essential for enabling the system to
resume operations seamlessly, even in the event of unexpected shutdowns or
system failures. By implementing robust persistence mechanisms, the application
can guarantee the persistence of user-generated content, configuration
settings, and other vital data, ensuring a consistent and reliable user
experience.

This feature request describes the key-value storage (KVS) that is needed by
applications to store either temporary or permanent data in an easy way that
conforms to most programming languages that provide a hash, hashmap, dictionary,
or similar data structure. Access to the KVS is possible from any supported
language through language-specific interfaces.

In the scope of S-CORE, an application can range from a system service to an
end-user visible UI. The application uses the KVS as an external memory store
to read and persist data as needed. For example, an application that controls
the air conditioning system in a car could use the KVS to store the current
temperature setting. When the car is started again, the application can
retrieve the temperature setting from the persistent KVS storage, providing a
seamless user experience by restoring the previous state.


Motivation
==========

The current solutions available mostly don't meet the specific needs of the
S-CORE project like storing specific datatypes without a BASE64 conversion or
having no rollback/replay feature. Also the integration into analysis tools is
simpler when the solution grows with the needs instead having to adapt existing
data structures through wrappers. Especially in the focus of security it will
be possible to build a system that integrates the layers from scratch and
provide them as API to any language whilst still using Rust as the backend.

A main USP of the solution will be the integration of a tracing framework that
allows to understand how events also in the context of other events interact.

A key-value storage is used within many applications to store e.g.
configuration data and is therefore seen crucial for the Eclipse S-CORE
platform.


Rationale
=========

1. | Requirement 1: Multiple key-value storages per application
   | Solution: Allow each application to have multiple key-value storages (KVS) to enable data separation and different levels of security.
2. | Requirement 2: Update mechanism for KVS versions
   | Solution: Implement an update mechanism to ensure compatibility through updates and rollbacks of different KVS versions.
3. | Requirement 3: Language-agnostic KVS interface
   | Solution: Design a flexible interface that allows the KVS to be read and written from multiple programming languages, including C++, Rust, and others.
4. | Requirement 4: Default values for KVS
   | Solution: Configure the KVS to store default values for all keys, returning either the default value or an error if the key needs to be written first.
5. | Requirement 5: Simple data representation for KVS
   | Solution: Utilize a simple data representation, such as JSON or Cap'n Proto, that supports versioned up- and downgrading and is easily debuggable by developers.
6. | Requirement 6: KVS integrity checking
   | Solution: Ensure the KVS maintains a consistent state, providing either the currently stored data or the previous snapshot if data retrieval is not possible.


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
behavior of the device, so it must be secured to prevent unauthorized access.
To achieve this, debug access should only be provided when a debug firmware
image is installed.


Safety Impact
=============

The expected ASIL level is ASIL-B. To reach this goal we will apply the S-CORE
development process. Key elements of it are listed in the process descriptions
of safety management and safety analysis. In the safety analysis we will
analyze the impact of the feature.

:need:`doc__persistency_fmea`

We use an iterative development process and apply results from the next steps
back to the feature request. For TinyJSON we will perform a software component
classification.

:need:`doc__persistency_component_classification`

To ensure the freedom of interference the feature key-value storage should not
be used within different processes.


License Impact
==============

.. note::
   The key-value storage itself uses the Apache-2.0 license. Licenses of
   used libraries are need to be checked.

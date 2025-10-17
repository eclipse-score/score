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

JSON-Library
============

.. document:: JSON-Library
   :id: doc__json
   :status: valid
   :safety: ASIL_B
   :tags: component_request


.. toctree::
   :hidden:

   requirements/index.rst
   architecture/index.rst
   json_wrapper/index.rst
   nlohman_json/index.rst


Abstract
========

This component request proposes the integration of a safe JSON-Library with parsing functionality.


Basic Functionality
----------------------
The component shall support parsing JSON data and convert that information to a compatible user format.


Future Extensions
----------------------
The component shall support a future extension for serializing from user format into JSON data.

Optional extensions which may be added if required:

* JSON schema validation.
* Compile-time parsing (used for test purposes to ensure that a component with errors cannot exist even in the absence of a pipeline).

Motivation
==========

S-CORE is targeting high-performance automotive systems with safety impact.
Some applications, like the IPC communication solution, require a safe JSON-Library with parsing functionality to enable loading of configuration information at runtime.
There is currently no solution for this inside S-CORE.

Rationale
=========

A JSON-Library with parsing functionality needs to be introduced in S-CORE software platform due to specific functional dependencies of different features (ex: IPC).

Further details are available in the following section:
.. _Specification:

Specification
=============

The following details and requirements describe the aspects of current feature in the context of S-CORE.

General considerations
----------------------

The JSON-Library should provide parsing, writing and data conversion capabilities:

* :need:`comp_req__json__deserialization`
* :need:`comp_req__json__serialization`
* :need:`comp_req__json__user_format`

User friendly API
-----------------

Programming languages have their own feature set and idioms.
It is crucial for any library that it seamlessly integrates into both.
This means, wherever possible and meaningful, infrastructure of the programming language and accompanying standard
libraries shall be reused.
Further, a developer used to the programming language shall have no problems understanding the API.
It should feel natural to use.
This includes error handling, which shall follow one of the error handling concepts of the programming language.

* :need:`comp_req__json__lang_idioms`
* :need:`comp_req__json__lang_infra`
* :need:`comp_req__json__type_compatibility`

Full testability for the public API
----------------------------------------

Our users will be required to proof certain coverage metrics, like line coverage or branch coverage.
For them to reach full coverage, they need to be easily able to mock or fake the public API of the JSON-Library in their unit tests.

* :need:`comp_req__json__full_testability`

Backwards Compatibility
=======================

As there is currently no previous solution in S-CORE, no backwards compatibility is required.

Security Impact
===============

[How could a malicious user take advantage of this new/modified component?]

Safety Impact
=============

Overall, the component shall support use cases up to ASIL-B:

* :need:`comp_req__json__asil`

License Impact
==============

[How could the copyright impacted by the license of the new contribution?]

How to Teach This
=================

[How to teach users, new and experienced, how to apply the CR to their work.]

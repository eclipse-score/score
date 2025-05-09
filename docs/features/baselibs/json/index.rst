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
===========================

.. document:: JSON-Library
   :id: doc__json
   :status: valid
   :safety: ASIL_B
   :tags: contribution_request, feature_request


.. toctree::
   :hidden:

   requirements/index.rst


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_json``

Abstract
========

This feature request proposes the integration of a safe JSON-Library with parsing functionality.


Basic Functionality
----------------------
The component shall support parsing JSON data and convert that information to a compatible user format.


Future Extensions
----------------------
The component shall support a future extension for serializing from user format into JSON data.


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

The JSON-Library should provide parsing and data conversion capabilities:

:need:`feat_req__json__validation`
:need:`feat_req__json__deserialization`

The component should be extensible in the future in order to support conversion of user format to JSON data.

User friendly API
-----------------

Programming languages have their own feature set and idioms.
It is crucial for any library that it seamlessly integrates into both.
This means, wherever possible and meaningful, infrastructure of the programming language and accompanying standard
libraries shall be reused.
Further, a developer used to the programming language shall have no problems understanding the API.
It should feel natural to use.
This includes error handling, which shall follow one of the error handling concepts of the programming language.

1. :need:`feat_req__json__lang_idioms`
2. :need:`feat_req__json__lang_infra`

Full testability for the public API
----------------------------------------

Our users will be required to proof certain coverage metrics, like line coverage or branch coverage.
For them to reach full coverage, they need to be easily able to mock or fake the public API of the JSON-Library in their unit tests.

:need:`feat_req__json__testability_mock_api`

Backwards Compatibility
=======================

As there is currently no previous solution in S-CORE, no backwards compatibility is required.

Security Impact
===============

The module will likely work with input and output streams.

Safety Impact
=============

Overall, the component shall support use cases up to ASIL-B.

License Impact
==============

[How could the copyright impacted by the license of the new contribution?]

How to Teach This
=================

[How to teach users, new and experienced, how to apply the CR to their work.]


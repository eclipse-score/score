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
============

In addition to the common JSON requirements shared by the different backends (such as "vajson" and ""nlohmann_json"), "vajson" offers extended capabilities.
These additional features are captured as requirements in the following section.

.. comp_req:: JSON Validation
   :id: comp_req__vajson__validation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

vaJson shall provide a service to check the well-formedness of JSON data.

   Errors shall be reported including the error reason and the location in the JSON document for malformed JSON and invalid schemata (user-defined errors).

.. comp_req:: JSON Deserialization RFC extensions
   :id: comp_req__vajson__deserialization_rfc_ext
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

vaJson shall provide a service to ignore trailing commas and accept hexadecimal integers.

.. comp_req:: JSON Event Callbacks
   :id: comp_req__vajson__event_callbacks
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

vaJson shall provide a service to listen to events for every parsed JSON item.
   The user shall be notified for every simple type directly, and for every complex type using start and end events.

.. comp_req:: Unicode Support
   :id: comp_req__vajson__unicode
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

vaJson shall provide support for UTF-8 encoded strings.
   UTF-8 encoded strings shall be decoded and encoded by vaJson.

.. comp_req:: Binary Content Support
   :id: comp_req__vajson__binary_content
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

vaJson shall allow for plain binary content and binary strings.
   Both types are represented as JSON values and handled accordingly (i.e., they must follow the JSON specification for values).

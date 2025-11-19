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

.. document:: JSON Requirements
   :id: doc__json_requirements
   :status: draft
   :safety: ASIL_B
   :realizes: wp__requirements_comp

General Requirements
====================

.. comp_req:: JSON Deserialization
   :id: comp_req__json__deserialization
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

   The JSON-Library shall provide a service to deserialize JSON data according to RFC8259, i.e.
   parse and check for well-formedness.

.. comp_req:: JSON Serialization
   :id: comp_req__json__serialization
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

   The JSON-Library shall provide a service to serialize user format into JSON data according to RFC8259.

.. comp_req:: Return data in user format
   :id: comp_req__json__user_format
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

   The JSON-Library shall return parsed data in a compatible user format.

   Note: The user format shall be a regular type and not defined within the library.

User friendly API for information exchange
==========================================

.. comp_req:: Support for programming language idioms
   :id: comp_req__json__lang_idioms
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library, feat_req__baselibs__consistent_apis
   :status: valid

   The public API shall support the idioms of the programming language it is written in.

.. comp_req:: Use programming language infrastructure
   :id: comp_req__json__lang_infra
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

   The public API shall use core infrastructure of its programming language and accompanying standard libraries,
   whenever possible and meaningful.

   Note: This includes error handling.

.. comp_req:: Enforce strict type compatibility
   :id: comp_req__json__type_compatibility
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

   The public API shall enforce strict type compatibility. When a user requests a value, the API shall
   validate that the requested return type is compatible with the type and value of the stored JSON data.

   Note: This includes checking if the stored value exceeds the range of the expected type.

Full testability for the user facing API
========================================

.. comp_req:: Fully testable public API
   :id: comp_req__json__full_testability
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library
   :status: valid

   The public API of the library shall support dependency injection with test doubles.

   Note: This enables full testability of the user code.

Safety Impact
=============

.. comp_req:: JSON library ASIL level
   :id: comp_req__json__asil
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__json_library, feat_req__baselibs__safety
   :status: valid

   The JSON library shall be ASIL-B compliant.

AoU Requirements
=================
.. aou_req:: JSON data integrity
   :id: aou_req__json__data_integrity
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   The user shall provide a string as input which is not corrupted due to HW or QM SW errors.

   Note: This could be achieved by using a safe read-only filesystem for JSON file storage or a checksum protection on the JSON file content.

.. aou_req:: Access control
   :id: aou_req__json__access_control
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   The user shall ensure access control and manipulation prevention on the JSON files.

   Note: This can be done by the hosting process and system configuration (e.g. by using dm-verity).

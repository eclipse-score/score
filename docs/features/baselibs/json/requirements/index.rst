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

General Requirements
====================

.. feat_req:: JSON Validation
   :id: feat_req__json__validation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__json_library
   :status: valid

   The JSON-Library shall provide a service to check the well-formedness of JSON data.

.. feat_req:: JSON Deserialization
   :id: feat_req__json__deserialization
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__json_library
   :status: valid

   The JSON-Library shall provide a service to parse JSON data according to RFC8259.

User friendly API for information exchange
==========================================

.. feat_req:: Support for programming language idioms
   :id: feat_req__json__lang_idioms
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__prog_languages
   :status: valid

   Each public API shall support the idioms of the programming language it is written in.

.. feat_req:: Use programming language infrastructure
   :id: feat_req__json__lang_infra
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__prog_languages
   :status: valid

   Each public API shall use core infrastructure of its programming language and accompanying standard libraries,
   whenever possible and meaningful.

   Note: This includes error handling.

Full testability for the user facing API
========================================

.. feat_req:: Fully mockable public API
   :id: feat_req__json__testability_mock_api
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__json_library
   :status: valid

   The public API shall be fully mockable.

Safety Impact
=============

.. feat_req:: JSON library ASIL level
   :id: feat_req__json__asil
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__json_library
   :status: valid

   The JSON library shall support safe communication up to ASIL-B.

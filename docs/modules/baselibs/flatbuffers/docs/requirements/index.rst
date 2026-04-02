..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

.. document:: FlatBuffers Requirements
   :id: doc__flatbuffers_requirements
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_comp

FlatBuffers Tooling Requirements
================================

.. tool_req:: FlatBuffers Code Generation for C++
   :id: tool_req__flatbuffers_codegen_cpp
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety, feat_req__baselibs__multi_language_apis
   :status: valid
   :implemented: NO

   The FlatBuffers-Library tooling shall generate code for serialization and read access of FlatBuffers data for C++.

.. tool_req:: FlatBuffers Code Generation for Rust
   :id: tool_req__flatbuffers_codegen_rust
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety, feat_req__baselibs__multi_language_apis
   :status: valid
   :implemented: NO

   The FlatBuffers-Library tooling shall generate code for serialization and read access of FlatBuffers data for Rust.

.. tool_req:: FlatBuffers Code Generation for Python
   :id: tool_req__flatbuffers_codegen_python
   :security: NO
   :safety: QM
   :satisfies: feat_req__baselibs__flatbuffers_library
   :status: valid
   :implemented: NO

   The FlatBuffers-Library tooling shall generate code for serialization and read access of FlatBuffers data for Python.

   .. note::
      Python code generation is nice-to-have for benchmark testing (scale configurations).
      It is not intended for safety certification (meta model check requires safety level ASIL-B).

.. tool_req:: FlatBuffers Binary Creation from JSON
   :id: tool_req__flatbuffers_tooling_json_to_bin
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety
   :status: valid
   :implemented: NO

   The FlatBuffers-Library tooling shall support creation of FlatBuffers binary files from
   JSON-encoded files conforming to the provided FlatBuffers schema, in case of violation
   of the FlatBuffers schema the tool shall fail with an appropriate error message.

.. tool_req:: FlatBuffers Data Constraint Validation
   :id: tool_req__flatbuffers_tooling_data_validate
   :security: NO
   :safety: QM
   :satisfies: feat_req__baselibs__flatbuffers_library
   :status: valid
   :implemented: NO

   The FlatBuffers-Library tooling shall provide a mechanism to validate JSON-encoded files containing
   FlatBuffers data against JSON-schema defined semantic constraints such as value ranges, allowed values
   and required field presence, in case of violation of the JSON-schema the tool shall fail with an appropriate error message.

   .. note::
      FlatBuffers schemas constrain values only via type bounds (e.g. uint8) or enum membership, arbitrary
      constraints such as custom value ranges must be enforced externally.
      Within FlatBuffers tables, scalar fields always carry a value (their default if not explicitly set)
      and cannot be absent. Reference-type fields (strings, vectors, nested tables, unions) can be
      marked with required to enforce their presence, otherwise they are optional.

.. tool_req:: FlatBuffers Schema Evolution Check
   :id: tool_req__flatbuffers_tooling_evolution
   :security: NO
   :safety: QM
   :satisfies: feat_req__baselibs__flatbuffers_library
   :status: valid
   :implemented: NO

   The FlatBuffers-Library tooling shall provide a mechanism to check whether a new version of a
   FlatBuffers schema is backward compatible with a previous version.

   .. note::
      Backward compatibility in FlatBuffers requires that existing fields are not removed or
      reordered, field types are not changed, and deprecated fields retain their field identifier.
      Breaking these rules silently corrupts data when old binaries access buffers produced from
      a new schema or vice versa.

FlatBuffers Library Requirements
================================

.. comp_req:: FlatBuffers Serialization
   :id: comp_req__flatbuffers__serialization
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_flatbuffers

   The FlatBuffers-Library shall provide functionality to serialize data into the FlatBuffers binary format.

.. comp_req:: FlatBuffers Access
   :id: comp_req__flatbuffers__access
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_flatbuffers

   The FlatBuffers-Library shall provide functionality to read FlatBuffers binary data.

   .. note::
      FlatBuffers uses a zero-copy approach where data is accessed directly from the binary buffer.

.. comp_req:: FlatBuffers Verification
   :id: comp_req__flatbuffers__verification
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_flatbuffers

   The FlatBuffers-Library shall provide a verification mechanism to validate the structural well-formedness of a FlatBuffers buffer.

   .. note::
      Verification only validates the buffer structure (e.g. offsets, vtables, field boundaries),
      not the correctness or integrity of the payload data.

.. comp_req:: Load FlatBuffers Binary File
   :id: comp_req__flatbuffers__load_binary
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_flatbuffers

   The FlatBuffers-Library shall provide functionality to load FlatBuffers binary files from the filesystem.

Buffer Identification and Versioning
=====================================

.. comp_req:: Common Buffer Identification
   :id: comp_req__flatbuffers__buffer_identification
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_flatbuffers

   The FlatBuffers-Library shall provide a common opt-in buffer identification mechanism consisting
   of a major version, a minor version, and a 4-character identifier.

.. comp_req:: Common Version Check
   :id: comp_req__flatbuffers__version_check
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_flatbuffers

   The FlatBuffers-Library shall provide a common opt-in version check mechanism that validates
   the major version, minor version, and 4-character identifier of a FlatBuffers buffer.

User friendly API for information exchange
==========================================

.. comp_req:: Support for programming language idioms
   :id: comp_req__flatbuffers__lang_idioms
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety, feat_req__baselibs__consistent_apis
   :status: valid
   :belongs_to: comp__baselibs_flatbuffers

   The public API shall support the idioms of the programming language it is written in.

.. comp_req:: Use programming language infrastructure
   :id: comp_req__flatbuffers__lang_infra
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_flatbuffers

   The public API shall use core infrastructure of its programming language and accompanying standard libraries,
   whenever possible and meaningful.

   .. note::
      This includes error handling.

Full testability for the user facing API
========================================

.. comp_req:: Fully testable public API
   :id: comp_req__flatbuffers__full_testability
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_flatbuffers

   The public API of the library shall support dependency injection with test doubles.

   .. note::
       This enables full testability of the user code.

Safety Impact
=============

.. comp_req:: FlatBuffers library ASIL level
   :id: comp_req__flatbuffers__asil
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__flatbuffers_library, feat_req__baselibs__safety
   :status: valid
   :belongs_to: comp__baselibs_flatbuffers

   The FlatBuffers library shall be ASIL-B compliant for C++ and Rust language support.

AoU Requirements
=================

.. aou_req:: FlatBuffers data integrity
   :id: aou_req__flatbuffers__data_integrity
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   The user shall provide FlatBuffers binary data as input which is not corrupted due to HW, QM SW, or communication channel errors.

   .. note::
      The FlatBuffers-Library verification mechanism only validates structural well-formedness,
      not payload data integrity. Data integrity shall be ensured by external means such as a safe
      read-only filesystem for FlatBuffers binary file storage or a checksum protection on the
      FlatBuffers binary file content.

.. aou_req:: FlatBuffers access control
   :id: aou_req__flatbuffers__access_control
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   The user shall ensure access control and manipulation prevention on the FlatBuffers binary files.

   .. note::
      This can be done by the hosting process and system configuration (e.g. by using dm-verity).

.. aou_req:: FlatBuffers buffer version check before access
   :id: aou_req__flatbuffers__verify_version
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   The user shall apply the version check mechanism provided by :need:`comp_req__flatbuffers__version_check`
   to a loaded buffer and confirm a successful result before accessing any data from that buffer.

   .. note::
      This provides early detection of schema or version mismatches before any further buffer data is
      verified or accessed.

.. aou_req:: FlatBuffers buffer verification before access
   :id: aou_req__flatbuffers__verify_structure
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   The user shall apply the verification mechanism provided by :need:`comp_req__flatbuffers__verification`
   to a loaded buffer and confirm a successful result before accessing any data from that buffer.

   .. note::
      Accessing data from an unverified or malformed buffer results in undefined behaviour.
      The verification mechanism only checks structural well-formedness; it does not replace
      the data integrity measures required by :need:`aou_req__flatbuffers__data_integrity`.


.. needextend:: "__flatbuffers__" in id
   :+tags: baselibs

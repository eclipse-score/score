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

FlatBuffers-Library
===================

.. document:: FlatBuffers-Library
   :id: doc__flatbuffers
   :status: valid
   :safety: ASIL_B
   :security: YES
   :tags: component_request
   :realizes: wp__cmpt_request


.. toctree::
   :hidden:

   requirements/index.rst
   architecture/index.rst


Abstract
========

This component request proposes the integration of Google FlatBuffers [#flatbuffers]_ providing
serialization, zero-copy read access, and structural verification of FlatBuffers data, as well as code
generation via the ``flatc`` compiler.

Additionally, the library introduces FlatBuffers binary configuration format to replace JSON-based
module configuration for runtime access. FlatBuffers provides zero-copy access, schema validation,
and access code generation for C++, Rust, and further languages. The approach eliminates the need
for runtime parsing and accelerates module startup times. Safety certification covers ``flatc`` tool
qualification, runtime library verification, and module-level testing of generated code.


Motivation
==========

Module specific configuration is a cross-cutting concern that impacts system startup time and
development efficiency. For read-only configuration scenarios, runtime parsing approaches can
limit startup performance in time-critical applications.

The FlatBuffers binary configuration approach addresses these engineering challenges by:
   - Eliminating the need for runtime parsing to meet aggressive startup time requirements
   - Providing compile-time type safety through generated access code
   - Reducing development effort through automated access code generation
   - Ensuring schema validation at build time


Rationale
=========

Real-world experience with complex modules (e.g. diagnostics, SOME/IP) demonstrates that read-only
configuration scenarios benefit significantly from zero-copy access patterns. For these use cases,
FlatBuffers is ideal as it allows zero-copy data access. The schema-driven code generation further
accelerates development by providing type-safe access patterns, reducing both implementation effort
and the potential for configuration-related runtime errors.


Specification
=============

The ``flatc`` compiler shall generate code for serializing, accessing, and verifying
FlatBuffers binary data. Code generation shall be provided for C++ and Rust at ASIL-B level
and other languages as needed at QM level (e.g. Python).

The FlatBuffers-Library shall provide services for serialization, zero-copy access of
FlatBuffers binary data, and structural verification of buffers. The library shall also support
loading FlatBuffers binary files and opt-in functionality for common buffer identification and version
checking mechanisms.

Note: FlatBuffers verification mechanism validates structural well-formedness only (e.g. offsets, vtables,
field boundaries), not payload data integrity.

Module configuration shall use FlatBuffers binary format for read-only configuration scenarios to
achieve aggressive start-up time requirements.

.. _flatbuffers_overview:

Design
------

.. figure:: _assets/flatbuffers_overview.drawio.svg
   :alt: FlatBuffers overview
   :align: center
   :width: 80%

| FlatBuffers schema files (``config.fbs``) define configuration structure using Interface Definition Language (IDL).
| The ``flatc`` compiler generates C++ or Rust access code from these schemas (``config.fbs``).
| The ``flatc`` compiler generates cross-platform data binary from schema (``config.fbs``) and JSON (``config.json``) input.
| Runtime access operates directly on binary config data (``config.bin``) without parsing (lazy loading).
| The ``flatc`` compiler can convert binary config data (``config.bin``) back to JSON using the schema (``config.fbs``) for debugging purposes.

Schema Evolution
^^^^^^^^^^^^^^^^

Backward compatibility through:
   - Optional fields for new parameters
   - Default values for missing fields
   - Controlled field deprecation

Schema Versioning
^^^^^^^^^^^^^^^^^

FlatBuffers binary files do not contain embedded schema information. Schema identification requires:
   - Embedded version fields in the schema root table
   - File naming conventions (e.g., config_v1.2.bin)

Build Integration
-----------------

Build system integration shall provide reusable rules for:
   - Binary configuration file generation from module specific schema and user-provided JSON data
   - Reverse conversion from binary to JSON for debugging purposes

Binary Config Loading
---------------------

The FlatBuffers-Library provides a unified interface for binary data file loading
(see :ref:`FlatBuffers overview <flatbuffers_overview>`).


Backwards Compatibility
=======================

Switching from JSON to FlatBuffers for module configuration is not backwards compatible.


Security Impact
===============

No change expected when compared to JSON based configuration approach.


Safety Impact
=============

**Tool Qualification**: ``flatc`` compiler qualification shall be limited to buffer serialization use case.
Brief qualification is supplemented by module-specific validation.

**Verification Runtime Library**: Footprint when excluding verifier/builder classes
   - C++: 12 headers, ~250 LOC (incl. comments), standard library only
   - Rust: 11 files, ~150 LOC (incl. comments), core/alloc only (assumes std/serialize features disabled)

**Verification Generated Code**: Module-level verification is equivalent to handwritten access code verification.
Module testing contributes to ``flatc`` tool validation for specific schemas.
Test from configuration data (JSON) to value verification in access APIs.


License Impact
==============

None. FlatBuffers is licensed under the Apache License Version 2.0.


How to Teach This
=================

Developer adoption requires practical examples and reusable patterns.
The FlatBuffers-Library should provide examples for reference implementations.


Rejected Ideas
==============

**Protocol Buffers**: Requires runtime parsing and memory allocation, defeating startup time objectives.

**Custom binary formats**: Higher development and maintenance overhead compared to proven FlatBuffers ecosystem.


Open Issues
===========

No open issues identified yet.


Footnotes
=========

.. [#flatbuffers] https://google.github.io/flatbuffers/

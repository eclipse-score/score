..
   # *******************************************************************************
   # Copyright (c) 2025-2026 Contributors to the Eclipse Foundation
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

.. document:: Baselibs Requirements
   :id: doc__baselibs_requirements
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_feat[version==1]

.. feat_req:: Core Software Utilities
   :id: feat_req__baselibs__core_utilities
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__functional_req__base_libraries[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The base libraries shall include core software utilities and common infrastructure components needed by multiple platform modules.

.. feat_req:: Safety Relevance
   :id: feat_req__baselibs__safety
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The base libraries shall implement functionality necessary to support safety-relevant platform components up to ASIL-B for selected functionalities.

.. feat_req:: Multi-Language APIs
   :id: feat_req__baselibs__multi_language_apis
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1], stkh_req__dev_experience__prog_languages[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The base libraries shall provide APIs for C++, Rust, or both, depending on the requirements of consuming platform components.

.. feat_req:: Consistent APIs
   :id: feat_req__baselibs__consistent_apis
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__functional_req__base_libraries[version==1], stkh_req__dev_experience__prog_languages[version==1], stkh_req__overall_goals__reuse_of_app_soft[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The base libraries shall provide consistent APIs while respecting language-specific idioms.

.. feat_req:: Maintainable Design
   :id: feat_req__baselibs__maintainable_design
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__functional_req__base_libraries[version==1], stkh_req__overall_goals__reuse_of_app_soft[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The base libraries shall be designed for maintainability and code reuse.

.. feat_req:: Security Robustness
   :id: feat_req__baselibs__security
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__functional_req__base_libraries[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The base libraries shall adhere to secure coding standards to prevent vulnerabilities across platform components.

.. feat_req:: JSON-Library
   :id: feat_req__baselibs__json_library
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The base libraries shall provide a JSON-Library with parsing functionality.

.. feat_req:: FlatBuffers-Library
   :id: feat_req__baselibs__flatbuffers_library
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__functional_req__base_libraries[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0
   :tags: inspected

   The base libraries shall provide a FlatBuffers-Library with serialization, read access, and structural verification of FlatBuffers data.

   .. note::
      FlatBuffers-Library provides both ASIL-B and QM compliant functionality depending on the programming language,
      the separation is done on component level.

.. feat_req:: Exception-Free Development Support
   :id: feat_req__baselibs__result_library
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The base libraries shall provide error handling mechanisms that enable development without relying on C++ exceptions.

.. feat_req:: Panic-Free Development Support
   :id: feat_req__baselibs__panic_free_development
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1

   The base libraries shall provide error handling mechanisms that enable development without relying on Rust panics.
   Where an idiomatic interface requires panics, an additional non-panicking option shall be provided as well.

.. feat_req:: Container Library
   :id: feat_req__baselibs__containers_library
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The base libraries shall provide a container library offering additional container types not present in the C++ standard library.

.. feat_req:: ABI-Compatible Containers
   :id: feat_req__baselibs__abi_containers
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1] ,stkh_req__communication__abi_compatible[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1

   The base libraries shall provide a library of containers that can serve as the basis for ABI-compatible container data structures.

.. feat_req:: Bit Manipulation Library
   :id: feat_req__baselibs__bitmanipulation
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The base libraries shall provide bit manipulation utilities for low-level operations on integral types.

.. feat_req:: Filesystem-Library
   :id: feat_req__baselibs__filesystem_library
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The base libraries shall provide a filesystem library with file and directory manipulation functionality.

.. feat_req:: Memory Library
   :id: feat_req__baselibs__memory_library
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The baselibs shall provide a memory management library that includes utilities for shared memory operations, polymorphic memory resources, position-independent pointers, endianness conversion, and inter-process synchronization mechanisms.

.. feat_req:: Concurrency Library
   :id: feat_req__baselibs__concurrency_library
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1
   :tags: inspected

   The base libraries shall provide a library for parallel execution of C++ callables with thread pool management.

.. feat_req:: Hash Library
   :id: feat_req__baselibs__hash_library
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 1

   The base libraries shall provide a hash library supporting cryptographic hash
   calculation (e.g. SHA-256, SHA-512) and checksum algorithms (e.g. CRC-32) over
   byte data and streams via a pluggable interface.

.. needextend:: is_external == False and "__baselibs" in id
   :+tags: baselibs

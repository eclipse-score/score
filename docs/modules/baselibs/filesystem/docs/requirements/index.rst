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

.. document:: Filesystem Library Requirements
   :id: doc__filesystem_lib_requirements
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_comp
   :tags: requirements, filesystem_library

Functional Requirements
=======================

.. comp_req:: Standard Filesystem Abstraction
   :id: comp_req__filesystem__api_abstraction
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__consistent_apis, feat_req__baselibs__filesystem_library
   :status: valid
   :belongs_to: comp__baselibs_filesystem

   The Filesystem library shall provide filesystem API based on the C++ standardization.

.. comp_req:: Path Manipulation Utilities
   :id: comp_req__filesystem__path_utilities
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__consistent_apis, feat_req__baselibs__filesystem_library
   :status: valid
   :belongs_to: comp__baselibs_filesystem

   The Filesystem library shall provide type-safe utilities for path construction and manipulation.

.. comp_req:: Directory Iterators
   :id: comp_req__filesystem__directory_iterators
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__filesystem_library
   :status: valid
   :belongs_to: comp__baselibs_filesystem

   The Filesystem library shall provide directory iterator types for traversing directory contents.

.. comp_req:: File I/O Operations
   :id: comp_req__filesystem__file_io
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__filesystem_library
   :status: valid
   :belongs_to: comp__baselibs_filesystem

   The Filesystem library shall provide functionality for reading from and writing to files, including buffered I/O operations.

.. comp_req:: Fully testable public API
   :id: comp_req__filesystem__full_testability
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__filesystem_library
   :status: valid
   :belongs_to: comp__baselibs_filesystem

   The public API of the library shall support dependency injection with test doubles.

   Note: This enables full testability of the user code.

.. comp_req:: File Utility Functions
   :id: comp_req__filesystem__file_utils
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__filesystem_library
   :status: valid
   :belongs_to: comp__baselibs_filesystem

   The Filesystem library shall provide additional file utility functions, such as temporary file handling and file comparison.

.. comp_req:: Mock and Fake Implementations
   :id: comp_req__filesystem__mock_fake
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__filesystem_library
   :status: valid
   :belongs_to: comp__baselibs_filesystem

   The Filesystem library shall provide mock and fake implementations for unit testing and validation.

Assumptions of Use (AoU)
========================

.. aou_req:: Low-Level Use Only
   :id: aou_req__filesystem__low_level_use_only
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   Users shall use this library only when they need to manipulate files, directories, and paths at the operating system level beyond what higher-level storage abstractions provide, accepting reduced portability to other platforms.

.. aou_req:: Supported Path Formats
   :id: aou_req__filesystem__supported_path_formats
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   Users shall not use Windows paths with this library.

.. aou_req:: Error Handling
   :id: aou_req__filesystem__error_handling
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   Users shall handle all function return values and take appropriate action on errors.

.. aou_req:: Thread Safety
   :id: aou_req__filesystem__thread_safety
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   Users shall implement appropriate synchronization mechanisms when accessing shared filesystem resources concurrently.

.. aou_req:: Performance
   :id: aou_req__filesystem__performance
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   Users shall not assume any performance characteristics.

   Note: Filesystem operations are subject to underlying OS and storage performance.

.. needextend:: "__filesystem__" in id
   :+tags: baselibs

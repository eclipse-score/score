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

   The Filesystem library shall provide filesystem API based on the C++ standardization.

.. comp_req:: Path Manipulation Utilities
   :id: comp_req__filesystem__path_utilities
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__consistent_apis, feat_req__baselibs__filesystem_library
   :status: valid

   The Filesystem library shall provide type-safe utilities for path construction and manipulation.

.. comp_req:: Directory Iterators
   :id: comp_req__filesystem__directory_iterators
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__filesystem_library
   :status: valid

   The Filesystem library shall provide directory iterator types for traversing directory contents.

.. comp_req:: File I/O Operations
   :id: comp_req__filesystem__file_io
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__filesystem_library
   :status: valid

   The Filesystem library shall provide functionality for reading from and writing to files, including buffered I/O operations.

.. comp_req:: Fully testable public API
   :id: comp_req__filesystem__full_testability
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__filesystem_library
   :status: valid

   The public API of the library shall support dependency injection with test doubles.

   Note: This enables full testability of the user code.

.. comp_req:: File Utility Functions
   :id: comp_req__filesystem__file_utils
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__filesystem_library
   :status: valid

   The Filesystem library shall provide additional file utility functions, such as temporary file handling and file comparison.

.. comp_req:: Mock and Fake Implementations
   :id: comp_req__filesystem__mock_fake
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__filesystem_library
   :status: valid

   The Filesystem library shall provide mock and fake implementations for unit testing and validation.

.. needextend:: "__filesystem__" in id
   :+tags: baselibs

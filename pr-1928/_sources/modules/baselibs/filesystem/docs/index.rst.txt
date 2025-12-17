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

filesystem
##############

.. document:: Filesystem Library
   :id: doc__filesystem
   :status: draft
   :safety: ASIL_B
   :security: YES
   :tags: baselibs_filesystem
   :realizes: wp__cmpt_request

.. toctree::
   :hidden:

   requirements/index.rst
   architecture/index.rst
   safety_analysis/fmea.rst
   safety_analysis/dfa.rst

Abstract
========

The Filesystem Library provides a set of APIs for file and directory manipulation, including creation, deletion, and traversal of the filesystem. It aims to offer a consistent and safe interface for filesystem operations across different platforms.

Motivation and Rationale
========================

The Filesystem Library is essential for applications that require interaction with the underlying filesystem. It provides a standardized way to perform file operations, ensuring safety and reliability.
The library is designed to handle various filesystem tasks while adhering to safety standards required for critical systems.

Specification
=============

The following details and requirements describe the aspects of the current feature in the context of S-CORE.

General considerations
----------------------

The Filesystem Library should provide robust and safe APIs for filesystem operations:

* :need:`comp_req__filesystem__api_abstraction`
* :need:`comp_req__filesystem__path_utilities`
* :need:`comp_req__filesystem__directory_iterators`
* :need:`comp_req__filesystem__file_io`
* :need:`comp_req__filesystem__full_testability`
* :need:`comp_req__filesystem__file_utils`
* :need:`comp_req__filesystem__mock_fake`

The library should ensure that all filesystem operations are performed safely, with appropriate error handling and resource management to prevent leaks and ensure system stability.

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

utils
######

.. document:: Utils Library
   :id: doc__utils
   :status: draft
   :safety: ASIL_B
   :tags: baselibs_utils
   :realizes: wp__cmpt_request

.. toctree::
   :hidden:

   requirements/index.rst

Abstract
========

This component request proposes the integration of a safe Utils library for common utility functions and algorithms.

Motivation and Rationale
========================

The Utils library shall provide safe and efficient implementations of common utility functions and algorithms.
The library shall enable developers to perform common tasks in a type-safe manner, reducing the risk of runtime errors and improving code quality.
A Utils library with type-safe utility functions is needed in the S-CORE software platform due to the frequent use of such functions in various features and the need for reliable utility operations.
There are multiple use-cases like calculating string hashes, embedding binary data in string format or managing resource lifetimes.

Specification
=============

The following details and requirements describe the aspects of the current feature in the context of S-CORE.

General considerations
----------------------

The Utils library should provide type-safe utility functions and efficient algorithms:

* :need:`comp_req__utils__string_hash`
* :need:`comp_req__utils__base64`
* :need:`comp_req__utils__pimpl_ptr`
* :need:`comp_req__utils__scoped_operation`
* :need:`comp_req__utils__deterministic_behavior`

The component should be extensible in the future to support additional utility functions and algorithms as needed.

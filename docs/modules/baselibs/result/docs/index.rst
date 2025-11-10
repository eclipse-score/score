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

result
######

.. document:: Result Library
   :id: doc__result
   :status: draft
   :safety: ASIL_B
   :tags: baselibs_result
   :realizes: wp__cmpt_request

.. toctree::
   :hidden:

   requirements.rst
   architecture/index.rst

Abstract
========

This component request proposes the integration of a safe Result library for type-safe error handling and value propagation.

Motivation and Rationale
========================

The Result library shall provide a type-safe mechanism to represent and propagate either a successful value or an error.
Result library will enable explicit error management and support the development of safety-critical features by providing clear value or error propagation paths.
A Result library with type-safe error handling is needed in the S-CORE software platform due to functional dependencies of different features and the need for explicit, reliable error propagation.
There are multiple use-case like logging error messages or comparing on expected error states to trigger other countermeasures.

Specification
=============

The following details and requirements describe the aspects of the current feature in the context of S-CORE.

General considerations
----------------------

The Result library should provide value/error propagation and error handling capabilities:

* :need:`comp_req__result__error_handling`
* :need:`comp_req__result__domain_error_information`
* :need:`comp_req__result__type_safety`
* :need:`comp_req__result__std_integration`
* :need:`comp_req__result__deterministic_behavior`
* :need:`comp_req__result__exception_free_operation`

The component should be extensible in the future to support richer error information and integration with other platform components.

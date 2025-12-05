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

containers
##########

.. document:: Containers Library
   :id: doc__containers
   :status: draft
   :safety: ASIL_B
   :tags: baselibs_containers
   :realizes: wp__cmpt_request
   :security: YES

.. toctree::
   :hidden:

   requirements/index.rst
   architecture/index.rst
   safety_analysis/fmea.rst
   safety_analysis/dfa.rst

Abstract
========

This component request proposes the integration of a safe Containers library for common data structures like dynamic arrays and linked lists.

Motivation and Rationale
========================

The Containers library shall provide safe and efficient implementations of common data structures, such as dynamic arrays and linked lists.
Containers library shall enable developers to manage collections of data in a type-safe manner, reducing the risk of runtime errors and improving code quality.
A Containers library with type-safe data structures is needed in the S-CORE software platform due to the frequent use of collections in various features and the need for reliable data management.
There are multiple use-cases like managing lists of sensor readings, storing configuration parameters, or handling dynamic data sets.

Specification
=============

The following details and requirements describe the aspects of the current feature in the context of S-CORE.

General considerations
----------------------

The Containers library should provide type-safe data structures and efficient memory management capabilities:

* :need:`comp_req__containers__dynamic_array`
* :need:`comp_req__containers__intrusive_list`
* :need:`comp_req__containers__type_safety`
* :need:`comp_req__containers__deterministic_behavior`

The component should be extensible in the future to support additional data structures and algorithms as needed.

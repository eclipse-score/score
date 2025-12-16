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

os
###

.. document:: OS Library
   :id: doc__os
   :status: draft
   :safety: ASIL_B
   :security: YES
   :tags: baselibs_os
   :realizes: wp__cmpt_request

.. toctree::
   :hidden:

Abstract
========

This component request proposes the integration of a safe OS library for operating system abstractions.

Motivation and Rationale
========================

The OS library shall provide safe and efficient abstractions for operating system functionalities.
The library shall enable developers to interact with the underlying operating system in a type-safe manner, reducing
the risk of runtime errors and improving code quality.
An OS library with type-safe abstractions is needed in the S-CORE software platform due to the frequent interaction with operating system features
and the need for reliable OS operations.

Specification
=============

The following details and requirements describe the aspects of the current feature in the context of S-CORE.

General considerations
----------------------
The OS library should provide type-safe abstractions for operating system functionalities:

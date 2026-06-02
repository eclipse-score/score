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

.. _baselibs_feature:

Base Libraries (v0.5 beta)
###########################

.. document:: Base Libraries
   :id: doc__baselibs
   :status: valid
   :safety: ASIL_B
   :tags: feature_request
   :security: YES
   :realizes: wp__feat_request


.. toctree::
   :hidden:

   docs/requirements/index.rst
   docs/requirements/chklst_req_inspection.rst
   docs/architecture/index.rst
   docs/architecture/chklst_arc_inspection.rst
   docs/safety_analysis/dfa.rst
   docs/safety_analysis/fmea.rst
   docs/safety_planning/index.rst
   abi_compatible_data_types/index.rst

Feature flag
============

To activate this feature, use the following feature flag:

``experimental_baselibs``

Abstract
========

This feature provides a set of base libraries for both C++ and Rust that can be used by S-CORE
components.
These libraries offer common functionality, ensuring consistent implementations, reducing code
duplication, and promoting interoperability between components.

The base libraries include utilities for bit manipulation, concurrency management, containers,
JSON processing, filesystem operations, memory handling, OS abstraction, error handling,
serialization, logging, and various other common utilities needed across the S-CORE system.

Motivation
==========

Base libraries are essential to ensure consistency, reduce code duplication, and improve quality
across S-CORE components.

Rationale
=========

A base library is developed only if it is required by at least two S-CORE components.
This ensures that the effort to create and maintain a base library is justified by real,
shared needs across the platform.

Each base library may provide an API for Rust, C++, or both, depending on the requirements of
the consuming components. When possible, a library should be implemented once in either Rust
or C++ and provide bindings to the other language to maximize maintainability and consistency.
However, if there are strong technical reasons (such as language-specific performance or safety
requirements), a library may be implemented separately in both Rust and C++.

Backwards Compatibility
=======================

As this is a new feature, there are no backwards compatibility concerns.

Security Impact
===============

Base libraries present varying security risks as vulnerabilities could affect multiple components
simultaneously.
Each library requires individual security impact analysis based on its functionality and usage patterns.

Safety Impact
=============

- Due to wide usage of the base libraries throughout the platform, extra care is needed in design,
  implementation, and testing to minimize safety impact.
- Libraries are developed at various integrity levels from QM (non-safety) up to ASIL-B,
  depending on their intended use cases.

License Impact
==============

The base libraries are licensed under Apache License 2.0.

How to Teach This
=================

Each library is expected to have a user manual that includes an API reference and usage examples
where necessary.

Rejected Ideas
==============

There are no rejected ideas related to the base libraries feature at this time.

Open Issues
===========

There are currently no open issues related to the base libraries feature.

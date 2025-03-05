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

Getting Started
###############

.. doc_getstrt:: Getting Started on Implementation
   :id: doc_getstrt__imp__getstrt
   :status: valid
   :tags: Implementation

This document describes the steps which need to be done to detailed unit design and implementation.

Therefore a detailed guideline :need:`gd_guidl__implementation` is available.


Detailed Design
***************

For the detailed design a template is :need:`gd_temp__detailed_design` available. With the detailed
design everything for the developer and tester is sufficent defined.

Tooling Support
***************

Coding Guidelines
=================

For C++17 devlopment MISRA C++:2023 shall be used <Link to source>

For Rust development a set of coding rules has to be defined. Therefore the following sources can be considered:
 |  https://github.com/PolySync/misra-rust/blob/master/MISRA-Rules.md#rule-55
 |  https://google.github.io/learn_unsafe_rust/undefined_behavior.html
 |  https://github.com/rustfoundation/safety-critical-rust-consortium/pull/182/files

Static Code Analyis
===================

<TDB> tool to enforce coding rules e.g. axivion, parasoft c++, helix qac


CI/CD Pipeline
==============

Description which Static Code Analysis Tools <TBD> are implmented in the CI/CD Pipeline.

.. Developer Experience
.. ====================

.. For all RST files also a linter is configured, it will be automatically run in the CI upon check-in.
.. Locally it can be run via

.. .. code-block:: shell

..    bazel test //:format.check



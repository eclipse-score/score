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

Guideline
#########

.. gd_guidl:: Implementation Guideline
   :id: gd_guidl__implementation
   :status: valid

This document describes the general guidances for implementation based on the concept which is defined :need:`[[title]]<doc_concept__imp__concept>`.

General Hints
=============

Template
---------

The detailded design template :need:`[[title]] <gd_temp__detailed_design>` shall be used to ensure that the correct syntax and attribute definition is used.


Attributes
----------


Checks
------

During the build checks will be performed on the implementation <TBD>



Workflow for Implementation
===========================

This section describes in detail which steps need for implementation.

.. Explenation of implementation of Coding Rules if needed

.. Explenation of procedure with Rust regarding to the discussions for coding rules for Rust

Creation of a detailed design by using the Template :need:`[[title]] <gd_temp__detailed_design>`.
The detailed design shall be so exact, that test and implementation can be run simultaneously.
The generated code and tests shall run the checks locally before commiting/pushing changes to a
branch to avoid unnecessary cycles. The checks can be executed by <TBD>. Use the explenations of
the tools.

In the CI/CDcd pipeline the checks <TBD> are executed. Use the explenations in the pipeline.

.. Exceptions handling




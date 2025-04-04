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

Concept Description
###################

.. doc_concept:: Concept Description
   :id: doc_concept__rel__process
   :status: draft
   :tags: release_management

This section describes the general concept for the release management process.
The release process can be separated into two parts. On the first level are the software module
releases. These are independent from the platform and can be separated over various repositories.
Once a software module is released it can be contained within a platform release which
can include multiple software module releases within a platform release scope.

Inputs
******

#. Module safety case
#. Platform safety case
#. Issue tracking system
#. Platform Management Plan

Outputs
*******
#. Module release plan
#. Module release note
#. Platform release plan
#. Platform release note

Platform Release Plan
=====================

The platform release plan provides a reliable plan on what software modules can be expected in the
upcoming platform release. The platform release plan is reflected by feature requests which are
demanded. Therefore it is of importance that the *Project Leads* are aligned with
the various software module *Technical Leads* and *Project Leads* to align the platform release
plan properly with the module release plan as the platform release plan has a clear dependency on
its output.

#. :need:`Tech Lead Circle <rl__technical_lead>`

   * Define and proposes scope of individual module release
   * Aligns module release timeline with platform release plan

#. :need:`Project Lead Circle <rl__project_lead>`

   * Creates and maintains the platform release plan
   * Aligns with the *Tech Lead Circle* the timeline from various module release plans

Platform Release
================

The Platform Release contains the full *SCORE* scope which spans over many modules. The releases
are proposed by the *Technical Leads* and approved by *Project Leads*. Every software module
has its own repository which contains multiple components, their requirements, architecture,
implementation and tests.

#. :need:`Tech Lead Circle <rl__technical_lead>`

   * Define and proposes scope of release
   * Writes platform release notes

#. :need:`Project Lead Circle <rl__project_lead>`

   * Approves the platform release notes
   * Adds and removes software modules to the platform
   * Releases the platform

Module Release Plan
===================

The module release plan gives a guidance when certain features can be expected on a module level.
It is created by the respective *Tech Leads* and *Project Leads* of the module.

#. :need:`Tech Lead Circle <rl__technical_lead>`

   * Define and proposes scope of individual module Release
   * Creates and maintains the module release plan

#. :need:`Project Lead Circle <rl__project_lead>`

   * Approves the module release plan

Module Release
==============

Each software module needs to have its dedicated release and the accompanying release notes.
Only released software modules can be included into a platform release.

#. :need:`Tech Lead Circle <rl__technical_lead>`

   * Provides the software module release notes

#. :need:`Project Lead Circle <rl__project_lead>`

   * Aligns software module release timing schedule
   * Adds and removes Software modules to the Platform

Branching Strategy
==================

Branches:
* main: Stable, production-ready code.
* release/\*: Branches for distinct releases, named release/<version-number>.


Workflow:

When ready for a new release, create a branch release/<version-number> from main.
Perform final testing and adjustments on the release branch.
Tag the release in the release branch.

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

.. _os-onboarding:

Onboarding and Promotion
========================

.. toctree::
   :titlesonly:

   Template <os_onboard_template>

This page describes how platforms are added and promoted.

The process requirements are defined in :ref:`platform_assumptions`.

Principle
---------

Promotion has two phases:

1. **Eligibility (Platform Maintainer)**:
   The platform maintainer resolves the **supplier** requirements of the target level.
   Only if these requirements are fulfilled, the OS can be considered for promotion.

2. **Acceptance + Lifecycle Guarantees (S-CORE)**:
   S-CORE reviews the promotion request.
   If accepted at **Functional** or **Certifiable**, S-CORE commits to maintain the
   guarantees of the accepted level across all increments.

Community level onboarding
--------------------------

**What it means**
  In-tree best-effort integration.
  S-CORE provides no guarantees.

**Eligibility requirements (Platform Maintainer / supplier requirements)**
  The OS maintainer must fulfil the Community level supplier requirements as defined in:
  :ref:`platform_assumptions`.

**Review and acceptance (S-CORE)**
  S-CORE reviews the documentation entry for completeness and consistency.
  Acceptance only means the platform is listed in-tree.
  No infrastructure or lifecycle support is implied.

Promotion to Functional
-----------------------

**What it means**
  S-CORE provides functional guarantees for the accepted reference integration and
  maintains them across all increments.

**Eligibility requirements (Platform Maintainer / supplier requirements)**
  The platform maintainer must fulfil the Functional level supplier requirements as defined in:
  :ref:`platform_assumptions`.

**Additional acceptance requirements (S-CORE / system integrator requirements)**
  From Functional level onwards, S-CORE must be able to continuously validate the platform.
  This requires infrastructure and test integration.

**Required approvals**
  Promotion to Functional requires explicit approval by:

  * Platform maintainers
  * Architecture WG
  * Infrastructure WG (CI / build & test environment support)
  * Testing WG
  * Quality Management

Promotion to Certifiable
------------------------

**What it means**
  S-CORE provides certifiability-oriented guarantees for the accepted reference integration
  and maintains them across all increments.

**Eligibility requirements (Platform Maintainer / supplier requirements)**
  The platform maintainer must fulfil the Certifiable level supplier requirements as defined in:
  :ref:`platform_assumptions`.

**Additional acceptance requirements (S-CORE / system integrator requirements)**
  Certifiable level implies additional safety/security expectations and evidence handling.

**Required approvals**
  Promotion to Certifiable requires explicit approval by:

  * OS module maintainers
  * Architecture WG
  * Infrastructure WG
  * Testing WG
  * Quality Management
  * Safety Manager
  * Security Manager

Demotion
--------

If the eligibility requirements or the S-CORE lifecycle guarantees of an accepted platform
can no longer be maintained, the platform must be demoted to the highest level that can be
sustained.

Onboarding Template
-------------------

Use the :doc:`onboarding template document <os_onboard_template>` as the starting point to add a new operating system to
one of the levels, as described in the previou sections of this document.

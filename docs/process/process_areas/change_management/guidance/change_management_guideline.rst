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

.. gd_guidl:: Change Request Guideline
   :id: gd_guidl__change__change_request
   :status: valid
   :complies: std_req__iso26262__support_8414, std_req__iso26262__support_8432, std_req__iso26262__support_8442, std_req__iso26262__support_8451

This document describes the general guidances for Change Management based on the concept which is defined :need:`[[title]]<doc_concept__change__process>`.

General Hints
=============

The detailed implementation of the Change Management for **S-CORE** is described in the :need:`[[title]]<doc__platform_change_management_plan>`.

Templates
---------

*Need* templates displaying the correct syntax and attribute definition are provided for each
Change Request type.

.. list-table:: Overview
   :header-rows: 1
   :widths: 37, 37

   * - Change Request Type
     - Template
   * - Feature
     - :need:`[[title]] <gd_temp__change__feature_request>`
   * - Feature Modification
     - :need:`[[title]] <gd_temp__change__feature_request>`
   * - Component
     - :need:`[[title]] <gd_temp__change__component_request>`
   * - Component Modification
     - :need:`[[title]] <gd_temp__change__component_request>`

Attributes
----------

For all Change Requests following mandatory attributes need to be defined:

.. needtable:: Overview of mandatory change request attributes
   :tags: change_management
   :filter: "mandatory" in tags and "attribute" in tags and type == "gd_req"
   :style: table
   :columns: title
   :colwidths: 30


* ID: Unique integer number
* For the remaining attributes only predefined values can be used. A more detailed description can
  be found here: :ref:`chm_attributes`


.. _workflow_chm_requirements:

Activities for Change Requests
==============================

This section describes in detail which steps need to be performed for a Change Request. They may
be combined in on Change Request or split to multiple Change Requests, if necessary.

Split may required, if

| 1. Implementation is to complex and has dependencies, thus separate the activities for analyzing and
|    approving and the multiple implementation and verification activities in different Change Requests,
|    and link them according their dependencies.

| 2. Affected work products are in different locations.

Refer to the :need:`Change Management Plan <doc__platform_change_management_plan>` for examples
how to create simple or more complex Change Requests.

.. list-table:: Activities for Change Request
   :header-rows: 1
   :widths: 10,60,30

   * - Step
     - Description
     - Responsible
   * - :ref:`1. <chm_create_change_request>`
     - Create change request
     - :need:`[[title]] <rl__contributor>`
   * - :ref:`2. <chm_analyze_change_request>`
     - Analyze Change Request
     - :need:`[[title]] <rl__contributor>`
   * - :ref:`3. <chm_approve_change_request>`
     - Approve Change Request
     - :need:`[[title]] <rl__committer>`
   * - :ref:`4. <chm_implement_change_request>`
     - Implement Change Request
     - :need:`[[title]] <rl__contributor>`
   * - :ref:`5. <chm_verify_change_request>`
     - Verify Change Request
     - :need:`[[title]] <rl__committer>`

.. _chm_create_change_request:

Create Change Request
---------------------

:need:`[[title]] <rl__contributor>` creates the Change Request in the defined Issue Tracking
System linked to the created Feature or Component Request work products based on the provided templates.
It is expected, that the UID will be provided by the Issue Tracking System.

The title of the Change Request should reflect the type (new feature/component request or
feature/component modification).

The description should reflect the detailed changes. In case of a new feature/component request,
fill-out the template sections properly. For modifications touch only the concerned sections.

Set the status of the Change Request to "draft", indicating that is not ready for review.

.. _chm_analyze_change_request:

Analyze Change Request
----------------------

To enable the **S-CORE** :need:`[[title]] <rl__committer>` to take a decision for approval of the
Change Request, :need:`[[title]] <rl__contributor>` analyses and documents the request concerning
the following topics in the created Change Request:

1. List of all affected work products
2. Provide potential implementation schedule including targeted Milestone
3. Identify risks for implementation, required **S-CORE** resources
4. Identify impact on existing work products and on functional safety, security
5. Define verification measures used to confirm the implementation

Use therefore the : :ref:`Impact Analysis Template <chm_impact_analysis_templates>` and copy it
into the created Change Request (Issue Tracking System).

Set the status of the Change Request to "draft", indicating that is not ready for review.
Otherwise, change the status to "in review", so that :need:`[[title]] <rl__committer>` is
informed to start approval.

.. _chm_approve_change_request:

Approve Change Request
----------------------

:need:`[[title]] <rl__committer>` checks the Change Request in status "in review" based on
checklist questions and provided content. If the check is passed, the Change Request is approved,
which is pre-requisite for the implementation of the Change Request. In this case the status
of the Change Request is changed to "accepted".

In case information are missing the status will be kept in "in review" and the creator is asked
for resolving the review comments.

Finally the Change Request may also "rejected", then the implementation is not wanted.

.. _chm_implement_change_request:

Implement Change Request
------------------------

:need:`[[title]] <rl__contributor>` implements the Change Request. This is indicated by the
Change Request status "in review". During implementation the responsible lead
:need:`[[title]] <rl__technical_lead>` or :need:`[[title]] <rl__module_lead>` reports regularly
the status to the involved **S-CORE** teams until is completed and verified.

The traceability from the Change Request to the affected work products must be established
during implementation.
Also the verification measures must be executed.

.. _chm_verify_change_request:

Verify Change Request
---------------------
:need:`[[title]] <rl__committer>` must finally check, that implementation is complete
and the defined verification measures are properly executed and successfully pass, before the
Change Request can be finally approved.

The Change Request is closed by setting the status to "accepted".

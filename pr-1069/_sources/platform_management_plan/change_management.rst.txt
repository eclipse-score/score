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

.. document:: Change Management Plan
   :id: doc__platform_change_management_plan
   :status: draft
   :safety: ASIL_B
   :tags: platform_management
   :realizes: PROCESS_wp__chm_plan

.. _change_mgmt_plan:

Change Management / Change Management Plan
------------------------------------------

This document implements parts of the :need:`PROCESS_wp__platform_mgmt`.

Purpose
+++++++
The purpose of the Change Management Plan is to guide the execution of the
Change Requests of a project including their creation, analysis, approval, implementation,
and verification.


Objectives and Scope
++++++++++++++++++++

Change Management Goals
^^^^^^^^^^^^^^^^^^^^^^^

* Requests for Changes are recorded and identified.
* Change Requests are analyzed, dependencies and relationships to work products or other Change
  Requests are identified, and the impact is estimated.
* Change Requests are approved before implementation and prioritized accordingly.
* Bidirectional traceability is established between Change Requests and affected work products.
* Implementation of Change Requests is confirmed.
* Change Requests are tracked to closure and status of Change Requests is communicated to
  affected parties.
* Requests for Changes are properly documented.

Approach
++++++++

Change Request Execution
^^^^^^^^^^^^^^^^^^^^^^^^

Contributions in general to the **S-CORE** project are described here
(compare :need:`doc__contr_guideline`).

A Change Request is a specific contribution, and
it is the **ONLY** way to contribute new features/components or to modify the scope of existing
features/components in the **S-CORE** project.

Change Request Infrastructure and Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:need:`GitHub Issues (ISSUE) <doc__issue_guideline>` are used for managing Change Requests.
The tool is used to create, plan, control, and monitor Change Requests within **S-CORE**.

:need:`GitHub Pull Requests (PR) <doc__pull_request_guideline>` are used for the implementation
of Change Requests. The tool is used to implement and verify Change Requests within **S-CORE**.

The next figure gives an overview, how Change Requests are realized in **S-CORE**. An ISSUE is
used to create a Change Request including required attributes as defined in
:need:`PROCESS_gd_req__change__attr_uid`.
The ISSUE may be linked to other ISSUEs or SUB-ISSUEs, if required, to manage more complex Change
Requests. The implementation of a Change Request requires at least one PR linked to the ISSUE created
for the Change Request.

.. figure:: _assets/score_change_request_overview.drawio.svg
  :width: 100%
  :align: center
  :alt: Change Request Overview

  Change Request Overview

Changes are clustered in the following types:

.. list-table:: Change Request Types
   :header-rows: 1
   :widths: 15,85,15

   * - Type
     - Description
     - Infrastructure
   * - Feature
     - Created by :need:`Contributor <PROCESS_rl__contributor>` to change requirements and work products, new feature
     - ISSUE with label ``feature_request``
   * - Feature Modification
     - Created by :need:`Contributor <PROCESS_rl__contributor>` to change requirements and work products, scope change
     - ISSUE with label ``feature_modification``
   * - Component
     - Created by :need:`Contributor <PROCESS_rl__contributor>` to change requirements and work products, new component
     - ISSUE with label ``component_request``
   * - Component Modification
     - Created by :need:`Contributor <PROCESS_rl__contributor>` to change requirements and work products, scope change
     - ISSUE with label ``component_modification``


Change Request Traceability Impact Analysis requires the following tools:

:need:`[[title]] <PROCESS_gd_req__change__tool_impact_analysis>`

Change Request Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^
:need:`PROCESS_gd_req__change__attr_uid` are implemented as follows:

:need:`[[title]] <PROCESS_gd_req__change__attr_uid>` is identical to the ISSUE number.

:need:`[[title]] <PROCESS_gd_req__change__attr_status>` is defined by the combination of the ISSUE state
and the states of the linked PRs.

:need:`[[title]] <PROCESS_gd_req__change__attr_title>` is identical to the ISSUE title.

:need:`[[title]] <PROCESS_gd_req__change__attr_impact_description>` is defined in the linked PR or part of the
description.

:need:`[[title]] <PROCESS_gd_req__change__attr_impact_safety>` is defined in the linked PR or part of the
description.

:need:`[[title]] <PROCESS_gd_req__change__attr_impact_security>` is defined in the linked PR or part of the
description.

:need:`[[title]] <PROCESS_gd_req__change__attr_types>` is defined by label of a ISSUE and part of the
description.

:need:`[[title]] <PROCESS_gd_req__change__attr_affected_wp>` is defined in the linked PR or part of the
description.

:need:`[[title]] <PROCESS_gd_req__change__attr_milestone>` is defined by the Milestone of a ISSUE.


.. _change_mgmt_workflow:

Change Request Workflow
^^^^^^^^^^^^^^^^^^^^^^^

In General, every Change Request follows the following steps:

* 1. Create the Change Request
* 2. Review the Change Request
* 3. Approve the Change Request


**To 1. Create the Change Request:**

An ISSUE is the **ONLY** way to create and manage a Change Request in **S-CORE**.
A PR is the **ONLY** way to implement a Change Request in **S-CORE**,
thus an ISSUE must be linked at least to one or more PRs.

The figure below shows the workflow for the simplest case of a Change Request.

An ISSUE with the label according to the Change Request type is created in status ``OPEN``.
The title of the ISSUE reflects the potential change. The description of the ISSUE may give a brief
description of the requested change or modification. Further add here the
:need:`Impact Analysis Template <PROCESS_gd_temp__change__impact_analysis>` and fill it out accordingly.

The details are part of the Feature/Component Request work product. The Feature/Component Request
is provided by a PR, which is linked to the ISSUE in status ``DRAFT``.

For a new Feature/Component Request the provided templates :need:`Feature Request<PROCESS_gd_temp__change__feature_request>`,
:need:`Component Request<PROCESS_gd_temp__change__component_request>` must be used. For a modification of an existing
Feature/Component, update the existing work products.

The linked PR in status ``DRAFT``, which contains the Feature/Component Requests, may contain also
other required affected and changed work products or implementation and verification proposals.

Planning is done by setting the milestone of the ISSUE accordingly.

As long as the :need:`Contributor <PROCESS_rl__contributor>` wants to modify the content of the Change
Request, the linked PR is kept in status ``DRAFT``.

Change request status: ``draft`` is implemented as
ISSUE status ``OPEN`` and PR status ``DRAFT``.

To trigger the next step the PR status is changed from ``DRAFT`` to ``OPEN``.

.. figure:: _assets/score_change_request_workflow_simple.drawio.svg
  :width: 100%
  :align: center
  :alt: Change Request Simple Workflow Overview

  Change Request Simple Workflow Overview


**To 2. Review the Change Request:**

The Change Request is reviewed from the :need:`Committer <PROCESS_rl__committer>` and the
review results are resolved by the :need:`Contributor <PROCESS_rl__contributor>`. The review results
are documented in the PR. As long as the information is not sufficient, the related PR is kept in
status ``OPEN``.

:need:`PROCESS_gd_chklst__change__cr_review` can help to verify whether the information is complete.

The realisation parts of the Change Request are reviewed according the checklists of the affected
work products. Verification of the realisation parts must be successful.
If the verification is not sufficient, the related PR is kept in status ``OPEN`` or may changed
back to ``DRAFT`` (compare :need:`doc__issue_guideline`).

Change request status: ``in review`` is implemented as
ISSUE status ``OPEN`` and PR status ``OPEN``.


**To 3. Approve the Change Request:**
:need:`Technical Lead <PROCESS_rl__technical_lead>` or  :need:`Module Lead <PROCESS_rl__module_lead>` decides finally,
if the Change Request is accepted or rejected.

:need:`Committer <PROCESS_rl__committer>` checks finally if the Change Request is completed and the
required verification measures are executed and successfully passed.

If ``approved``, the status of the concerned PRs change to ``MERGED``,
otherwise, if rejected, PR status changes to ``CLOSED``.

If ``approved`` the status of the ISSUE is ``CLOSED``. This is also the case for rejected Change
Requests.


The figure below shows the workflow for a complex case of a Change Request.

The ISSUE is linked to SUB-ISSUES, and each SUB-ISSUE is linked to a PR. In principle the Change
Request workflows applies for all SUB-ISSUEs independently. Finally the ISSUE must be closed
manually.

.. figure:: _assets/score_change_request_workflow_complex_1.drawio.svg
  :width: 100%
  :align: center
  :alt: Change Request Complex Workflow Overview Case 1

  Change Request Complex Workflow Overview Case 1

The figure below shows the workflow for another complex case of a Change Request.

Here the Change Request has an impact on work products in different repositories, e.g. the
**S-CORE** repository, contains feature work products and a Module repository, contains
Component work products.
The ISSUE is linked to SUB-ISSUES in the **S-CORE** repository, and the SUB-ISSUE is linked to a PR.
But in addition the ISSUE is now linked to another ISSUE in the Module repository, also linked
to a PR. In principle the Change Request workflows applies for all SUB-ISSUEs, ISSUES in
Module repository independently. Finally the ISSUE in the **S-CORE** repository must be closed
manually.

.. figure:: _assets/score_change_request_workflow_complex_2.drawio.svg
  :width: 100%
  :align: center
  :alt: Change Request Complex Workflow Overview Case 2

  Change Request Complex Workflow Overview Case 2

Change Management SW Platform Work Products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: SW Platform work products
    :header-rows: 1

    * - work product Id
      - Link to process
      - Process status
      - Link to issue
      - Link to WP
      - WP status

    * - :need:`PROCESS_wp__issue_track_system`
      - :doc:`index`
      - :ndf:`copy('status', need_id='doc__platform_mgt_plan')`
      - n/a
      - `Project issues <https://github.com/eclipse-score/score/issues>`_
      - established

    * - :need:`PROCESS_wp__platform_mgmt`
      - :need:`PROCESS_wf__platform__cr_mt_platform_mgmt_plan`
      - :ndf:`copy('status', need_id='PROCESS_wf__platform__cr_mt_platform_mgmt_plan')`
      - <Link to issue>
      - :doc:`index`
      - :ndf:`copy('status', need_id='doc__platform_mgt_plan')`

    * - :need:`PROCESS_wp__process_definition`
      - :need:`PROCESS_wf__def_app_process_definition`
      - :ndf:`copy('status', need_id='PROCESS_wf__def_app_process_definition')`
      - `Process community issues <https://github.com/orgs/eclipse-score/projects/7>`_
      - `Process description <https://eclipse-score.github.io/process_description/main/index.html>`_
      - <automated>

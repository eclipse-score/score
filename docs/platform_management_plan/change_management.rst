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

Change management / Change Management Plan
------------------------------------------

This document implements parts of the :need:`wp__platform_mgmt`.

Purpose
+++++++
The purpose of the Change Management Plan is to guide the execution of the
change requests of a project including their anlysis, evaluation, tracking, approval,
implementation, verification and reporting.


Objectives and Scope
++++++++++++++++++++

Change Management Goals
^^^^^^^^^^^^^^^^^^^^^^^

* Requests for changes are recorded and identified.
* Change requests are analyzed, dependencies and relationships to other change requests are
  identified, and the impact is estimated.
* Change requests are approved before implementation and prioritized accordingly.
* Bidirectional traceability is established between change requests and affected work products.
* Implementation of change requests is confirmed.
* Change requests are tracked to closure and status of change requests is communicated to
  affected parties.
* Requests for changes are properly documented.

Approach
++++++++

Change Request Execution
^^^^^^^^^^^^^^^^^^^^^^^^

Contributions to the **S-CORE** project are the key to grow the content including the code.
Contributions may cover simple improvement proposals, bug or problem reports, but also more complex
scope changes of features up to new feature requests. Depending on the contribution scope,
several steps may be required to finally merge it within the **S-CORE** repository.

A change request is the **ONLY** way to contribute **CODE** to the **S-CORE** project.

As the **S-CORE** project defines a Change Requests as the defined and only allowed trigger to start
the active contribution to the **S-CORE** project. That means obviously that a
:need:`PR (Pull Request) <gd_guidl__platform__pull_request>` is a Change Request.

For simple contributions, like fixing bugs or improvements, just creating a PR is sufficient.

For more complex contributions, like adding a new feature, where it's unfitting to just open a PR,
open a (:need:`GitHub Issue (ISSUE) <gd_guidl__platform__issue>`) to discuss with the community before
starting work on it, would be the preferred way.

You can also join our Slack for real-time discussions.

Summary:

* You want to report something (like a bug) or start a discussion where you do not know the code
  solution yet, open a ISSUE.
* You want to manage complex coordination problems (planning activities) that require collaboration
  across multiple stakeholders, open a ISSUE.
* You want to propose a scope change of a feature or a new feature, open an ISSUE and add required
  PRs to that ISSUE.
* You want to report a bug or problem including a code solution? Start with a PR.
* You want to propose an improvement (also to a process or other work products) including a code
  solution? Start with a PR.

Whenever your PR gets too big or involves committs of several contributors , we strongly encourage
to open and link a ISSUE, so this can get better planned.

For a PR to be merged, in any case an approval of a committer is needed. If the committer decides,
that only a PR is not sufficient and a ISSUE is needed, then the contributor shall also create a
corresponding ISSUE.

ISSUEs are categorized using various types. For categorizing of PRs using of labels, e.g. bug or
improvement, is mandatory (compare :ref:`Platform Management Plan <pmp>`).

For all possibilites the project contains simple templates (provided by committers
(:need:`Committer <rl__committer>`)).

Available templates:
Feature request: :need:`gd_temp__change__feature_request`


.. gd_guidl:: Pull Request Guideline
   :id: gd_guidl__platform__pull_request
   :status: valid

What is a Pull Request (PR)?
""""""""""""""""""""""""""""
A Pull Request (**PR**) is the **ONLY** way to contribute **CODE** to the **S-CORE** project.

The figure below shows a simplified workflow for a PR.

* The contributor (:need:`Contributor <rl__contributor>`) starts by creating a PR:
  `Creating a Pull Request (Github Docs) <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_.
* Required reviewers will be automatically assigned based on the contributed content
  (via CODEOWNERS).
* If the content fullfils the review and acceptance criteria, a
  committer (:need:`Committer <rl__committer>`) will approve the PR and thus it can be merged.

.. figure:: _assets/score_contribution_request_simple.drawio.svg
  :width: 100%
  :align: center
  :alt: Simple PR based contribution request workflow overview

  Simple PR based contribution request workflow overview

Content in general may contain features, requirements, architectural designs, modules, components,
detailed designs, implementations and source code, tests, process descriptions, any documentations,
guidelines, tutorials, tools, or infrastructure topics and more of the **S-CORE** project.
In case of doubt or for any other input we strongly encourage to open a ISSUE first.

The PR should provide all required information of the new or changed content. Therefore the
**S-CORE** project provides content specific templates, which the
contributor (:need:`Contributor <rl__contributor>`) must use for his PR
(ToDo link here to the templates overview). Templates may PR templates, ISSUE templates and also
additional document or work product templates.

The content of any PR is the commit content and the description as well as the comments given in
GitHub and is kept in a versioned repository, their revision history is the historical record
of the PR.

This historical record is available by the normal git commands for retrieving older revisions,
and can also be browsed on GitHub.


Detailed **S-CORE** Pull Request Workflow
"""""""""""""""""""""""""""""""""""""""""
This chapter is only for optional read to understand the details for the Pull Request workflow
defined in **S-CORE**.

The figure below gives an overview about all the possible steps for a PR until it is either
accepted or rejected.

.. figure:: _assets/score_contribution_request_standard.drawio.svg
  :width: 100%
  :align: center
  :alt: Detailed **S-CORE** Pull request workflow overview

  Detailed **S-CORE** Pull request workflow overview

Create a PR
"""""""""""
The contributor (:need:`Contributor <rl__contributor>`) creates a PR.

Reviewers will be automatically assigned (:need:`Committer <rl__committer>`) based on the
contributed content (ruleset as defined by the committers). In addition several checks for the
contributed content (ToDo: Link to the description of the checks) will be started.

Review and merge a PR
"""""""""""""""""""""
A PR is reviewed with all content that adds/modifies it. As long as a PR requires further work by
the contributor (:need:`Contributor <rl__contributor>`), the PR is not approved and thus not merged
and further changes are requested. Once the contributor (:need:`Contributor <rl__contributor>`)
considers all review comments as resolved, :need:`Contributor <rl__contributor>` can re-request a
review. The committer (:need:`Committer <rl__committer>`) reviews the PR content according the
**S-CORE** review and acceptance criteria (ToDo link here to the criteria).
Further the contributor (:need:`Contributor <rl__contributor>`) must resolve found issues from the
automated checks, if they do not pass.

As long as the PR does not meet the defined criteria and the checks does not pass, it will not be
approved. If it does not follow the required templates, based on the provided content or the
templates are not filled out properly, the committer as reviewer (:need:`Committer <rl__committer>`)
will place the PR to the "Draft" state.

It is then the responsibility of the contributor (:need:`Contributor <rl__contributor>`) to add the
missing information and to re-start the contribution by placing the PR back for review.

To change from "Draft" to "Open" see `Changing the stage of a pull request (Github Docs) <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request>`_.

At any point the contributor (:need:`Contributor <rl__contributor>`) may decide not to continue
with the PR, then the contributor (:need:`Contributor <rl__contributor>`) just closes the PR.


.. gd_guidl:: Issue Guideline
   :id: gd_guidl__platform__issue
   :status: valid


What is a GitHub Issue (ISSUE)?
"""""""""""""""""""""""""""""""
A ISSUE is the way to report bugs or propose improvements without knowing the solution and to
request features (incl. scope changes).

For creating GitHub Issue compare here:  `Creating a GitHub Issue (Github Docs) <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue>`_.

Create an ISSUE to collect feedback, before investing too much effort into a PR. ISSUEs may be
accompanied by draft PRs if code is to be shown.

It can also be used to collect community input and for planning and tracking activities.

The figure below shows options to report something.

.. figure:: _assets/score_discussion_request_options.drawio.svg
  :width: 100%
  :align: center
  :alt: Reporting options overview

  Reporting options overview

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

    * - :need:`wp__policies`
      - n/a (comes from outside the project)
      - n/a
      - n/a
      - `Eclipse Foundation Project Handbook: <https://www.eclipse.org/projects/handbook/>`_
      - RELEASED

    * - :need:`wp__issue_track_system`
      - :doc:`index`
      - n/a
      - n/a
      - `Project issues <https://github.com/eclipse-score/score/issues>`_
      - established

    * - :need:`wp__platform_mgmt`
      - :need:`wf__cr_mt_platform_mngmt_plan`
      - n/a
      - <Link to issue>
      - this document
      - see above

    * - :need:`wp__process_definition`
      - :need:`wf__def_app_process_definition`
      - :ndf:`copy('status', need_id='wf__def_app_process_definition')`
      - `Process community issues <https://github.com/orgs/eclipse-score/projects/7>`_
      - :ref:`process_description`
      - <automated>



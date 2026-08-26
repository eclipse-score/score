..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

.. _pull_request:

Pull Request (PR) Guide
=======================

.. document:: Pull Request Guide
   :id: doc__pull_request_guide
   :status: valid
   :version: 1
   :safety: QM
   :security: NO
   :realizes: wp__training_path[version==1]

A Pull Request (**PR**) is the **ONLY** way to contribute **CODE** to the *S-CORE* project.

The figure below shows a simplified workflow for a PR.

* The contributor (:need:`Contributor <rl__contributor>`) starts by creating a PR:  `Creating a Pull Request (Github Docs) <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_.
* Required reviewers will be automatically assigned based on the contributed content (via CODEOWNERS).
* If the content fullfils the review and acceptance criteria, a committer (:need:`Committer <rl__committer>`) will approve the *PR* and thus it can be merged.

.. figure:: _assets/pull_request_simple.drawio.svg
  :width: 600
  :align: center
  :alt: Simple *PR* based contribution workflow overview

  Simple *PR* based contribution workflow overview

Content in general may contain features, requirements, architectural designs, modules, components, detailed designs, implementations and source code, tests, process descriptions, any documentations, guidelines, tutorials, tools, or infrastructure topics and more of the *S-CORE* project. In case of doubt or for any other input we strongly encourage to open a *GitHub Issue* (:need:`doc__issue_guide`) first.

The *PR* should provide all required information of the new or changed content. Therefore the *S-CORE* project provides content specific templates, which the contributor (:need:`Contributor <rl__contributor>`) must use for their *PR* (ToDo link here to the templates overview). Templates may be *PR* templates, *GitHub Issue* templates and also additional document or work product templates.

The content of any *PR* is the commit content and the description as well as the comments given in GitHub and is kept in a versioned repository, their revision history is the historical record of the PR.

This historical record is available by the normal git commands for retrieving older revisions, and can also be browsed on GitHub.


Detailed *S-CORE* Pull Request Workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This chapter is only for optional read to understand the details for the Pull Request workflow defined in *S-CORE*.

The figure below gives an overview about all the possible steps for a *PR* until it is either accepted or rejected.

.. figure:: _assets/pull_request_standard.drawio.svg
  :width: 100%
  :align: center
  :alt: Detailed *S-CORE* Pull request workflow overview

  Detailed *S-CORE* Pull request workflow overview

Create a PR
^^^^^^^^^^^

The contributor (:need:`Contributor <rl__contributor>`) creates a PR.

Reviewers ill be automatically assigned (:need:`Committer <rl__committer>`) based on the contributed content (ruleset as defined by the committers). In addition several checks for the contributed content (ToDo: Link to the description of the checks) will be started.

Review and merge a PR
^^^^^^^^^^^^^^^^^^^^^

A *PR* is reviewed with all content that adds/modifies it. As long as a *PR* requires further work by the contributor (:need:`Contributor <rl__contributor>`), the *PR* is not approved and thus not merged and further changes are requested. Once the contributor (:need:`Contributor <rl__contributor>`) considers all review comments as resolved, :need:`Contributor <rl__contributor>` can re-request a review. The committer (:need:`Committer <rl__committer>`) reviews the *PR* content according the *S-CORE* review and acceptance criteria (ToDo link here to the criteria).
Further the contributor (:need:`Contributor <rl__contributor>`) must resolve found issues from the automated checks, if they do not pass.

As long as the *PR* does not meet the defined criteria and the checks does not pass, it will not be approved. If it does not follow the required templates, based on the provided content or the templates are not filled out properly, the committer as reviewer (:need:`Committer <rl__committer>`) will place the *PR* to the "Draft" state.

It is then the responsibility of the contributor (:need:`Contributor <rl__contributor>`) to add the missing information and to re-start the contribution by placing the *PR* back for review.

To change from "Draft" to "Open" see `Changing the stage of a pull request (Github Docs) <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request>`_.

At any point the contributor (:need:`Contributor <rl__contributor>`) may decide not to continue with the PR, then the contributor (:need:`Contributor <rl__contributor>`) just closes the PR.

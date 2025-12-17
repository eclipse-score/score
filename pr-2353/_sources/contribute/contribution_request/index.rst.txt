..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

.. _contribute_contribution_guideline:

How to Contribute?
##################

.. document:: Contribution Guideline
   :id: doc__contr_guideline
   :status: valid
   :safety: QM

How we Work
===========

At S-CORE, we believe that every contribution makes our platform stronger. Whether you're a seasoned developer or just starting out in open source, your ideas and work are warmly welcomed. We follow a structured yet flexible process rooted in our change management principles and overall lifecycle concept. For more details on our processes, feel free to explore our `Life Cycle Concept <https://eclipse-score.github.io/process_description/main/general_concepts/score_lifecycle_concept.html>`_ and the :need:`doc__platform_change_management_plan`. And if you want to dive right into contributing, check out :ref:`what_is_a_pr` and :ref:`what_is_a_github_issue`.

Feature Requests: Our Shared Roadmap
------------------------------------

Feature requests are at the heart of our evolution. They describe the intended functionality of the S-CORE platform and serve as a collaborative starting point where maintainers and contributors align on new ideas. These requests not only define the motivation and requirements but also shape the technical roadmap for future developments. We invite you to check out all current feature requests on our
`Feature Request Board <https://github.com/orgs/eclipse-score/projects/4>`_.

From Vision to Reality: Calling for Contributions
-------------------------------------------------

Once a feature request is embraced by the community, it becomes a targeted opportunity for innovation. At this stage, we issue a call for contributions, inviting anyone with a solution - whether in-house or open source - to submit a contribution pitch. We ask that your pitch focuses on the technical aspects and clearly outlines how you plan to meet the feature goals (and not a sales pitch 😉). Don't worry if you're still polishing your idea; as long as the source code is already available (or will be within about three weeks with a publicly committed roadmap), you're ready to join in the conversation.

How We Evaluate Contributions
-----------------------------

We work together with contributors to review each pitch based on several criteria:

- **Alignment with the Feature Request:**
  Your solution should fully or partially meet the specified functionality, with room for further enhancements as needed.

- **Availability of the Source Code:**
  We value open source solutions under an OSI-compliant license. If your code isn't public yet, a clear plan to open source it is just as welcome.

- **Technical Maturity:**
  We look at whether your implementation is built in a safety-certifiable subset of C++ or Rust, or if it might need some refinements.

- **Initial Impact Assessment:**
  Please state the assumed impact on other systems. It makes a significant difference if your solution requires other components to refactor versus extending functionality through existing APIs.

- **Supporting Artifacts:**
  To ensure everything is in order for certification and further development, we check that all necessary artifacts are available or that there's a plan to make them available.

For a deeper dive into our evaluation process, you can review the notes from our very first call for contributions on our
`Architecture Community F2F Workshop [2025-02-11 - 2025-02-13] <https://github.com/orgs/eclipse-score/discussions/375>`_.

Once a contribution is selected, it not only implements a new feature but also helps guide the ongoing evolution of S-CORE.

**Replacement of existing functionality**
In S-CORE we aim for having only one solution for a specific problem. If you have an idea for improving an existing feature, you're welcome to pitch a replacement implementation. Just be sure to highlight clearly the benefits over the current solution.


Join Us in Building S-CORE
--------------------------

- **Have a New Idea?**
  Start by raising a new feature request to help expand the scope of our platform.

- **Ready to Code?**
  Submit a contribution pitch for a specific feature request if you have a solution you'd like to share.

- **Looking to Improve What's Already There?**
  Contribute enhancements to existing implementations or get involved with one of our Feature Teams (FTs).

We're excited to have you on board. Together, we can shape S-CORE into a platform that's not only innovative but also a joy to be a part of.

.. _what_is_a_pr:

What is a Pull Request (PR)?
============================

.. document:: Pull Request Guideline
   :id: doc__pull_request_guideline
   :status: valid
   :safety: QM

A Pull Request (**PR**) is the **ONLY** way to contribute **CODE** to the *S-CORE* project.

The figure below shows a simplified workflow for a PR.

* The contributor (:need:`Contributor <rl__contributor>`) starts by creating a PR:  `Creating a Pull Request (Github Docs) <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_.
* Required reviewers will be automatically assigned based on the contributed content (via CODEOWNERS).
* If the content fullfils the review and acceptance criteria, a committer (:need:`Committer <rl__committer>`) will approve the *PR* and thus it can be merged.

.. figure:: _assets/score_contribution_request_simple.drawio.svg
  :width: 600
  :align: center
  :alt: Simple *PR* based contribution workflow overview

  Simple *PR* based contribution workflow overview

Content in general may contain features, requirements, architectural designs, modules, components, detailed designs, implementations and source code, tests, process descriptions, any documentations, guidelines, tutorials, tools, or infrastructure topics and more of the *S-CORE* project. In case of doubt or for any other input we strongly encourage to open a *GitHub Issue* (:need:`doc__issue_guideline`) first.

The *PR* should provide all required information of the new or changed content. Therefore the *S-CORE* project provides content specific templates, which the contributor (:need:`Contributor <rl__contributor>`) must use for his *PR* (ToDo link here to the templates overview). Templates may be *PR* templates, *GitHub Issue* templates and also additional document or work product templates.

The content of any *PR* is the commit content and the description as well as the comments given in GitHub and is kept in a versioned repository, their revision history is the historical record of the PR.

This historical record is available by the normal git commands for retrieving older revisions, and can also be browsed on GitHub.


Detailed *S-CORE* Pull Request Workflow
---------------------------------------

This chapter is only for optional read to understand the details for the Pull Request workflow defined in *S-CORE*.

The figure below gives an overview about all the possible steps for a *PR* until it is either accepted or rejected.

.. figure:: _assets/score_contribution_request_standard.drawio.svg
  :width: 100%
  :align: center
  :alt: Detailed *S-CORE* Pull request workflow overview

  Detailed *S-CORE* Pull request workflow overview

Create a PR
-----------

The contributor (:need:`Contributor <rl__contributor>`) creates a PR.

Reviewers will be automatically assigned (:need:`Committer <rl__committer>`) based on the contributed content (ruleset as defined by the committers). In addition several checks for the contributed content (ToDo: Link to the description of the checks) will be started.

Review and merge a PR
---------------------

A *PR* is reviewed with all content that adds/modifies it. As long as a *PR* requires further work by the contributor (:need:`Contributor <rl__contributor>`), the *PR* is not approved and thus not merged and further changes are requested. Once the contributor (:need:`Contributor <rl__contributor>`) considers all review comments as resolved, :need:`Contributor <rl__contributor>` can re-request a review. The committer (:need:`Committer <rl__committer>`) reviews the *PR* content according the *S-CORE* review and acceptance criteria (ToDo link here to the criteria).
Further the contributor (:need:`Contributor <rl__contributor>`) must resolve found issues from the automated checks, if they do not pass.

As long as the *PR* does not meet the defined criteria and the checks does not pass, it will not be approved. If it does not follow the required templates, based on the provided content or the templates are not filled out properly, the committer as reviewer (:need:`Committer <rl__committer>`) will place the *PR* to the "Draft" state.

It is then the responsibility of the contributor (:need:`Contributor <rl__contributor>`) to add the missing information and to re-start the contribution by placing the *PR* back for review.

To change from "Draft" to "Open" see `Changing the stage of a pull request (Github Docs) <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request>`_.

At any point the contributor (:need:`Contributor <rl__contributor>`) may decide not to continue with the PR, then the contributor (:need:`Contributor <rl__contributor>`) just closes the PR.

.. _what_is_a_github_issue:

What is a GitHub Issue?
=======================

.. document:: Issue Guideline
   :id: doc__issue_guideline
   :status: valid
   :safety: QM

A *GitHub Issue* is the way to report bugs or propose improvements without knowing the solution and to request features (incl. scope changes).

For creating *GitHub Issue* compare here:  `Creating a GitHub Issue (Github Docs) <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue>`_.

Create an *GitHub Issue* to collect feedback, before investing too much effort into a *PR*. *GitHub Issues* may be accompanied by draft *PRs* if code is to be shown.

It can also be used to collect community input and for planning and tracking activities.

The figure below shows options to report something.

.. figure:: _assets/score_discussion_request_options.drawio.svg
  :width: 400
  :align: center
  :alt: Reporting options overview

  Reporting options overview

.. toctree::
   :hidden:
   :maxdepth: 2

   feature_request

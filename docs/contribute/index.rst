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

.. _contribution_guide:

Contribution Guide
##################


.. document:: Contribution Guide
   :id: doc__contribution_guide
   :status: valid
   :version: 1
   :safety: QM
   :security: NO
   :realizes: wp__training_path[version==1]


.. note::

  There is no single path: you can fix a small bug, implement a requested feature, or simply start a
  conversation with the community. The sections below describe the most common entry points.

  **Join Us in Building S-CORE**


  - **Have a New Idea?**
     Start by raising a new feature request to help expand the scope of our platform.

  - **Ready to Code?**
     Submit a contribution pitch for a specific feature request if you have a solution you'd like to share.

  - **Looking to Improve What's Already There?**
      Contribute enhancements to existing implementations or get involved with one of our Feature Teams (FTs).

  We're excited to have you on board. Together, we can shape S-CORE into a platform that's not only innovative but also a joy to be a part of.


How to get in contact with S-CORE
=================================

If you want to get into contact with S-CORE, these are your primary entry points:

- `Project/Technical Leads <https://github.com/orgs/eclipse-score/discussions/104>`__
- `Platform Architects <https://github.com/orgs/eclipse-score/discussions/110>`__


How to get involved into S-CORE
===============================

The only way to influence S-CORE is **TO CONTRIBUTE**. Everybody can contribute - S-CORE is open.

Active Contributions to the S-CORE project are the basis for getting involved. The S-CORE Project works according to the Eclipse Project Handbook and has named and elected project leads and committers (see `Eclipse Safe Open Vehicle Core <https://projects.eclipse.org/projects/automotive.score>`_). The direction of the S-CORE project is discussed and decided in the project lead circle, the technical direction is created and upfront in the tech lead circle. Meeting notes are transparent via the `S-CORE GitHub Discussions <https://github.com/orgs/eclipse-score/discussions>`_.

We aim to build a safety ready full stack architecture, where components fit to each other in automotive grade Software Quality and performance. To achieve this, we follow a strict :ref:`feature roadmap and architecture <platform_releases>` and a `rigid software development process <https://eclipse-score.github.io/process_description/main/index.html>`_ (currently under development).

Contributions to the S-CORE project must therefore follow the technical direction of the project and the S-CORE architecture.

Based on successful code contributions to the S-CORE roadmap, further steps in involvement (like becoming a committer) will be handled according to the rules of the Eclipse Foundation Project Handbook. We value real code based collaboration and will judge new potential contributors and committers mainly on the validity of their work. Active and sustaining contributions are the basis for the ability to shape S-CORE.


How is S-CORE organized
=======================

Eclipse S-CORE is an open source project, so everyone is welcome to contribute. Since we are organized within the Eclipse Foundation, you must have an Eclipse Foundation account to participate - please see :ref:`contribution_attribution_guide` for details.

The project is structured into various :ref:`communities <pmp_pm_communities>`, which focus on cross-cutting topics and :ref:`feature teams <pmp_pm_feature_teams>` responsible for the implementation of specific functionalities. Their meetings are public; feel free to join or review the minutes via our `GitHub Discussions <https://github.com/orgs/eclipse-score/discussions>`_.

Additionally, :ref:`steering committees <pmp_pm_steering_committees>`, the Technical / Project Lead Circle, oversee the overall steering and planning of S-CORE.

For further details on our project structure and planning, please refer to the :need:`Project Management Plan <doc__project_mgt_plan>`.

How to Set Up your Environment
===============================

Find the necessary information for setting up your :ref:`Development Environment <setup_dev_environment>` ready.

How to become a Contributor
===========================

#. **Read the Introduction** — Work through the complete :ref:`Introduction <introduction>` from top to bottom to
   build a solid foundation of S-CORE knowledge.

#. **Start the S-CORE test application "scrample"** — Run `Scrample <https://github.com/eclipse-score/scrample/releases>`_ locally to experience the
   full development loop (build, test, CI/CD) on a real, self-contained project.

#. **Implement an open issue and create a pull request** — Pick up an open issue in any S-CORE
   module repository, implement your fix or improvement, and go through the pull-request review
   process.

#. **Get in touch with the project leads** — Once you have proven basic S-CORE knowledge,
   contact the project leads. If your capability and planned capacity are substantial, you may
   qualify for a **Buddy Program**: a dedicated project lead guides you (or your team)
   personally until your first task is assigned, and stays available for potential long-term
   support on request.

#. **Become an Eclipse S-CORE Contributor** - Steps to be done for ensuring contributions are correctly attributed to organizations in the **Eclipse S-CORE** project: :ref:`Contribution Attribution <contribution_attribution_guide>`.




How we Work
===========

At S-CORE, we believe that every contribution makes our platform stronger.
Whether you're a seasoned developer or just starting out in open source, your ideas and work are warmly welcomed.
We follow a structured yet flexible process rooted in our change management principles and overall lifecycle concept.
For more details on our processes, feel free to explore our `Life Cycle Concept <https://eclipse-score.github.io/process_description/main/general_concepts/score_lifecycle_concept.html>`_
and the :need:`doc__platform_change_management_plan`.

Issues and Pull Requests
------------------------

All activities shall be planned and documented with the help of :ref:`Issues <issue>` and :ref:`Pull Requests <pull_request>`

Feature Requests
----------------

Feature requests are at the heart of our evolution. They describe the intended functionality of the S-CORE platform and serve as a collaborative starting point where maintainers and contributors align on new ideas. These requests not only define the motivation and requirements but also shape the technical roadmap for future developments. We invite you to check out all current feature requests on our
`Feature Request Board <https://github.com/orgs/eclipse-score/projects/4>`_.

New Feature and major Feature Modification requests go through the :ref:`Feature Request Guideline <feature_request_guideline>`, where an Architecture Community Shepherd guides the proposal to a Final Comment Period before it's decided. Component-level and single-Feature-Team changes are handled directly by the responsible team, as described in the :need:`doc__platform_change_management_plan`.

From Vision to Reality: Calling for Contributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once a feature request is embraced by the community, it becomes a targeted opportunity for innovation. At this stage, we issue a call for contributions, inviting anyone with a solution - whether in-house or open source - to submit a contribution pitch. We ask that your pitch focuses on the technical aspects and clearly outlines how you plan to meet the feature goals (and not a sales pitch 😉). Don't worry if you're still polishing your idea; as long as the source code is already available (or will be within about three weeks with a publicly committed roadmap), you're ready to join in the conversation.

How We Evaluate Contributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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




What rules to follow
====================

.. needtable:: Parts of SW Development Plan
   :style: table
   :columns: title;id;status
   :colwidths: 45,45,10
   :sort: docname
   :filter: "wp__sw_development_plan" in realizes


Where to find more trainings
============================

.. needtable:: Training Documents
   :style: table
   :columns: title;id;status
   :colwidths: 45,45,10
   :sort: docname
   :filter: "wp__training_path" in realizes





.. toctree::
   :hidden:
   :maxdepth: 2

   contribute_new_module/index

   documentation/docs-as-code_guide
   documentation/publishing-gh-pages

   development/api_guideline
   development/setup_dev_environment
   development/traceability_guidelines

   development/cpp/cpp_code_analysis
   development/cpp/cpp_coding_guidelines
   development/cpp/cpp_misra_rules

   development/fork/index


   development/rust/rust_api_design
   development/rust/rust_coding_guidelines

   development/python/python_coding_guidelines

   feature_request/feature_request

   general/naming_conventions
   general/git
   general/issue
   general/pullrequest

   general/folder_structure_convention
   general/feature_flags
   general/contribution_attribution_guide
   general/module_release_guide

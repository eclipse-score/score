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

.. document:: Project Management Plan
   :id: doc__project_mgt_plan
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__project_mgt
   :tags: platform_management

.. _pmp_pm_plan:

Project Management Plan
-----------------------

Purpose
+++++++
The purpose of the Project Management Plan is to define

- how to manage, analyze and control changes of the work products during the project life cycle.
- the project stakeholder and how to communicate with them.
- how and where to create and maintain the project schedule.
- how to track planned work.
- how and where to escalate.

Objectives and Scope
++++++++++++++++++++

Project Management Goals and Definition of Done
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*  The stakeholders/stakeholder groups and organization are defined:
    - :ref:`Org Chart and structure description <pmp_pm_organization>` is available and up to date.
* Communication and reporting paths are described:
    - Team Overview with meeting structure is available & Slack channels are established and maintained.
    - Meetings are scheduled in the Eclipse SDV calendar.
* The scope of the work is defined.
    - S-CORE Handbook (:need:`doc__platform_handbook`) is available and up to date.
    - :ref:`Features <features>` are described.
* Project Plan is planned and followed:
    - Roadmap with :ref:`Milestones <pmp_pm_milestone>` and :ref:`Releases <pmp_pm_release>` are available and up to date.
    - :ref:`Features <features>` are described.
* Escalation paths are described.
* All Reviews are performed according to their definitions, the respective templates are used.

.. _pmp_pm_organization:

Project Organization
++++++++++++++++++++


Org Chart and Main Platform Management Plan Responsibilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: _assets/score_project_management_organization_orgchart.drawio.svg
   :width: 900
   :alt: Infrastructure overview
   :align: center

.. _pmp_pm_steering_committees:

Steering Committees
^^^^^^^^^^^^^^^^^^^
Steering of the project is done with the help of *Lead Circles*.

.. _pmp_pm_lc:

- `TLC - Technical Lead Circle <https://github.com/orgs/eclipse-score/discussions/104>`_

.. _pmp_pm_communities:

Communities
^^^^^^^^^^^
*Communities* are installed to work on cross functional topics, such as program level architectural decisions,
commonly used development & testing infrastructure, processes or final integration & release.
Each *Community* has a *Community Lead* to organize the community`s work.

.. _pmp_pm_arc:

- `ARC - Architecture Community <https://github.com/orgs/eclipse-score/discussions/110>`_
- `PRC - Process Community <https://github.com/orgs/eclipse-score/discussions/108>`_
- `INF - Infrastructure Community <https://github.com/orgs/eclipse-score/discussions/107>`_
- `TST - Testing Community <https://github.com/orgs/eclipse-score/discussions/109>`_
- `REL - Release Community <https://github.com/orgs/eclipse-score/discussions/2884>`_

.. _pmp_pm_mcm:

- `MCM - Marketing and Communication Community <https://github.com/orgs/eclipse-score/discussions/106>`_


Feature Teams
^^^^^^^^^^^^^
*Feature Teams*  have end-to-end responsibility for providing specific functionalities. This includes all
development aspects beginning with the architecture definition to the integration test.
One *Team* may work independently of other *Teams* on the team-assigned *GitHub Issues*,
and needs at least one :need:`Committer <rl__committer>` who can approve & merge the Pull Requests.
Each *Feature Team* has one *Lead* to organize the Team`s work.

- `BAS - Baselibs Feature Team <https://github.com/orgs/eclipse-score/discussions/1223>`_
- `COM - Communication Feature Team <https://github.com/orgs/eclipse-score/discussions/112>`_
- `CFG - Configuration Feature Team <https://github.com/orgs/eclipse-score/discussions/2283>`_
- `DIA - Diagnostics Feature Team <https://github.com/orgs/eclipse-score/discussions/2632>`_
- `FEO - Fixed Execution Order Feature Team <https://github.com/orgs/eclipse-score/discussions/113>`_
- `LCM - Lifecycle Feature Team <https://github.com/orgs/eclipse-score/discussions/1798>`_
- `LOG - Logging Feature Team <https://github.com/orgs/eclipse-score/discussions/114>`_
- `ORC - Orchestration Feature Team <https://github.com/orgs/eclipse-score/discussions/115>`_
- `PER - Persistency Feature Team <https://github.com/orgs/eclipse-score/discussions/116>`_
- `SEC - Security Feature Team <https://github.com/orgs/eclipse-score/discussions/2839>`_
- `TIM - Timings Feature Team <https://github.com/orgs/eclipse-score/discussions/2890>`_

Organization Management
^^^^^^^^^^^^^^^^^^^^^^^
Decision to adapt the *Project Organization* is done in the *Technical Lead Circle* / *Project Management Circle*, documented in the meeting minutes and planned with a *Task*:

- creating of a new Team (*Community* or *Feature Team*)
- setting an existing Team (*Community* or *Feature Team*) on hold
- deleting an existing Team (*Community* or *Feature Team*)

Creation of a new Feature Team
""""""""""""""""""""""""""""""
In case a new Feature Team creation is necessary, the following steps have to be done:

- `Adding a new Team to GitHub Teams <https://github.com/orgs/eclipse-score/teams>`_ and adding the Core Members by editing
  `orgs.newTeam <https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet>`_.
- Adding a new Repository to GitHub by editing
  `orgs.newRepo <https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet>`_.
- Definition of Repository specific :ref:`CODEOWNERS <pmp_pm_codeowners>`.
- `Creation of a Team GitHub Project <https://github.com/orgs/eclipse-score/projects>`_ with a Kanban View and a Task View.
- `Creation of a Team Discussion <https://github.com/eclipse-score/score/discussions>`_ for basic information and meeting minutes etc.
- Creation of a Team Label

.. code::

    committee:<Name of Committee>,
    community:<Name of Community> or
    ft:<Name of Feature Team>

- Creation of a Slack Channel: https://sdvworkinggroup.slack.com
- Adapting the PMP

External Communication
**********************
The external communication is done via GitHub, LinkedIn, etc. Publications by :ref:`Marketing and Communication Community <pmp_pm_mcm>`.


Internal Communication
++++++++++++++++++++++
The project internal communication is ensured with help of:

- virtual and face-to-face meetings and their minutes
- *GitHub issues* and *GitHub pull requests*
- online communication using Slack

Meetings
^^^^^^^^
All meetings are scheduled in the `Eclipse S-CORE Calendar <https://calendar.google.com/calendar/u/0/embed?src=c_2ampi2bmoka3qter4dceap1d5g@group.calendar.google.com&ctz=Europe/Berlin>`_ , are open for everyone
but mentioned team members are mandatory. Meeting minutes are public and stored in the project specific *GitHub Team Wikis*.


.. _pmp_pm_repository_structure:

Repository structure
++++++++++++++++++++
The Platform follows a multiple repositories approach. The root repository is

.. _pmp_pm_root_repository:

https://github.com/eclipse-score.

It contains among others:

- :ref:`stakeholder requirements <Stakeholder_Requirements>`
- documentation of all :ref:`platform features <features>`, features flags,
  feature requirements and architecture
- build system including *S-CORE* specific *macros* and *rules*
- integration rules for software modules.

which are stored in the :ref:`Folder Structure of Platform Repository <platform_folder_structure>`.


Every software module has its own repository, that contains among others:

- multiple components
- their requirements
- architecture
- implementation
- tests

within the following :ref:`Module Folder Structure <module_folder_structure>`.


.. _pmp_pm_codeowners:

Codeowners
^^^^^^^^^^
While creating a new repository, :ref:`Project / Technical Leads <pmp_pm_lc>` nominate initial `CODEOWNERS <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners#codeowners-and-branch-protection>`_,
whose review is mandatory for merging PRs to the repository and who are at the end allowed to merge PRs to the repository as well as maintaining it.

Possible members are software developers , who

- understand how the particular feature works or should work
- are the initial authors of the software
- and are :need:`Committers <rl__committer>`

The Codeownership has to be regularly updated and changes have to be documented.

Planning & Tracking
+++++++++++++++++++

Cadence
^^^^^^^

Iteration
"""""""""
The Project calendar is divided into iterations. Each iteration is two weeks long.

Release Frequence
"""""""""""""""""
After every 4th iteration, the work is baselined into a Release.


Planning & Tracking Infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The planning and tracking of the work is done inside **GitHub**.
GitHub **Issues** are used to document all necessary work packages.

Issues
^^^^^^
To organize the work :ref:`Github Types <pmp_pm_issue_types>`,  :ref:`GitHub Labels <pmp_pm_gh_labels>` and
:ref:`GitHub Projects <pmp_pm_gh_projects>` are used.
The Progress of the work is documented with help of the :ref:`Status of an Issue <pmp_pm_issue_status_flow>`.


.. _pmp_pm_issue_types:

Issues Types
""""""""""""

.. image:: _assets/score_project_management_issue_types.drawio.svg
   :width: 900
   :alt: Issue Types
   :align: center

|

Architectural Issues
""""""""""""""""""""

.. _pmp_pm_feature_request:

**Feature Request**

A *Feature Request* represents an independent work package used to describe and
track a high-level request for the project. *Feature Request* work packages can be linked to
other work packages, but they must not be treated as parent work packages. *Feature Request* covers new Features as well as significant modifications of existing Features.
They are in the responsibility of the :ref:`Architecture Community <pmp_pm_arc>`, shall aligned with :ref:`Lead Circle <pmp_pm_lc>` and the issues are part of the :ref:`Root Repository <pmp_pm_root_repository>`.

`About Features <https://eclipse-score.github.io/score/main/features/index.html>`_

`Feature Request issue template <https://github.com/eclipse-score/.github/.github/ISSUE_TEMPLATE/1a_FeatureRequest.yml>`_

.. _pmp_pm_component_request:

**Component Request**

A *Component Request* represents an independent work package used to describe modifications inside a *Feature*, either adding new components or modifying existing ones.
*Component Request* work packages can be linked to other work packages, but they must not be treated as parent work packages. They shall be discussed with
:ref:`Architecture Community <pmp_pm_arc>` and the issues are owned by a Team and are part of the Team`s main repository..

`About Components <https://eclipse-score.github.io/score/main/modules/index.html>`_

`Component Request issue template <https://github.com/eclipse-score/.github/.github/ISSUE_TEMPLATE/1b_ComponentRequest.yml>`_


Planning Issues
"""""""""""""""

.. _pmp_pm_product_increment:

**Product Increment**

A *Product Increment* represents the highest level in the work package hierarchy and
cannot be linked as a child of another issue. If you need to group multiple *Product Increment* work packages,
labels have to be used. One *Product Increment* is the planning element for a version of a :ref:`Module <modules>`.
A *Product Increment* can have multiple *Epic* work packages as children. *Product Increments* are owned by
:ref:`Lead Circle <pmp_pm_lc>` and are part of the :ref:`Root Repository <pmp_pm_root_repository>`.

`Product Increment issue template <https://github.com/eclipse-score/.github/.github/ISSUE_TEMPLATE/2_ProductIncrement.yml>`_

.. _pmp_pm_epic:

**Epic**

An *Epic* is the primary planning work package for development teams.
*Epic* work packages should be scoped in a way that allows them to be completed within
a release cycle of the S-CORE project.
While an *Epic* can be implemented by multiple team members, it is recommended
that one developer takes main responsibility for its completion. Quality assurance activities,
such as code reviews, can be performed by other team members.
*Epics* are typically grouped under an *Product Increment*. However, an *Epic* work package can also exist
as a standalone work package if its outcome represents a complete functional improvement,
making a related *Product Increment* work package unnecessary.
Sometimes support of other teams might be necessary for the completion of the work, therefore an
*Epic* can have team-internal and team-external *Task* child issues. *Epics* are owned by a Team and are part
of the Team`s main repository.

`Epic issue template <https://github.com/eclipse-score/.github/.github/ISSUE_TEMPLATE/3_ProductIncrement.yml>`_

.. _pmp_pm_task:

**Task**

A *Task GitHub Issue* represents the smallest unit of planning and typically corresponds
to a concrete piece of work to be completed, such as by a developer. *Task* work packages are usually
grouped under an *Epic* work package.
In certain cases, a *Task* may exist as a standalone *GitHub Issue*.
However, standalone *Task* work packages must not be grouped using labels.
If multiple *Task* work packages are related, a *Epic* work package should be created instead,
with all associated *Task* work packages added as child work packages under that *Epic*. *Tasks* are owned by a Team and are part
of any Team`s repository.

`Task issue template <https://github.com/eclipse-score/.github/.github/ISSUE_TEMPLATE/4_Task.yml>`_

.. _pmp_pm_bug:

**Bug**

A *Bug GitHub Issue* is used to report any kind of problem or malfunction. It is considered
a special type of work package and follows the same rules as regular *Epic* work packages,
with the key difference that it focuses on fixing defects in existing functionality
rather than creating or extending functionality. *^Bugs* are owned by a Team and are part
of any Team`s repository.

`Bug issue template <https://github.com/eclipse-score/.github/.github/ISSUE_TEMPLATE/5_Bug.yml>`_

.. _pmp_pm_issue_status_flow:

Issue Status
""""""""""""
Each *GitHub issue* has a **Status** depending on the :ref:`GitHub Project <pmp_pm_gh_projects>`,
we use the following Standard Flow for all :ref:`Issue Types <pmp_pm_issue_types>`:

.. image:: _assets/score_project_management_issue_status_flow.drawio.svg
    :width: 900
    :alt: Issue Status
    :align: center

Issue Attributes
""""""""""""""""
- Standard Attributes
    - Assignees
    - :ref:`Labels <pmp_pm_gh_labels>`
    - :ref:`Type <pmp_pm_issue_types>`
- Common Project Attributes
    - :ref:`Status <pmp_pm_issue_status_flow>`
    - Priority (1 - High, 2 - Middle, 3 - Low)
    - Size (S - Day, M - Week, L - Month, XL - Quarter)
    - (planned finishing) Iteration



Issue Templates
"""""""""""""""
Templates defined in *GitHub* ensure the availability of the type relevant information for all issues.

Hierarchies
"""""""""""
Hierarchies are realized as parent-child relations with the `GitHub Sub-Issue Feature <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues>`_.

Dependencies
""""""""""""
Dependencies are realized with blocked by or blocking relations described in the `GitHub Issue Dependency Feature <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies>`_.

.. _pmp_pm_milestone:

Milestone
^^^^^^^^^
A milestone is indicating an important dedicated point in the schedule like
a Release or a Process Audit, etc.
`GitHub Milestones <https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones>`_ offer to connect *Issues* and *Pull Requests* to the `S-CORE-defined Milestones <https://github.com/eclipse-score/score/milestones>`_

.. _pmp_pm_release:

Releases
^^^^^^^^
*Releases* are special milestones and used for baselining of the development activities.

.. _pmp_pm_gh_labels:


Labels
^^^^^^
`GitHub Labels <https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels>`_ are used to organize Issues, Pull Requests etc. having same context. Although
Labels are powerful, the definition of new Labels shall be wisely done and organization wide used.
Therefore their management is limited to Organization owners.

The following `Labels <https://github.com/eclipse-score/score/labels>`_ are defined.

.. _pmp_pm_gh_projects:

GitHub Projects
^^^^^^^^^^^^^^^
The `GitHub Project Feature <https://docs.github.com/en/issues/planning-and-tracking-with-projects>`_
helps to plan the work and monitor its progress.

Multiple *GitHub Projects* are defined at https://github.com/orgs/eclipse-score/projects/.

Beside one for each (committee, community, feature) Team, there is one for `Feature / Component Requests <https://github.com/orgs/eclipse-score/projects/4>`_
and one for the complete `Roadmap <https://github.com/orgs/eclipse-score/projects/17>`_. Inside a GitHub Project, there is the possibility to generate different views
for Table, Board and Roadmap supporting Backlogs, Open Point or Task Lists and other useful perspectives.

.. image:: _assets/score_project_management_planning_overview.drawio.svg
    :width: 900
    :alt: Planning Overview
    :align: center



Kanban View
"""""""""""
The `GitHub Board <https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-board-layout>`_ is supporting the Kanban View, enabling to set the Work In Progress Limits.

.. image:: _assets/score_project_management_kanban.drawio.svg
    :width: 900
    :alt: Kanban View
    :align: center


Task List View
""""""""""""""
The `GitHub Table <https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-table-layout>`_ is supporting the List View, enabling to adapt the priority by reordering the rows.

Roadmap View
""""""""""""
The `GitHub Roadmap <https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout>`_ is supporting the Road View, provididing a high-level visualization of your project across a configurable timespan.

Traceability
^^^^^^^^^^^^
To achieve traceability all *Pull Requests* have to be `linked <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue>`_
to the corresponding *GitHub Issues*.

Planning of Work
^^^^^^^^^^^^^^^^

Generally, every team is responsible for planning its work within its own plan with the help of its :ref:`GitHub Project <pmp_pm_gh_projects>` filled with :ref:`Epics <pmp_pm_epic>`, :ref:`Tasks <pmp_pm_task>` and :ref:`Bugs <pmp_pm_bug>`.

The planning of :ref:`Feature Requests <pmp_pm_feature_request>` and :ref:`Component Requests <pmp_pm_component_request>` is in the responsibility of the :ref:`Architects <pmp_pm_arc>`,
whereas the overall top-down plan is in the responsibility of the :ref:`Lead Circle <pmp_pm_lc>` with the help of :ref:`Product Increments <pmp_pm_product_increment>`,
:ref:`Milestones <pmp_pm_milestone>` and :ref:`Releases <pmp_pm_release>`.

.. image:: _assets/score_project_management_process_issue_overview.drawio.svg
    :width: 600
    :alt: Planning Overview
    :align: center




Tracking Progress
^^^^^^^^^^^^^^^^^
The :ref:`Lead Circle <pmp_pm_lc>` regularly monitors the status of the work for upcoming Milestones and Releases in https://github.com/orgs/eclipse-score/projects/17/ based on
:ref:`Product Increments <pmp_pm_product_increment>`.


Dashboards
""""""""""

GitHub offers mechanism in form of charts to track issues see `Insights <https://github.com/orgs/eclipse-score/projects/17/insights>`_.

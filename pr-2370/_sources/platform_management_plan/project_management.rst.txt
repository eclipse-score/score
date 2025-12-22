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

.. document:: Project Management Plan
   :id: doc__project_mgt_plan
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__project_mgt
   :tags: platform_management

Project management plan
#######################

Project organization
====================

.. _pmp_pm_steering_committees:

Steering committees
-------------------
Steering of the project is done by two committees: *project lead circle* and *technical lead circle*.

* **Project lead circle**

  Members of *Project lead circle* are the project leads of the *S-CORE* project. The election of project leads is done as described in the `Project Roles chapter <https://www.eclipse.org/projects/handbook/#roles-pl>`_ of *Eclipse Foundation Project Handbook*. In case of absence, a project lead can nominate a deputy.

  The main tasks of the *Project lead circle* are:

  * Definition, discussion of and decisions about strategical topics (e.g. which associations to approach, confirmation of roadmap, representation in public).
  * Decision on which new software modules should be added or removed from the project. The decision is done based on proposal from the *Technical lead circle*. In case of changes to the existing modules and no concordant decision in the *Technical Lead Circle*, the *Project Lead Circle* has to decide about the change.
  * Election of Technical Leads.
  * Last instance of escalation path.

  *Project lead circle* proposes and elects a *Project lead circle Assistant* and his deputy with bare majority, who is responsible for scheduling and announcing meetings, preparing and announcing agenda, writing meeting minutes and protocols. *Project lead circle* can reelect *Project lead circle Assistant* at any time. The *Project lead circle Assistant* and his deputy can resign anytime on their own will.

* **Technical lead circle**

  Each *Project Lead* is allowed to nominate one *Technical Lead*. The *Technical Leads* form the "Technical Lead Circle". In case of absence, a technical lead can nominate a deputy. *Technical Leads* have the following responsibilities:

  * Review and approval of contributions, e.g. *Feature Requests*, which add or modify S-CORE platform features.
  * Project management of the platform development, e.g., creation of the roadmap.
  * High-level project control and coordination between multiple software modules.
  * Escalation instance for software module project leads and committers.

  *Technical lead circle* proposes and elects a *Technical lead circle Assistant* and his deputy with bare majority during *Technical Lead Circle meeting*, who is responsible for scheduling and announcing meetings, preparing and announcing agenda, writing meeting minutes and protocols. *Technical lead circle* can reelect *Technical lead circle Assistant* at any time. The *Technical lead circle Assistant* and his deputy can resign anytime on their own will.

.. _pmp_pm_technical_committees:

Technical committees
--------------------
* **Communities**

  *Communities* allow committers and contributors to exchange their
  opinions, take architectural decisions and implement the topics of some special
  technical domain, e.g. testing tooling. One of the *Communities*' important activities
  is to do a breakdown of platform sagas to the concrete tasks (see `Planning`_) .
  Currently following *Communities* are defined in the *S-CORE* project:

  * *Infrastructure*: *community* for all kind of infra topics:
    compiler, IDE, build toolchain and etc. See `GitHub Discussions/Infrastructure Community  <https://github.com/orgs/eclipse-score/discussions/categories/infrastructure-community>`_ for more.
  * *Testing*: *community* to clarify questions and define testing strategy
    for the 'S-CORE' project. See `GitHub Discussions/Testing Community <https://github.com/orgs/eclipse-score/discussions/categories/testing-community>`_ for more.
  * *Software Architecture*: *community* for clarification of software architecture topics,
    e.g. discussion of new features or coding guidelines. See `GitHub Discussions/Architecture Community <https://github.com/orgs/eclipse-score/discussions/categories/architecture-community>`_ for more.
  * *Software Development Process*: *community* for definition and maintaining
    of safety, security and quality software development process. See `GitHub Discussions/SW Dev Process Community <https://github.com/orgs/eclipse-score/discussions/categories/sw-dev-process-community>`_ for more.
  * *Marketing & Communication (MarCom)*: *community* for coordination of public relations, e.g. the maintenance of the website & organization of general events.
    See `GitHub Discussions/MarCom Community <https://github.com/orgs/eclipse-score/discussions/categories/marcom-community>`_ for more.

  The planning of the activities is done by every *Community* independent of other
  teams. Each *Community* has a *Community Lead*, who is nominated by the *Technical lead circle*. The prioritization of some topics can be requested by the *Technical lead circle*
  in order to achieve milestones on time. All important architectural decisions
  should be reported to the project as *Feature Request* to get the final approvement from the *Technical lead circle*.

* **Feature Teams**

  *Feature Teams* have end-to-end responsibility for specific functionalities. This includes all
  aspects beginning with the architecture definition to the integration test. They are usually assigned
  to the *S-CORE* main integration project or to one particular software module. *Feature Teams* work
  independently of each other on *GitHub Issues* in the assigned software module.
  *Feature Teams* consist mainly of the contributors, who can specify requirements, define architecture,
  develop source code and implement tests afterwards. *Project Leads* and *Committers* are also *Contributors*
  and effectively work on processing of *GitHub Issues*.

  Every *Feature Team* should have at least one committer who can approve and merge the Pull Requests of the Contributors.

  Every *Feature Team* should also have a *Feature Team Lead*. The person with this role is responsible for
  organizing the meetings, writing meeting protocols and representing the current status of the *Feature Team*
  work in various management reporting or plannig calls. *Feature Team Lead* is nominated by *Technical Leads* by election.
  Normally, this is the owner of the original *Feature Request*.


Creation of a new Feature Team
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Decision to create a new *Feature Team* is normally done in *Technical Lead Circle* in case a particular,
already *accepted* *Feature Request* can not be assigned to any of already existing *Feature Teams*.

As a first step, the decision to create a new Feature Team is protocolled in the `Tech Lead Circle meeeting minutes <https://github.com/orgs/eclipse-score/discussions/categories/technical-lead-circle>`_.
Afterwards a GitHub Issue is created in the `Technical Lead Cirle LOP project <https://github.com/orgs/eclipse-score/projects/3>`_
using the special *Feature Team Creation* GitHub Issue template and is assigned to one of the Technical Leads.

**ToDo**: create such a template.

Usage of the special GitHub Issue template ensures, that all GitHub issues for creation of new *Feature
Teams* follow the same rules, e.g. that the title always has the same format or
that the description always contains the reasoning for the creation of a new *Feature Team*.

Additionally, the GitHub Issue created from the template includes a *DoD list*, which serves as a checklist
for the Technical Lead to ensure that all necessary activities and steps have been completed to establish a new *Feature Team*.
Its current *DoD list* is always documented in the template. The most important activities are:

* **Creation of labels**

  Every *Feature Team* should have its own label for filtering of GitHub Issues, PRs or discussions.

* **Creation of discussion**

  Every *Feature Team* should have its own discussion section in the `Feature Teams section <https://github.com/orgs/eclipse-score/discussions>`_
  of the main *S-CORE* project.

* **Adding a new Team to the main S-CORE GitHub project**

  Every *Feature Team* should be added as a further select option of the "Team" field
  in the `main S-CORE project <https://github.com/orgs/eclipse-score/projects/17/views/27>`_, so that *Technical Leads*
  can assign tickets to the team and filter for the tickets of the new team.
  Additionally, every team is free to create its own GitHub project, but then the team tickets should be still
  visible in the main S-CORE project.

* **Creation of repository**

  Normally, every *Feature Team* should have a dedicated repository. Creation of new repository is done
  be extending the `otterdog configuration file <https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet>`_
  and creating a new PR, that has to be approved by the *Eclipse Project Security Team*. Creation of the
  repository is the responsibility of the *Feature Team Lead*.

* **Developer GitHub Team**

  Every *Feature Team* should have a corresponding software developer GitHub team, e.g. *ipc_ft_dev*, that contains all
  developers, that are actively participating in this *Feature Team*. This GitHub group can be used e.g. to
  send notifications for upcoming meetings or discussions.

* **Codeowner GitHub Team**

  Every *Feature Team* should have a corresponding codeowner GitHub team, e.g. *ipc_ft_co*, that contains all
  software developers, whose review is mandatory for every PR in the repository and who have rights to merge PRs to the repository.


Merge rights & code ownership
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As already stated, every *Feature Team* has normally a dedicated repository. Before the creation of the new repository,
*Feature Team Lead* together with *Technical Leads* should nominate initial codeowners, whose review is mandatory for merging PRs to the repository
and who is at the end allowed to merge PRs to the repository.

In the S-CORE project, the configuration whose review is mandatory to merge a PR to the repository is done
using `CODEOWNERS file and branch protection <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners#codeowners-and-branch-protection>`_ .
Every repository has a CODEOWNERS file, where one or multiple teams are specified, whose review is needed for the PR
to be able to be merged. The teams listed there are normally:

* *Codeowner GitHub Team* for this *Feature Team*
* GitHub Team for security managers
* GitHub Team for quality managers
* GitHub Team for safety managers

**ToDo**: can we have an 'AND relationship' for teams in CODEOWNERS file?

*Codeowner GitHub Team* for the corresponding *Feature Team* consists of the software developers, that understand how
the particular feature works or should work. The members of this team should be selected and agreed
during the creation of the *Feature Team* by the *Technical Leads* and *Feature Team Lead*. The criteria for the selection should be the
technical competence of the software developers, e.g. in case during the :ref:`Feature Request process <feature_request_guideline>`
it was decided to take over already existing source code, then persons who were actively participating in the
development of that code are always good candidates to be part of *Codeowner GitHub team*.
The decision who should be initially part of the *Codeowner GitHub team* and the reasoning for this
should be protocolled in the GitHub Issue, that is used for creation of the *Feature Team*.

In case further software developers should be added to the *Codeowener GitHub team* in the future,
that decision and its reasoning should be protocolled in one of the *Feature Team* GitHub discussions.

Members of the *Codeowner GitHub team* should also be authorized to merge pull requests (PRs) into the corresponding repository.
Therefore, once the *Codeowner GitHub team* has been created, the Technical Lead assigned to the ticket for the *Feature
Team* setup should initiate committer elections for all software developers in the *Codeowner GitHub team*.
All other Technical Leads who are already committers in the S-CORE project are expected to support these
elections by voting positively, provided there are no specific objections.

Meeting Structure
-----------------

* **Project Lead Circle meeting**

  Regular participants of *Project Lead Circle meeting* are the *Project Leads* and *Technical Leads* of the main *S-CORE* project. The main purpose of the meeting is the exchange between *Project Leads* and the reporting of the *Technical Lead Circle* to the *Project Lead Circle* and vice versa.

  The *Project Lead Circle meetings* are announced via *score-dev@eclipse.org* mailing list and are open for everyone who is registered to this mailing list. All meetings are documented as *GitHub Discussions* in `Project Lead Circle section <https://github.com/orgs/eclipse-score/discussions/categories/project-lead-circle>`_ and can be read by everyone. Topics for the *Project lead circle meetings* can be proposed only by regular participants and will be prioritized by the *Project lead circle Assistant*. Proposals for agenda topics can be added as comment to the respective *GitHub Discussion* or sent to the *Project lead circle Assistant*.

  Open points from the meetings will be handled by *GitHub Issues* in the *S-CORE* main repository and can be filtered via *project_lead_circle* label.

  The *Project Lead Circle meeting* takes place usually once a week.


* **Technical Lead Circle meeting**

  Regular participants of the *Technical Lead Circle meeting* are the *Technical Leads* of the main *S-CORE* project. The main purpose of the meeting is the exchange between technical leads for fulfilling their responsibilities.

  The *Technical Lead Circle meetings* are announced via *score-dev@eclipse.org* mailing list and are open for everyone who is registered to this mailing list. All meetings are documented as *GitHub Discussions* in `Technical Lead Circle section <https://github.com/orgs/eclipse-score/discussions/categories/technical-lead-circle>`_ and can be read by everyone. Topics for the *Technical lead circle meetings* can be proposed only by regular participants and will be prioritized by the *Technical lead circle Assistant*. Proposals for agenda topics can be added as comment to the respective *GitHub Discussion* or sent to the *Technical lead circle Assistant*.

  Open points from the meetings will be handled by *GitHub Issues* in the *S-CORE* main repository and can be filtered via label *technical_lead_circle*.

  The *Technical Lead Circle meeting* takes place usually once a week.

* **Committer Circle Meeting**

  Regular participants of the *Committer Circle meeting* are the *Committers* of the main *S-CORE* project and of all software modules/child projects. The *Committer Circle Meeting* is lead by the *Technical Leads*. The main purpose of the meeting are in-depth technical discussions and evaluation of contributions, e.g. *Feature Requests*, that could not be approved in the *Technical Lead Circle meeting* and demand more technical discussions.

  The *Committer Circle meetings* are announced via *score-dev@eclipse.org* mailing list and are open for everyone who is registered to this mailing list. All meetings are documented as *GitHub Discussions* in `Committer Circle section <https://github.com/orgs/eclipse-score/discussions/categories/committer-circle>`_ and can be read by everyone. Topics for the *Committer circle meetings* can be proposed only by regular participants and will be prioritized by the *Technical lead circle*. Proposals for agenda topics can be added as comment to the respective *GitHub Discussion* or sent to the *Technical lead circle Assistant*.

  The *Committer Circle meeting* takes place on demand. The decision for the scheduling of the *Committer Circle Meeting* is taken by the *Technical Lead Circle*.

Platform structure
==================
Platform consists of multiple repositories. The main repository, *S-CORE*,
is the integration repository, where everything comes together. It contains:

* :ref:`stakeholder requirements <Stakeholder_Requirements>`
* documentation of all :ref:`platform features <features>` and features flags,
  feature requirements and architecture
* build system including *S-CORE* specific *macros* and *rules*
* integration rules for software modules.

The main repository references multiple other repositories, mostly repositories, where
software modules or toolchains are defined. This results in the following :ref:`Folder Structure of Platform Repository <platform_folder_structure>`. Every software module has its own repository, that contains multiple components, their requirements, architecture, implementation and tests.
A software module and its repository can be part of the main S-CORE *Eclipse Project* and corresponding *GitHub organization* or can be moved to a standalone *Eclipse child project*, if necessary.

  .. image:: _assets/project_organization.svg
     :width: 900
     :alt: Infrastructure overview
     :align: center

Platform organization
=======================
Also in case the software module repositories are not placed
in standalone *Eclipse child projects*, we still consider all software modules
to be standalone *Eclipse child projects*, having their own *Committers* and *Project Leads*
as defined by the *Eclipse Foundation Project Handbook*. Software module committers
and software module project leads are responsible for managing the software module as if it were
a normal *Eclipse child project*. The election of the project leads and committers for software module projects should be done using the main integration *S-CORE* project mailing list, *score-dev@eclipse.org*. This means, that the decision who will be the project lead and committer of the new software module will be taken by the project leads and committers of the main *S-CORE* project respectively. The elected project leads or committers of the software modules are not automatically project leads and committers of the main integration *S-CORE* project. Typically, before becoming a project lead or a committer of the main integration *S-CORE* project, you need to build up a good reputation by contributing to the main integration *S-CORE* project and being project lead or committer for one of the software modules.

Before introducing a new *Eclipse child project* for a software module, it should first reside as a repository in the main *S-CORE* project. If the software module later would be moved to a real standalone *Eclipse child project*, e.g., as there is a wish to use this software module independent of the *S-CORE* project, then the elected project leads and committers of the software module will be simply taken over as project leads and committers of the new *Eclipse child project* and their tasks will stay the same. Further in this document differentiation between a software module and  *Eclipse child project* will be done only if necessary. For the software module that resides in the separate repository of the main *S-CORE* project, the configuration and the control
of who is committer and project lead is done using
`CODEOWNER files <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners>`_
located in the subfolder of the corresponding repository of the software module.

Main task of project leads is planning and prioritizing of activities, and together with the committers maintaining of the backlog and ensuring, that the software development is done according to process described in the main S-CORE project. The planning should be done as described in the `Planning`_ chapter. A more detailed description of PLs' and Committers' activities is given in *Eclipse Foundation Project Handbook*.

The main project *S-CORE* has certainly also project leaders and committers, but
their roles are slightly different compared to the software module committers and
project leads. The role of the *S-CORE* project as the central project is, as already
described, to ensure proper integration of multiple software modules, provide common
integration guidelines and mechanisms, e.g. build toolchain. Additionally *S-CORE* project
takes care of all overarching topics, as e.g. roadmap and milestone planning or
definition of cross-functional topics. Therefore there exist number of additional
meetings, where such topics are discussed and decided, see `Steering committees`_ for further details.

Planning
========

Planning infrastructure
------------------------
`GitHub issues <https://github.com/features/issues>`_ are used to plan and to track
work. To be able to find issues faster and to filter for them more efficiently,
we use labels.

Labels
^^^^^^
To facilitate the organization and tracking of tickets related to the same feature
or topic, labels are utilized for issues and pull requests. Labels are a powerful
feature that allows you to search and filter tickets based on specific labels, and
you can save these filters in a *GitHub Project* view. However, it is important
to exercise caution when creating labels to avoid confusion and ensure easy tracking.

It's worth noting that labels are associated with a repository, not a *GitHub Project*.
To create new labels in the repository requires special rights and only
*project leads* and *committers* should have this capability.

For the main *S-CORE* repository, there exist already some predefined labels:

* *feature_request* label is used to identify *PRs* and *GitHub Issues* that are part
  of a *Feature request process*
* *project_lead_circle*  label is used to identify *PRs* and *GitHub Issues* that are relevant
  for *Project lead circle*
* *tech_lead_circle*  label is used to identify *PRs* and *GitHub Issues* that are relevant
  for *Technical lead circle*
* *infrastructure*  label is used to identify *PRs* and *GitHub Issues* that are relevant
  for *Tooling/Infrastructure Community*
* *testing*  label is used to identify *PRs* and *GitHub Issues* that are relevant for
  *Testing Community*
* *software_architecture*  label is used to identify *PRs* and *GitHub Issues* that are relevant
  for *Software Architecture community*
* *software_development_process*  label is used to identify *PRs* and *GitHub Issues* that are
  relevant for *Software Development Process Community*

  .. image:: _assets/contribution_request_label.png
     :width: 800
     :alt: Infrastructure overview
     :align: center

Additionally, in the main *S-CORE* repository there should exist a label for every
software module.

Every software module project, located in another repository, is free to define
additionally its own labels. It is recommended to create labels at least
for specific areas that may encompass multiple features.

Types of work packages and structure
------------------------------------
For better structuring of the tickets following *GitHub Issue* types are introduced
in the main *S-CORE* repository. In order to create a consistent overview of all work packages (WPs),
the WPs need to be maintained in one single project within the main *S-CORE* repository.
Having separate WP backlogs within separate repositories will increase the complexity
and reduce the transparency too much.

All *child projects* are only allowed to have their separate list of issues. All other WP types
shall not be available for them. The planning WPs of the main *S-CORE* repository therefore are used
to link WPs to *GitHub issues* of *child projects*.
For example a *Bug* WP within the main repository is linked to a *GitHub Issue* of the *communication*
repository but no *Bug* WP shall be created in the *child project* repository.

.. image:: _assets/issue_types.png
    :width: 600
    :alt: Issue types overview
    :align: center

* A *Task* *GitHub Issue* represents the smallest unit of planning and typically corresponds
  to a concrete piece of work to be completed, such as by a developer. *Task* work packages are usually
  grouped under a *Story* work package.
  In certain cases, a *Task* may exist as a standalone *GitHub Issue*.
  However, standalone *Task* work packages must not be grouped using labels.
  If multiple *Task* work packages are related, a *Story* work package should be created instead,
  with all associated *Task* work packages added as child work packages under that *Story*.

* A *Story* *GitHub Issue* is the primary planning work package for development teams.
  *Story* work packages should be scoped in a way that allows them to be completed within
  the release cycle of the S-CORE project.
  While a *Story* work package can be implemented by multiple team members, it is recommended
  that one developer takes main responsibility for its completion. Quality assurance activities,
  such as code reviews, should be performed by other team members.
  *Story* work packages are typically grouped under an *Product Increment* work package.
  However, a *Story* work package can also exist as a standalone work package if its outcome represents
  a complete functional improvement, making a related *Product Increment* work package unnecessary.

* A *Product Increment* *GitHub Issue* represents the highest level in the work package hierarchy and
  cannot be linked as a child of another issue. If you need to group multiple *Product Increment* work packages,
  this must be done using labels.
  A *Product Increment* work package can have multiple *Story* work packages as child work packages.
  In exceptional cases, a *Story* work package may also be linked as a child of a *Product Increment* work package
  if its outcome represents a complete functional improvement.

* A *Feature Request* *GitHub Issues* represents an independent work package used to describe and
  track a high-level request for the project. *Feature Request* work packages can be linked to
  other work packages, but they must not be treated as parent work packages.

* A *Bug* *GitHub Issue* is used to report any kind of problem or malfunction. It is considered
  a special type of *Story* work package and follows the same rules as regular *Story* work packages,
  with the key difference that it focuses on fixing defects in existing functionality
  rather than creating or extending functionality.

Main *S-CORE* project defines templates for every type of *GitHub Issues*
to ensure, that every ticket has all necessary information.

For a better structuring of the *GitHub Issues*, we use a beta
`sub-issue feature <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues>`_,
that should be officially released in the beginning of 2025.
*Sub-issue feature* allows to create a "parent-child" relationship between *GitHub Issues*.
That allows better structuring of the project and helps to keep *GitHub Issues*, that
are related to the same topic, together.

.. image:: _assets/sub_issues.png
    :width: 600
    :alt: Sub issues overview
    :align: center

Traceability
^^^^^^^^^^^^
To achieve a better traceability it is highly recommended to link all *PRs* to the corresponding
*GitHub Issues*. If done properly, you will be able to see for every *GitHub Issue*
all relevant source code changes. Normally *PRs* reference *GitHub issues* of type *Story*
or of type *Bug*. How to link *PRs* to *GitHub Issues* is described in more details in this
`guide <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue>`_.

.. image:: _assets/traceability.png
    :width: 300
    :alt: Traceability overview
    :align: center

GitHub Projects
^^^^^^^^^^^^^^^
*GitHub Projects* is a very powerful tool that allows creation of various views on
the status of the project, helps to plan the work and to monitor the current progress.
In particular, *GitHub Project* allows to extend *GitHub Issues* with following information:

* objective
* dependencies on other activities or information
* responsible person
* resources
* mapping to work product
* start, end, duration, effort

Note: The information on start, end, duration, and effort may sometimes be complicated
to estimate in the execution in an open source environment. Nevertheless, tasks
should be planned as part of releases, which sets already an implicit
duration and end date.

Software module project leads shall also use *GitHub Project* for their planning. The overview of *GitHub Project* features can be found `here <https://docs.github.com/en/issues/planning-and-tracking-with-projects>`_.

Multiple *GitHub projects* are defined in the main *S-CORE* project:

* a separate project for every community
* a project for technical lead circle
* a (GitHub) *roadmap project* with the overview of all upcoming features & releases.

  As *GitHub Projects* are not restricted to one repository but
  can include information from multiple repositories of the same organization,
  *roadmap project* gives an overview of all *Sagas*, that are relevant for the roadmap,
  including those ones in the software modules. Prerequisite for this is that project
  leads of all software modules always assign their sagas to the *roadmap project*.
  All sagas in the *roadmap project* are extended with additional information
  as e.g. start date and due date, to keep the status of the project always transparent.
  Additionally, the main *S-CORE* repository defines project wide milestones & releases,
  that are visible in the roadmap as well.

.. image:: _assets/roadmap_example.png
    :width: 600
    :alt: Roadmap example
    :align: center

Releases and milestones
^^^^^^^^^^^^^^^^^^^^^^^^
GitHub allows to define various milestones & releases for every repository. The definition of the milestones and releases is proposed by the *Technical Leads* and is approved by *Project Leads*.

In the main *S-CORE* project we use milestones to mark important stages of the project and map sagas or in some cases also other *GitHub Issues* to them.

*Releases* are used for structuring of the development activities. Exact scheme for the releases of the *S-CORE* will be provided here later.

You can find "up to date" overview of the release plan and milestones in the following section `S-CORE Releases <https://eclipse-score.github.io/score/score_releases/index.html>`_.

The users of the S-CORE platform need to adapt their planning to the milestones defined in the S-CORE project,
but they have always the possibility to takeover the development of a new feature, modifications and bugfixes
in their own development branch / fork and merge these improvements in the next or later releases
back into the S-CORE "main" line.

Planning process
----------------
Generally, every team is responsible for planning and managing of its backlog.
For small improvements or clarifications, you can create *GitHub Issue* with a exhaustive
description and map it to the topic using labels. For small improvements/bugs
in the software modules you should create *GitHub Issues* directly in the repository
of the submodule. The project leads and committers of the corresponding software module,
circle or community will check the issue and in case they will accept it, they will
take it over to one of their *GitHub Projects*. In case, the topic, that you raise in the issue has a big impact on the platform, you can be asked by the committers to raise a *Feature Request* and to do a POC in the `incubation repository <https://eclipse-score.github.io/score/features/integration/index.html#incubation-repositories>`_ .

Contribution to the project is described in more details in `Contribution Guideline <https://eclipse-score.github.io/score/main/contribute/index.html>`_.
In general, everyone who wants to provide something new to the project, e.g. a new feature
or a tool, should provide an exhaustive description, requirements and in some cases
also initial draft of the architecture as part of the *Feature Request*.
*Feature Requests* are regularly reviewed in the *Technical lead circle*
and then get either accepted or declined.

After the *Feature Request* was accepted, then the *Pull Request* with the
*Feature Request* gets merged. The corresponding *GitHub Issue* gets a reference to the
newly defined saga which plans the implementation of the feature request and afterwards *GitHub Issue* for *Feature Request* gets closed. The saga is at the beginning in the state *"Draft"*. Please be aware, that "status" of the tickets is modelled in *GitHub Project* as *GitHub Issues* do not provide the possibility to define additional states.

The *Technical lead circle* is responsible for maintenance of the backlog with sagas,
their prioritization and creation of the roadmap. Together with software module
project leads and community leads in the "Committer circle" they go through the backlog, decide when and which saga should be implemented in which order and update the roadmap accordingly.

As soon as the saga was planned for implementation, its state is changed to *"Open"*.
As next step, a *GitHub Issue* of type *epic* is created as sub-issue of the saga
and gets assigned to one of the *Communities* for refinement. The state of the saga changes from "Open" to "In Specification".

.. image:: _assets/saga_status_workflow.svg
    :width: 900
    :alt: Planning workflow
    :align: center

The members of the *Responsible Community* define or refine feature, process or tool requirements. They may also create feature architecture and high level component requirements for every involved software component. Depending on the feature scope, one of the feature team can be requested to make a POC in the `incubation repository <https://eclipse-score.github.io/score/features/integration/index.html#incubation-repositories>`_. Finally, *Responsible Community* does the break down of the corresponding *saga* to the tickets that can be assigned to the individual software modules or *communities*.
As most of the software modules will have their own separate repository,
then the detailed tracking of their work will also happen inside of that repository.
However, the corresponding saga of the S-CORE repository will still have a sub-issue of type epic,
that will describe the work, that should be done inside of the software module for better planning.
In the epic description there should be a link to the software module repository ticket,
where the detailed information and break down to the stories can be found.
For those communities or modules, that are part of the main *S-CORE* repository,
the break down to the stories should be done directly inside of the epic.

As soon as the work on saga starts, its status is changed to "In Progress"
and its sub-tickets get assigned to the project leads of the software modules
or leads of the *communities*. During the development of the saga,
we use "trunk based approach", it means, that we do not create any separate branches,
but develop the software directly in the trunk/main using feature flag, that is marked as "experimental" at the beginning.

The *Technical lead circle* regularly monitors the status of the sagas with the status
"In Progress", resolves conflicts and updates the roadmap if necessary.

As soon as the saga is implemented and fulfills to 100% our software development process requirements, the decision is taken in the *Technical lead circle* whether the feature should be
officially available and in case of the positive decision, the feature flag status
is changed from "experimental" to "official".

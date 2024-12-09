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

Project management plan
#######################

+---------------------------+-------------------------------+
| DOCUMENT IDENTIFICATION   |                               |
+===========================+===============================+
| Document Type             | Plan                          |
+---------------------------+-------------------------------+
| Document ID               | PROJECT-MANAGEMENT-PLAN       |
+---------------------------+-------------------------------+
| Project Name              | SCORE                         |
+---------------------------+-------------------------------+
| ASIL                      | B                             |
+---------------------------+-------------------------------+
| AUTHOR                    | <Process Manager>             |
+---------------------------+-------------------------------+
| Reviewer                  | <Quality Manager>             |
+---------------------------+-------------------------------+
| Approver                  | <Project Manager>             |
+---------------------------+-------------------------------+
| Status                    | DRAFT                         |
+---------------------------+-------------------------------+

Project organization
====================

Steering committees
-------------------
Steering of the project is done by two committees: *project lead circle* and *technical lead circle*.

* **Project lead circle**

  Members of *Project lead circle* are the project leads of the *SCORE* project. The election of project leads is done as described in the `Project Roles chapter <https://www.eclipse.org/projects/handbook/#roles-pl>`_ of *Eclipse Foundation Project Handbook*. In case of absence, a project lead can nominate a deputy.

  The main tasks of the *Project lead circle* are:

  * Definition, discussion of and decisions about strategical topics (e.g. which associations to approach, confirmation of roadmap, representation in public).
  * Decision on which new software modules should be added or removed from the project. The decision is done based on proposal from the *Technical lead circle*. In case of changes to the existing modules and no concordant decision in the *Technical Lead Circle*, the *Project Lead Circle* has to decide about the change.
  * Election of new Project Leads.
  * Election of Technical Leads.
  * Last instance of escalation path.

  *Project lead circle* proposes and elects a *Project lead circle Assistant* and his deputy with bare majority, who is responsible for scheduling and announcing meetings, preparing and announcing agenda, writing meeting minutes and protocols. *Project lead circle* can reelect *Project lead circle Assistant* at any time. The *Project lead circle Assistant* and his deputy can resign anytime on their own will.

* **Technical lead circle**

  Each *Project Lead* is allowed to nominate one *Technical Lead*. The *Technical Leads* form the "Technical Lead Circle". In case of absence, a technical lead can nominate a deputy. *Technical Leads* have the following responsibilities:

  * Review and approval of *Contribution Requests*, which add or modify SCORE platform features.
  * Project management of the platform development, e.g., creation of the roadmap.
  * High-level project control and coordination between multiple software modules.
  * Escalation instance for software module project leads and committers.

  *Technical lead circle* proposes and elects a *Technical lead circle Assistant* and his deputy with bare majority during *Technical Lead Circle meeting*, who is responsible for scheduling and announcing meetings, preparing and announcing agenda, writing meeting minutes and protocols. *Technical lead circle* can reelect *Technical lead circle Assistant* at any time. The *Technical lead circle Assistant* and his deputy can resign anytime on their own will.

Technical committees
--------------------
* **Communities**

  *Communities* allow committers and contributors to exchange their
  opinions, take architectural decisions and implement the topics of some special
  technical domain, e.g. testing tooling. One of the *Communities*' important activities
  is to do a breakdown of platform sagas to the concrete tasks (see `Planning`_) .
  Currently following *Communities* are defined in the *SCORE* project:

  * *Tooling/Infrastructure*: *community* for all kind of infra topics:
    compiler, IDE, build toolchain and etc.
  * *Testing*: *community* to clarify questions and define testing strategy
    for the 'SCORE' project
  * *Software Architecture*: *community* for clarification of software architecture topics,
    e.g. discussion of new features or coding guidelines.
  * *Software Development Process*: *community* for definition and maintaining
    of safety, security and quality software development process.

  The planning of the activities is done by every *Community* independent of other
  teams. Each *Community* has a *Community Lead*, who is nominated by the *Technical lead circle*. The prioritization of some topics can be requested by the *Technical lead circle*
  in order to achieve milestones on time. All important architectural decisions
  should be reported to the project as *Contribution Request*
  to get the final approvement from the *Technical lead circle*.

* **Cross functional teams**

  *Cross functional teams* are responsible for some piece
  of work from the beginning (e.g. definition of the architecture) till the end
  (e.g. integration tests) and are usually assigned to the *SCORE* main integration project or to one particular software module. *Cross-functional teams* work independently from each other on *GitHub* issues in the assigned software module. *Cross-functional teams* consist of the contributors, who can specify requirements, define architecture, develop source code and implement tests afterwards. *Project Leads* and *Committers* are also *Contributors* and effectively work on processing of *GitHub* issues.

  *Cross-functional team* usually consists of the following roles: Project Lead, Safety Manager, Quality Manager, Security Manager, Committers and Contributors. Every *cross-functional* team has at least one committer who can approve and merge the Pull Requests of the Contributors.

  In case *Cross-functional team* needs to request a new repository, this can be done be extending the `otterdog configuration file <https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet>`_ and creating a new PR, that should be approved by the *Eclipse Project Security Team*.


Meeting Structure
-----------------

* **Project Lead Circle meeting**

  Regular participants of *Project Lead Circle meeting* are the *Project Leads* and *Technical Leads* of the main *SCORE* project. The main purpose of the meeting is the exchange between *Project Leads* and the reporting of the *Technical Lead Circle* to the *Project Lead Circle* and vice versa.

  The *Project Lead Circle meetings* are announced via *score-dev@eclipse.org* mailing list and are open for everyone who is registered to this mailing list. All meetings are documented as *GitHub Discussions* in `Project Lead Circle section <https://github.com/orgs/eclipse-score/discussions/categories/project-lead-circle>`_ and can be read by everyone. Topics for the *Project lead circle meetings* can be proposed only by regular participants and will be prioritized by the *Project lead circle Assistant*. Proposals for agenda topics can be added as comment to the respective *GitHub Discussion* or sent to the *Project lead circle Assistant*.

  Open points from the meetings will be handled by *GitHub Issues* in the *SCORE* main repository and can be filtered via *project_lead_circle* label.

  The *Project Lead Circle meeting* takes place usually once a week.

* **Technical Lead Circle meeting**

  Regular participants of the *Technical Lead Circle meeting* are the *Technical Leads* of the main *SCORE* project. The main purpose of the meeting is the exchange between technical leads for fulfilling their responsibilities.

  The *Technical Lead Circle meetings* are announced via *score-dev@eclipse.org* mailing list and are open for everyone who is registered to this mailing list. All meetings are documented as *GitHub Discussions* in `Technical Lead Circle section <https://github.com/orgs/eclipse-score/discussions/categories/technical-lead-circle>`_ and can be read by everyone. Topics for the *Technical lead circle meetings* can be proposed only by regular participants and will be prioritized by the *Technical lead circle Assistant*. Proposals for agenda topics can be added as comment to the respective GitHub discussion or sent to the *Technical lead circle Assistant*.

  Open points from the meetings will be handled by GitHub Issues in the *SCORE* main repository and can be filtered via label *technical_lead_circle*.

  The *Technical Lead Circle meeting* takes place usually once a week.

* **Committer Circle Meeting**

  Regular participants of the *Committer Circle meeting* are the *Committers* of the main *SCORE* project and of all software modules/child projects. The *Committer Circle Meeting* is lead by the *Technical Leads*. The main purpose of the meeting are in-depth technical discussions and evaluation of the *Contribution Requests*.

  The *Committer Circle meetings* are announced via *score-dev@eclipse.org* mailing list and are open for everyone who is registered to this mailing list. All meetings are documented as GitHub Discussions in `Committer Circle section <https://github.com/orgs/eclipse-score/discussions/categories/committer-circle>`_ and can be read by everyone. Topics for the *Committer circle meetings* can be proposed only by regular participants and will be prioritized by the *Technical lead circle*. Proposals for agenda topics can be added as comment to the respective GitHub discussion or sent to the *Technical lead circle Assistant*.

  The *Committer Circle meeting* takes place on demand. The decision for the scheduling of the *Committer Circle Meeting* is taken by the *Technical Lead Circle*.

Platform structure
==================
Platform consists of multiple repositories. The main repository, *SCORE*,
is the integration repository, where everything comes together. It contains:

* :ref:`stakeholder requirements <Stakeholder_Requirements>`
* documentation of all :ref:`platform features <Platform_Features>` and features flags,
  feature requirements and architecture
* build system including *SCORE* specific *macros* and *rules*
* integration rules for software modules.

The main repository references multiple other repositories, mostly repositories, where
software modules or toolchains are defined. This results in the following :ref:`Folder Structure of Platform Repository <Platform_Folder_Structure>`. Every software module has its own repository, that contains multiple components, their requirements, architecture, implementation and tests.
A software module and its repository can be part of the main SCORE *Eclipse Project* and corresponding *GitHub organization* or can be moved to a standalone *Eclipse child project*, if necessary.

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
a normal *Eclipse child project*. The election of the project leads and committers for software module projects should be done using the main integration *SCORE* project mailing list, *score-dev@eclipse.org*. This means, that the decision who will be the project lead and committer of the new software module will be taken by the project leads and committers of the main *SCORE* project respectively. The elected project leads or committers of the software modules are not automatically project leads and committers of the main integration *SCORE* project. Typically, before becoming a project lead or a committer of the main integration *SCORE* project, you need to build up a good reputation by contributing to the main integration *SCORE* project and being project lead or committer for one of the software modules.

Before introducing a new *Eclipse child project* for a software module, it should first reside as a repository in the main *SCORE* project. If the software module later would be moved to a real standalone *Eclipse child project*, e.g., as there is a wish to use this software module independent of the *SCORE* project, then the elected project leads and committers of the software module will be simply taken over as project leads and committers of the new *Eclipse child project* and their tasks will stay the same. Further in this document differentiation between a software module and  *Eclipse child project* will be done only if necessary. For the software module that resides in the separate repository of the main *SCORE* project, the configuration and the control
of who is committer and project lead is done using
`CODEOWNER files <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners>`_
located in the subfolder of the corresponding repository of the software module.

Main task of project leads is planning and prioritizing of activities, and together with the committers maintaining of the backlog and ensuring, that the software development is done according to process described in the main SCORE project. The planning should be done as described in the `Planning`_ chapter. A more detailed description of PLs' and Committers' activities is given in *Eclipse Foundation Project Handbook*.

The main project *SCORE* has certainly also project leaders and committers, but
their roles are slightly different compared to the software module committers and
project leads. The role of the *SCORE* project as the central project is, as already
described, to ensure proper integration of multiple software modules, provide common
integration guidelines and mechanisms, e.g. build toolchain. Additionally *SCORE* project
takes care of all overarching topics, as e.g. roadmap and milestone planning or
definition of cross-functional topics. Therefore there exist number of additional
meetings, where such topics are discussed and decided, see `Steering committees`_ for further details.

Planning
========
coming soon

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

Project Management Plan
#######################

.. document:: Project Management Plan
   :id: doc__project_mgt_plan
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__project_mgt
   :tags: platform_management

.. _pmp_pm_organization:

Project Organization
====================

.. code::

   Team Documentation Structure in this Document:

   - Responsibilities
   - Members
   - Speaker / Lead
   - Meeting Minutes
   - Slack channel
   - Open Point List
   - Repository Ownership


..
   Team Template

   XYZ Team (XYZ)
   ^^^^^^^^^^^^^^

   .. _XYZ Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-XYZ-team
   .. _XYZ Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-XYZ-lead
   .. _XYZ Meeting Minutes: https://github.com/eclipse-score/score/wiki/XYZM
   .. _XYZ Slack Channel: https://sdvworkinggroup.slack.com/archives/XYZ
   ..  _XYZ Open Point List: https://github.com/orgs/eclipse-score/projects/XYZ


   - XYZ Responsibilities
     - tbd
   - `XYZ Core Members`_
   - `XYZ Lead`_
   - `XYZ Meeting Minutes`_
   - `XYZ Slack Channel <>`_
   - `XYZ Open Point List <>`_
   - XYZ Repositories:
     - https://github.com/eclipse-score/tbd


Org Chart and Main Platform Management Plan Responsibilities
------------------------------------------------------------

.. image:: _assets/organization_orgchart.drawio.svg
   :width: 900
   :alt: Infrastructure overview
   :align: center


.. _pmp_pm_steering_committees:

Steering Committees
-------------------
Steering of the project is done by two committees:

Project Lead Circle (PLC)
^^^^^^^^^^^^^^^^^^^^^^^^^
.. _PLC Members: https://github.com/orgs/eclipse-score/teams/automotive-score-PLC-team
.. _PLC Speaker: https://github.com/orgs/eclipse-score/teams/automotive-score-PLC-lead
.. _PLC Meeting Minutes: https://github.com/eclipse-score/score/wiki/PLCM
.. _PLC Slack Channel: https://sdvworkinggroup.slack.com/archives/PLC
.. _PLC Open Point List: https://github.com/orgs/eclipse-score/projects/PLC

- Responsibilities
   - Decisions about strategical topics
   - Review and approval of contributions, e.g. Feature Requests, which add or modify features
   - Project Management
   - Planning and Approval of Releases
   - Escalation instance
- `PLC Members`_
    - `PLC election <https://www.eclipse.org/projects/handbook/#roles-pl>`_
- `PLC Speaker`_
- `PLC Meeting Minutes`_
- `PLC Slack channel`_
- `PLC Open Point List`_

.. _pmp_pm_tlc:

Technical Lead Circle (TLC)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Technical Lead Circle will soon be merged with the Project Lead Circle: `#2381: Merge TLC into PLC <https://github.com/eclipse-score/score/issues/2381>`_

.. _TLC Members: https://github.com/orgs/eclipse-score/teams/automotive-score-TLC-team
.. _TLC Speaker: https://github.com/orgs/eclipse-score/teams/automotive-score-TLC-lead
.. _TLC Meeting Minutes: https://github.com/eclipse-score/score/wiki/TLCM
.. _TLC Slack Channel: https://sdvworkinggroup.slack.com/archives/C085F44D2CS
.. _TLC Open Point List: https://github.com/orgs/eclipse-score/projects/3

- TLC Responsibilities:
   - Review and approval of contributions, e.g. *Feature Requests*, which add or modify S-CORE platform features.
   - Project management of the platform development, e.g., creation of the roadmap.
   - High-level project control and coordination between multiple software modules.
   - Escalation instance for software module project leads and committers.
- `TLC Members`_
   - TLC Election: Each *Project Lead* is allowed to nominate one *Technical Lead*.
- `TLC Meeting Minutes`_
- `TLC Slack Channel`_
- `TLC Open Point List`_
- TLC Repositories:
   - https://github.com/eclipse-score/score

.. _pmp_pm_communities:

Communities
-----------
*Communities* are installed to work on cross functional topics, such as program level architectural decisions,
commonly used development & testing infrastructure, processes or final integration & release.
Each *Community* has a *Community Lead* to organize the community`s work.

The following *Communities* are established:

.. _pmp_pm_arc:

Architecture Community (ARC)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _ARC Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-ARC-team
.. _ARC Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-ARC-lead
.. _ARC Meeting Minutes: https://github.com/eclipse-score/score/wiki/ARCM
.. _ARC Slack Channel: https://sdvworkinggroup.slack.com/archives/C08C1HG5AKY
.. _ARC Open Point List: https://github.com/orgs/eclipse-score/projects/3

- ARC Responsibilities
   - clarification of software architecture topics, e.g. discussion of new features or coding guidelines
- `ARC Core Members`_
- `ARC Lead`_
- `ARC Meeting Minutes`_
- `ARC Slack Channel`_
- `ARC Open Point List`_
- ARC Repositories:
   - https://github.com/eclipse-score/score

Process Community (PRC)
^^^^^^^^^^^^^^^^^^^^^^^
.. _PRC Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-PRC-team
.. _PRC Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-PRC-lead
.. _PRC Meeting Minutes: https://github.com/eclipse-score/score/wiki/PRCM
.. _PRC Slack Channel: https://sdvworkinggroup.slack.com/archives/C0864L05332
.. _PRC Open Point List: https://github.com/orgs/eclipse-score/projects/21
.. _PIM Open Point List: https://github.com/orgs/eclipse-score/projects/7

- PRC Responsibilities
   - defining and maintaining the software development process (incl. safety, security and quality)
   - defining and maintaining the process implementation (PIM)
- `PRC Core Members`_
- `PRC Lead`_
- `PRC Meeting Minutes`_
- `PRC Slack Channel`_
- `PRC Open Point List`_
- `PIM Open Point List`_
- PRC Repositories:
   - https://github.com/eclipse-score/process_description
   - https://github.com/eclipse-score/score


Infrastructure Community (INF)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _INF Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-INF-team
.. _INF Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-INF-lead
.. _INF Meeting Minutes: https://github.com/eclipse-score/score/wiki/INFM
.. _INF Slack Channel: https://sdvworkinggroup.slack.com/archives/C0894QGRZDM
.. _INF Open Point List: https://github.com/orgs/eclipse-score/projects/6

- INF Responsibilities
   - providing and maintaining the development infrastructure: Compiler, IDE, build toolchains
- `INF Core Members`_
- `INF Lead`_
- `INF Meeting Minutes`_
- `INF Slack Channel`_
- `INF Open Point List`_
- INF Toolchain Repositories:
   - https://github.com/eclipse-score/bazel_platforms
   - https://github.com/eclipse-score/toolchains_gcc
   - https://github.com/eclipse-score/toolchains_gcc_packages
   - https://github.com/eclipse-score/toolchains_qnx
   - https://github.com/eclipse-score/toolchains_rust
- INF Tooling Repositories:
   - https://github.com/eclipse-score/devcontainer
   - https://github.com/eclipse-score/docs-as-code
   - https://github.com/eclipse-score/tooling
- INF other Repositories:
   - https://github.com/eclipse-score/apt-install
   - https://github.com/eclipse-score/cicd-workflows
   - https://github.com/eclipse-score/bazel_registry
   - https://github.com/eclipse-score/bazel_registry_ui
   - https://github.com/eclipse-score/.eclipsefdn
   - https://github.com/eclipse-score/examples

Testing Community (TST)
^^^^^^^^^^^^^^^^^^^^^^^
.. _TST Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-TST-team
.. _TST Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-TST-lead
.. _TST Meeting Minutes: https://github.com/eclipse-score/score/wiki/TSTM
.. _TST Slack Channel: https://sdvworkinggroup.slack.com/archives/TSTC08B6C78EF3
.. _TST Open Point List: https://github.com/orgs/eclipse-score/projects/5


- TST Responsibilities
   - defining and maintaining testing strategy and infrastructure
- `TST Core Members`_
- `TST Lead`_
- `TST Meeting Minutes`_
- `TST Slack Channel`_
- `TST Open Point List`_
- TST Repositories:
   - https://github.com/eclipse-score/itf
   - https://github.com/eclipse-score/testing_tools


Integration and Release Community (INT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _INT Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-INT-team
.. _INT Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-INT-lead
.. _INT Meeting Minutes: https://github.com/eclipse-score/score/wiki/INTM
.. _INT Slack Channel: https://sdvworkinggroup.slack.com/archives/INT
.. _INT Open Point List: https://github.com/orgs/eclipse-score/projects/INT


- INT Responsibilities
   - integration of available modules to one or several reference integrations
   - releasing
- `INT Core Members`_
- `INT Lead`_
- `INT Meeting Minutes`_
- `INT Slack Channel`_
- `INT Open Point List`_
- INT Repositories:
   - https://github.com/eclipse-score/score

Marketing & Communication Community
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _MCM Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-MCM-team
.. _MCM Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-MCM-lead
.. _MCM Meeting Minutes: https://github.com/eclipse-score/score/wiki/MCMM
.. _MCM Slack Channel: https://sdvworkinggroup.slack.com/archives/C032X75QGTT
.. _MCM Open Point List: https://github.com/orgs/eclipse-score/projects/11

- MCM Responsibilities
   - coordination of public relations, e.g. the maintenance of the website & organization of general events
- `MCM Core Members`_
- `MCM Lead`_
- `MCM Meeting Minutes`_
- `MCM Slack Channel`_
- `MCM Open Point List`_
- MCM Repositories:
   - https://github.com/eclipse-score/eclipse-score.github.io
   - https://github.com/eclipse-score/eclipse-score-website
   - https://github.com/eclipse-score/eclipse-score-website-preview
   - https://github.com/eclipse-score/eclipse-score-website-published

Feature Teams
-------------
*Feature Teams* have end-to-end responsibility for providing specific functionalities. This includes all
development aspects beginning with the architecture definition to the integration test.
One *Team* may work independently of other *Teams* on the team-assigned *GitHub Issues*,
and needs at least one :need:`Committer <rl__committer>` who can approve & merge the Pull Requests
Each *Feature Team* has one *Lead* to organize the Team`s work.

The following *Feature Teams* are defined in the *S-CORE* project:

Baselibs Feature Team (BAS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _BAS Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-BAS-team
.. _BAS Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-BAS-lead
.. _BAS Meeting Minutes: https://github.com/eclipse-score/score/wiki/BASM
.. _BAS Slack Channel: https://sdvworkinggroup.slack.com/archives/C090UKSL5L2
.. _BAS Open Point List: https://github.com/orgs/eclipse-score/projects/24

- BAS Responsibilities
   - development of the base libraries
- `BAS Core Members`_
- `BAS Lead`_
- `BAS Meeting Minutes`_
- `BAS Slack Channel`_
- `BAS Open Point List`_
- BAS Repositories:
   - https://github.com/eclipse-score/baselibs
   - https://github.com/eclipse-score/baselibs_rust

.. _pmp_pm_com:

Communication Feature Team (COM)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _COM Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-COM-team
.. _COM Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-COM-lead
.. _COM Meeting Minutes: https://github.com/eclipse-score/score/wiki/COMM
.. _COM Slack Channel: https://sdvworkinggroup.slack.com/archives/C08C0JATADP
.. _COM Open Point List: https://github.com/orgs/eclipse-score/projects/19

- COM Responsibilities
   - development of the communication and protocols
- `COM Core Members`_
- `COM Lead`_
- `COM Meeting Minutes`_
- `COM Slack Channel`_
- `COM Open Point List`_
- COM Repositories:
   - https://github.com/eclipse-score/communication
   - https://github.com/eclipse-score/inc_mw_com
   - https://github.com/eclipse-score/inc_someip_gateway

.. _pmp_pm_cfg:

Configuration Management Feature Team (CFG)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _CFG Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-CFG-team
.. _CFG Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-CFG-lead
.. _CFG Meeting Minutes: https://github.com/eclipse-score/score/wiki/CFGM
.. _CFG Slack Channel: https://sdvworkinggroup.slack.com/archives/CFG
.. _CFG Open Point List: https://github.com/orgs/eclipse-score/projects/CFG

- CFG Responsibilities
   - development of configuration management
- `CFG Core Members`_
- `CFG Lead`_
- `CFG Meeting Minutes`_
- `CFG Slack Channel`_
- `CFG Open Point List`_
- CFG Repositories:
   - https://github.com/eclipse-score/config_management
   - https://github.com/eclipse-score/inc_config_management


Fixed Execution Order Team (FEO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _FEO Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-FEO-team
.. _FEO Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-FEO-lead
.. _FEO Meeting Minutes: https://github.com/eclipse-score/score/wiki/FEOM
.. _FEO Slack Channel: https://sdvworkinggroup.slack.com/archives/FEO
.. _FEO Open Point List: https://github.com/orgs/eclipse-score/projects/9

- FEO Responsibilities
   - development of fixed execution order
- `FEO Core Members`_
- `FEO Lead`_
- `FEO Meeting Minutes`_
- `FEO Slack Channel`_
- `FEO Open Point List`_
- FEO Repositories:
   - https://github.com/eclipse-score/feo
   - https://github.com/eclipse-score/inc_feo


Kyron Team (KYR)
^^^^^^^^^^^^^^^^
.. _KYR Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-KYR-team
.. _KYR Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-KYR-lead
.. _KYR Meeting Minutes: https://github.com/eclipse-score/score/wiki/KYRM
.. _KYR Slack Channel: https://sdvworkinggroup.slack.com/archives/KYR
.. _KYR Open Point List: https://github.com/orgs/eclipse-score/projects/38


- KYR Responsibilities
   - development of Kyron
- `KYR Core Members`_
- `KYR Lead`_
- `KYR Meeting Minutes`_
- `KYR Slack Channel`_
- `KYR Open Point List`_
- KYR Repositories:
   - https://github.com/eclipse-score/kyron


Logging Team (LOG)
^^^^^^^^^^^^^^^^^^
.. _LOG Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-LOG-team
.. _LOG Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-LOG-lead
.. _LOG Meeting Minutes: https://github.com/eclipse-score/score/wiki/LOGM
.. _LOG Slack Channel: https://sdvworkinggroup.slack.com/archives/C089XP2PGQZ
.. _LOG Open Point List: https://github.com/orgs/eclipse-score/projects/31

- LOG Responsibilities
   - development of Logging
- `LOG Core Members`_
- `LOG Lead`_
- `LOG Meeting Minutes`_
- `LOG Slack Channel`_
-  `LOG Open Point List`_
- LOG Repositories:
   - https://github.com/eclipse-score/logging
   - https://github.com/eclipse-score/inc_mw_log

Lifecycle Management and Health Monitoring Team (LCM)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _LCM Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-LCM-team
.. _LCM Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-LCM-lead
.. _LCM Meeting Minutes: https://github.com/eclipse-score/score/wiki/LCMM
.. _LCM Slack Channel: https://sdvworkinggroup.slack.com/archives/C094Z3BN1K4
.. _LCM Open Point List: https://github.com/orgs/eclipse-score/projects/33

- LCM Responsibilities
   - development of Lifecycle Management and Health Monitoring
- `LCM Core Members`_
- `LCM Lead`_
- `LCM Meeting Minutes`_
- `LCM Slack Channel`_
- `LCM Open Point List`_
- LCM Repositories:
   - https://github.com/eclipse-score/lifecycle

Orchstrator Team (ORC)
^^^^^^^^^^^^^^^^^^^^^^^
.. _ORC Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-ORC-team
.. _ORC Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-ORC-lead
.. _ORC Meeting Minutes: https://github.com/eclipse-score/score/wiki/ORCM
.. _ORC Slack Channel: https://sdvworkinggroup.slack.com/archives/C099W80FU2C
.. _ORC Open Point List: https://github.com/orgs/eclipse-score/projects/29

-  Responsibilities
   - development of Orchstrator
- `ORC Core Members`_
- `ORC Lead`_
- `ORC Meeting Minutes`_
- `ORC Slack Channel`_
- `ORC Open Point List`_
- ORC Repositories:
   - https://github.com/eclipse-score/orchestrator

.. _pmp_pm_per:

Persistency Team (PER)
^^^^^^^^^^^^^^^^^^^^^^
.. _PER Core Members: https://github.com/orgs/eclipse-score/teams/automotive-score-PER-team
.. _PER Lead: https://github.com/orgs/eclipse-score/teams/automotive-score-PER-lead
.. _PER Meeting Minutes: https://github.com/eclipse-score/score/wiki/PERM
.. _PER Slack Channel: https://sdvworkinggroup.slack.com/archives/C08B339ETQU
.. _PER Open Point List: https://github.com/orgs/eclipse-score/projects/20

-  Responsibilities
   - development of Persistency
- `PER Core Members`_
- `PER Lead`_
- `PER Meeting Minutes`_
- `PER Slack Channel`_
- `PER Open Point List`_
- PER Repositories:
   - https://github.com/eclipse-score/persistency


Organization Management
-----------------------
Decision to adapt the *Project Organization* is done in the *Technical Lead Circle* / *Project Management Circle*, documented in the meeting minutes and planned with a *Task*:

- creating of a new Team (*Community* or *Feature Team*)
- setting an existing Team (*Community* or *Feature Team*) on hold
- deleting an existing Team (*Community* or *Feature Team*)

Creation of a new Feature Team
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In case a new Feature Team creation is necessary, the following steps have to be done:

- `Adding a new Team to GitHub Teams <https://github.com/orgs/eclipse-score/teams>`_ and adding the Core Members by editing
  `orgs.newTeam <https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet>`_.
- Adding a new Repository to GitHub by editing
  `orgs.newRepo <https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet>`_.
- Definition of Repository specific :ref:`CODEOWNERS <pmp_pm_codeowners>`.
- `Creation of a Team GitHub Project <https://github.com/orgs/eclipse-score/projects>`_ with a Kanban View and a Task View.
- `Creation of a Team Meeting Wiki <https://github.com/eclipse-score/score/wiki>`_ for the meeting minutes

- Creation of a Team Label
    .. code::

       committee:<Name of Committee>,
       community:<Name of Community> or
       ft:<Name of Feature Team>

- Creation of a Slack Channel: https://sdvworkinggroup.slack.com
- Adapting the PMP

Internal Communication
======================

The project internal communication is ensured with help of:

- virtual and face-to-face meetings and their minutes
- *GitHub issues* and *GitHub pull requests*
- online communication using Slack

Meetings
--------
All meetings are scheduled in the `Eclipse S-CORE Calendar <https://calendar.google.com/calendar/u/0/embed?src=c_2ampi2bmoka3qter4dceap1d5g@group.calendar.google.com&ctz=Europe/Berlin>`_ , are open for everyone
but mentioned team members are mandatory. Meeting minutes are public and stored in the project specific *GitHub Team Wikis*.


.. _pmp_pm_repository_structure:

Repository structure
====================
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
----------
While creating a new repository, :ref:`Technical Leads <pmp_pm_tlc>` nominate initial `CODEOWNERS <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners#codeowners-and-branch-protection>`_,
whose review is mandatory for merging PRs to the repository and who are at the end allowed to merge PRs to the repository.

Possible members are software developers, who

- understand how the particular feature works or should work
- are the initial authors of the software

The Codeownership has to be regularly updated and changes have to be documented.




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

PMP Definition of Done
======================
- The **Definitions of Done** for all Platform Management Plans are fulfilled.
- Project Organization: Org Chart and description is available and up to date.
- Project Internal Communication: Team Overview with meeting structure is available and and Slack channels are established and maintained.
- Scheduling: Meetings are scheduled in the Eclipse SDV calendar.
- Milestones & Releases: Roadmap with Milestones and Releases are available and up to date.
- General: All Reviews are performed according to their definitions, the respective templates are used.

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

.. _pmp_pm_plan:

Project Management Plan
#######################

Purpose
=======
The purpose of the Project Management Plan is to define

- how to manage, analyse and control changes of the work products during the project life cycle.
- the project stakeholder and how to communicate with them.
- how and where to create and maintain the project schedule.
- how to track planned work.
- how and where to escalation.

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

<<<<<<< HEAD
.. _TLC Members: https://github.com/orgs/eclipse-score/teams/automotive-score-TLC-team
.. _TLC Speaker: https://github.com/orgs/eclipse-score/teams/automotive-score-TLC-lead
.. _TLC Meeting Minutes: https://github.com/eclipse-score/score/wiki/TLCM
.. _TLC Slack Channel: https://sdvworkinggroup.slack.com/archives/C085F44D2CS
.. _TLC Open Point List: https://github.com/orgs/eclipse-score/projects/3
=======
  *Project lead circle* proposes and elects a *Project lead circle Assistant* and their deputy with bare majority, who is responsible for scheduling and announcing meetings, preparing and announcing agenda, writing meeting minutes and protocols. *Project lead circle* can reelect *Project lead circle Assistant* at any time. The *Project lead circle Assistant* and their deputy can resign anytime on their own will.
>>>>>>> f9f5ae6 (Update language for gender neutrality in project management plan)

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

.. _pmp_pm_technical_committees:

Communities
-----------
*Communities* are installed to work on cross functional topics, such as program level architectural decisions,
commonly used development & testing infrastructure, processes or final integration & release.
Each *Community* has a *Community Lead* to organize the community`s work.

<<<<<<< HEAD
The following *Communities* are established:
=======
  *Technical lead circle* proposes and elects a *Technical lead circle Assistant* and their deputy with bare majority during *Technical Lead Circle meeting*, who is responsible for scheduling and announcing meetings, preparing and announcing agenda, writing meeting minutes and protocols. *Technical lead circle* can reelect *Technical lead circle Assistant* at any time. The *Technical lead circle Assistant* and their deputy can resign anytime on their own will.
>>>>>>> f9f5ae6 (Update language for gender neutrality in project management plan)

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

.. _pmp_pm_feature_teams:

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

Planning & Tracking
===================

Cadence
-------

Iteration
^^^^^^^^^
Each iteration is two weeks long.

Release Frequence
^^^^^^^^^^^^^^^^^
After every 3rd iteration, the work is baselined into a Release.


Planning & Tracking Infrastructure
----------------------------------
The planning and tracking of the work is done inside **GitHub**.
GitHub **Issues** are used to document all necessary work packages.

Issues
------
To organize the work :ref:`Github Types <pmp_pm_issue_types>`,  :ref:`GitHub Labels <pmp_pm_gh_labels>` and
:ref:`GitHub Projects <pmp_pm_gh_projects>` are used.
The Progress of the work is documented with help of the :ref:`Status of an Issue <pmp_pm_issue_status_flow>`.


.. _pmp_pm_issue_types:

Issues Types
^^^^^^^^^^^^

.. image:: _assets/issue_types.drawio.svg
   :width: 900
   :alt: Issue Types
   :align: center

.. _pmp_pm_feature_request:

Feature Request
"""""""""""""""
A *Feature Request* represents an independent work package used to describe and
track a high-level request for the project. *Feature Request* work packages can be linked to
other work packages, but they must not be treated as parent work packages. They are in the responsibility of the
:ref:`Architecture Community <pmp_pm_arc>` and are part of the :ref:`Root Repository <pmp_pm_root_repository>`.

.. _pmp_pm_product_increment:

Product Increment
"""""""""""""""""
A *Product Increment* represents the highest level in the work package hierarchy and
cannot be linked as a child of another issue. If you need to group multiple *Product Increment* work packages,
labels have to be used.
A *Product Increment* can have multiple *Epic* work packages as children. *Product Increments* areowned by
:ref:`Technical Lead Circle <pmp_pm_tlc>` and are part of the :ref:`Root Repository <pmp_pm_root_repository>`.


.. _pmp_pm_epic:

Epic
""""
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


.. _pmp_pm_task:

Task
""""

A *Task GitHub Issue* represents the smallest unit of planning and typically corresponds
to a concrete piece of work to be completed, such as by a developer. *Task* work packages are usually
grouped under an *Epic* work package.
In certain cases, a *Task* may exist as a standalone *GitHub Issue*.
However, standalone *Task* work packages must not be grouped using labels.
If multiple *Task* work packages are related, a *Epic* work package should be created instead,
with all associated *Task* work packages added as child work packages under that *Epic*. *Tasks* are owned by a Team and are part
of any Team`s repository.

.. _pmp_pm_bug:

Bug
"""

A *Bug GitHub Issue* is used to report any kind of problem or malfunction. It is considered
a special type of *Story* work package and follows the same rules as regular *Epic* work packages,
with the key difference that it focuses on fixing defects in existing functionality
rather than creating or extending functionality. *Tasks* are owned by a Team and are part
of any Team`s repository.

.. _pmp_pm_issue_status_flow:

Issue Status
^^^^^^^^^^^^
Each *GitHub issue* has a **Status** depending on the :ref:`GitHub Project <pmp_pm_gh_projects>`,
we use the following Standard Flow for all :ref:`Issue Types <pmp_pm_issue_types>`:

.. image:: _assets/issue_status_flow.drawio.svg
    :width: 300
    :alt: Issue Status
    :align: center

Issue Attributes
^^^^^^^^^^^^^^^^
- Standard Attributes
    - Assignees
    - :ref:`Labels <pmp_pm_gh_labels>`
    - :ref:`Type <pmp_pm_issue_types>`
- Common Project Attributes
    - :ref:`Status <pmp_pm_issue_status_flow>`
    - Priority (High, Middle, Low)
    - Size (S=hours,M=days,L=weeks, XL=months)
    - (planned finishing) Iteration
    - Team
    - Category (e.g. Work stream)
    - Release

Issue Templates
^^^^^^^^^^^^^^^
Templates defined in *GitHub* ensure the availability of the type relevant information for all issues.

- `Bug Template <https://github.com/eclipse-score/score/blob/main/.github/ISSUE_TEMPLATE/bug.yml>`_
- `Feature Request Template <https://github.com/eclipse-score/score/blob/main/.github/ISSUE_TEMPLATE/feature_request.yml>`_
- `Product Increment Template <https://github.com/eclipse-score/score/blob/main/.github/ISSUE_TEMPLATE/product_increment.yml>`_
- `Epic Template <https://github.com/eclipse-score/score/blob/main/.github/ISSUE_TEMPLATE/epic.yml>`_
- `Task Template <https://github.com/eclipse-score/score/blob/main/.github/ISSUE_TEMPLATE/task.yml>`_

Hierarchies
^^^^^^^^^^^
Hierarchies are realized as parent-child relations with the `GitHub Sub-Issue Feature <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues>`_.

Dependencies
^^^^^^^^^^^^
Dependencies are realized with blocked by or blocking relations described in thè `GitHub Issue Dependency Feature <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies>`_.

.. _pmp_pm_milestone:

Milestone
---------
A milestone is indicating an important dedicated point in the schedule like
a Release or a Quality (ASPICE, ASIL) Assessment.
`GitHub Milestones <https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones>`_ offer to connect *Issues* and *Pull Requests* to the `S-CORE-defined Milestones <https://github.com/eclipse-score/score/milestones>`_

.. _pmp_pm_release:

Releases
--------
*Releases* are special milestones and used for baselining of the development activities.


.. _pmp_pm_gh_labels:


Labels
------
`GitHub Labels <https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels>`_ are used to organize Issues, Pull Requests etc. having same context. Although
Labels are powerful, the definition of new Labels shall be wisely done and organization wide used.
Therefore their management is limited to Organization owners.

The following `Labels <https://github.com/eclipse-score/score/labels>`_ are defined.

.. _pmp_pm_gh_projects:

GitHub Projects
---------------
The `GitHub Project Feature <https://docs.github.com/en/issues/planning-and-tracking-with-projects>`_
helps to plan the work and monitor its progress.

Multiple *GitHub Projects* are defined at https://github.com/orgs/eclipse-score/projects/.

Beside one for each (committee, community, feature) Team, there is one for `Feature Requests <https://github.com/orgs/eclipse-score/projects/4>`_
and one for the complete `S-CORE Roadmap <https://github.com/orgs/eclipse-score/projects/17>`_. Inside a GitHub Project, there is the possibility to generate different views
for Table, Board and Roadmap supporting Backlogs, Open Point or Task Lists and other useful perspectives.

.. image:: _assets/planning_overview.drawio.svg
    :width: 900
    :alt: Planning Overview
    :align: center



Kanban View
^^^^^^^^^^^
The `GitHub Board <https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-board-layout>`_ is supporting the Kanban View, enabling to set the Work In Progress Limits.

.. image:: _assets/kanban.drawio.svg
    :width: 900
    :alt: Kanban View
    :align: center


Task List View
^^^^^^^^^^^^^^
The `GitHub Table <https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-table-layout>`_ is supporting the List View, enabling to adapt the priority by reordering the rows.

Roadmap View
^^^^^^^^^^^^
The `GitHub Roadmap <https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout>`_ is supporting the Road View, provididing a high-level visualization of your project across a configurable timespan.

Traceability
------------
To achieve traceability all *Pull Requests* have to be `linked <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue>`_
to the corresponding *GitHub Issues*.

Planning of Work
----------------

Generally, every team is responsible for planning its work within its own plan with the help of its :ref:`GitHub Project <pmp_pm_gh_projects>` filled with :ref:`Epics <pmp_pm_epic>`, :ref:`Tasks <pmp_pm_task>` and :ref:`Bugs <pmp_pm_bug>`.

The planning of :ref:`Feature Requests <pmp_pm_feature_request>` is in the responsibility of the :ref:`Architects <pmp_pm_arc>`,
whereas the overall top-down plan is in the responsibility of the :ref:`Technical Lead Circle <pmp_pm_tlc>` with the help of :ref:`Product Increments <pmp_pm_product_increment>`,
:ref:`Milestones <pmp_pm_milestone>` and :ref:`Releases <pmp_pm_release>`.

Tracking Progress
-----------------
The :ref:`Technical Lead Circle <pmp_pm_tlc>` regularly monitors the status of the work for upcoming Milestones and Releases in https://github.com/orgs/eclipse-score/projects/17 based on
:ref:`Product Increments <pmp_pm_product_increment>`.


Dashboards
^^^^^^^^^^

GitHub offers mechanism in form of charts to track issues:

- `Product Increments Open last 3 months <https://github.com/orgs/eclipse-score/projects/17/insights/4>`_

PMP Definition of Done
======================
- The **Definitions of Done** for all Platform Management Plans are fulfilled.
- Project Organization: Org Chart and description is available and up to date.
- Project Internal Communication: Team Overview with meeting structure is available & Slack channels are established and maintained.
- Scheduling: Meetings are scheduled in the Eclipse SDV calendar.
- Milestones & Releases: Roadmap with Milestones and Releases are available and up to date.
- General: All Reviews are performed according to their definitions, the respective templates are used.

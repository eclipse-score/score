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
-----------------------

Purpose
+++++++
The purpose of the Project Management Plan is to define

- how to manage, analyse and control changes of the work products during the project life cycle.
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
    - S-CORE Handbook (:need:`doc__platform_handbook`) is available and up to date.
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
Steering of the project is done with the help of *Committees*.

.. _PLCMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-PLC-team
.. _PLCSPK: https://github.com/orgs/eclipse-score/teams/automotive-score-PLC-lead
.. _PLCMM: https://github.com/eclipse-score/score/wiki/PLCM
.. _PLCSLC: https://sdvworkinggroup.slack.com/archives/PLC
.. _PLCBKL: https://github.com/orgs/eclipse-score/projects/PLC

.. _TLCMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-TLC-team
.. _TLCSPK: https://github.com/orgs/eclipse-score/teams/automotive-score-TLC-lead
.. _TLCMM: https://github.com/eclipse-score/score/wiki/TLCM
.. _TLCSLC: https://sdvworkinggroup.slack.com/archives/C085F44D2CS
.. _TLCBKL: https://github.com/orgs/eclipse-score/projects/3

.. list-table:: Steering
   :header-rows: 1
   :widths: 22,7,7,7,7,7,24

   * - Purpose
     - Members
     - Speaker
     - Meeting Minutes
     - Slack Channel
     - Backlog
     - Owned Repository
   * - .. _pmp_pm_plc:

       **PLC**
     - **Project**
     - **Lead**
     - **Circle**
     - **-----------**
     - **-----------**
     - **-----------------------**

   * - - Decisions about strategical topics
       - Review and approval of contributions, e.g. Feature Requests, which add or modify features
       - Project Management
       - Planning and Approval of Releases
       - Escalation instance
     - `PLCMBRS`_
     - `PLCSPK`_
     - `PLCMM`_
     - `PLCSLC`_
     - `PLCBKL`_
     - n.a.
   * - .. _pmp_pm_tlc:

       **TLC**
     - **Technical**
     - **Lead**
     - **Circle**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - - Review and approval of contributions, e.g. Feature Requests, which add or modify S-CORE platform features.
       -  Project management of the platform development, e.g. creation of the roadmap.
       - High-level project control and coordination between multiple software modules.
       - Escalation instance for software module project leads and committers.
     - `TLCMBRS`_
     - `TLCSPK`_
     - `TLCMM`_
     - `TLCSLC`_
     - `TLCBKL`_
     - - https://github.com/eclipse-score/score

.. _pmp_pm_communities:

Communities
^^^^^^^^^^^
*Communities* are installed to work on cross functional topics, such as program level architectural decisions,
commonly used development & testing infrastructure, processes or final integration & release.
Each *Community* has a *Community Lead* to organize the community`s work.

.. _ARCMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-ARC-team
.. _ARCLD: https://github.com/orgs/eclipse-score/teams/automotive-score-ARC-lead
.. _ARCMM: https://github.com/eclipse-score/score/wiki/ARCM
.. _ARCSLC: https://sdvworkinggroup.slack.com/archives/C08C1HG5AKY
.. _ARCBKL: https://github.com/orgs/eclipse-score/projects/3

.. _INFMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-INF-team
.. _INFLD: https://github.com/orgs/eclipse-score/teams/automotive-score-INF-lead
.. _INFMM: https://github.com/eclipse-score/score/wiki/INFM
.. _INFSLC: https://sdvworkinggroup.slack.com/archives/C0894QGRZDM
.. _INFBKL: https://github.com/orgs/eclipse-score/projects/6

.. _PRCMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-PRC-team
.. _PRCLD: https://github.com/orgs/eclipse-score/teams/automotive-score-PRC-lead
.. _PRCMM: https://github.com/eclipse-score/score/wiki/PRCM
.. _PRCSLC: https://sdvworkinggroup.slack.com/archives/C0864L05332
.. _PRCBKL: https://github.com/orgs/eclipse-score/projects/21
.. _PIMBKL: https://github.com/orgs/eclipse-score/projects/7

.. _TSTMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-TST-team
.. _TSTLD: https://github.com/orgs/eclipse-score/teams/automotive-score-TST-lead
.. _TSTMM: https://github.com/eclipse-score/score/wiki/TSTM
.. _TSTSLC: https://sdvworkinggroup.slack.com/archives/TSTC08B6C78EF3
.. _TSTBKL: https://github.com/orgs/eclipse-score/projects/5

.. _INTMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-INT-team
.. _INTLD: https://github.com/orgs/eclipse-score/teams/automotive-score-INT-lead
.. _INTMM: https://github.com/eclipse-score/score/wiki/INTM
.. _INTSLC: https://sdvworkinggroup.slack.com/archives/INT
.. _INTBKL: https://github.com/orgs/eclipse-score/projects/INT

.. _MCMMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-MCM-team
.. _MCMLD: https://github.com/orgs/eclipse-score/teams/automotive-score-MCM-lead
.. _MCMMM: https://github.com/eclipse-score/score/wiki/MCMM
.. _MCMSLC: https://sdvworkinggroup.slack.com/archives/C032X75QGTT
.. _MCMBKL: https://github.com/orgs/eclipse-score/projects/11


.. list-table:: Community
   :header-rows: 1
   :widths: 22,7,7,7,7,7,24

   * - Purpose
     - Members
     - Lead
     - Meeting Minutes
     - Slack Channel
     - Backlog
     - Owned Repository
   * - .. _pmp_pm_arc:

       **ARC**
     - **Architecture**
     - **Community**
     - **-----------**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - - clarification of software architecture topics, e.g. discussion of new features or coding guidelines
     - `ARCMBRS`_
     - `ARCLD`_
     - `ARCMM`_
     - `ARCSLC`_
     - `ARCBKL`_
     - https://github.com/eclipse-score/score
   * - .. _pmp_pm_prc:

       **PRC**
     - **Process**
     - **Community**
     - **-----------**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - - defining and maintaining the software development process (incl. safety, security and quality)
       - defining and maintaining the process implementation (PIM)
     - `PRCMBRS`_
     - `PRCLD`_
     - `PRCMM`_
     - `PRCSLC`_
     - `PRCBKL`_
       `PIMBKL`_
     - | https://github.com/eclipse-score/process_description
       | https://github.com/eclipse-score/score
   * - .. _pmp_pm_inf:

       **INF**
     - **Infrastructure**
     - **Community**
     - **-----------**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - - providing and maintaining the development infrastructure: Compiler, IDE, build toolchains
     - `INFMBRS`_
     - `INFLD`_
     - `INFMM`_
     - `INFSLC`_
     - `INFBKL`_
     - | Toolchain Repositories:

          | https://github.com/eclipse-score/bazel_platforms
          | https://github.com/eclipse-score/toolchains_gcc
          | https://github.com/eclipse-score/toolchains_gcc_packages
          | https://github.com/eclipse-score/toolchains_qnx
          | https://github.com/eclipse-score/toolchains_rust

       | Tooling Repositories:

          | https://github.com/eclipse-score/devcontainer
          | https://github.com/eclipse-score/docs-as-code
          | https://github.com/eclipse-score/tooling

       | other Repositories:

          | https://github.com/eclipse-score/apt-install
          | https://github.com/eclipse-score/cicd-workflows
          | https://github.com/eclipse-score/bazel_registry
          | https://github.com/eclipse-score/bazel_registry_ui
          | https://github.com/eclipse-score/.eclipsefdn
          | https://github.com/eclipse-score/examples

   * - .. _pmp_pm_tst:

       **TST**
     - **Testing**
     - **Community**
     - **-----------**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - defining and maintaining testing strategy and infrastructure
     - `TSTMBRS`_
     - `TSTLD`_
     - `TSTMM`_
     - `TSTSLC`_
     - `TSTBKL`_
     - | https://github.com/eclipse-score/itf
       | https://github.com/eclipse-score/testing_tools
   * - .. _pmp_pm_int:

       **INT**
     - **Integration &**
     - **Release**
     - **Community**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - - integration of available modules to one or several reference integrations
       - releasing

     - `INTMBRS`_
     - `INTLD`_
     - `INTMM`_
     - `INTSLC`_
     - `INTBKL`_
     - | https://github.com/eclipse-score/score
   * - .. _pmp_pm_mcm:

       **MCM**
     - **Integration &**
     - **Release**
     - **Community**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - - coordination of public relations, e.g. the maintenance of the website & organization of general events
     - `MCMMBRS`_
     - `MCMLD`_
     - `MCMMM`_
     - `MCMSLC`_
     - `MCMBKL`_
     - | https://github.com/eclipse-score/eclipse-score.github.io
       | https://github.com/eclipse-score/eclipse-score-website
       | https://github.com/eclipse-score/eclipse-score-website-preview
       | https://github.com/eclipse-score/eclipse-score-website-published

.. _pmp_pm_feature_teams:

Feature Teams
^^^^^^^^^^^^^
*Feature Teams*  have end-to-end responsibility for providing specific functionalities. This includes all
development aspects beginning with the architecture definition to the integration test.
One *Team* may work independently of other *Teams* on the team-assigned *GitHub Issues*,
and needs at least one :need:`Committer <rl__committer>` who can approve & merge the Pull Requests
Each *Feature Team* has one *Lead* to organize the Team`s work.

.. _BASMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-BAS-team
.. _BASLD: https://github.com/orgs/eclipse-score/teams/automotive-score-BAS-lead
.. _BASMM: https://github.com/eclipse-score/score/wiki/BASM
.. _BASSLC: https://sdvworkinggroup.slack.com/archives/C090UKSL5L2
.. _BASBKL: https://github.com/orgs/eclipse-score/projects/24

.. _COMMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-COM-team
.. _COMLD: https://github.com/orgs/eclipse-score/teams/automotive-score-COM-lead
.. _COMMM: https://github.com/eclipse-score/score/wiki/COMM
.. _COMSLC: https://sdvworkinggroup.slack.com/archives/C08C0JATADP
.. _COMBKL: https://github.com/orgs/eclipse-score/projects/19

.. _CFGMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-CFG-team
.. _CFGLD: https://github.com/orgs/eclipse-score/teams/automotive-score-CFG-lead
.. _CFGMM: https://github.com/eclipse-score/score/wiki/CFGM
.. _CFGSLC: https://sdvworkinggroup.slack.com/archives/CFG
.. _CFGBKL: https://github.com/orgs/eclipse-score/projects/CFG

.. _FEOMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-FEO-team
.. _FEOLD: https://github.com/orgs/eclipse-score/teams/automotive-score-FEO-lead
.. _FEOMM: https://github.com/eclipse-score/score/wiki/FEOM
.. _FEOSLC: https://sdvworkinggroup.slack.com/archives/FEO
.. _FEOBKL: https://github.com/orgs/eclipse-score/projects/9

.. _KYRMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-KYR-team
.. _KYRLD: https://github.com/orgs/eclipse-score/teams/automotive-score-KYR-lead
.. _KYRMM: https://github.com/eclipse-score/score/wiki/KYRM
.. _KYRSLC: https://sdvworkinggroup.slack.com/archives/KYR
.. _KYRBKL: https://github.com/orgs/eclipse-score/projects/38

.. _LCMMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-LCM-team
.. _LCMLD: https://github.com/orgs/eclipse-score/teams/automotive-score-LCM-lead
.. _LCMMM: https://github.com/eclipse-score/score/wiki/LCMM
.. _LCMSLC: https://sdvworkinggroup.slack.com/archives/C094Z3BN1K4
.. _LCMBKL: https://github.com/orgs/eclipse-score/projects/33

.. _LOGMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-LOG-team
.. _LOGLD: https://github.com/orgs/eclipse-score/teams/automotive-score-LOG-lead
.. _LOGMM: https://github.com/eclipse-score/score/wiki/LOGM
.. _LOGSLC: https://sdvworkinggroup.slack.com/archives/C089XP2PGQZ
.. _LOGBKL: https://github.com/orgs/eclipse-score/projects/31

.. _ORCMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-ORC-team
.. _ORCLD: https://github.com/orgs/eclipse-score/teams/automotive-score-ORC-lead
.. _ORCMM: https://github.com/eclipse-score/score/wiki/ORCM
.. _ORCSLC: https://sdvworkinggroup.slack.com/archives/C099W80FU2C
.. _ORCBKL: https://github.com/orgs/eclipse-score/projects/29

.. _PERMBRS: https://github.com/orgs/eclipse-score/teams/automotive-score-PER-team
.. _PERLD: https://github.com/orgs/eclipse-score/teams/automotive-score-PER-lead
.. _PERMM: https://github.com/eclipse-score/score/wiki/PERM
.. _PERSLC: https://sdvworkinggroup.slack.com/archives/C08B339ETQU
.. _PERBKL: https://github.com/orgs/eclipse-score/projects/20

.. list-table:: Feature Teams
   :header-rows: 1
   :widths: 22,7,7,7,7,7,24

   * - Purpose
     - Members
     - Lead
     - Meeting Minutes
     - Slack Channel
     - Backlog
     - Owned Repository
   * - .. _pmp_pm_bas:

       **BAS**
     - **Baselibs**
     - **Feature**
     - **Team**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - - development of the base libraries
     - `BASMBRS`_
     - `BASLD`_
     - `BASMM`_
     - `BASSLC`_
     - `BASBKL`_
     - | https://github.com/eclipse-score/baselibs
       | https://github.com/eclipse-score/baselibs_rust
   * - .. _pmp_pm_com:

       **COM**
     - **Communication**
     - **Feature**
     - **Team**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - - development of the communication and protocols
     - `COMMBRS`_
     - `COMLD`_
     - `COMMM`_
     - `COMSLC`_
     - `COMBKL`_
     - | https://github.com/eclipse-score/communication
       | https://github.com/eclipse-score/inc_mw_com
       | https://github.com/eclipse-score/inc_someip_gateway
   * - .. _pmp_pm_cfg:

       **CFG**
     - **Configuration**
     - **Management**
     - **Feature**
     - **Team**
     - **-----------**
     - **-----------------------**
   * - - development of configuration management
     - `CFGMBRS`_
     - `CFGLD`_
     - `CFGMM`_
     - `CFGSLC`_
     - `CFGBKL`_
     - | https://github.com/eclipse-score/config_management
       | https://github.com/eclipse-score/inc_config_management
   * - .. _pmp_pm_feo:

       **FEO**
     - **Fixed**
     - **Execution**
     - **Order**
     - **Feature**
     - **Team**
     - **-----------------------**
   * - - development of fixed execution order
     - `FEOMBRS`_
     - `FEOLD`_
     - `FEOMM`_
     - `FEOSLC`_
     - `FEOBKL`_
     - | https://github.com/eclipse-score/feo
       | https://github.com/eclipse-score/inc_feo
   * - .. _pmp_pm_kyr:

       **KYR**
     - **Kyron**
     - **Feature**
     - **Team**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - - development of Kyron
     - `KYRMBRS`_
     - `KYRLD`_
     - `KYRMM`_
     - `KYRSLC`_
     - `KYRBKL`_
     - | https://github.com/eclipse-score/kyron
   * - .. _pmp_pm_log:

       **LOG**
     - **Logging**
     - **Feature**
     - **Team**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - - development of Logging
     - `LOGMBRS`_
     - `LOGLD`_
     - `LOGMM`_
     - `LOGSLC`_
     - `LOGBKL`_
     - | https://github.com/eclipse-score/logging
       | https://github.com/eclipse-score/inc_mw_log

   * - .. _pmp_pm_lcm:

       **LCM**
     - **Lifecycle**
     - **Management &**
     - **Health Monitoring**
     - **Feature**
     - **Team**
     - **-----------------------**
   * - - development of Lifecycle Management and Health Monitoring
     - `LCMMBRS`_
     - `LCMLD`_
     - `LCMMM`_
     - `LCMSLC`_
     - `LCMBKL`_
     - | https://github.com/eclipse-score/lifecycle

   * - .. _pmp_pm_ocr:

       **OCR**
     - **Orchestrator**
     - **Feature**
     - **Team**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - - development of Orchestrator
     - `ORCMBRS`_
     - `ORCLD`_
     - `ORCMM`_
     - `ORCSLC`_
     - `ORCBKL`_
     - | https://github.com/eclipse-score/orchestrator

   * - .. _pmp_pm_per:

       **PER**
     - **Persistency**
     - **Feature**
     - **Team**
     - **-----------**
     - **-----------**
     - **-----------------------**
   * - - development of Persistency
     - `PERMBRS`_
     - `PERLD`_
     - `PERMM`_
     - `PERSLC`_
     - `PERBKL`_
     - | https://github.com/eclipse-score/persistency

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
- `Creation of a Team Meeting Wiki <https://github.com/eclipse-score/score/wiki>`_ for the meeting minutes
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
While creating a new repository, :ref:`Technical Leads <pmp_pm_tlc>` nominate initial `CODEOWNERS <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners#codeowners-and-branch-protection>`_,
whose review is mandatory for merging PRs to the repository and who are at the end allowed to merge PRs to the repository.

Possible members are software developers, who

- understand how the particular feature works or should work
- are the initial authors of the software

The Codeownership has to be regularly updated and changes have to be documented.

Planning & Tracking
+++++++++++++++++++

Cadence
^^^^^^^

Iteration
"""""""""
The Project calendar is devided into iterations. Each iteration is two weeks long.

Release Frequence
"""""""""""""""""
After every 3rd iteration, the work is baselined into a Release.


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

.. _pmp_pm_feature_request:

**Feature Request**

A *Feature Request* represents an independent work package used to describe and
track a high-level request for the project. *Feature Request* work packages can be linked to
other work packages, but they must not be treated as parent work packages. They are in the responsibility of the
:ref:`Architecture Community <pmp_pm_arc>` and are part of the :ref:`Root Repository <pmp_pm_root_repository>`.

.. _pmp_pm_product_increment:

**Product Increment**

A *Product Increment* represents the highest level in the work package hierarchy and
cannot be linked as a child of another issue. If you need to group multiple *Product Increment* work packages,
labels have to be used.
A *Product Increment* can have multiple *Epic* work packages as children. *Product Increments* areowned by
:ref:`Technical Lead Circle <pmp_pm_tlc>` and are part of the :ref:`Root Repository <pmp_pm_root_repository>`.

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

.. _pmp_pm_bug:

**Bug**

A *Bug GitHub Issue* is used to report any kind of problem or malfunction. It is considered
a special type of *Story* work package and follows the same rules as regular *Epic* work packages,
with the key difference that it focuses on fixing defects in existing functionality
rather than creating or extending functionality. *Tasks* are owned by a Team and are part
of any Team`s repository.

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
    - Priority (High, Middle, Low)
    - Size (S=hours,M=days,L=weeks, XL=months)
    - (planned finishing) Iteration
    - Team
    - Category (e.g. Work stream)
    - Release

Issue Templates
"""""""""""""""
Templates defined in *GitHub* ensure the availability of the type relevant information for all issues.

- `Bug Template <https://github.com/eclipse-score/score/blob/main/.github/ISSUE_TEMPLATE/bug.yml>`_
- `Feature Request Template <https://github.com/eclipse-score/score/blob/main/.github/ISSUE_TEMPLATE/feature_request.yml>`_
- `Product Increment Template <https://github.com/eclipse-score/score/blob/main/.github/ISSUE_TEMPLATE/product_increment.yml>`_
- `Epic Template <https://github.com/eclipse-score/score/blob/main/.github/ISSUE_TEMPLATE/epic.yml>`_
- `Task Template <https://github.com/eclipse-score/score/blob/main/.github/ISSUE_TEMPLATE/task.yml>`_

Hierarchies
"""""""""""
Hierarchies are realized as parent-child relations with the `GitHub Sub-Issue Feature <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues>`_.

Dependencies
""""""""""""
Dependencies are realized with blocked by or blocking relations described in thè `GitHub Issue Dependency Feature <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies>`_.

.. _pmp_pm_milestone:

Milestone
^^^^^^^^^
A milestone is indicating an important dedicated point in the schedule like
a Release or a Quality (ASPICE, ASIL) Assessment.
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

Beside one for each (committee, community, feature) Team, there is one for `Feature Requests <https://github.com/orgs/eclipse-score/projects/4>`_
and one for the complete `S-CORE Roadmap <https://github.com/orgs/eclipse-score/projects/17>`_. Inside a GitHub Project, there is the possibility to generate different views
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

The planning of :ref:`Feature Requests <pmp_pm_feature_request>` is in the responsibility of the :ref:`Architects <pmp_pm_arc>`,
whereas the overall top-down plan is in the responsibility of the :ref:`Technical Lead Circle <pmp_pm_tlc>` with the help of :ref:`Product Increments <pmp_pm_product_increment>`,
:ref:`Milestones <pmp_pm_milestone>` and :ref:`Releases <pmp_pm_release>`.

Tracking Progress
^^^^^^^^^^^^^^^^^
The :ref:`Technical Lead Circle <pmp_pm_tlc>` regularly monitors the status of the work for upcoming Milestones and Releases in https://github.com/orgs/eclipse-score/projects/17/ based on
:ref:`Product Increments <pmp_pm_product_increment>`.


Dashboards
""""""""""

GitHub offers mechanism in form of charts to track issues:

- `Product Increments Open last 3 months <https://github.com/orgs/eclipse-score/projects/17/insights/4>`_

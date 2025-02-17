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

.. _safety_management:

.. document:: Platform Safety Plan
   :id: DOC__PLATFORM-SAFETY-PLAN
   :status: draft
   :safety: ASIL-B
   :tags: platform_management
   :compliance-gd: GD_Plt_Mgt_Plan_Template

Safety management / Platform Safety Plan
----------------------------------------

This document implements :need:`WP_PLATFORM_SAFETY_PLAN`.

Purpose
+++++++

The main purpose of the safety plan is to:

* adhere to ISO 26262 where applicable for the project according to the defined tailoring

And:

* to define and assign the roles and responsibilities regarding safety activities
* to define the tailored safety activities, to provide the corresponding rationales for tailoring and to review the provided rationales
* to plan the safety activities
* to coordinate and track the progress of safety activities in accordance with the safety plan
* to ensure a correct progression of the safety activities throughout the safety lifecycle
* to plan to create a comprehensible safety case in order to provide the argument for the achievement of functional safety
* to judge whether the SW achieves functional safety (i.e. the functional safety assessment, audit, confirmation reviews)

Objectives and scope
++++++++++++++++++++

Functional Safety Management Goals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Adherence to the ISO 26262 according to the defined tailoring

in detail

* to plan all Functional Safety related activities and work products
* to monitor and facilitate all activities
* to measure and report Functional Safety Status based on well-defined metrics

Functional Safety Management Scope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is no deviation from the scope defined in the :doc:`../overview/index`.
The platform and its components are developed, and integrated for an assumed technical system as Safety Element out of Context (SEooC).
The development of the platform and its components follows the defined processes.
Responsibilites for development, implementation, integration and verification are also defined int the processes.

Regarding the platform specifics:

* the highest ASIL in the project is ASIL B
* all safety activities from a procedural point of view are developed according to ASIL B
* all safety related SW in the project is developed according to Iso 26262 ASIL B

This is valid for all development to provide FFI (freedom from interference).
The SW platform functionality consists of features, which are based on a set of requirements and are developed in parallel.
These features are developed into SW components contained in "modules", which are another set of SEooCs (initiated by a contribution request). A template exists to guide this: :need:`GD_Saf_Plan_Template`. See also :doc:`/process/process_model/guidance/architecture/index` meta-model.

Tailoring
^^^^^^^^^
Tailoring of safety activities:

* The tailoring is divided into project wide and module specific rules.
* Project wide tailoring is documented in this document - this is based on developement of a platform SEooC.
* Module SEooC specific tailoring is documented in the module development Safety Plans - this may be based on SEooC specifics or because component qualification according to ISO 26262 part 8 clause 12 (or ISO PAS 8926) is selected.
* In case of a change request on an existing feature (i.e. a contribution request), the subsequent safety planning will be done based on an impact analysis.

The following ISO26262 defined safety work products are not relevant for the SCORE SW platform development:

Because these are in responsibility of the system integrator: :need:`STD_WP_ISO26262__management_11`,
:need:`STD_WP_ISO26262__system_2`, :need:`STD_WP_ISO26262__system_3`, :need:`STD_WP_ISO26262__system_4`,
:need:`STD_WP_ISO26262__system_5`, :need:`STD_WP_ISO26262__system_6`, :need:`STD_WP_ISO26262__system_7`,
:need:`STD_WP_ISO26262__system_8`, :need:`STD_WP_ISO26262__system_9`, :need:`STD_WP_ISO26262__system_10`,
:need:`STD_WP_ISO26262__system_11`

Because there is no calibration used for the SCORE SW platform components, only configuration: :need:`STD_WP_ISO26262__software_19`,
:need:`STD_WP_ISO26262__software_21`, :need:`STD_WP_ISO26262__software_24`

Because distributed development is not how the project is organized. All contributors are seen as part of the project team.
When used, OSS components are qualified and external SEooCs are integrated in the project scope: :need:`STD_WP_ISO26262__support_1`,
:need:`STD_WP_ISO26262__support_2`, :need:`STD_WP_ISO26262__support_3`, :need:`STD_WP_ISO26262__support_4`, :need:`STD_WP_ISO26262__support_5`

Because in the SCORE SW platform HW elements are out of scope: :need:`STD_WP_ISO26262__support_21`, :need:`STD_WP_ISO26262__support_22`, :need:`STD_WP_ISO26262__support_23`

Because in the SCORE SW platform a proven in use argument will not be applied: :need:`STD_WP_ISO26262__support_24`, :need:`STD_WP_ISO26262__support_25`

Because in the SCORE SW platform interfacing of out of scope of ISO 26262 applications is not planned: :need:`STD_WP_ISO26262__support_26`

Because in the SCORE SW platform integration of safety-related systems not developed according to ISO 26262 is not planned: :need:`STD_WP_ISO26262__support_27`

Because in the SCORE SW platform no ASIL decomposition is planned: :need:`STD_WP_ISO26262__analysis_1`, :need:`STD_WP_ISO26262__analysis_2`

Approach
++++++++

Functional Safety Management Organization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is the project strategy to qualify the platform or components of the platform to the appropriate international standards and directives.
Therefore the project approach to facilitate a common culture regarding safety and security is part of our documentation.
The project will be under the Eclipse Foundation and so the `Eclipse Foundation Project Handbook: <https://www.eclipse.org/projects/handbook/>`_ applies.

*Eclipse Roles*


* `Contributors <https://www.eclipse.org/projects/handbook/#contributing-contributors>`_ can be everyone and we will not discourage the open source community from this. As the contributor cannot merge code (or any other work product) into the project's codebase, the safety development competence of the contributor is irrelevant.
* `Committers <https://www.eclipse.org/projects/handbook/#contributing-committers>`_ play the main development role in the project, as only these are allowed to merge, so they are the ultimate responsibles for the project's repository content.
* The Eclipse `Project Lead(s) <https://www.eclipse.org/projects/handbook/#roles-pl>`_ has the ISO 26262 project manager role.

*Project Roles*
Roles are defined in every process and in a generic roles section. All those are matched to Eclipse roles.
Project role assignment is done in every feature development Safety Plan.

*Critical dependencies*

The project has not implemented a quality management system yet.
But it aims to be conform to ASPICE, as defined in the management system.
Continuous improvement is part to all processes. Improvements are handled in the scope of Quality Management.

*Risk*

Organization and management system has not a mature level yet.

*Skills*

The main safety related project roles are the project manager and the safety manager and these also have to have the (Eclipse) committer role.
As defined in `Committer Training <https://www.eclipse.org/projects/training/>`_ the committers are elected in a meritrocatic manner, meaning those have to show their skills and understanding of the project processes in several previous pull requests.

As each project can adopt additional criteria for the committers election, we define the following:

each committer has to prove his knowledge in functional safety SW development by

* an absolved training in ISO 26262 (or equivalent standard, at least 16h of SW development specific training by a trusted training provider) OR
* by attending the projects's ISO 26262 SW development training (given by a safety team member)

Additionally the project repository is organized in "CODEOWNER" sections. These "CODEOWNERS" need to approve any pull request modifying a file in their area before it is merged.

In case of safety related "CODEOWNER" sections (e.g. a file containing feature requirements with an ASIL level) the persons having "CODEOWNER" rights need to have:
* One year of professional practice of safety related SW development (or management) relevant for the section content

The successful checking of committers and CODEOWNERS skills is ensured by the safety manager and documented in the role assignment document.
One important aspect to this is, that we ensure the identity of the committer by applying the GitHub digital signature mechanism.

Functional Safety Ressources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A dedicated Safety Manager is defined as part of the Maintainer role.

The Safety Manager, supported by the Project Manager, and all other stakeholder,  will ensure that
safety activities are actively planned, developed, analyzed, verified and tested and managed throughout the life cycle of the project.
As all the implementation of safety functions takes place within module development there is a safety manager appointed in the module's safety plan.

Resources and milestones are planned in Github Issues for all activities.
There are issue templates for sagas (covering one feature development) and for epics (covering one development work product each).
Resource and milestone planning is done as defined in the :doc:`project_management`

*Tools*

The whole development and thus all work products are located in Github. The development is automated as much as possible and follows the defined processes.
Github issues are used as planning tool.
The issue types and issue types workflows are described in the platform management plan.
For safety relevant issues types a "safety" label is used.

Functional Safety Management Communication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To exchange general information and to clarify general topics the following communication channels are used:

* Regular (online) meetings, at least every two months.
* E-Mails
* Messager Services e.g., Slack, Microsoft Teams, Github Notifications
* Ad hoc safety related meetings are set up for clarification topics.

*Reporting*

The safety management status is reported due the meeting defined in the platform management plan.
The status report includes at least the defined Quality Criteria defined below in chapter TODO, LINK TO TEMPLATE

*Escalation*

* Safety Manager to Project Manager
* Project Manger to Steering Council

Examples for valid escalation causes are:

* Safety issues cannot be resolved on module level or with the available resources.
* There are conflicting points-of-view between the Project Manager and the Safety Manager

Functional Safety Management Life Cycle Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lifecycle is defined in the process description.
Note that the Eclipse Foundation also defines `project phases <https://www.eclipse.org/projects/handbook/#starting-project-phases>`_.
Eclipse definition is more about the process maturity for the whole project, if we are in Mature Phase, we latest will have the project lifecycle as defined in our process description.
Nevertheless, Safety Development and even Safety Case release is independent from Mature and Incubation Phase as the completeness and appropriateness of the platform process and artefacts
is determined by Safety Audit and not be Eclipse project reviews.

Functional Safety Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Requirement Engineering is defined in the process description. See :ref:`requirements_engineering`
The application of ISO 26262 standards requirements is realized by defining process guidances and matching those to the ISO 26262 requirements (see :ref:`processes_introduction`).

Functional Safety Schedule
^^^^^^^^^^^^^^^^^^^^^^^^^^
The schedule is defined in section "Platform Safety Plan" below, but also within each module safety plan. See linked issues below and in :need:`GD_TEMP__module_safety_plan`.

Functional Safety Development
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The SW development is defined in the project-wide software development plan. See :doc:`software_development`

Functional Safety Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The platform management plan defines the :doc:`software_verification`

Functional Safety Tool Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The platform management plan defines :doc:`tool_management`

Functional Safety Work products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The work products relevant for a module development is defined within each module safety management plan. See :need:`GD_TEMP__module_safety_plan`.
Generic project wide work products are defined below.

Functional Safety Quality Criteria
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The platform management plan defines :doc:`quality_management`

Platform Safety Plan
++++++++++++++++++++

Functional Safety Management SW Platform work products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Functional Safety Management Feature specific work products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Functional Safety work products status charts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



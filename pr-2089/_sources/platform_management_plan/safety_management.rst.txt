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

.. document:: Platform Safety Plan
   :id: doc__platform_safety_plan
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__platform_safety_plan,wp__tailoring
   :tags: platform_management

Safety management / Platform Safety Plan
----------------------------------------

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
* to plan to create a comprehensible safety case (collection of the safety related work products)
* to judge whether the SW achieves functional safety process conformance (i.e. the functional safety audit, confirmation reviews)

Objectives and Scope
++++++++++++++++++++

Functional Safety Management Goals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Adherence to the ISO 26262 according to the defined tailoring

in detail

* to plan all functional safety related activities and work products
* to monitor and facilitate all activities
* to measure and report functional safety status based on well-defined metrics

Functional Safety Management Scope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is no deviation from the scope presented in the `S-CORE project page <https://eclipse-score.github.io/>`_ .
The platform and its components are developed, and integrated for an assumed technical system as Safety Element out of Context (SEooC).
The development of the platform and its components follows the defined processes.
Responsibilities for development, implementation, integration and verification are also defined int the processes.

Regarding the platform specifics:

* the highest ASIL in the project is ASIL B
* all safety activities from a procedural point of view are developed according to ASIL B
* all safety related SW in the project is developed according to ISO 26262 ASIL B

The SW platform functionality consists of features, which are based on a set of requirements and are developed in parallel.
These features are developed into SW components contained in "modules", which are another set of SEooCs (initiated by a change request).
A template exists to guide this: :need:`gd_temp__module_safety_plan`.

Tailoring
^^^^^^^^^
Tailoring of safety activities:

* The tailoring is divided into project wide and module specific rules.
* Project wide tailoring is documented in this document - this is based on development of a platform SEooC.
* Module SEooC specific tailoring is documented in the module development Safety Plans - this may be based on SEooC specifics or because component qualification according to ISO 26262 part 8 clause 12 (or ISO PAS 8926) is selected.
* In case of a change request on an existing feature (i.e. a change request), the subsequent safety planning will be done based on an impact analysis.

The following  ISO 26262 defined safety work products are not relevant for the S-CORE SW platform development:

* Because these are in responsibility of the system integrator: :need:`std_wp__iso26262__management_751`,
  :need:`std_wp__iso26262__system_652`, :need:`std_wp__iso26262__system_653`, :need:`std_wp__iso26262__system_654`,
  :need:`std_wp__iso26262__system_655`, :need:`std_wp__iso26262__system_656`, :need:`std_wp__iso26262__system_657`,
  :need:`std_wp__iso26262__system_751`, :need:`std_wp__iso26262__system_752`, :need:`std_wp__iso26262__system_851`,
  :need:`std_wp__iso26262__system_852`

  Note that stakeholder requirements (:need:`std_wp__iso26262__system_651`) are in scope of the project,
  to be able to cover System and HW related failures which are usually covered by SW (e.g. end to end protection for ECU external communication).
  But those are the "Assumed Technical Safety Requirements" of the SW platform SEooC and do not need to be tested by SEooC supplier.
  I.e. the system testing is out of scope. Note that S-CORE will implement platform test of stakeholder requirements for demonstration,
  but these are not intended to be completely covering the stakeholder requirements.
  There will be SW integration tests of feature requirements, as required by ISO 26262 part 6-10.
  These may be reused by the users on their HW platform to cover Technical Safety Requirements towards the SW platform.
  But if these are sufficiently also covering the TSRs must be analyzed and decided by the user.

* Also tailored out is the SW testing on the target, as the S-CORE project can only test on reference HW
  (part of SW integration testing). So these are not relevant: :need:`std_wp__iso26262__software_1151`, :need:`std_wp__iso26262__software_1152`

* Because there is no calibration used for the S-CORE SW platform components, only configuration: :need:`std_wp__iso26262__software_app_c_52`,
  :need:`std_wp__iso26262__software_app_c_54`, :need:`std_wp__iso26262__software_app_c_57`

* Because distributed development is not how the project is organized. All contributors are seen as part of the project team.
  When used, OSS components are qualified and external SEooCs are integrated in the project scope: :need:`std_wp__iso26262__support_551`,
  :need:`std_wp__iso26262__support_552`, :need:`std_wp__iso26262__support_553`, :need:`std_wp__iso26262__support_554`, :need:`std_wp__iso26262__support_555`

* Because in the S-CORE SW platform HW elements are out of scope: :need:`std_wp__iso26262__support_1351`, :need:`std_wp__iso26262__support_1352`, :need:`std_wp__iso26262__support_1353`

* Because in the S-CORE SW platform a proven in use argument will not be applied: :need:`std_wp__iso26262__support_1451`, :need:`std_wp__iso26262__support_1452`

* Because in the S-CORE SW platform interfacing of out of scope of ISO 26262 applications is not planned: :need:`std_wp__iso26262__support_1551`

* Because in the S-CORE SW platform integration of safety-related systems not developed according to ISO 26262 is not planned: :need:`std_wp__iso26262__support_1651`

* Because in the S-CORE SW platform no ASIL decomposition is planned: :need:`std_wp__iso26262__analysis_551`, :need:`std_wp__iso26262__analysis_552`

* Because HSI is coming from HW (and systems) engineering which are not part of S-CORE
  and the standard only asks for refinement during SW development. As the input is missing, there is nothing to refine.
  Expectations towards the HW/Environment are covered by AoUs. Additionally S-CORE only provides reference HW integration,
  so every user of the platform would have to redo the effort anyway: :need:`std_wp__iso26262__software_652`

* Because the SW platform is not an safety item but an element: :need:`std_wp__iso26262__management_651`

But also some activities based on requirements defining what has to be done to create a workproduct which is in scope of the S-CORE platform are tailored:

* Because those are not relevant for ASIL_B: :need:`std_req__iso26262__system_6423`,
  :need:`std_req__iso26262__system_6424`, :need:`std_req__iso26262__system_6425`

Approach
++++++++

Safety Culture
^^^^^^^^^^^^^^

The safety of the project S-CORE is inherent. It relies on the personal dedication and integrity of every person who is involved in the project.
The safety thinking in the project allows a questioning attitude and fosters the taking of responsibility.
Every participation, e.g. with the raise up of an improvement or by asking questions in the discussion section of GitHub is welcomed.
The processes, guidelines and templates define the organizational framework.
Adherence is verified by automated checks and manual inspections.
All the aspects of ISO 26262 are directly implemented in the development process to ensure a proper communication and high understanding of functional safety.
With continuous improvements, an integral aspect in all processes, we want to achieve excellence.

Functional Safety Management Organization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is the project strategy to qualify the platform or components of the platform to the appropriate international standards and directives.
Therefore the project approach to facilitate a common culture regarding safety and security is part of our documentation.
The project will be under the Eclipse Foundation and so the `Eclipse Foundation Project Handbook: <https://www.eclipse.org/projects/handbook/>`_ applies.

*Eclipse Roles*

* `Contributors <https://www.eclipse.org/projects/handbook/#contributing-contributors>`_ can be everyone and we will not discourage the open source community from this. As the contributor cannot merge code (or any other work product) into the project's codebase, the safety development competence of the contributor is irrelevant.
* `Committers <https://www.eclipse.org/projects/handbook/#contributing-committers>`_ play the main development role in the project, as only these are allowed to merge, so they are the ultimate responsible for the project's repository content.
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
As defined in `Committer Training <https://www.eclipse.org/projects/training/>`_ the committers are elected in a meritocratic manner, meaning those have to show their skills and understanding of the project processes in several previous pull requests.

As each project can adopt additional criteria for the committers election, we define the following:

each committer has to prove his knowledge in functional safety SW development by

* an absolved training in ISO 26262 (or equivalent standard, at least 16h of SW development specific training by a trusted training provider) OR
* by attending the projects's ISO 26262 SW development training (given by a safety team member)

Additionally the project repository is organized in "CODEOWNER" sections. These "CODEOWNERS" need to approve any pull request modifying a file in their area before it is merged.

In case of safety related "CODEOWNER" sections (e.g. a file containing feature requirements with an ASIL level) the persons having "CODEOWNER" rights need to have:
* One year of professional practice of safety related SW development (or management) relevant for the section content

The successful checking of committers and CODEOWNERS skills is ensured by the safety manager and documented in the role assignment document.
One important aspect to this is, that we ensure the identity of the committer by applying the GitHub digital signature mechanism.

Functional Safety Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A dedicated safety manager is elected by :need:`rl__project_lead` for all the S-CORE SEooCs development.

The safety manager, supported by the project manager (i.e. the :need:`rl__technical_lead`),  will ensure that
safety activities are actively planned, developed, analyzed, verified and tested and managed throughout the life cycle of the project.
As all the implementation of safety functions takes place within module development, there is a safety manager appointed in the module's safety plan.

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

* Regular (online) meetings, at least every month.
* E-Mails
* Messenger Services e.g., Slack, Microsoft Teams, Github Notifications
* Ad hoc safety related meetings are set up for clarification topics.

*Reporting*

The safety management status is reported in the Technical Lead Circle Meeting which is defined in :need:`doc__project_mgt_plan`.
The status report is based on safety plans work product lists (see below) and verification reports on platform and module level:

* :need:`wp__platform_safety_plan`
* :need:`wp__module_safety_plan`
* :need:`wp__verification_platform_ver_report`
* :need:`wp__verification_module_ver_report`

*Escalation*

* :need:`rl__safety_manager` to :need:`rl__technical_lead`
* :need:`rl__technical_lead` to :need:`rl__project_lead`

Examples for valid escalation causes are:

* Safety issues cannot be resolved on module level or with the available resources.
* There are conflicting points-of-view between the project manager and the safety manager

Functional Safety Management Life Cycle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The safety lifecycle of the S-CORE project is initiated at the project set-up and driven and maintained by the safety manager supported by the :need:`rl__process_community`.
Note that the Eclipse Foundation also defines `project phases <https://www.eclipse.org/projects/handbook/#starting-project-phases>`_.
Eclipse definition is more about the process maturity for the whole project, if we are in Mature Phase, we latest will have the project lifecycle as defined in our process description.
Nevertheless, Safety Development and even Safety Case release is independent from Mature and Incubation Phase as the completeness and appropriateness of the platform process and artifacts
is determined by Safety Audit and not be Eclipse project reviews.

Functional Safety Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Requirement Engineering is defined in the process description. See :need:`doc__project_mgt_plan`.

The application of ISO 26262 standards requirements is realized by defining process guidances and matching those to the ISO 26262 requirements (see e.g. for example :need:`gd_req__safety_doc_status`).

Functional Safety Schedule
^^^^^^^^^^^^^^^^^^^^^^^^^^
The schedule is defined in section "Platform Safety Plan" below, but also within each module safety plan. See linked issues below and in :need:`gd_temp__module_safety_plan`.

Functional Safety Development
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The SW development is defined in the project-wide software development plan. See :doc:`software_development`

Functional Safety Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The platform management plan defines the :doc:`software_verification`

Functional Safety Tool Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The platform management plan defines :doc:`tool_management`

Functional Safety Work Products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The work products relevant for a module development is defined within each module safety management plan. See :need:`gd_temp__module_safety_plan`.
Generic project wide work products are defined below.

Functional Safety Quality Criteria
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The platform management plan defines :doc:`quality_management`

Platform Safety Plan
++++++++++++++++++++

Functional Safety Management SW Platform Work Products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: SW Platform work products
    :header-rows: 1

    * - work product Id
      - Link to process
      - Process status
      - Link to issue
      - Link to WP
      - WP status

    * - :need:`wp__policies`
      - n/a (comes from outside the project)
      - n/a
      - n/a
      - `Eclipse Foundation Project Handbook: <https://www.eclipse.org/projects/handbook/>`_
      - RELEASED

    * - :need:`wp__training_path`
      - n/a
      - n/a
      - n/a
      - not open sourced
      - to be shown to assessor

    * - :need:`wp__qms_plan`
      - :need:`wf__platform_cr_mt_platform_mgmt_plan`
      - :ndf:`copy('status', need_id='wf__platform_cr_mt_platform_mgmt_plan')`
      - `#316 <https://github.com/eclipse-score/score/issues/316>`_
      - :doc:`quality_management`
      - not started

    * - :need:`wp__issue_track_system`
      - :doc:`index`
      - :ndf:`copy('status', need_id='doc__platform_mgt_plan')`
      - n/a
      - `Project issues <https://github.com/eclipse-score/score/issues>`_
      - established

    * - :need:`wp__platform_mgmt`
      - :need:`wf__platform_cr_mt_platform_mgmt_plan`
      - :ndf:`copy('status', need_id='wf__platform_cr_mt_platform_mgmt_plan')`
      - `#540 <https://github.com/eclipse-score/score/issues/540>`_
      - :doc:`index`
      - :ndf:`copy('status', need_id='doc__platform_mgt_plan')`

    * - :need:`wp__process_description`
      - :need:`wf__def_app_process_description`
      - :ndf:`copy('status', need_id='wf__def_app_process_description')`
      - `Process community issues <https://github.com/orgs/eclipse-score/projects/7>`_
      - `Process description <https://eclipse-score.github.io/process_description/main/index.html>`_
      - <automated>

    * - :need:`wp__process_impr_report`
      - :need:`wf__mon_imp_process_description`
      - :ndf:`copy('status', need_id='wf__mon_imp_process_description')`
      - <Link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__process_strategy`
      - :need:`wf__cr_mt_process_mgt_strategy`
      - :ndf:`copy('status', need_id='wf__cr_mt_process_mgt_strategy')`
      - `#232 <https://github.com/eclipse-score/score/issues/232>`_
      - `Process community issues <https://github.com/orgs/eclipse-score/projects/7>`_
      - <automated>

    * - :need:`wp__platform_safety_plan`
      - :need:`gd_guidl__saf_plan_definitions`
      - :ndf:`copy('status', need_id='gd_guidl__saf_plan_definitions')`
      - `#381 <https://github.com/eclipse-score/score/issues/381>`_
      - this document
      - see above

    * - :need:`wp__platform_safety_package`
      - :need:`gd_guidl__saf_package`
      - :ndf:`copy('status', need_id='gd_guidl__saf_package')`
      - <Link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__fdr_reports` (platform Safety Plan)
      - :need:`gd_chklst__safety_plan`
      - :ndf:`copy('status', need_id='gd_chklst__safety_plan')`
      - <Link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__fdr_reports` (platform Safety Package)
      - :need:`gd_chklst__safety_package`
      - :ndf:`copy('status', need_id='gd_chklst__safety_package')`
      - <Link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__fdr_reports` (feature's Safety Analyses & DFA)
      - Safety Analysis FDR tbd
      - <automated>
      - <Link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__audit_report`
      - performed by external experts
      - n/a
      - `#470 <https://github.com/eclipse-score/score/issues/470>`_
      - <Link to WP>
      - intermediate

    * - :need:`wp__feature_dfa`
      - <Link to process>
      - <Process status>
      - <Link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__platform_sw_build_config`
      - :need:`doc__software_development_plan`
      - :ndf:`copy('status', need_id='doc__software_development_plan')`
      - <Link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__platform_safety_manual`
      - :need:`gd_temp__safety_manual`
      - :ndf:`copy('status', need_id='gd_temp__safety_manual')`
      - <Link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__platform_sw_release_note`
      - :need:`gd_temp__rel_plat_rel_note`
      - :ndf:`copy('status', need_id='gd_temp__rel_plat_rel_note')`
      - <Link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__verification_platform_ver_report`
      - :need:`gd_temp__mod_ver_report`
      - :ndf:`copy('status', need_id='gd_temp__mod_ver_report')`
      - <Link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__requirements_stkh`
      - :need:`gd_temp__req_stkh_req`
      - :ndf:`copy('status', need_id='gd_temp__req_stkh_req')`
      - n/a (done already)
      - :ref:`stakeholder_requirements`
      - <automated>

    * - :need:`wp__sw_development_plan`
      - :need:`wf__platform_cr_mt_platform_mgmt_plan`
      - :ndf:`copy('status', need_id='wf__platform_cr_mt_platform_mgmt_plan')`
      - `#583 <https://github.com/eclipse-score/score/issues/583>`_
      - :need:`doc__software_development_plan`
      - :ndf:`copy('status', need_id='doc__software_development_plan')`

    * - :need:`wp__verification_plan`
      - :need:`wf__platform_cr_mt_platform_mgmt_plan`
      - :ndf:`copy('status', need_id='wf__platform_cr_mt_platform_mgmt_plan')`
      - `#611 <https://github.com/eclipse-score/score/issues/611>`_
      - :need:`doc__verification_plan`
      - :ndf:`copy('status', need_id='doc__verification_plan')`

    * - :need:`wp__tool_verification_report`
      - :need:`doc__platform_tool_management_plan`
      - :ndf:`copy('status', need_id='doc__platform_tool_management_plan')`
      - <Link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__tailoring` (generic)
      - :need:`gd_guidl__saf_plan_definitions`
      - :ndf:`copy('status', need_id='gd_guidl__saf_plan_definitions')`
      - `#307 <https://github.com/eclipse-score/score/issues/307>`_
      - :need:`std_req__iso26262__management_5421` & :need:`doc__platform_safety_plan`
      - valid


Note: list of features for v0.5 according to `S-CORE Roadmap <https://github.com/orgs/eclipse-score/projects/17>`_
and :ref:`releases`

Platform Management Plan - Documents Status Chart
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`doc_platform_management_plan`

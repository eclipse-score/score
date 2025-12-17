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
   :id: doc__score_platform_safety_plan
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__platform_safety_plan, wp__tailoring
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
  to be able to address System and HW related failures which are typically mitigated by SW (e.g. end-to-end protection for ECU external communication).
  However, these are considered "Assumed Technical Safety Requirements" of the SW platform SEooC and do not require testing by the SEooC supplier.
  Thus, system-level testing is out of scope. S-CORE will implement platform tests of stakeholder requirements for demonstration purposes,
  but these are not intended to provide complete coverage of the stakeholder requirements.
  There will be SW integration tests of feature requirements as specified in ISO 26262 part 6-10.
  These tests may be reused by users on their HW platform to address Technical Safety Requirements for the SW platform.
  Whether these are sufficient to cover the TSRs must be analyzed and decided by the user.
  to be able to cover System and HW related failures which are usually covered by SW (e.g. end to end protection for ECU external communication).
  But those are the "Assumed Technical Safety Requirements" of the SW platform SEooC and do not need to be tested by SEooC supplier.
  I.e. the system testing is out of scope. Note that S-CORE will implement Platform Integration Test of stakeholder requirements for demonstration,
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

* Because the SW platform is not an safety item but an element: :need:`std_wp__iso26262__management_651`, hence impact analysis of the item level is tailored out

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

Cybersecurity Interface
^^^^^^^^^^^^^^^^^^^^^^^

Cybersecurity is a critical aspect of the overall safety culture and is recognized as an essential element in the development and operation of the S-CORE platform.
While functional safety and cybersecurity have distinct objectives, their interaction is managed through coordinated processes and shared responsibilities.

The project acknowledges the need to address cybersecurity risks that may impact safety. To this end, the following measures are implemented:

* Regular collaboration between the safety and cybersecurity teams to identify and assess potential cyber threats that could affect safety functions.
* Integration of cybersecurity considerations into safety analyses, including risk assessments, to ensure that cyber risks are systematically evaluated.
* Alignment of safety and cybersecurity requirements in the development lifecycle, with traceability between stakeholder safety requirements and relevant cybersecurity controls.
* Participation in cross-functional reviews and audits to ensure that both safety and cybersecurity requirements are met and that any conflicts are resolved.
* Continuous monitoring of emerging cybersecurity threats and updating the security plan accordingly; update the safety plan only if safety-related impacts are identified.

The project is committed to further strengthening the interface between safety and cybersecurity, and will regularly review and update its processes to reflect best practices and regulatory requirements.
This approach ensures that cybersecurity is not treated in isolation, but as an integral part of the platform's safety culture and management system.
The security management aspects are defined in the :doc:`security_management`.

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
Project role assignment is documented in dedicated documents.

*Critical dependencies*

The project has not implemented a quality management system yet.
But it aims to be conform to ASPICE, as defined in the management system.
Continuous improvement is part to all processes. Improvements are handled in the scope of Quality Management.

*Risk*

Organization and management system has not a mature level yet.

*Skills*

The main safety related project roles are the project manager, the safety manager and the safety engineer, these also have to have the (Eclipse) committer role.
As defined in `Committer Training <https://www.eclipse.org/projects/training/>`_ the committers are elected in a meritocratic manner, meaning those have to show their skills and understanding of the project processes in several previous pull requests.

For the :need:`rl__project_lead`, the :need:`rl__safety_manager` and the :need:`rl__safety_engineer` the required skills and experience are described
in these project role definitions. They are also elected in a meritocratic way and this election is documented including the evidences checked to prove the experience.

Committers in the S-CORE project can work on the development of safety related or non-safety related SW modules.
If they work on safety related modules they have to prove (additionaly to their committer election, which already shows they are skilled developers):

* two years practice of safety related SW development (or management) relevant for the section content (includes trainings in safety standards like ISO 26262)
* training on the S-CORE processes

To ensure this, the platform and module repositories folders (and files) are protected by "CODEOWNER" sections.
These "CODEOWNERS" need to approve any pull request modifying a file in their area before it is merged.

The successful checking of CODEOWNERS experience is ensured by the safety manager and documented in the role assignment document.
One important aspect to this is, that we ensure the identity of the committer by applying the GitHub digital signature mechanism.

Functional Safety Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A dedicated safety manager is elected for all the S-CORE SEooCs development - see :need:`doc__platform_safety_manager`.

The safety manager, supported by the project manager (:need:`rl__project_lead`) or the assigned Feature team leads, will ensure that
safety activities are actively planned, developed, analyzed, verified and tested and managed throughout the life cycle of the project.
As all the implementation of safety functions takes place within module development, there is a responsible safety manager documented in the module's safety plan.

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

The safety management status is reported in the Project Lead Circle Meeting which is defined in :need:`doc__project_mgt_plan`.
The status report is based on safety plans work product lists (see below) and verification reports on platform and module level:

* :need:`wp__platform_safety_plan`
* :need:`wp__module_safety_plan`
* :need:`wp__verification_platform_ver_report`
* :need:`wp__verification_module_ver_report`

*Escalation*

* :need:`rl__safety_manager` to :need:`rl__project_lead` (in the Project Lead Circle)

The Project Lead Circle is the ultimate decision instance within the S-CORE project.
But as in every Eclipse project the rules and committee decisions of Eclipse have to be followed.

Examples for valid escalation causes are:

* Safety issues cannot be resolved on module level or with the available resources.
* There are conflicting points-of-view between the module project manager (= Feature team lead) and any safety manager
* Safety anomalies detected by the safety manager are not accepted by the module project manager

Functional Safety Management Life Cycle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The safety lifecycle of the S-CORE project is initiated at the project set-up and driven and maintained by the safety manager supported by the :need:`rl__process_community`.
Note that the Eclipse Foundation also defines `project phases <https://www.eclipse.org/projects/handbook/#starting-project-phases>`_.
Eclipse definition is more about the process maturity for the whole project, if we are in Mature Phase, we latest will have the project lifecycle as defined in our process description.
Nevertheless, Safety Development and even Safety Case release is independent from Mature and Incubation Phase as the completeness and appropriateness of the platform process and artifacts
is determined by Safety Audit and not be Eclipse project reviews.
The S-CORE project implements a reduced ISO 26262 safety lifecycle, covering only those phases relevant to software SEooC development.
All omitted phases (e.g., HARA, system/hardware development, calibration, proven-in-use) are justified and documented in the Tailoring section.
All safety activities, planning, and evidence generation are tracked via the Platform Safety Plan, Module Safety Plans, and associated GitHub Issues.
This approach ensures compliance with ISO 26262 for software SEooC, while avoiding unnecessary activities not applicable to the S-CORE context.

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

.. _sw_platform_wp_list:

Functional Safety/Security Management SW Platform Work Products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: SW Platform work products
    :header-rows: 1

    * - work product Id
      - Process status
      - Link to WP
      - WP status

    * - :need:`wp__policies`
      - n/a (comes from outside the project)
      - `Eclipse Foundation Project Handbook: <https://www.eclipse.org/projects/handbook/>`_
      - RELEASED

    * - :need:`wp__qms_plan`
      - :ndf:`copy('status', need_id='wf__cr_mt_qlm_plan')`
      - :need:`doc__platform_quality_plan`
      - :ndf:`copy('status', need_id='doc__platform_quality_plan')`

    * - :need:`wp__issue_track_system`
      - :ndf:`copy('status', need_id='wf__platform_mr_im_platform_mgmt_plan')`
      - `Project issues <https://github.com/eclipse-score/score/issues>`_
      - established

    * - :need:`wp__platform_mgmt`
      - :ndf:`copy('status', need_id='wf__platform_cr_mt_platform_mgmt_plan')`
      - :doc:`index`
      - :ndf:`copy('status', need_id='doc__platform_mgt_plan')`

    * - :need:`wp__process_description`
      - :ndf:`copy('status', need_id='wf__def_app_process_description')`
      - `Process description <https://eclipse-score.github.io/process_description/main/index.html>`_
      - Maturity Level 1

    * - :need:`wp__process_impr_report`
      - :ndf:`copy('status', need_id='wf__mon_imp_process_description')`
      - `Process issues <https://github.com/eclipse-score/process_description/issues>`_
      - see issues

    * - :need:`wp__process_strategy`
      - :ndf:`copy('status', need_id='wf__cr_mt_process_mgt_strategy')`
      - `Process community planning <https://github.com/orgs/eclipse-score/projects/21>`_
      - see planning board

    * - :need:`wp__platform_handbook`
      - :ndf:`copy('status', need_id='wf__rel_platform_handbook')`
      - :need:`doc__platform_handbook`
      - :ndf:`copy('status', need_id='doc__platform_handbook')`

    * - :need:`wp__platform_sw_release_note`
      - :ndf:`copy('status', need_id='wf__rel_platform_rel_note')`
      - :need:`doc__score_v05_alpha_release_note`
      - :ndf:`copy('status', need_id='doc__score_v05_alpha_release_note')`

    * - :need:`wp__verification_platform_ver_report`
      - :ndf:`copy('status', need_id='wf__verification_platform_ver_report')`
      - <Link to WP>
      - <automated>

    * - :need:`wp__requirements_stkh`
      - :ndf:`copy('status', need_id='wf__req_stkh_req')`
      - :ref:`stakeholder_requirements`
      - <automated>

    * - :need:`wp__sw_development_plan`
      - :ndf:`copy('status', need_id='wf__sw_development_plan')`
      - :need:`doc__software_development_plan`
      - :ndf:`copy('status', need_id='doc__software_development_plan')`

    * - :need:`wp__verification_plan`
      - :ndf:`copy('status', need_id='wf__verification_plan')`
      - :need:`doc__verification_plan`
      - :ndf:`copy('status', need_id='doc__verification_plan')`

    * - :need:`wp__tool_verification_report`
      - :ndf:`copy('status', need_id='wf__tool_create_tool_verification_report')`
      - :ref:`tools`
      - see WP link


Functional Safety Specific SW Platform Work Products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: SW Platform safety work products
    :header-rows: 1

    * - work product Id
      - Process status
      - Link to WP
      - WP status

    * - :need:`wp__platform_safety_plan`
      - :ndf:`copy('status', need_id='wf__cr_mt_safety_plan')`
      - this document
      - see above

    * - :need:`wp__platform_safety_package`
      - :ndf:`copy('status', need_id='wf__cr_mt_safety_package')`
      - <Link to WP>
      - <automated>

    * - :need:`wp__fdr_reports` (platform Safety Plan)
      - :ndf:`copy('status', need_id='wf__p_formal_rv')`
      - <Link to WP>
      - <automated>

    * - :need:`wp__fdr_reports` (platform Safety Package)
      - :ndf:`copy('status', need_id='wf__p_formal_rv')`
      - <Link to WP>
      - <automated>

    * - :need:`wp__fdr_reports` (feature's Safety Analyses & DFA)
      - <Process status>
      - <Link to WP>
      - <automated>

    * - :need:`wp__audit_report`
      - performed by external experts
      - <Link to WP>
      - intermediate

    * - :need:`wp__feature_dfa`
      - <Process status>
      - <Link to WP>
      - <automated>

    * - :need:`wp__platform_safety_manual`
      - :ndf:`copy('status', need_id='wf__cr_mt_safety_manual')`
      - <Link to WP>
      - <automated>

    * - :need:`wp__tailoring` (generic)
      - :ndf:`copy('status', need_id='wf__def_app_process_description')`
      - :need:`wp__tailoring_work_products` & :need:`doc__score_platform_safety_plan`
      - valid

Process status: Status of the workflow which "outputs" the work product, derived from the docs it "has" and guidances it "contains".


Platform Management Plan - Feature Work Product Lists
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:need:`doc__baselibs_safety_wp`

:need:`doc__com_ipc_safety_wp`

:need:`doc__feo_safety_wp`

:need:`doc__orchestration_safety_wp`

:need:`doc__persistency_safety_wp`

Note: list of features according to :ref:`releases`


Platform Management Plan - Documents Status Chart
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`doc_platform_management_plan`

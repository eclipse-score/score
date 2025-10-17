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

Quality Management / Platform Quality Management Plan
=====================================================

.. document:: Platform Quality Management Plan
   :id: doc__platform_quality_plan
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: PROCESS_wp__qms_plan
   :tags: platform_management

Purpose
-------

The purpose of this document is to define a quality strategy and an approach for the platform.
This includes an approach to providing an independent and objective assurance that work products and processes
comply with predefined provisions and plans and that non-conformance is resolved and further prevented.
This document includes quality assurance activities, roles and responsibilities, goals, schedule, etc. and a
general strategy to implement quality assurance process in this platform. The quality assurance is
ensured by automated checks and restrictions, manual checks which includes to proof that there is no manipulation
of the workflows.

Statement of Independence
-------------------------

The :need:`PROCESS_rl__quality_manager` provides only support to the project with consulting them to improve the
quality of the project/platform product. Although the quality report is also sent to the :need:`PROCESS_rl__technical_lead`,
the :need:`PROCESS_rl__quality_manager` is independent of the delivery of the product.

  .. image:: _assets/score_project_organisation.drawio.svg
     :width: 900
     :alt: Project Organization
     :align: center

In S-CORE we have different Tier and OEM stakeholder involved: Every solution will be checked by the other stakeholders.
This is another strong independent mechanism to ensure quality.

Objectives and scope
--------------------

3.1 Quality Objectives
^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Standards to comply with
    :header-rows: 1
    :widths: 15,85,15

    * - #
      - **Standard Name**
      - **Version**
    * - 1
      - Automotive SPICE PAM
      - 4.0
    * - 2
      - ISO 262626:2018
      - 2018
    * - 3
      - ISO/SAE 21434:2021
      - 2021
    * - 4
      - ISO PAS 8926:2024 (will be integrated into ISO 26262 3rd edition as updated part 8 clause 12)
      - 2024


3.2 Quality Performance Objectives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Quality assurance activities and frequence of performing them
    :header-rows: 1

    * - #
      - **Activities**
      - **Cadence**
    * - 1
      - Platform process audit
      - Once for every platform release or on demand
    * - 2
      - Feature process conformance checks
      - Once for every feature release
    * - 3
      - Work product review
      - Once for every feature release
    * - 4
      - Platform release verification and approval
      - Once for every release
    * - 5
      - Process consulting / Quality trainings
      - Continuously
    * - 6
      - Process monitoring / Process improvement
      - Continuously


3.3 Quantitative Quality Goals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Quantitative Quality Goals
    :header-rows: 1

    * - #
      - **Quality Criteria**
      - **Source**
      - **Target value**
      - **Allowed variation**
      - **Metric**
    * - 1
      - One Platform process audit per release
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of the Platform process audit has be done for every release
      - Delta audit allowed to achieve 100%
      - Ensured by the process quality management, :need:`PROCESS_wf__exe_pltprocess_audit` - Platform process audit is available
    * - 2
      - One process conformance check for every feature release
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - One process conformance check has been done for every stable feature release
      - Feature is released as experimental
      - Ensured by the process quality and tool management, :need:`PROCESS_wp__qms_report` - Process conformance is available
    * - 3
      - Only quality-assured project/platform work products are delivered to the community
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of project/platform work products are quality-assured
      - Feature is released as experimental
      - Ensured by the process quality and tool management, :need:`PROCESS_wp__verification_platform_ver_report` - Work products contain the verification of the quality assurance
    * - 4
      - Only quality-assured project/platform releases are delivered to the community
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of project/platform releases delivered to the community are quality-assured
      - Feature is released as experimental
      - Ensured by the process release management, :need:`PROCESS_wp__platform_sw_release_note` contain the verification and approval of the quality-assurance
    * - 5
      - Only quality-trained personnel are part of the :need:`PROCESS_rl__committer`
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of personnel are trained as per committer role description in :need:`PROCESS_rl__committer`
      - None
      - Ensured by the process platform management, :need:`PROCESS_wp__training_path` contain the training material and evidences for conducted trainings
    * - 6
      - No overdue quality assurance closure activities
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of the quality improvement, non-conformance issues are closed
      - None
      - Ensured by the process quality management, :need:`PROCESS_wp__issue_track_system` contain improvements and non-conformance


3.4 Work Product Quality Goals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For all generated work products, the following quality goals are defined:

**Quality Criteria**

All work products have to be available and valid. Templates, checklists, and guidelines shall be used.
Plans have to be up to date.

The training material shall be available in the training path.
The issues in the issue tracking system following the planning strategy.

**Target value**

The target value for all work products is 100%.

**Allowed variation**

There is no allowed variation for the work products.

**Metric**

The metric for the work products is ensured by the process that contains the work product. Only valid work products can be merged. Reviews are required and therefore checklists are prepared. If applicable, script based checks are implemented.

3.5 Quality Management Scope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
There is no deviation from the scope defined in the :need:`doc__project_mgt_plan`. The platform and its
components are developed, and integrated for an assumed technical system, for functional safety purposes as
Safety Element out of Context (SEooC).

The development of the platform and its components follows the defined processes. Responsibilities for management,
development, implementation, integration, and verification are also defined in the processes.

The SW platform consists of features, which are based on a set of requirements and are developed in parallel.

**Tailoring of quality assurance activities**

* The tailoring is divided into project wide and feature specific rules.
* Project wide tailoring is documented in `ASPICE 4.0 <https://eclipse-score.github.io/process_description/main/standards/aspice_40/aspice.html>`_ - this is based on the development of a SW element.

3.6 Quality Management Organization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is the project strategy to qualify the platform or components of the platform to the appropriate international
standards and directives. Therefore the project approach to facilitate a common culture regarding quality, safety
and security is part of the documentation. The project is stewarded by the Eclipse Foundation and so the
`Eclipse Foundation Project Handbook <https://www.eclipse.org/projects/handbook/>`_ applies.

**Project Roles**

The project roles are defined in the processes and are aligned to Eclipse roles.

.. needtable::
   :style: table
   :columns: title;id;tags
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["role"]):
                results.append(need)


| **Critical dependencies**

The project has not implemented a quality management system yet, but aims to be conformant to ASPICE 4.0,
as defined in the management system. Continuous improvement is part of all processes. Improvements are handled
in the scope of Quality Management.

**Risk**

Organization and management system is currently not mature.

**Skills**

The main quality related project roles are the Quality Manager :need:`PROCESS_rl__quality_manager` and the Technical Lead :need:`PROCESS_rl__technical_lead`. These also have to have
the (Eclipse) committer role. As defined in `Committer Training <https://www.eclipse.org/projects/training/>`_ the
committers are elected in a meritrocratic manner, meaning those have to show their skills and understanding of the
project processes in several previous pull requests.

As each project can adopt additional criteria for the committers election, S-CORE defines that each committer has to prove
his knowledge in quality SW development by:

- by attending the project's ASPICE 4.0 SW management and development training.

Additionally, the project repository shall be organized in a way that independent roles (to the technical solution)
 have to approve any pull request before it's merged. The persons who are able to approve need to be qualified
 according to the roles description Quality Manager :need:`PROCESS_rl__quality_manager`.

The successful checking of the skills of the committers and independent roles is ensured by the Project and Quality Manager :need:`PROCESS_rl__quality_manager` and documented
in the role assignment document.

.. note:: The identity of the committer by applying the GitHub digital signature mechanism will be used to confirm the authenticity of the Quality Manager :need:`PROCESS_rl__quality_manager` role for the approvals

4 Quality Management Planning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
4.1 Quality Resources
""""""""""""""""""""""
A dedicated Quality Manager is defined as part of the cross functional feature teams as defined in :doc:`project_management`. The Quality Manager :need:`PROCESS_rl__quality_manager`, supported by the
Project Lead :need:`PROCESS_rl__project_lead`, and all other stakeholders, will ensure that quality activities are actively planned, developed,
analyzed, verified, tested, and managed throughout the life cycle of the project. As all the implementation
takes place within feature development, there is a Quality Manager :need:`PROCESS_rl__quality_manager` appointed in the feature development plan.

Resources and milestones are planned in Github Issues for all activities. Resource and
milestone planning is done as defined in the :doc:`project_management`.

**Tools**

The whole development and thus all work products are located in Github. The development is automated as much as
possible and follows the defined processes.

- Github issues are used for planning.
- The issue types and their workflows are described in the platform management plan.
- For quality relevant issue types the ``quality`` label is used.

4.2 Quality Management Communication
""""""""""""""""""""""""""""""""""""
To exchange general information and to clarify general topics, the following communication channels are used:
- Regular (online) meetings
- E-Mails
- Messenger Services e.g., Slack, Microsoft Teams, Github Notifications

Ad-hoc quality related meetings are set up for clarification topics.

**Reporting**

The quality management status :need:`PROCESS_wp__qms_report` is reported as defined in the platform management plan.

**Escalation**

- Quality Manager :need:`PROCESS_rl__quality_manager` to steering committee documented in :need:`doc__project_mgt_plan`.

**Examples for valid escalation causes are:**

- Quality issues cannot be resolved on feature level or with the available resources.
- There are conflicting points of view between the Project Lead :need:`PROCESS_rl__project_lead`, Technical Lead :need:`PROCESS_rl__technical_lead`, Safety Manager :need:`PROCESS_rl__safety_manager`, Security Manager :need:`PROCESS_rl__security_manager` and the Quality Manager :need:`PROCESS_rl__quality_manager`

4.3 Quality Management Specifics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
None

4.4 Quality Management Generic workproducts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table:: Quality related work products
        :header-rows: 1

        * - Workproduct Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - :need:`PROCESS_wp__audit_report`
          - :need:`PROCESS_gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__saf_plan_definitions')`
          - `#470 <https://github.com/eclipse-score/score/issues/470>`_
          - :need:`doc__platform_change_management_plan`
          - <automated>

        * - :need:`PROCESS_wp__chm_plan`
          - :need:`PROCESS_gd_guidl__change_change_request`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__change_change_request')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__cmpt_request`
          - :need:`PROCESS_gd_guidl__change_change_request`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__change_change_request')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__component_arch`
          - :need:`PROCESS_gd_guidl__arch_design`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__arch_design')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__document_mgt_plan`
          - :need:`PROCESS_gd_guidl__documentation`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__documentation')`
          - <Link to issue>
          - :need:`doc__documentation_mgt_plan`
          - <automated>

        * - :need:`PROCESS_wp__fdr_reports`
          - :need:`PROCESS_gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__saf_plan_definitions')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__feat_request`
          - :need:`PROCESS_gd_guidl__change_change_request`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__change_change_request')`
          - <Link to issue>
          - :need:`doc__logging`, :need:`doc__com`, :need:`doc__frameworks_feo`, :need:`doc__persistency_kvs`
          - <automated>

        * - :need:`PROCESS_wp__feature_arch`
          - :need:`PROCESS_gd_guidl__arch_design`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__arch_design')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__feature_dfa`
          - :need:`PROCESS_gd_guidl__safety_analysis`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__safety_analysis')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__module_safety_manual`
          - :need:`PROCESS_gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__saf_plan_definitions')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__module_safety_package`
          - :need:`PROCESS_gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__saf_plan_definitions')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__module_safety_plan`
          - :need:`PROCESS_gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__saf_plan_definitions')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__module_sw_release_note`
          - :need:`PROCESS_gd_guidl__rel_management`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__rel_management')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__module_sw_release_plan`
          - :need:`PROCESS_gd_guidl__rel_management`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__rel_management')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__platform_dfa`
          - :need:`PROCESS_gd_guidl__safety_analysis`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__safety_analysis')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__platform_safety_manual`
          - :need:`PROCESS_gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__saf_plan_definitions')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__platform_safety_plan`
          - :need:`PROCESS_gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__saf_plan_definitions')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__platform_safety_package`
          - :need:`PROCESS_gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__saf_plan_definitions')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__platform_sw_build_config`
          - n/a
          - draft
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__platform_sw_release_note`
          - :need:`PROCESS_gd_guidl__rel_management`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__rel_management')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__platform_sw_release_plan`
          - :need:`PROCESS_gd_guidl__rel_management`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__rel_management')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__policies`
          - n/a
          - draft
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__prm_plan`
          - :need:`PROCESS_gd_guidl__problem_problem`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__problem_problem')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__process_description`
          - n/a
          - draft
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__process_impr_report`
          - :need:`PROCESS_gd_guidl__platform_mgmt_plan`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__platform_mgmt_plan')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__process_strategy`
          - n/a
          - draft
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__project_mgt`
          - :need:`PROCESS_gd_guidl__platform_mgmt_plan`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__platform_mgmt_plan')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__qms_plan`
          - :need:`PROCESS_gd_guidl__qlm_plan_definitions`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__qlm_plan_definitions')`
          - <Link to issue>
          - :need:`doc__platform_quality_plan`
          - <automated>

        * - :need:`PROCESS_wp__qms_report`
          - :need:`PROCESS_gd_guidl__qlm_plan_definitions`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__qlm_plan_definitions')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__requirements_comp`
          - :need:`PROCESS_gd_guidl__req_engineering`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__req_engineering')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__requirements_comp_aou`
          - :need:`PROCESS_gd_guidl__req_engineering`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__req_engineering')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__requirements_feat`
          - :need:`PROCESS_gd_guidl__req_engineering`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__req_engineering')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__requirements_feat_aou`
          - :need:`PROCESS_gd_guidl__req_engineering`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__req_engineering')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__requirements_inspect`
          - :need:`PROCESS_gd_guidl__req_engineering`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__req_engineering')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__requirements_stkh`
          - :need:`PROCESS_gd_guidl__req_engineering`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__req_engineering')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__sw_arch_verification`
          - :need:`PROCESS_gd_guidl__arch_design`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__arch_design')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__sw_component_class`
          - :need:`PROCESS_gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__saf_plan_definitions')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__sw_component_dfa`
          - :need:`PROCESS_gd_guidl__safety_analysis`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__safety_analysis')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__sw_component_fmea`
          - :need:`PROCESS_gd_guidl__safety_analysis`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__safety_analysis')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__sw_component_dfa`
          - :need:`PROCESS_gd_guidl__safety_analysis`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__safety_analysis')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__sw_development_plan`
          - :need:`PROCESS_gd_guidl__implementation`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__implementation')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__sw_implementation`
          - :need:`PROCESS_gd_guidl__implementation`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__implementation')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__sw_implementation_inspection`
          - :need:`PROCESS_gd_guidl__implementation`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__implementation')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__tailoring`
          - :need:`PROCESS_gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__saf_plan_definitions')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__tlm_plan`
          - :need:`PROCESS_doc_concept__tool_process`
          - :ndf:`copy('status', need_id='PROCESS_doc_concept__tool_process')`
          - <Link to issue>
          - :need:`doc__platform_tool_management_plan`
          - <automated>

        * - :need:`PROCESS_wp__tool_verification_report`
          - :need:`PROCESS_doc_concept__tool_process`
          - :ndf:`copy('status', need_id='PROCESS_doc_concept__tool_process')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__training_path`
          - n/a
          - draft
          - <Link to issue>
          - <Link to WP>
          - <automated>


        * - :need:`PROCESS_wp__verification_comp_int_test`
          - :need:`PROCESS_gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__verification_guide')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__verification_feat_int_test`
          - :need:`PROCESS_gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__verification_guide')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__verification_module_ver_report`
          - :need:`PROCESS_gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__verification_guide')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__verification_plan`
          - :need:`PROCESS_gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__verification_guide')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__verification_platform_test`
          - :need:`PROCESS_gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__verification_guide')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__verification_platform_ver_report`
          - :need:`PROCESS_gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__verification_guide')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`PROCESS_wp__verification_sw_unit_test`
          - :need:`PROCESS_gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='PROCESS_gd_guidl__verification_guide')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

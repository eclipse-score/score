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
   :realizes: wp__qms_plan
   :tags: platform_management

Purpose
-------

The purpose of this document is to is to define a quality strategy and an approach for the platform.
This includes an approach to providing an independent and objective assurance that work products and processes
comply with predefined provisions and plans and that non-conformances are resolved and further prevented.
This document includes quality assurance activities, roles and responsibilities, goals, schedule, etc. and a
general strategy to implement quality assurance process in this platform. The quality assurance is
ensured by automated checks and restrictions, manual checks which inculdes to proof that there is no manipulation
of the workflows.

Statement of Independence
-------------------------

The :need:`rl__quality_manager` provides only support to the project with consulting them to improve the
quality of the project/platform product. Although the quality report is also sent to the :need:`rl__technical_lead`,
the :need:`rl__quality_manager` is independent of the delivery of the product.

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
      - ISO PAS 8926:2024
      - 2024


3.2 Quality Performance Objectives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Quality assurance activities and frequence of performing them
    :header-rows: 1

    * - #
      - **Activities**
      - **Cadence**
    * - 1
      - Platform Process audit
      - Once for every platform release or on demand
    * - 2
      - Feature Process conformance checks
      - Once for every feature release
    * - 3
      - Feature Work product review
      - Once for every feature release
    * - 4
      - Platform Release verification and approval
      - Once for every release
    * - 5
      - Process consulting / Quality Trainings
      - Continuously
    * - 6
      - Process monitoring / Process Improvement
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
      - One platform process audit per release
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of the platform process audit has be done for every release
      - Delta audit allowed to achieve 100%
      - Ensured by the process process management, :need:`wp__process_impr_report` - Platform process audit is available
    * - 2
      - One process conformance check for every feature release
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - One process conformance check has been done for every stable feature release
      - Feature is released as experimental
      - Ensured by the process quality and tool management, :need:`wp__qms_report` - Process conformance is available
    * - 3
      - Only quality-assured project/platform work products are delivered to the community
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of project/platform work products are quality-assured
      - Feature is released as experimental
      - Ensured by the process quality and tool management, :need:`wp__verification__platform_ver_report` - Work products contain the verification of the quality assurance
    * - 4
      - Only quality-assured project/platform releases are delivered to the community
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of project/platform releases delivered to the community are quality-assured
      - Feature is released as experimental
      - Ensured by the process release management, :need:`wp__platform_sw_release_note` contain the verification and approval of the quality-assurance
    * - 5
      - Only quality-trained personnel are part of the :need:`rl__committer`
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of personnel are trained
      - None
      - Ensured by the process platform management, :need:`wp__training_path` contain the training material and evidences for conducted trainings
    * - 6
      - No overdue quality assurance closure activities
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of the quality improvement, non-conformance issues are closed
      - None
      - Ensured by the process quality management, :need:`wp__issue_track_system` contain improvments and non-coformancees


3.4 Work Product Quality Goals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Work Product Quality Goals
    :header-rows: 1

    * - #
      - **Work Product**
      - **Quality Criteria**
      - **Target value**
      - **Allowed variation**
      - **Metric**
    * - 1
      - :need:`wp__feat_request`
      - | Feature request is reviewed and accepted
      - 100%
      - None
      - Ensured by process livecycle concept, evidences for participants available, feedback of participants documented
    * - 2
      - :doc:`../requirements/stakeholder/index`
      - | All stakeholder requirements are reviewed and valid
        | All stakeholder requirements are at least satisfied by one feature requirement
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid requirements can be merged, review required, script based check
    * - 3
      - <wp__tool_verification_report>
      - | All tool requirements are reviewed and valid
        | All tool requirements have bidirectional traceability to and from process requirements or guidance
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid requirements can be merged, review required, script based check
    * - 4
      - :need:`wp__requirements__feat`
      - | All feature requirements are reviewed and valid
        | All feature requirements have bidirectional traceability to and from stakeholder requirements
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid requirements can be merged, review required, script based check
    * - 5
      - :need:`wp__requirements__comp`
      - | All component requirements are reviewed and valid
        | All component requirements have bidirectional traceability to and from feature requirements
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid requirements can be merged, review required, script based check
    * - 6
      - :need:`wp__requirements__feat_aou`
      - | All feature aou are reviewed and valid
        | All feature aou have bidirectional traceability to and from feature requirements
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid requirements can be merged, review required, script based check
    * - 7
      - :need:`wp__requirements__comp_aou`
      - | All component aou are reviewed and valid
        | All component aou have bidirectional traceability to and from feature requirements
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid requirements can be merged, review required, script based check
    * - 8
      - :need:`wp__hsi`
      - | Hardware and Software interaction is specified and consistent with the technical safety concept
        | All component HW parts that are controlled by the software are included
        | All HW resources that support the SW execution are included
      - 100%
      - None
      - Ensured by quality management, only verified and valid documents can be merged, review required
    * - 9
      - :need:`wp__requirements__inspect`
      - | All requirements were inspected by review with inspection checklist.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid requirements can be merged, review required, script based check
    * - 10
      - :need:`wp__feature_arch`
      - | All feature architectures are reviewed and valid
        | All feature architectures have bidirectional traceability to and from feature requirements
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid requirements can be merged, review required, script based check
    * - 11
      - :need:`wp__feature_safety_analysis`
      - | Inductive (bottom-up) safety analysis e.g. FMEA is completed. Analysis verifies the feature architecture.
        | All detection and prevention mitigations are linked to Software Feature Requirements or Assumptions of use.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid safety analysis can be merged, review required, script based check
    * - 12
      - :need:`wp__component_arch`
      - | All component architectures are reviewed and valid
        | All component architectures have bidirectional traceability to and from components requirements or feature architectures
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid architecture can be merged, review required, script based check
    * - 13
      - :need:`wp__sw_component_safety_analysis`
      - | Inductive (bottom-up) safety analysis e.g. FMEA is completed. Analysis verifies the component architecture.
        | All detection and prevention mitigations are linked to Software Component Requirements or Assumptions of use.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid safety analysis can be merged, review required, script based check
    * - 14
      - :need:`wp__sw_arch_verification`
      - | Architecture verification is available and valid.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid architecture can be merged, review required, script based check
    * - 15
      - :need:`wp__sw_implementation`
      - | Implementation of source code has been done after creation of detailed design.
        | SW configuration is described.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid Detailed Design and Code can be merged, verification required, script based check
    * - 16
      - :need:`wp__verification__sw_unit_test`
      - | Detailed design is verified by unit testing.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid Detailed Design and Code can be merged, verification required, script based check
    * - 17
      - :need:`wp__sw_implementation_inspection`
      - | Inspection is done by inspection checklist.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid Detailed Design and Code can be merged, verification required, script based check
    * - 18
      - :need:`wp__verification__feat_int_test`
      - | All interfaces from static view and all flows from dynamic view are valid and reviewed.
        | Performance expectations (RAM, processor usage, ..) on reference hardware are described.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid features can be merged, verification required, script based check
    * - 19
      - :need:`wp__verification__comp_int_test`
      - | All interfaces from static view and all flows from dynamic view are valid and reviewed.
        | Integration of units into components is based on the detailed design.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid components can be merged, verification required, script based check
    * - 20
      - :need:`wp__verification__module_ver_report`
      - | Module verification report is available and valid for every module.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid components can be merged, verification required, script based check
    * - 21
      - :need:`wp__sw_component_class`
      - | Software component classification is available and valid.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid components can be merged, verification required, script based check
    * - 22
      - :need:`wp__training_path`
      - | All training material is available and valid, training planned and executed
        | All training paths has been scheduled and executed
      - 100%
      - None
      - Ensured by process platform management, evidences for participants available, feedback of participants documented
    * - 23
      - :need:`wp__issue_track_system`
      - All issues follow the planning strategy defined in the project/platform management plan
      - 100%
      - None
      - Ensured by project management and tool management, only issues following the strategy can be part of any PR
    * - 24
      - :need:`wp__platform_mgmt`
      - All findings from work product review are resolved anf reviewed. Document is valid.
      - 100%
      - None
      - Ensured by project management, only verified and valid documents can be merged, review required
    * - 25
      - :need:`wp__process_definition`
      - All findings from platform audit are resolved and reviewed. Document is valid.
      - 100%
      - None
      - Ensured by process management and tool management, only verified and valid documents can be merged, review required
    * - 26
      - :need:`wp__process_impr_report`
      - Process improvement report is available and valid for every platform release.
      - 100%
      - None
      - Ensured by quality management and tool management, only verified and valid documents can be merged, review required
    * - 27
      - :need:`wp__process_plan`
      - The process strategy is defined, available and valid.
      - 100%
      - None
      - Ensured by process management and tool management, only verified and valid documents can be merged, review required
    * - 28
      - :need:`wp__module_safety_plan`
      - All findings from work product review are resolved and reviewed. Document is valid.
      - 100%
      - None
      - Ensured by safety management, only verified and valid documents can be merged, review required
    * - 29
      - :need:`wp__module_safety_package`
      - All findings from work product review are resolved and reviewed. Document is valid.
      - 100%
      - None
      - Ensured by safety management, only verified and valid documents can be merged, review required
    * - 30
      - :need:`wp__platform_safety_plan`
      - All findings from work product review are resolved and reviewed. Document is valid.
      - 100%
      - None
      - Ensured by safety management, only verified and valid documents can be merged, review required
    * - 31
      - :need:`wp__platform_safety_package`
      - All findings from work product review are resolved and reviewed. Document is valid.
      - 100%
      - None
      - Ensured by safety management, only verified and valid documents can be merged, review required
    * - 32
      - :need:`wp__fdr_reports`
      - CMR reports (Safety Plan, Safety Case, Safety Analyses and DFA) are available and valid for every platform release.
      - 100%
      - None
      - Ensured by safety management, only verified and valid documents can be merged, review required
    * - 33
      - :need:`wp__audit_report`
      - Process Safety Audit report is available and valid for every platform release.
      - 100%
      - None
      - Ensured by safety management, only verified and valid documents can be merged, review required
    * - 34
      - :need:`wp__feature_dfa`
      - | DFA on platform/feature level is available and valid.
        | All detection and prevention mitigations linked to Software Feature Requirements or Assumptions of Use.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid safety analysis can be merged, review required, script based check
    * - 35
      - :need:`wp__sw_component_dfa`
      - | DFA on component/module level is available and valid.
        | All detection and prevention mitigations linded to Software Component Requirements or Assumptions of Use.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid safety analysis can be merged, review required, script based check
    * - 36
      - :need:`wp__module_sw_build_config`
      - | Build configuration is capable to create the SEooC Library on the reference HW, module level.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid documents can be merged, review required, script based check
    * - 37
      - :need:`wp__module_safety_manual`
      - | Safety Manual for every module is available, up to date and valid.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid documents can be merged, review required, script based check
    * - 38
      - :need:`wp__module_sw_release_note`
      - | All known bugs are described with a clear statement that these bugs do not lead to violation of any safety requirements or corresponding workaround measures.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid documents can be merged, review required, script based check
    * - 39
      - :need:`wp__sw_development_plan`
      - | SW Development Plan is available, up to date and valid.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid documents can be merged, review required, script based check
    * - 40
      - :need:`wp__verification__plan`
      - | Verification Plan is available, up to date and valid.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid documents can be merged, review required, script based check
    * - 41
      - :need:`wp__tool_verification_report`
      - | All tool conficence levels (TCL) are determined. Appropriate qualification methods are applied.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid documents can be merged, review required, script based check
    * - 42
      - :need:`wp__tailoring`
      - | Argumentation for all tailored (not needed) work products in the project is available and valid.
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid documents can be merged, review required, script based check
    * - 43
      - :need:`wp__qms_plan`
      - | Quality Management Plan is available, up to date and valid
      - 100%
      - None
      - Ensured by process configuration and tool management, only valid documents can be merged, review required, script based check

3.5 Quality Management Scope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
There is no deviation from the scope defined in the :need:`doc__project_mgt_plan`. The platform and its
components are developed, and integrated for an assumed technical system, for functional safety purposes as
Safety Element out of Context (SEooC).

The development of the platform and its components follows the defined processes. Responsibilities for management,
development, implementation, integration and verification are also defined in the processes.

The SW platform consists of features, which are based on a set of requirements and are developed in parallel.

**Tailoring of quality assurance activities**

* The tailoring is divided into project wide and feature specific rules.
* Project wide tailoring is documented in :doc:`/process/standards/aspice_40/aspice` - this is based on the development of a SW element

3.6 Quality Management Organization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is the project strategy to qualify the platform or components of the platform to the appropriate international
standards and directives. Therefore the project approach to facilitate a common culture regarding quality, safety
and security is part of our documentation. The project will be under the Eclipse Foundation and so the
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

The project has not implemented a quality management system yet. But it aims to be conformant to ASPICE 4.0,
as defined in the management system. Continuous improvement is part of all processes. Improvements are handled
in the scope of Quality Management.

**Risk**

Organization and management system is currently not mature.

**Skills**

The main quality related project roles are the project manager and the quality manager and these also have to have
the (Eclipse) committer role. As defined in `Committer Training <https://www.eclipse.org/projects/training/>`_ the
committers are elected in a meritrocratic manner, meaning those have to show their skills and understanding of the
project processes in several previous pull requests.

As each project can adopt additional criteria for the committers election, we define that each committer has to prove
his knowledge in quality SW development by:

- by attending the project's ASPICE 4.0 SW management and development training (given by a project lead, quality manager or safety team member)

Additionally the project repository is organized in "CODEOWNER" sections. These "CODEOWNERS" need to approve any pull
request modifying a file in their area before it is merged. In case of quality related "CODEOWNER" sections (e.g.
any documentation artefacts) the persons having "CODEOWNER" rights need to have:

- At least one year of professional practice of quality related SW development (or management) relevant for the section content with demonstrable and verifiable results.

The successful checking of committers and CODEOWNERS skills is ensured by the project and quality manager and documented
in the role assignment document.

.. note:: The identity of the committer by applying the GitHub digital signature mechanism will be used to confirm the authenticity of the quality manager role for the approvals

4 Quality Management Planning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
4.1 Quality Resources
""""""""""""""""""""""
A dedicated Quality Manager is defined as part of the cross functional teams as defined in :doc:`project_management`. The Quality Manager, supported by the
Project Manager, and all other stakeholders, will ensure that quality activities are actively planned, developed,
analyzed, verified and tested and managed throughout the life cycle of the project. As all the implementation
takes place within feature development, there is a quality manager appointed in the feature development plan.

Resources and milestones are planned in Github Issues for all activities. There are issue templates for sagas
(covering one feature development) and for epics (covering one development workproduct each). Resource and
milestone planning is done as defined in the :doc:`project_management`.

**Tools**

The whole development and thus all work products are located in Github. The development is automated as much as
possible and follows the defined processes.

- Github issues are used for planning.
- The issue types and issue types workflows are described in the platform management plan.
- For quality relevant issue types a ``quality`` label is used.

4.2 Quality Management Communication
""""""""""""""""""""""""""""""""""""
To exchange general information and to clarify general topics, the following communication channels are used:
- Regular (online) meetings
- E-Mails
- Messager Services e.g., Slack, Microsoft Teams, Github Notifications

Ad-hoc quality related meetings are set up for clarification topics.

**Reporting**

The quality management status is reported as defined in the platform management plan. The status report includes
at least the defined Quality Criteria defined in this document.

**Escalation**

- Quality Manager to Steering Council

**Examples for valid escalation causes are:**

- Quality issues cannot be resolved on feature level or with the available resources.
- There are conflicting points of view between the Project Manager, Safety Manager and the Quality Manager

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

        * - wp__audit_report
          - :doc:`/process/process_areas/safety_management/index`
          - valid
          -
          - :need:`wp__audit_report`
          - valid

        * - wp__chm_plan
          - :doc:`/process/process_areas/change_management/index`
          - valid
          -
          - :need:`wp__chm_plan`
          - valid

        * - wp__cmpt_request
          - :doc:`/process/process_areas/change_management/index`
          - valid
          -
          - :need:`wp__cmpt_request`
          - valid

        * - wp__component_arch
          - :doc:`/process/process_areas/architecture_design/index`
          - valid
          -
          - :need:`wp__component_arch`
          - valid

        * - wp__document_mgt_plan
          - :doc:`/process/process_areas/documentation_management/index`
          - valid
          - n/a
          - :need:`wp__document_mgt_plan`
          - valid

        * - wp__fdr_reports
          - :doc:`/process/process_areas/safety_management/index`
          - valid
          - n/a
          - :need:`wp__fdr_reports`
          - valid

        * - wp__feat_request
          - :doc:`/process/process_areas/change_management/index`
          - valid
          -
          - :need:`wp__feat_request`
          - valid

        * - wp__feature_arch
          - :doc:`/process/process_areas/architecture_design/index`
          - valid
          -
          - :need:`wp__feature_arch`
          - valid

        * - wp__feature_dfa
          -
          - valid
          - n/a
          - :need:`wp__feature_dfa`
          - valid

        * - wp__feature_safety_analysis
          -
          - valid
          - n/a
          - :need:`wp__feature_safety_analysis`
          - valid

        * - wp__hsi
          - n/a
          - valid
          - n/a
          - :need:`wp__hsi`
          - valid

        * - wp__issue_track_system
          - :doc:`/process/process_areas/change_management/index`
          - valid
          -
          - :need:`wp__issue_track_system`
          - valid

        * - wp__module_safety_manual
          - :doc:`/process/process_areas/safety_management/index`
          - valid
          - n/a
          - :need:`wp__module_safety_manual`
          - valid

        * - wp__module_safety_package
          - :doc:`/process/process_areas/safety_management/index`
          - valid
          - n/a
          - :need:`wp__module_safety_package`
          - valid

        * - wp__module_safety_plan
          - :doc:`/process/process_areas/safety_management/index`
          - valid
          - n/a
          - :need:`wp__module_safety_plan`
          - valid

        * - wp__platform_sw_build_config
          -
          -
          - n/a
          - :need:`wp__platform_sw_build_config`
          - draft

        * - wp__platform_sw_release_note
          -
          -
          - n/a
          - :need:`wp__platform_sw_release_note`
          - valid

        * - wp__policies
          -
          -
          - n/a
          - :need:`wp__policies`
          - draft

        * - wp__prm_plan
          - :doc:`/process/process_areas/problem_resolution/index`
          - valid
          - n/a
          - :need:`wp__prm_plan`
          - valid

        * - valid
          -
          -
          - n/a
          - :need:`wp__process_definition`
          - draft

        * - wp__process_impr_report
          - :doc:`/process/process_areas/quality_management/index`
          - valid
          - n/a
          - :need:`wp__process_impr_report`
          - valid

        * - wp__process_plan
          -
          - valid
          - n/a
          - :need:`wp__process_plan`
          - valid

        * - wp__project_mgt
          -
          - valid
          - n/a
          - :need:`wp__project_mgt`
          - valid

        * - wp__qms_plan
          - :doc:`/process/process_areas/quality_management/index`
          - valid
          - n/a
          - :need:`wp__qms_plan`
          - valid

        * - wp__qms_report
          - :doc:`/process/process_areas/quality_management/index`
          - valid
          - n/a
          - :need:`wp__qms_report`
          - valid

        * - wp__requirements__comp
          - :doc:`/process/process_areas/requirements_engineering/index`
          - valid
          - n/a
          - :need:`wp__requirements__comp`
          - valid

        * - wp__requirements__comp_aou
          - :doc:`/process/process_areas/requirements_engineering/index`
          - valid
          - n/a
          - :need:`wp__requirements__comp_aou`
          - valid

        * - wp__requirements__feat
          - :doc:`/process/process_areas/requirements_engineering/index`
          - valid
          - n/a
          - :need:`wp__requirements__feat`
          - valid

        * - wp__requirements__feat_aou
          - :doc:`/process/process_areas/requirements_engineering/index`
          - valid
          - n/a
          - :need:`wp__requirements__feat_aou`
          - valid

        * - wp__requirements__inspect
          - :doc:`/process/process_areas/requirements_engineering/index`
          - valid
          - n/a
          - :need:`wp__requirements__inspect`
          - valid

        * - wp__requirements__stkh
          - :doc:`/process/process_areas/requirements_engineering/index`
          - valid
          - n/a
          - :need:`wp__requirements__stkh`
          - valid

        * - wp__sw_arch_verification
          - :doc:`/process/process_areas/architecture_design/index`
          - valid
          - n/a
          - :need:`wp__sw_arch_verification`
          - valid

        * - wp__sw_component_class
          - :doc:`/process/process_areas/safety_management/index`
          - valid
          - n/a
          - :need:`wp__sw_component_class`
          - valid

        * - wp__sw_component_dfa
          -
          - valid
          - n/a
          - :need:`wp__sw_component_dfa`
          - valid

        * - wp__sw_component_safety_analysis
          -
          - valid
          - n/a
          - :need:`wp__sw_component_safety_analysis`
          - valid

        * - wp__sw_development_plan
          - :doc:`/process/process_areas/implementation/index`
          - valid
          - n/a
          - :need:`wp__sw_development_plan`
          - valid

        * - wp__sw_implementation
          - :doc:`/process/process_areas/implementation/index`
          - valid
          - n/a
          - :need:`wp__sw_implementation`
          - valid

        * - wp__sw_implementation_inspection
          - :doc:`/process/process_areas/implementation/index`
          - valid
          - n/a
          - :need:`wp__sw_implementation_inspection`
          - valid

        * - wp__tailoring
          - :doc:`/process/process_areas/safety_management/index`
          - valid
          - n/a
          - :need:`wp__tailoring`
          - valid

        * - wp__tailoring_platform
          - :doc:`/process/process_areas/safety_management/index`
          - valid
          - n/a
          - :need:`wp__tailoring_platform`
          - valid

        * - wp__tool_verification
          -
          -
          - n/a
          - :need:`wp__tool_verification_report`
          - valid

        * - wp__training_path
          -
          -
          - n/a
          - :need:`wp__training_path`
          - draft

        * - wp__verification__comp_int_test
          - :doc:`/process/process_areas/verification/index`
          - valid
          - n/a
          - :need:`wp__verification__comp_int_test`
          - valid

        * - wp__verification__feat_int_test
          - :doc:`/process/process_areas/verification/index`
          - valid
          - n/a
          - :need:`wp__verification__feat_int_test`
          - valid

        * - wp__verification__module_ver_report
          - :doc:`/process/process_areas/verification/index`
          - valid
          - n/a
          - :need:`wp__verification__module_ver_report`
          - valid

        * - wp__verification__plan
          - :doc:`/process/process_areas/verification/index`
          - valid
          - n/a
          - :need:`wp__verification__plan`
          - valid

        * - wp__verification__platform_test
          - :doc:`/process/process_areas/verification/index`
          - valid
          - n/a
          - :need:`wp__verification__platform_test`
          - valid

        * - wp__verification__platform_ver_report
          - :doc:`/process/process_areas/verification/index`
          - valid
          - n/a
          - :need:`wp__verification__platform_ver_report`
          - valid

        * - wp__verification__sw_unit_test
          - :doc:`/process/process_areas/verification/index`
          - valid
          - n/a
          - :need:`wp__verification__sw_unit_test`
          - valid


.. Jetzt kommt eine neue Tabelle


.. .. needtable:: Quality related work products Quality Management
..    :style: table
..    :columns: id;tags;title;status;Link to WP
..    :colwidths: 20,20,20,20,20
..    :sort: id

..    results = []

..    for need in needs.filter_types(["workproduct"]):
..       for tags_id in need['tags']:
..           if tags_id == 'quality_management':
..                 results.append(need)
..       for tags_id in need['tags']:
..           if tags_id == 'requirements_engineering':
..                 results.append(need)
..    for need in needs.filter_types(["doc_concept"]):
..       for tags_id in need['tags']:
..           if tags_id == 'implementation':
..                 results.append(need)

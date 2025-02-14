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

Workflows
---------

.. workflow:: Create/Maintain Safety Plan
   :id: WF__cr_mt_safety_plan
   :status: valid
   :responsible: RL__safety_manager
   :approved_by: RL__technical_lead
   :input: WP_PLATFORM_MGMT, WP_ISSUE_TRACK_SYSTEM, WP__sw_component_class
   :output: WP__module_safety_plan, WP__platform_safety_plan
   :contains: GD_GUIDL__saf_plan_definitions, GD_TEMP__feature_safety_wp, GD_TEMP__module_safety_plan
   :has: DOC_CONCEPT__safety_management

   | The Safety Manager is responsible for the planning and coordination of the safety activities for the platform.
   | The Safety Manager creates and maintains the safety plan.
   | For this a template exists to guide the creator of the safety plan.

.. workflow:: Create Component Classification
   :id: WF__cr_comp_class
   :status: valid
   :responsible: RL_committer
   :approved_by: RL__safety_manager
   :input: WP_PLATFORM_MGMT, WP_ISSUE_TRACK_SYSTEM
   :output: WP__sw_component_class
   :contains: GD_GUIDL__component_classification, GD_TEMP__component_classification
   :has: DOC_CONCEPT__safety_management

   | The Safety Manager shall approve the OSS component classification performed by an expert on this component.

.. workflow:: Create/Maintain Draft Safety Case
   :id: WF__cr_mt_safety_case
   :status: valid
   :responsible: RL__safety_manager
   :approved_by: RL__technical_lead
   :input: WP__module_safety_plan, WP__platform_safety_plan, WP_ISSUE_TRACK_SYSTEM
   :output: WP__module_safety_case, WP__platform_safety_case
   :contains: GD_GUIDL__saf_case, GD_TEMP__feature_safety_wp, GD_TEMP__module_safety_plan
   :has: DOC_CONCEPT__safety_management

   | The Safety Manager in SCORE is NOT responsible to provide the argument for the achievement of functional safety.
   | But the Safety Manager creates and maintains the safety case in the sense of a collection of safety related work products.
   | The generation and the maintainance of this draft safety case shall be automtated as much as possible.
   | It is draft in a sense that it does not contain the final argumentation of the safety of the product.
   | As the draft safety case is only a collection of work products, the safety plan (template) can be used for documentation.

.. workflow:: Perform Safety Audit
   :id: WF__p_fs_audit
   :status: valid
   :responsible: RL__external_auditor
   :approved_by: RL__safety_manager
   :input: WP__module_safety_plan, WP__platform_safety_plan, WP__module_safety_case, WP__platform_safety_case
   :output: WP_audit_report
   :contains: GD_GUIDL__saf_plan_definitions
   :has: DOC_CONCEPT__safety_management

   | The external auditor is reponsible to perform a safety audit.
   | The Safety Team shall support the external auditor during this.
   | The Project Manager and and the Safety Manager shall approve the audit report.

.. workflow:: Perform Confirmation Reviews
   :id: WF__p_confirm_rv
   :status: valid
   :responsible: RL__external_auditor
   :approved_by: RL__safety_manager
   :input: WP__module_safety_plan, WP__platform_safety_plan, WP__module_safety_case, WP__platform_safety_case
   :output: WP__cmr_reports
   :contains: GD_GUIDL__saf_plan_definitions, GD_CHKLST__safety_plan, GD_CHKLST__safety_case
   :has: DOC_CONCEPT__safety_management

   | The external auditor is responsible to perform the confirmation reviews on Safety plan and Safety Analysis.
   | The Safety Team shall support the external auditor during the reviews.
   | The Project Manager and and the Safety Manager shall approve the confirmation reports.
   | Therefore a checklists exist to guide the creator of the relevant safety documents.

.. workflow:: Create/Maintain Safety Manual
   :id: WF__cr_mt_safety_manual
   :status: valid
   :responsible: RL__safety_manager
   :approved_by: RL__technical_lead
   :input: WP_FEATURE_AOU, WP_FEATURE_REQ, WP_FEATURE_ARCHITECTURE, WP_FEATURE_SAFETY_ANALYSES, WP_FEATURE_DFA, WP_SW_COMPONENT_AOU, WP_SW_COMPONENT_REQ, WP_SW_COMPONENT_ARCHITECTURE, WP_SW_COMPONENT_SAFETY_ANALYSES, WP_SW_COMPONENT_DFA
   :output: WP__platform_safety_manual, WP__module_safety_manual
   :contains: GD_GUIDL__saf_man, GD_TEMP__safety_manual
   :has: DOC_CONCEPT__safety_management

   | The Safety Manager collects the necessary input for the safety manuals on platform and module level and documents it.
   | He makes sure all items are in valid state for a release of the safety manual.
   | Also for the safety manual a template exists as a guidance.

.. workflow:: Monitor/Verify Safety
   :id: WF__mr_vy_safety
   :status: valid
   :responsible: RL__safety_manager
   :approved_by: RL__technical_lead
   :input: WP__module_safety_plan, WP__platform_safety_plan, WP__module_safety_case, WP__platform_safety_case, WP_audit_report, WP__cmr_reports
   :output: WP_ISSUE_TRACK_SYSTEM, WP_MODULE_SW_RELEASE_NOTE, WP_PLATFORM_SW_RELEASE_NOTE
   :contains: GD_GUIDL__saf_plan_definitions
   :has: DOC_CONCEPT__safety_management

   | The Safety Manager is responsible for the monitoring of the safety activities against the safety plan.
   | The Safety Manager is responsible to verify, that the preconditions for the "release for production", which are  part of the release notes, are fulfilled.
   | The Safety Manager is responsible to verify the correctness, completeness and consistency of the release notes.

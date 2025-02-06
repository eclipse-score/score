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

Safety Management
=================


Workflows
---------

todo: need to add guidance and standard links

.. workflow:: Create/Maintain Safety Plan
   :id: WF_CR_MT_SAFETY_PLAN
   :status: draft
   :tags: safety_management
   :responsible: RL_safety_manager
   :approved_by: RL_technical_lead
   :supported_by: RL_quality_manager
   :input: WP_PLATFORM_MGMT, WP_ISSUE_TRACK_SYSTEM
   :output: WP_MODULE_SAFETY_PLAN, WP_PLATFORM_SAFETY_PLAN

   | The Safety Manager is responsible for the planning and coordination of the safety activities for the platform.
   | The Safety Manager creates and maintains the safety plan.
   | For this a template exists to guide the creator of the safety plan (compare here: need link to GD_Saf_Plan_Definitions need link to GD_Saf_Plan_Template)

.. workflow:: Create/Maintain Safety Case
   :id: WF_CR_MT_SAFETY_CASE
   :status: draft
   :tags: safety_management
   :responsible: RL_safety_manager
   :approved_by: RL_technical_lead
   :supported_by: RL_quality_manager
   :input: WP_MODULE_SAFETY_PLAN, WP_PLATFORM_SAFETY_PLAN, WP_ISSUE_TRACK_SYSTEM
   :output: WP_MODULE_SAFETY_CASE, WP_PLATFORM_SAFETY_CASE

   | The Safety Manager is responsible to provide the argument for the achievement of functional safety.
   | The Safety Manager creates and maintains therefore the safety case.
   | The generation and the maintainance of the safety case shall be automtated as much as possible.
   | Therefore a template exists to guide the creator of the safety case (compare here: need link to GD_Saf_Case need link to GD_Saf_Case_Report_Template)

.. workflow:: Perform Safety Audit/Assessment
   :id: WF_P_FS_AUDIT_ASSESSMENT
   :status: draft
   :tags: safety_management
   :responsible: RL_external_assessor
   :approved_by: RL_safety_manager
   :supported_by: RL_technical_lead
   :input: WP_MODULE_SAFETY_PLAN, WP_PLATFORM_SAFETY_PLAN, WP_MODULE_SAFETY_CASE, WP_PLATFORM_SAFETY_CASE
   :output: WP_ASSESSMENT_REPORT

   | The external assessor is reponsible to perform a safety audit and a safety assessment.
   | The Safety Team shall support the external assessor during the audit.
   | The Project Manager and and the Safety Manager shall approve the audit and assessment reports.

.. workflow:: Perform Confirmation Reviews
   :id: WF_P_CONFIRM_RV
   :status: draft
   :tags: safety_management
   :responsible: RL_external_assessor
   :approved_by: RL_safety_manager
   :supported_by: RL_technical_lead
   :input: WP_MODULE_SAFETY_PLAN, WP_PLATFORM_SAFETY_PLAN, WP_MODULE_SAFETY_CASE, WP_PLATFORM_SAFETY_CASE, WP_ASSESSMENT_REPORT
   :output: WP_CMR_REPORTS

   | The external assessor is responsible to perform the confirmation reviews.
   | The Safety Team shall support the external assessor during the reviews.
   | The Project Manager and and the Safety Manager shall approve the confirmation reports.
   | Therefore a checklists exist to guide the creator of the relevant saftey documents.
   | (compare here: need link to GD_Saf_Plan_Confirmation_Review_Checklist_Template, need link to GD_Saf_Case_Confirmation_Review_Checklist_Template)

.. workflow:: Monitor/Verify Safety
   :id: WF_MR_VY_Safety
   :status: draft
   :tags: safety_management
   :responsible: RL_safety_manager
   :approved_by: RL_technical_lead
   :supported_by: RL_quality_manager
   :input: WP_MODULE_SAFETY_PLAN, WP_PLATFORM_SAFETY_PLAN, WP_MODULE_SAFETY_CASE, WP_PLATFORM_SAFETY_CASE, WP_ASSESSMENT_REPORT, WP_CMR_REPORTS
   :output: WP_ISSUE_TRACK_SYSTEM, WP_MODULE_SW_RELEASE_NOTE, WP_PLATFORM_SW_RELEASE_NOTE

   | The Safety Manager is responsible for the monitoring of the safety activities against the safety plan.
   | The Safety Manager is responsible to verify, that the preconditions for the "release for production", which are  part of the release notes, are fulfilled.
   | The Safety Manager is responsible to verify the correctness, completeness and consistency of the release notes.

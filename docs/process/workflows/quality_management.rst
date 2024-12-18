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

Quality Management
==================


Workflows
---------

todo: need to add guidance and standard links

.. workflow:: Create/Maintain Quality Plan
   :id: WF_CR_MT_QLM_PLAN
   :status: draft
   :tags: quality_management
   :responsible: RL_committer
   :approver: RL_quality_manager
   :supporter: RL_technical_lead
   :input: WP_POLICIES, WP_ISSUE_TRACK_SYSTEM
   :output: WP_QMS

   | The quality plan is created and maintained by a :need:`RL_committer`.

.. workflow:: Verify/Approve Platform Release
   :id: WF_VY_AP_PltRelease
   :status: draft
   :tags: quality_management
   :responsible: RL_committer
   :approver: RL_quality_manager
   :supporter: RL_technical_lead
   :input: WP_QMS
   :output: WP_PLATFORM_SW_RELEASE_NOTE

   | The project/platform release is verified and approved.

.. workflow:: Execute Platform Process Audit
   :id: WF_EXE_PltProcess_Audit
   :status: draft
   :tags: quality_management
   :responsible: RL_quality_manager
   :approver: RL_technical_lead
   :supporter: RL_safety_manager, RL_security_manager
   :input: WP_QMS, WP_PROCESS_DEFINITION
   :output: WP_PROCESS_IMPR_REPORT

   | The project/platform processes are audited.

.. workflow:: Execute Feature Process Compliance Checks
   :id: WF_EXE_FeatProcess_Compliance_Checks
   :status: draft
   :tags: quality_management
   :responsible: RL_committer
   :approver: RL_quality_manager
   :supporter: RL_technical_lead
   :input: WP_QMS, WP_FEAT_REQUEST, WP_PROCESS_DEFINITION
   :output: WP_QMS_REPORT

   | The compliance of the feature contribution is checked.

.. workflow:: Execute Feature Work Product Reviews
   :id: WF_EXE_FeatWP_Review
   :status: draft
   :tags: quality_management
   :responsible: RL_committer
   :approver: RL_quality_manager
   :supporter: RL_technical_lead
   :input: WP_QMS, WP_PROCESS_DEFINITION
   :output: WP_PLATFORM_SW_VERIFICATION_REPORT

   | The quality of the work products is assured.

.. workflow:: Consult and Execute Quality Trainings
   :id: WF_CONSULT_EXE_QLY_TRAINING
   :status: draft
   :tags: quality_management
   :responsible: RL_committer
   :approver: RL_quality_manager
   :supporter: RL_technical_lead
   :input: WP_QMS, WP_POLICIES, WP_PROCESS_DEFINITION
   :output: WP_TRAINING_PATH

   | The quality manager consults all project/platform stakeholder for quality topics and executes regulary quality trainings.

.. workflow:: Monitor/Improve Quality Activities
   :id: WF_MR_IMP_QLM_PLAN_PROCESSES
   :status: draft
   :tags: quality_management
   :responsible: RL_committer
   :approver: RL_quality_manager
   :supporter: RL_technical_lead
   :input: WP_QMS, WP_PLATFORM_SW_RELEASE_NOTE, WP_MODULE_SW_RELEASE_NOTE, WP_PROCESS_IMPR_REPORT, WP_QMS_REPORT, WP_PLATFORM_SW_VERIFICATION_REPORT, WP_MODULE_SW_VERIFICATION_REPORT, WP_TRAINING_PATH
   :output: WP_ISSUE_TRACK_SYSTEM

   | The Quality Manager is responsible for the monitoring of the activities against the quality management plan.
   | The Quality Manager is responsible to adjust the plan, if deviations are detected.

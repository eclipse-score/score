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
   :id: wf_cr_mt_qlm_plan
   :status: draft
   :tags: quality_management
   :responsible: rl_committer
   :approved_by: rl_quality_manager
   :supported_by: rl_technical_lead
   :input: wp_policies, wp_issue_track_system
   :output: wp_qms

   | The quality plan is created and maintained by a :need:`rl_committer`.

.. workflow:: Verify/Approve Platform Release
   :id: wf_vy_ap_pltrelease
   :status: draft
   :tags: quality_management
   :responsible: rl_committer
   :approved_by: rl_quality_manager
   :supported_by: rl_technical_lead
   :input: wp_qms
   :output: wp_platform_sw_release_note

   | The project/platform release is verified and approved.

.. workflow:: Execute Platform Process Audit
   :id: wf_exe_pltprocess_audit
   :status: draft
   :tags: quality_management
   :responsible: rl_quality_manager
   :approved_by: rl_technical_lead
   :supported_by: rl_safety_manager, rl_security_manager
   :input: wp_qms, wp_process_definition
   :output: wp_process_impr_report

   | The project/platform processes are audited.

.. workflow:: Execute Feature Process Compliance Checks
   :id: wf_exe_featprocess_compliance_checks
   :status: draft
   :tags: quality_management
   :responsible: rl_committer
   :approved_by: rl_quality_manager
   :supported_by: rl_technical_lead
   :input: wp_qms, wp_feat_request, wp_process_definition
   :output: wp_qms_report

   | The compliance of the feature contribution is checked.

.. workflow:: Execute Feature Work Product Reviews
   :id: wf_exe_featwp_review
   :status: draft
   :tags: quality_management
   :responsible: rl_committer
   :approved_by: rl_quality_manager
   :supported_by: rl_technical_lead
   :input: wp_qms, wp_process_definition
   :output: wp_platform_sw_verification_report

   | The quality of the work products is assured.

.. workflow:: Consult and Execute Quality Trainings
   :id: wf_consult_exe_qly_training
   :status: draft
   :tags: quality_management
   :responsible: rl_committer
   :approved_by: rl_quality_manager
   :supported_by: rl_technical_lead
   :input: wp_qms, wp_policies, wp_process_definition
   :output: wp_training_path

   | The quality manager consults all project/platform stakeholder for quality topics and executes regulary quality trainings.

.. workflow:: Monitor/Improve Quality Activities
   :id: wf_mr_imp_qlm_plan_processes
   :status: draft
   :tags: quality_management
   :responsible: rl_committer
   :approved_by: rl_quality_manager
   :supported_by: rl_technical_lead
   :input: wp_qms, wp_platform_sw_release_note, wp_module_sw_release_note, wp_process_impr_report, wp_qms_report, wp_platform_sw_verification_report, wp_module_sw_verification_report, wp_training_path
   :output: wp_issue_track_system

   | The Quality Manager is responsible for the monitoring of the activities against the quality management plan.
   | The Quality Manager is responsible to adjust the plan, if deviations are detected.

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

.. _quality_workflows:

Workflows
---------

todo: need to add guidance and standard links

.. workflow:: Create/Maintain Quality Plan
   :id: wf__cr_mt_qlm_plan
   :status: draft
   :responsible: rl__committer
   :approved_by: rl__quality_manager
   :supported_by: rl__technical_lead
   :input: wp__policies, wp__issue_track_system
   :output: wp__qms_plan
   :contains: gd_guidl__qlm_plan_definitions, gd_temp__qlm_plan
   :has: doc_concept__quality__process, doc_getstrt__quality__process

   | The quality plan is created and maintained by a :need:`rl__committer`.

.. workflow:: Verify/Approve Platform Release
   :id: wf__vy_ap_pltrelease
   :status: draft
   :responsible: rl__committer
   :approved_by: rl__quality_manager
   :supported_by: rl__technical_lead
   :input: wp__qms_plan
   :output: wp__platform_sw_release_note

   | The project/platform release is verified and approved.

.. workflow:: Execute Platform Process Audit
   :id: wf__exe_pltprocess_audit
   :status: draft
   :responsible: rl__quality_manager
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager, rl__security_manager
   :input: wp__qms_plan, wp__process_definition
   :output: wp__process_impr_report

   | The project/platform processes are audited.

.. workflow:: Execute Feature Process Compliance Checks
   :id: wf__exe_featprocess_compliance_checks
   :status: draft
   :responsible: rl__committer
   :approved_by: rl__quality_manager
   :supported_by: rl__technical_lead
   :input: wp__qms_plan, wp__feat_request, wp__process_definition
   :output: wp__qms_report

   | The compliance of the feature contribution is checked.

.. workflow:: Execute Feature Work Product Reviews
   :id: wf__exe_featwp_review
   :status: draft
   :responsible: rl__committer
   :approved_by: rl__quality_manager
   :supported_by: rl__technical_lead
   :input: wp__qms_plan, wp__process_definition
   :output: wp__verification__platform_ver_report

   | The quality of the work products is assured.

.. workflow:: Consult and Execute Quality Trainings
   :id: wf__consult_exe_qly_training
   :status: draft
   :responsible: rl__committer
   :approved_by: rl__quality_manager
   :supported_by: rl__technical_lead
   :input: wp__qms_plan, wp__policies, wp__process_definition
   :output: wp__training_path

   | The quality manager consults all project/platform stakeholder for quality topics and executes regulary quality trainings.

.. workflow:: Monitor/Improve Quality Activities
   :id: wf__mr_imp_qlm_plan_processes
   :status: draft
   :responsible: rl__committer
   :approved_by: rl__quality_manager
   :supported_by: rl__technical_lead
   :input: wp__qms_plan, wp__platform_sw_release_note, wp__module_sw_release_note, wp__process_impr_report, wp__qms_report, wp__verification__platform_ver_report, wp__verification__module_ver_report, wp__training_path
   :output: wp__issue_track_system

   | The Quality Manager is responsible for the monitoring of the activities against the quality management plan.
   | The Quality Manager is responsible to adjust the plan, if deviations are detected.

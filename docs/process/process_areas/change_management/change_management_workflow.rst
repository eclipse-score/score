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


Workflow Change Management
##########################

.. workflow:: Create/Analyze Change Request
   :id: wf__change__cr_an_change_request
   :status: valid
   :tags: change_management
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__technical_lead, rl__module_lead
   :input: wp__policies, wp__issue_track_system, wp__feat_request, wp__cmpt_request
   :output: wp__issue_track_system, wp__feat_request, wp__cmpt_request
   :contains: gd_guidl__change__change_request, gd_temp__change__feature_request, gd_temp__change__component_request, gd_temp__change__impact_analysis, gd_temp__component_classification, gd_req__change__attr_uid, gd_req__change__attr_status, gd_req__change__attr_title, gd_req__change__attr_impact_description, gd_req__change__attr_impact_safety, gd_req__change__attr_impact_security, gd_req__change__attr_types, gd_req__change__attr_affected_wp, gd_req__change__attr_milestone, gd_req__change_tool_impact_analysis
   :has: doc_concept__change__process, doc_getstrt__change__process

   The Change Request is created and analyzed.

   The Change Request must be filled out based on existing templates, including affected work
   products, impact on functional safety and security, schedule, risk resources and verification
   measures.

   All affected work products are traced.

   Until the template is not filled out properly, the Change Request may be kept in “draft” from
   the [Committer (rl__committer)]. The possible outcome is either a Change Request with status
   “draft” or “in review”.

.. workflow:: Review/Approve Change Request
   :id: wf__change__rv_ap_change_request
   :status: valid
   :tags: change_management
   :responsible: rl__committer
   :approved_by: rl__technical_lead, rl__module_lead
   :supported_by: rl__safety_manager, rl__security_manager, rl__quality_manager
   :input: wp__issue_track_system, wp__feat_request, wp__cmpt_request
   :output: wp__issue_track_system, wp__feat_request, wp__cmpt_request
   :contains: gd_guidl__change__change_request, gd_temp__change__feature_request, gd_temp__change__component_request, gd_temp__change__impact_analysis, gd_temp__component_classification, gd_req__change__attr_uid, gd_req__change__attr_status, gd_req__change__attr_title, gd_req__change__attr_impact_description, gd_req__change__attr_impact_safety, gd_req__change__attr_impact_security, gd_req__change__attr_types, gd_req__change__attr_affected_wp, gd_req__change__attr_milestone, gd_req__change_tool_impact_analysis
   :has: doc_concept__change__process, doc_getstrt__change__process

   The Change Request is evaluated based on the analysis result either approved, rejected or delayed.

   The Change Request is implemented and verified. The defined verification measures must be
   available and pass.

   The final approval is done by the [Technical Lead (rl__technical_lead)] or the
   [Module Project Lead (rl__module_lead)] dependent on the scope.

   The possible outcome is either a Change Request with status “accepted” or “rejected” or kept
   "in review".

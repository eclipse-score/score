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

.. workflow:: Create/Discuss Change Request
   :id: wf__change__cr_dc_change_request
   :status: valid
   :tags: change_management
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__technical_lead, rl__module_lead
   :input: wp__policies, wp__issue_track_system, wp__feat_request
   :output: wp__issue_track_system, wp__feat_request
   :contains: gd_guidl__change__change_request, gd_temp__change__feature_request, gd_temp__component_classification, gd_req__change__attr_uid
   :has: doc_concept__change__process, doc_getstrt__change__process

   The change request is created and discussed.
   The change request must be filled out based on existing templates.
   Until the template is not filled out properly, the change request may be kept in “draft” from the [Committer (rl__committer)].
   The possible outcome is either a change request with status “draft” or “in review”.

.. workflow:: Review/Approve Change Request
   :id: wf__change__rv_ap_change_request
   :status: valid
   :tags: change_management
   :responsible: rl__committer
   :approved_by: rl__technical_lead, rl__module_lead
   :supported_by: rl__safety_manager, rl__security_manager, rl__quality_manager
   :input: wp__issue_track_system, wp__feat_request
   :output: wp__issue_track_system, wp__feat_request
   :contains: gd_guidl__change__change_request, gd_temp__change__feature_request, gd_temp__component_classification,
   :has: doc_concept__change__process, doc_getstrt__change__process

   The change request is reviewed and approved.
   The final approval is done by the [Technical Lead (rl__technical_lead)] or the [Module Project Lead (rl__module_lead)] dependent on scope.
   The possible outcome is either a change request with status “accepted” or “rejected”.
   Only if the request is accepted, it will be implemented.

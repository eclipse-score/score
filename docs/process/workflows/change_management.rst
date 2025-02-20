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

Change Management
=================


Workflows
---------

todo: need to add standard links

.. workflow:: Create/Discuss Change request
   :id: wf_cr_dc_changerequest
   :status: valid
   :tags: change_management
   :responsible: rl_contributor
   :approved_by: rl_committer
   :supported_by: rl_technical_lead, rl_module_lead
   :input: wp_policies, wp_issue_track_system
   :output: wp_feat_request, wp_issue_track_system
   :contains: gd_guidl__contr_request_guideline, gd_guidl__pull_request_guideline, gd_guidl__issue_guideline

   | The change/contribution request is created and discussed.
   | The request must be filled out based on the existing templates.
   | The possible outcome is a contribution request from type change.
   | Until the template is not filled out properly, the change request may be kept in "Draft" from the :need:`rl_committer`.
   | The possible outcome is either a change request with status "Draft" or "In Review".


.. workflow:: Review/Approve Change request
   :id: wf_rv_ap_changerequest
   :status: valid
   :tags: change_management
   :responsible: rl_committer
   :approved_by: rl_technical_lead, rl_module_lead
   :supported_by: rl_safety_manager, rl_security_manager, rl_quality_manager
   :input: wp_feat_request, wp_issue_track_system
   :output: wp_feat_request, wp_issue_track_system
   :contains: gd_guidl__contr_request_guideline, gd_guidl__pull_request_guideline, gd_guidl__issue_guideline

   | The change/contribution request is reviewed and approved.
   | The final approval is done by the :need:`rl_technical_lead` or the :need:`rl_module_lead` dependent on scope.
   | The possible outcome is either a change request with status "Accepted" or "Rejected".
   | Only if the request is accepted, it will be merged.

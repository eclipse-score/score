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
   :id: WF_CR_DC_ChangeRequest
   :status: valid
   :tags: change_management
   :responsible: RL_contributor
   :approver: RL_committer
   :supporter: RL_technical_lead, RL_module_lead
   :input: WP_POLICIES, WP_ISSUE_TRACK_SYSTEM
   :output: WP_FEAT_REQUEST, WP_ISSUE_TRACK_SYSTEM
   :guidance: GD_GUIDL__Contr_Request_Guideline, GD_GUIDL__Pull_Request_Guideline, GD_GUIDL__Issue_Guideline

   | The change/contribution request is created and discussed.
   | The request must be filled out based on the existing templates.
   | The possible outcome is a contribution request from type change.
   | Until the template is not filled out properly, the change request may be kept in "Draft" from the :need:`RL_committer`.
   | The possible outcome is either a change request with status "Draft" or "In Review".


.. workflow:: Review/Approve Change request
   :id: WF_RV_AP_ChangeRequest
   :status: valid
   :tags: change_management
   :responsible: RL_committer
   :approver: RL_technical_lead, RL_module_lead
   :supporter: RL_safety_manager, RL_security_manager, RL_quality_manager
   :input: WP_FEAT_REQUEST, WP_ISSUE_TRACK_SYSTEM
   :output: WP_FEAT_REQUEST, WP_ISSUE_TRACK_SYSTEM
   :guidance: GD_GUIDL__Contr_Request_Guideline, GD_GUIDL__Pull_Request_Guideline, GD_GUIDL__Issue_Guideline

   | The change/contribution request is reviewed and approved.
   | The final approval is done by the :need:`RL_technical_lead` or the :need:`RL_module_lead` dependent on scope.
   | The possible outcome is either a change request with status "Accepted" or "Rejected".
   | Only if the request is accepted, it will be merged.

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
   :id: wf__cr_dc_changerequest
   :status: valid
   :tags: change_management
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__technical_lead, rl__module_lead
   :input: wp__policies, wp__issue_track_system
   :output: wp__feat_request, wp__issue_track_system
   :contains: gd_guidl__contr_request_guideline, gd_guidl__pull_request_guideline, gd_guidl__issue_guideline

   | The change/contribution request is created and discussed.
   | The request must be filled out based on the existing templates.
   | The possible outcome is a contribution request from type change.
   | Until the template is not filled out properly, the change request may be kept in "Draft" from the :need:`rl__committer`.
   | The possible outcome is either a change request with status "Draft" or "In Review".


.. workflow:: Review/Approve Change request
   :id: wf__rv_ap_changerequest
   :status: valid
   :tags: change_management
   :responsible: rl__committer
   :approved_by: rl__technical_lead, rl__module_lead
   :supported_by: rl__safety_manager, rl__security_manager, rl__quality_manager
   :input: wp__feat_request, wp__issue_track_system
   :output: wp__feat_request, wp__issue_track_system
   :contains: gd_guidl__contr_request_guideline, gd_guidl__pull_request_guideline, gd_guidl__issue_guideline

   | The change/contribution request is reviewed and approved.
   | The final approval is done by the :need:`rl__technical_lead` or the :need:`rl__module_lead` dependent on scope.
   | The possible outcome is either a change request with status "Accepted" or "Rejected".
   | Only if the request is accepted, it will be merged.

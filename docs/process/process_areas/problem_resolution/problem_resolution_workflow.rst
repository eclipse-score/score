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


Workflow Problem Resolution
###########################

.. workflow:: Create/Analyze Problem
   :id: wf__problem__cr_an_problem
   :status: valid
   :tags: problem_resolution
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__technical_lead, rl__module_lead, rl__safety_manager, rl__security_manager, rl__quality_manager
   :input: wp__issue_track_system, wp__prm_plan
   :output: wp__issue_track_system
   :contains: gd_temp__problem__template, gd_chklst__problem__cr_review, gd_guidl__problem__problem, gd_req__problem__attr_uid
   :has: doc_concept__problem__process, doc_getstrt__problem__process

   The Problem is created.

   For creating the Problem template must be used.

   To start review and analyis the Problem status is changed to "in review". Until the template is
   not filled out properly, the Problem may be set back to “open” from the
   [Committer (rl__committer)].

   If the problem shall be resolved, the Problem status is set to "in implementation", Otherwise
   to "rejected".

   The [Contributor (rl__contributor)] may cancel it, thus the status is set to "cancelled".

.. workflow:: Initiate/Monitor Problem resolution
   :id: wf__problem__ini_mon_problem
   :status: valid
   :tags: problem_resolution
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__technical_lead, rl__module_lead, rl__safety_manager, rl__security_manager, rl__quality_manager
   :input: wp__issue_track_system
   :output: wp__issue_track_system
   :contains: gd_temp__problem__template, gd_chklst__problem__cr_review, gd_guidl__problem__problem, gd_req__problem__attr_uid
   :has: doc_concept__problem__process, doc_getstrt__problem__process

   The Problem resolution is implemented.

   This may require Change Requests or other activities, inlcuding creating ISSUEs and PRs.
   These are linked to the Problem and monitored until closure.

   The problem resoultion is done, if all linked activities has been closed. Then the Problem
   status is set to "closed."

   The [Comitter (rl__committer)] may still reject it, thus the status is set to "rejected".

   The [Contributor (rl__contributor)] may cancel it, thus the status is set to "cancelled".

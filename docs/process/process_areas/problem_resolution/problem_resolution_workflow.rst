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

.. workflow:: Create Problem Report
   :id: wf__problem__create_pr
   :status: valid
   :tags: problem_resolution, wf
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__technical_lead, rl__module_lead, rl__safety_manager, rl__security_manager, rl__quality_manager
   :input: wp__issue_track_system, wp__prm_plan
   :output: wp__issue_track_system
   :contains: gd_temp__problem__template, gd_chklst__problem__cr_review, gd_guidl__problem__problem
   :has: doc_concept__problem__process, doc_getstrt__problem__process

   The Problem Report is created.

   For creating the Problem Report template must be used.

   To start the review and the analysis the Problem status is changed to "in review"

.. workflow:: Analyse Problem Report
   :id: wf__problem__analyse_pr
   :status: valid
   :tags: problem_resolution, wf
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__technical_lead, rl__module_lead, rl__safety_manager, rl__security_manager, rl__quality_manager
   :input: wp__issue_track_system, wp__prm_plan
   :output: wp__issue_track_system
   :contains: gd_temp__problem__template, gd_chklst__problem__cr_review, gd_guidl__problem__problem
   :has: doc_concept__problem__process, doc_getstrt__problem__process

   The Problem Report is analysed.

   Until the template is not filled out properly, the Problem may be set back to “open” from the
   :need:`Committer <rl__committer>`.

   If the Problem shall be resolved, the Problem status is set to "in implementation", otherwise
   to "rejected".

   The author of the Problem Report may cancel it, thus the status is set to "rejected".

.. workflow:: Initiate and Monitor Problem Resolution
   :id: wf__problem__initiate_monitor_pr
   :status: valid
   :tags: problem_resolution, wf
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__technical_lead, rl__module_lead, rl__safety_manager, rl__security_manager, rl__quality_manager
   :input: wp__issue_track_system, wp__prm_plan
   :output: wp__issue_track_system
   :contains: gd_temp__problem__template, gd_chklst__problem__cr_review, gd_guidl__problem__problem
   :has: doc_concept__problem__process, doc_getstrt__problem__process

   The Problem Resolution is implemented and monitored.

   This may require Change Requests or other activities, inlcuding creating ISSUEs and PRs.
   These are linked to the Problem and monitored until closure.

   The Problem Resolution is done, if all linked activities has been closed and confirmed.
   Before closing the Problem Resoultion, :need:`Committer <rl__committer>` must check the
   correctness.

   The :need:`Committer <rl__committer>` may still reject it, thus the status is set to "rejected".

   The author of the Problem Report may cancel it, thus the status is set to "rejected".

.. workflow:: Close Problem Resolution
   :id: wf__problem__close_pr
   :status: valid
   :tags: problem_resolution, wf
   :responsible: rl__committer
   :approved_by: rl__technical_lead, rl__module_lead
   :supported_by: rl__safety_manager, rl__security_manager, rl__quality_manager
   :input: wp__issue_track_system, wp__prm_plan
   :output: wp__issue_track_system
   :contains: gd_temp__problem__template, gd_chklst__problem__cr_review, gd_guidl__problem__problem
   :has: doc_concept__problem__process, doc_getstrt__problem__process

   The Problem Resolution is closed.

   The Problem Resolution is closed only, if the implementation is sufficient. That is verified
   by the :need:`Committer <rl__committer>` finally.

   Otherwise the :need:`Committer <rl__committer>` keeps the status "in implementation".


RAS(IC) for Problem Resolution:
*******************************

.. needtable:: RASIC Overview for Problem Resolution
   :tags: problem_resolution
   :filter: "problem_resolution" in tags and "wf" in tags
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30

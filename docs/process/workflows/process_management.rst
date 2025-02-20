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

Process Management
==================


Workflows
---------

todo: need to add guidance and standard links

.. workflow:: Create/Maintain Process Management Strategy
   :id: wf_cr_mt_proc_mgt_strategy
   :status: draft
   :tags: process
   :responsible: rl_process_community
   :approved_by: rl_project_lead
   :supported_by: rl_external_assessor
   :input: wp_policies, wp_issue_track_system
   :output: wp_process_plan

   Process management strategy is created and maintained.
   Process metamodel see :ref:`processes_introduction`.

.. workflow:: Define/Approve Process
   :id: wf_def_app_process_defintion
   :status: draft
   :tags: process
   :responsible: rl_process_community
   :approved_by: rl_technical_lead
   :supported_by: rl_external_assessor
   :input: wp_process_plan, wp_issue_track_system
   :output: wp_process_definition

   Process is defined and approved.

.. workflow:: Monitor/Control Process
   :id: wf_mon_ctrl_process_defintion
   :status: draft
   :tags: process
   :responsible: rl_process_community
   :approved_by: rl_technical_lead
   :supported_by: rl_external_assessor
   :input: wp_process_definition
   :output: wp_process_impr_report

   Process is monitored and improvements are triggered, if required.

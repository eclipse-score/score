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
   :id: wf__cr_mt_proc_mgt_strategy
   :status: draft
   :tags: process
   :responsible: rl__process_community
   :approved_by: rl__project_lead
   :supported_by: rl__external_auditor
   :input: wp__policies, wp__issue_track_system
   :output: wp__process_plan

   Process management strategy is created and maintained.
   Process metamodel see :ref:`processes_introduction`.

.. workflow:: Define/Approve Process
   :id: wf__def_app_process_definition
   :status: draft
   :tags: process
   :responsible: rl__process_community
   :approved_by: rl__technical_lead
   :supported_by: rl__external_auditor
   :input: wp__process_plan, wp__issue_track_system
   :output: wp__process_definition, wp__tailoring

   Process is defined and approved.

.. workflow:: Monitor/Control Process
   :id: wf__mon_ctrl_process_definition
   :status: draft
   :tags: process
   :responsible: rl__process_community
   :approved_by: rl__technical_lead
   :supported_by: rl__external_auditor
   :input: wp__process_definition
   :output: wp__process_impr_report

   Process is monitored and improvements are triggered, if required.

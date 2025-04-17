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

.. _workflow_tlm_requirements:

Workflow Tool Management
########################

.. workflow:: Create Tool Verification Report
   :id: wf__tool__create_tool_verification_report
   :status: valid
   :responsible: rl__infrastructure_tooling_community
   :approved_by: rl__safety_manager
   :supported_by: rl__technical_lead, rl__module_lead, rl__security_manager
   :input: wp__issue_track_system, wp__tlm_plan
   :output: wp__tool_verification
   :contains: gd_temp__tool_management__verif_rpt_template, gd_chklst__tool__cr_review
   :has: doc_concept__tool__process, doc_getstrt__tool__process

   The Tool Verification Report is created during identification of a tool.

   Each identified tool to is evaluated and if applicable, qualified. During evaluation and
   qualification the Tool Verification Report is updated.

   Finally the Tool Verification Report is verified and approved, and thus in Released state.

   For creating the Tool Verification Report template must be used.


.. needextend:: "process_areas/tool_management" in docname
   :+tags: tool_management

RAS(IC) for Tool Management:
****************************

.. needtable:: RASIC Overview for Tool Management
   :tags: tool_management
   :filter: "tool_management" in tags and type == "workflow"
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30

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

Requirements Management
=======================


Workflows
---------

todo: need to add guidance and standard links

.. workflow:: Create/Maintain Stakeholder requirements
   :id: wf_create_maintain_stakeholder_requirements
   :status: valid
   :responsible: rl_contributor
   :approved_by: rl_technical_lead
   :supported_by: rl_safety_manager
   :input: wp_policies, wp_issue_track_system
   :output: wp_stakeholder_req
   :contains: gd_temp__stakeholder_requirements_template, gd_temp__requirement_formulation

   | Stakeholder requirements can be created during a contribution request. Any contributor can create a stakeholder requirement and propose it for approval.

.. workflow:: Create/Maintain Feature requirements
   :id: wf_create_maintain_feature_requirements
   :status: valid
   :tags: requirements_management
   :responsible: rl_contributor
   :approved_by: rl_technical_lead
   :supported_by: rl_safety_manager
   :input: wp_stakeholder_req, wp_issue_track_system, wp_feature_safety_analyses, wp_feature_dfa
   :output: wp_feature_req, wp_feature_aou, wp_platform_sw_safety_manual
   :contains: gd_temp__feature_requirements_template, gd_temp__requirement_formulation

   | Depending on the stakeholder requirements feature requirements can be derived. This can be done by any contributor and will be approved by a contributor. If needed a Safety Manager can provide support.

.. workflow:: Create/Maintain Component requirements
   :id: wf_create_maintain_component_requirements
   :status: valid
   :tags: requirements_management
   :responsible: rl_contributor
   :approved_by: rl_committer
   :supported_by: rl_safety_manager
   :input: wp_feature_req, wp_issue_track_system, wp_sw_component_safety_analyses, wp_sw_component_dfa
   :output: wp_sw_component_req, wp_sw_component_aou, wp_module_sw_safety_manual
   :contains: gd_temp__component_requirements_template, gd_temp__requirement_formulation

   | On the lowest level the component requirements are created and maintained. This can be done by any contributor and will be approved by a committer. If needed a safety manager can provide support.

.. workflow:: Create/Maintain Tool requirements
   :id: wf_create_maintain_tool_requirements
   :status: valid
   :tags: requirements_management
   :responsible: rl_process_community
   :approved_by: rl_infrastructure_tooling_community
   :supported_by: rl_safety_manager
   :input: wp_policies, wp_stakeholder_req, wp_issue_track_system
   :output: wp_tool_req
   :contains: gd_temp__tool_requirements_template, gd_temp__requirement_formulation

   | The tool requirements are created and maintained.

.. workflow:: Monitor/Verify Requirements
   :id: wf_monitor_verify_requirements
   :status: valid
   :tags: requirements_management
   :responsible: rl_committer
   :approved_by: rl_committer
   :supported_by: rl_safety_manager
   :input: wp_stakeholder_req, wp_tool_req, wp_feature_req, wp_sw_component_req, wp_feature_aou, wp_sw_component_aou, wp_platform_sw_safety_manual, wp_module_sw_safety_manual
   :output: wp_issue_track_system, wp_sw_req_inspect

   | The requirements are monitored and verified. The inspection shall be implemented as integral part of the review in GitHub.

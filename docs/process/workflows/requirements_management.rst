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
   :id: wf__create_maintain_stakeholder_requirements
   :status: valid
   :responsible: rl__contributor
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager
   :input: wp__policies, wp__issue_track_system
   :output: wp__stakeholder_req
   :contains: gd_temp__stakeholder_requirements_template, gd_temp__requirement_formulation

   | Stakeholder requirements can be created during a contribution request. Any contributor can create a stakeholder requirement and propose it for approval.

.. workflow:: Create/Maintain Feature requirements
   :id: wf__create_maintain_feature_requirements
   :status: valid
   :tags: requirements_management
   :responsible: rl__contributor
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager
   :input: wp__stakeholder_req, wp__issue_track_system, wp__feature_safety_analyses, wp__feature_dfa
   :output: wp__feature_req, wp__feature_aou, wp__platform_sw_safety_manual
   :contains: gd_temp__feature_requirements_template, gd_temp__requirement_formulation

   | Depending on the stakeholder requirements feature requirements can be derived. This can be done by any contributor and will be approved by a contributor. If needed a Safety Manager can provide support.

.. workflow:: Create/Maintain Component requirements
   :id: wf__create_maintain_component_requirements
   :status: valid
   :tags: requirements_management
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__safety_manager
   :input: wp__feature_req, wp__issue_track_system, wp__sw_component_safety_analyses, wp__sw_component_dfa
   :output: wp__sw_component_req, wp__sw_component_aou, wp__module_sw_safety_manual
   :contains: gd_temp__component_requirements_template, gd_temp__requirement_formulation

   | On the lowest level the component requirements are created and maintained. This can be done by any contributor and will be approved by a committer. If needed a safety manager can provide support.

.. workflow:: Create/Maintain Tool requirements
   :id: wf__create_maintain_tool_requirements
   :status: valid
   :tags: requirements_management
   :responsible: rl__process_community
   :approved_by: rl__infrastructure_tooling_community
   :supported_by: rl__safety_manager
   :input: wp__policies, wp__stakeholder_req, wp__issue_track_system
   :output: wp__tool_req
   :contains: gd_temp__tool_requirements_template, gd_temp__requirement_formulation

   | The tool requirements are created and maintained.

.. workflow:: Monitor/Verify Requirements
   :id: wf__monitor_verify_requirements
   :status: valid
   :tags: requirements_management
   :responsible: rl__committer
   :approved_by: rl__committer
   :supported_by: rl__safety_manager
   :input: wp__stakeholder_req, wp__tool_req, wp__feature_req, wp__sw_component_req, wp__feature_aou, wp__sw_component_aou, wp__platform_sw_safety_manual, wp__module_sw_safety_manual
   :output: wp__issue_track_system, wp__sw_req_inspect

   | The requirements are monitored and verified. The inspection shall be implemented as integral part of the review in GitHub.

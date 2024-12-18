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
   :id: WF_create_maintain_stakeholder_requirements
   :status: valid
   :responsible: RL_contributor
   :approver: RL_technical_lead
   :supporter: RL_safety_manager
   :input: WP_POLICIES, WP_ISSUE_TRACK_SYSTEM
   :output: WP_STAKEHOLDER_REQ
   :guidance: GD_TEMP__stakeholder_requirements_template, GD_TEMP__requirement_formulation

   | Stakeholder requirements can be created during a contribution request. Any contributor can create a stakeholder requirement and propose it for approval.

.. workflow:: Create/Maintain Feature requirements
   :id: WF_create_maintain_feature_requirements
   :status: valid
   :tags: requirements_management
   :responsible: RL_contributor
   :approver: RL_technical_lead
   :supporter: RL_safety_manager
   :input: WP_STAKEHOLDER_REQ, WP_ISSUE_TRACK_SYSTEM, WP_FEATURE_SAFETY_ANALYSES, WP_FEATURE_DFA
   :output: WP_FEATURE_REQ, WP_FEATURE_AOU, WP_PLATFORM_SW_SAFETY_MANUAL
   :guidance: GD_TEMP__feature_requirements_template, GD_TEMP__requirement_formulation

   | Depending on the stakeholder requirements feature requirements can be derived. This can be done by any contributor and will be approved by a contributor. If needed a Safety Manager can provide support.

.. workflow:: Create/Maintain Component requirements
   :id: WF_create_maintain_component_requirements
   :status: valid
   :tags: requirements_management
   :responsible: RL_contributor
   :approver: RL_committer
   :supporter: RL_safety_manager
   :input: WP_FEATURE_REQ, WP_ISSUE_TRACK_SYSTEM, WP_SW_COMPONENT_SAFETY_ANALYSES, WP_SW_COMPONENT_DFA
   :output: WP_SW_COMPONENT_REQ, WP_SW_COMPONENT_AOU, WP_MODULE_SW_SAFETY_MANUAL
   :guidance: GD_TEMP__component_requirements_template, GD_TEMP__requirement_formulation

   | On the lowest level the component requirements are created and maintained. This can be done by any contributor and will be approved by a committer. If needed a safety manager can provide support.

.. workflow:: Create/Maintain Tool requirements
   :id: WF_create_maintain_tool_requirements
   :status: valid
   :tags: requirements_management
   :responsible: RL_process_community
   :approver: RL_infrastructure_tooling_community
   :supporter: RL_safety_manager
   :input: WP_POLICIES, WP_STAKEHOLDER_REQ, WP_ISSUE_TRACK_SYSTEM
   :output: WP_TOOL_REQ
   :guidance: GD_TEMP__tool_requirements_template, GD_TEMP__requirement_formulation

   | The tool requirements are created and maintained.

.. workflow:: Monitor/Verify Requirements
   :id: WF_monitor_verify_requirements
   :status: valid
   :tags: requirements_management
   :responsible: RL_committer
   :approver: RL_committer
   :supporter: RL_safety_manager
   :input: WP_STAKEHOLDER_REQ, WP_TOOL_REQ, WP_FEATURE_REQ, WP_SW_COMPONENT_REQ, WP_FEATURE_AOU, WP_SW_COMPONENT_AOU, WP_PLATFORM_SW_SAFETY_MANUAL, WP_MODULE_SW_SAFETY_MANUAL
   :output: WP_ISSUE_TRACK_SYSTEM, WP_SW_REQ_INSPECT

   | The requirements are monitored and verified. The inspection shall be implemented as integral part of the review in GitHub.

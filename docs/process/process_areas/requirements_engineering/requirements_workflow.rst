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


Workflow Requirements Engineering
#################################

.. workflow:: Create/Maintain Stakeholder requirements
   :id: WF__req__stkh_req
   :status: valid
   :tags: requirements_engineering
   :responsible: RL_contributor
   :approved_by: RL_technical_lead
   :supported_by: RL_safety_manager
   :input: WP_POLICIES, WP_ISSUE_TRACK_SYSTEM
   :output: wp__requirements__stkh
   :contains: GD_TEMP__req__stkh_req, GD_TEMP__req__formulation, GD_REQ__req__linkage, GD_REQ__req__attr_impl, GD_REQ__req__attr_testlink, GD_REQ__req__attr_hash, GD_REQ__req__linkage_fulfill, GD_REQ__req__linkage_architecture, GD_REQ__req__linkage_safety, GD_REQ__req__attr_mandatory
   :has: DOC_CONCEPT__req__process, DOC_GETSTRT__req__process

   Stakeholder requirements can be created during a contribution request. Any contributor can create a stakeholder requirement and propose it for approval.

.. workflow:: Create/Maintain Feature requirements
   :id: WF__req__feat_req
   :status: valid
   :responsible: RL_contributor
   :approved_by: RL_technical_lead
   :supported_by: RL_safety_manager
   :input: wp__requirements__stkh, WP_ISSUE_TRACK_SYSTEM, WP_FEATURE_SAFETY_ANALYSES, WP_FEATURE_DFA
   :output: wp__requirements__feat, wp__requirements__feat_aou, WP_PLATFORM_SW_SAFETY_MANUAL
   :contains: GD_TEMP__req__feat_req, GD_TEMP__req__formulation, GD_REQ__req__linkage, GD_REQ__req__attr_impl, GD_REQ__req__attr_testlink, GD_REQ__req__attr_hash, GD_REQ__req__linkage_fulfill, GD_REQ__req__linkage_architecture, GD_REQ__req__linkage_safety, GD_REQ__req__attr_mandatory
   :has: DOC_CONCEPT__req__process, DOC_GETSTRT__req__process

   Depending on the stakeholder requirements feature requirements can be derived. This can be done by any contributor and will be approved by a contributor. If needed a Safety Manager can provide support.


.. workflow:: Create/Maintain Component requirements
   :id: WF_create_maintain_component_requirements
   :status: valid
   :tags: requirements_engineering
   :responsible: RL_contributor
   :approved_by: RL_committer
   :supported_by: RL_safety_manager
   :input: wp__requirements__feat, WP_ISSUE_TRACK_SYSTEM, WP_SW_COMPONENT_SAFETY_ANALYSES, WP_SW_COMPONENT_DFA
   :output: wp__requirements__comp, wp__requirements__comp_aou, WP_MODULE_SW_SAFETY_MANUAL
   :contains: GD_TEMP__req__comp_req, GD_TEMP__req__formulation, GD_REQ__req__linkage, GD_REQ__req__attr_impl, GD_REQ__req__attr_testlink, GD_REQ__req__attr_hash, GD_REQ__req__linkage_fulfill, GD_REQ__req__linkage_architecture, GD_REQ__req__linkage_safety, GD_REQ__req__attr_mandatory
   :has: DOC_CONCEPT__req__process, DOC_GETSTRT__req__process

   On the lowest level the component requirements are created and maintained. This can be done by any contributor and will be approved by a committer. If needed a safety manager can provide support.

.. workflow:: Monitor/Verify Requirements
   :id: WF_monitor_verify_requirements
   :status: valid
   :tags: requirements_engineering
   :responsible: RL_committer
   :approved_by: RL_committer
   :supported_by: RL_safety_manager
   :input: wp__requirements__stkh, wp__requirements__feat, wp__requirements__comp, wp__requirements__feat_aou, wp__requirements__comp_aou, WP_PLATFORM_SW_SAFETY_MANUAL, WP_MODULE_SW_SAFETY_MANUAL
   :output: WP_ISSUE_TRACK_SYSTEM, WP_SW_REQ_INSPECT
   :contains: GD_CHKLST__req__inspection

   The requirements are monitored and verified. The inspection shall be implemented as integral part of the review in GitHub.

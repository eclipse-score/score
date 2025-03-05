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
   :id: wf__req__stkh_req
   :status: valid
   :tags: requirements_engineering
   :responsible: rl__contributor
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager
   :input: wp__policies, wp__issue_track_system
   :output: wp__requirements__stkh
   :contains: gd_temp__req__stkh_req, gd_temp__req__formulation
   :has: doc_concept__req__process, doc_concept__req__process

   Stakeholder requirements can be created during a contribution request. Any contributor can create a stakeholder requirement and propose it for approval.

.. workflow:: Create/Maintain Feature requirements
   :id: wf__req__feat_req
   :status: valid
   :tags: requirements_engineering
   :responsible: rl__contributor
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager, rl__security_manager
   :input: wp__requirements__stkh, wp__issue_track_system, wp__feature_safety_analyses, wp__feature_dfa
   :output: wp__requirements__feat, wp__requirements__feat_aou, wp__platform_safety_manual
   :contains: gd_temp__req__feat_req, gd_temp__req__formulation
   :has: doc_concept__req__process, doc_concept__req__process

   Depending on the stakeholder requirements feature requirements can be derived. This can be done by any contributor and will be approved by a contributor. If needed safety and security managers can provide support.


.. workflow:: Create/Maintain Component requirements
   :id: wf__req__comp_req
   :status: valid
   :tags: requirements_engineering
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__safety_manager, rl__security_manager
   :input: wp__requirements__feat, wp__issue_track_system, wp__sw_component_safety_analyses, wp__sw_component_dfa
   :output: wp__requirements__comp, wp__requirements__comp_aou, wp__platform_safety_manual
   :contains: gd_temp__req__comp_req, gd_temp__req__formulation
   :has: doc_concept__req__process, doc_concept__req__process

   On the lowest level the component requirements are created and maintained. This can be done by any contributor and will be approved by a committer. If needed safety and security managers can provide support.

.. workflow:: Monitor/Verify Requirements
   :id: wf__monitor_verify_requirements
   :status: valid
   :tags: requirements_engineering
   :responsible: rl__committer
   :approved_by: rl__committer
   :supported_by: rl__safety_manager
   :input: wp__requirements__stkh, wp__requirements__feat, wp__requirements__comp, wp__requirements__feat_aou, wp__requirements__comp_aou, wp__platform_safety_manual, wp__module_safety_manual
   :output: wp__issue_track_system, wp__requirements__inspect
   :contains: gd_chklst__req__inspection

   The requirements are monitored and verified. The inspection shall be implemented as integral part of the review in GitHub.

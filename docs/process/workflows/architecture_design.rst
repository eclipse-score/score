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

Architecture Design
===================


Workflows
---------

todo: need to add guidance and standard links

.. workflow:: Create/Maintain Feature architecture
   :id: WF_CR_MT_FeatArch
   :status: valid
   :tags: architecture_design
   :responsible: RL_contributor
   :approved_by: RL_committer
   :supported_by: RL_safety_manager, RL_security_manager
   :input: WP_FEATURE_REQ, WP_ISSUE_TRACK_SYSTEM
   :output: WP_FEATURE_ARCHITECTURE

   | The feature architectures are created and maintained.

.. workflow:: Create/Maintain Components architecture
   :id: WF_CR_MT_CompArch
   :status: invalid
   :tags: architecture_design
   :responsible: RL_contributor
   :approved_by: RL_committer
   :supported_by: RL_safety_manager, RL_security_manager
   :input: WP_FEATURE_ARCHITECTURE, WP_SW_COMPONENT_REQ, WP_ISSUE_TRACK_SYSTEM
   :output: WP_SW_COMPONENT_ARCHITECTURE

   | The component architectures are created and maintained.

.. workflow:: Monitor/Verify Architecture
   :id: WF_MR_VY_Arch
   :status: valid
   :tags: architecture_design
   :responsible: RL_contributor
   :approved_by: RL_committer
   :supported_by: RL_safety_manager, RL_security_manager
   :input: WP_FEATURE_ARCHITECTURE, WP_SW_COMPONENT_ARCHITECTURE
   :output: WP_ISSUE_TRACK_SYSTEM, WP_SW_ARCH_VERIFICATION

   | The architecture designs are monitored and verified.
   | The inspection shall be implemented as integral part of the review in GitHub.

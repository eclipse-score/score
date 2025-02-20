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
   :id: wf_cr_mt_featarch
   :status: valid
   :tags: architecture_design
   :responsible: rl_contributor
   :approved_by: rl_committer
   :supported_by: rl_safety_manager, rl_security_manager
   :input: wp_feature_req, wp_issue_track_system
   :output: wp_feature_architecture

   | The feature architectures are created and maintained.

.. workflow:: Create/Maintain Components architecture
   :id: wf_cr_mt_comparch
   :status: invalid
   :tags: architecture_design
   :responsible: rl_contributor
   :approved_by: rl_committer
   :supported_by: rl_safety_manager, rl_security_manager
   :input: wp_feature_architecture, wp_sw_component_req, wp_issue_track_system
   :output: wp_sw_component_architecture

   | The component architectures are created and maintained.

.. workflow:: Monitor/Verify Architecture
   :id: wf_mr_vy_arch
   :status: valid
   :tags: architecture_design
   :responsible: rl_contributor
   :approved_by: rl_committer
   :supported_by: rl_safety_manager, rl_security_manager
   :input: wp_feature_architecture, wp_sw_component_architecture
   :output: wp_issue_track_system, wp_sw_arch_verification

   | The architecture designs are monitored and verified.
   | The inspection shall be implemented as integral part of the review in GitHub.

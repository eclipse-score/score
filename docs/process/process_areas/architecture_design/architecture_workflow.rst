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

.. _arch_workflow:

Architecture Workflow
=====================

.. workflow:: Create/Maintain Feature architecture
   :id: wf__cr_mt_featarch
   :status: valid
   :tags: architecture_design
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__safety_manager, rl__security_manager
   :input: wp__requirements__feat, wp__issue_track_system
   :output: wp__feature_arch
   :contains: gd_guidl__arch__design, gd_chklst__arch__inspection_checklist, gd_temp__arch__feature, gd_temp__arch__comp
   :has: doc_concept__arch__process, doc_getstrt__arch__process

   The feature architectures are created and maintained.

.. workflow:: Create/Maintain Components architecture
   :id: wf__cr_mt_comparch
   :status: valid
   :tags: architecture_design
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__safety_manager, rl__security_manager
   :input: wp__feature_arch, wp__requirements__comp, wp__issue_track_system
   :output: wp__component_arch
   :contains: gd_guidl__arch__design, gd_chklst__arch__inspection_checklist, gd_temp__arch__feature, gd_temp__arch__comp
   :has: doc_concept__arch__process, doc_getstrt__arch__process

   The component architectures are created and maintained.

.. workflow:: Monitor/Verify Architecture
   :id: wf__mr_vy_arch
   :status: valid
   :tags: architecture_design
   :responsible: rl__committer
   :approved_by: rl__committer
   :supported_by: rl__safety_manager, rl__security_manager
   :input: wp__feature_arch, wp__component_arch
   :output: wp__issue_track_system, wp__sw_arch_verification
   :contains: gd_guidl__arch__design, gd_chklst__arch__inspection_checklist, gd_temp__arch__comp
   :has: doc_concept__arch__process, doc_getstrt__arch__process

   The architecture designs are monitored and verified.

   The inspection shall be implemented as integral part of the review in GitHub.

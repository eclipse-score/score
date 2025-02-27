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

Workflow Verification
#####################

.. workflow:: Create Component Test
   :id: wf__verification__comp_test
   :status: valid
   :tags: verification
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__safety_manager
   :input: wp__requirements__comp, wp__requirements__comp_aou, wp__sw_component_architecture, wp__verification__plan, wp__verification__specification
   :output: wp__requirements__stkh
   :contains: gd_req__link_tests
   :has: doc_concept__req__process, doc_concept__req__process

   Component test cases are based on component requirements.
   Any contributor can create a component test and create a PR for it.
   During the review process the test cases will be approved by a committer.
   Committer and contributor need to differ.

``[TODO: Additional workflows to be added]``

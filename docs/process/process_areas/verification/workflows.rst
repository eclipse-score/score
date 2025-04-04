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

.. _verification_workflows:

Workflow Verification
#####################

.. workflow:: Create/Perform Unit Test
   :id: wf__verification__unit_test
   :status: valid
   :tags: implementation
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__safety_manager
   :input: wp__sw_implementation, wp__verification__plan
   :output: wp__verification__sw_unit_test
   :has: doc_concept__verification__process, doc_getstrt__verification__process,
         doc_concept__imp__concept, doc_getstrt__imp__getstrt

   Every Unit shall have at least one Unit Test. They verify the detailed design of the implementation.
   Unit tests are automatically executed as part of the CI after PR merge.
   In case of changes at inputs, the workflow need to be executed again as part of maintenance.
   Any contributor can create a component test and create a PR for it.
   During the review process the test cases will be approved by a committer.
   Committer and contributor need to differ.
   The actual :need:`rl__committer` of the implementation can also be the creator of the unit tests.
   Independence is achieved by different approver at PRs and by the :need:`wp__verification__module_ver_report`.

.. workflow:: Create/Maintain Component Integration Test
   :id: wf__verification__comp_int_test
   :status: valid
   :tags: verification
   :responsible: rl__contributor
   :approved_by: rl__committer, rl__testing_community
   :supported_by: rl__safety_manager
   :input: wp__component_arch, wp__sw_implementation, wp__requirements__comp, wp__requirements__comp_aou, wp__verification__plan
   :output: wp__verification__comp_int_test
   :contains: gd_req__link_tests, gd_guidl__verification_specification
   :has: doc_concept__verification__process, doc_getstrt__verification__process

   Component Integration test cases are based on component architecture and component requirements.
   They may optionally cover the detailed design of implementation as an optional element where units are seen complex.
   Any contributor can create a component integration test and create a PR for it.
   During the review process the test cases will be approved by a committer.
   Committer and contributor need to differ.
   The tests are automatically executed as part of the CI after PR merge.
   In case of changes at inputs, the workflow need to be executed again as part of maintenance.


.. workflow:: Create/Maintain Feature Integration Test
   :id: wf__verification__feat_int_test
   :status: valid
   :tags: verification
   :responsible: rl__contributor
   :approved_by: rl__committer, rl__testing_community
   :supported_by: rl__safety_manager
   :input: wp__feature_arch, wp__requirements__feat, wp__requirements__feat_aou,
           wp__verification__plan
   :output: wp__verification__feat_int_test
   :contains: gd_req__link_tests, gd_guidl__verification_specification
   :has: doc_concept__verification__process, doc_getstrt__verification__process

   Feature Integration test cases are based on feature requirements and architecture of a specific feature.
   Any contributor can create a feature integration test and create a PR for it.
   During the review process the test cases will be approved by a committer.
   Committer and contributor need to differ.
   The tests are automatically executed as part of the CI after PR merge.
   In case of changes at inputs, the workflow need to be executed again as part of maintenance.

.. workflow:: Create/Maintain Platform Test
   :id: wf__verification__platform_test
   :status: valid
   :tags: verification
   :responsible: rl__contributor
   :approved_by: rl__committer, rl__testing_community
   :supported_by: rl__safety_manager
   :input: wp__requirements__stkh, wp__verification__plan
   :output: wp__verification__platform_test
   :contains: gd_req__link_tests, gd_guidl__verification_specification
   :has: doc_concept__verification__process, doc_getstrt__verification__process

   Platform test cases are based on Stakeholder requirements. This is the highest test level.
   Any contributor can create a platform test and create a PR for it.
   During the review process the test cases will be approved by a committer.
   Committer and contributor need to differ.
   The tests are automatically executed as part of the CI after PR merge.
   In case of changes at inputs, the workflow need to be executed again as part of maintenance.

.. workflow:: Create Verification Plan
   :id: wf__verification__plan
   :status: valid
   :tags: verification
   :responsible: rl__committer, rl__testing_community
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager, rl__infrastructure_tooling_community
   :input: wp__requirements__stkh, wp__platform_mgmt, wp__tool_verification
   :output: wp__verification__plan
   :contains: gd_guidl__verification_guide, gd_temp__verification__plan
   :has: doc_concept__verification__process, doc_getstrt__verification__process

   The verification plan is created by :need:`rl__committer`. It clearly
   outlines all aspects of the verification activities, provide a roadmap for the verification
   efforts throughout the software development lifecycle. The plan should be dynamic and updated
   as needed throughout the project lifecycle by :need:`wf__verification__plan_maintain`.

.. workflow:: Maintain Verification Plan
   :id: wf__verification__plan_maintain
   :status: valid
   :tags: verification
   :responsible: rl__committer, rl__testing_community
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager, rl__infrastructure_tooling_community
   :input: wp__verification__plan, wp__requirements__stkh, wp__platform_mgmt,
           wp__feature_arch, wp__requirements__feat, wp__requirements__feat_aou,
           wp__component_arch, wp__requirements__comp, wp__requirements__comp_aou,
           wp__tool_verification
   :output: wp__verification__plan
   :contains: gd_guidl__verification_guide, gd_temp__verification__plan
   :has: doc_concept__verification__process, doc_getstrt__verification__process

   The verification plan is maintained by :need:`rl__committer`. The plan should be dynamic and updated
   as needed throughout the project lifecycle, as verification activities may be impacted, by new
   requirements, architectural decisions, introduction of tools.

   Note that during the initial creation of the verification plan in :need:`wf__verification__plan`
   not every input down to component level may be available.

.. workflow:: Create Module Verification Report
   :id: wf__verification__mod_ver_report
   :status: valid
   :tags: verification
   :responsible: rl__committer, rl__testing_community
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager, rl__infrastructure_tooling_community
   :input: wp__verification__plan, wp__requirements__comp, wp__requirements__comp_aou,
           wp__component_arch, wp__module_sw_release_note, wp__platform_mgmt,
           wp__sw_component_safety_analysis, wp__sw_component_dfa,
           wp__sw_arch_verification, wp__sw_implementation_inspection, wp__requirements__inspect,
           wp__verification__comp_int_test, wp__verification__sw_unit_test
   :output: wp__verification__module_ver_report
   :contains: gd_temp__mod_ver_report
   :has: doc_concept__verification__process, doc_getstrt__verification__process

   The verification report is created and maintained by a :need:`rl__committer`.
   It is based on the :need:`wp__verification__plan` and covers all the components of a module.
   This includes their requirements, AoUs, Architecture, Detailed Design, Units, DFA, Safety Analyses,
   Unit Code coverage. The respective necessary test methods and rigor of their application is
   defined in the :need:`wp__verification__plan`.

   The report is valid for ONE version of a module.

.. workflow:: Create Platform Verification Report
   :id: wf__verification__platform_ver_report
   :status: valid
   :tags: verification
   :responsible: rl__committer, rl__testing_community
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager, rl__infrastructure_tooling_community
   :input: wp__verification__plan, wp__requirements__stkh, wp__requirements__feat, wp__requirements__feat_aou,
           wp__feature_arch, wp__platform_sw_release_note, wp__platform_mgmt,
           wp__feature_safety_analysis, wp__feature_dfa,
           wp__sw_arch_verification, wp__requirements__inspect,
           wp__verification__feat_int_test, wp__verification__platform_test
   :output: wp__verification__platform_ver_report
   :contains: gd_temp__platform_ver_report
   :has: doc_concept__verification__process, doc_getstrt__verification__process

   The verification report is created and maintained by a :need:`rl__committer`.
   It is based on the :need:`wp__verification__plan` and covers all the selected features of a SW platform.
   This includes their requirements, AoUs, Architecture, DFA, Safety Analyses,
   The respective necessary test methods and rigor of their application is
   defined in the :need:`wp__verification__plan` and :need:`wp__platform_mgmt`.

   The report is valid for ONE specific platform version baseline.

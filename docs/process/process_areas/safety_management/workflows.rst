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

Workflows
---------

.. workflow:: Create/Maintain Safety Plan
   :id: wf__cr_mt_safety_plan
   :status: valid
   :responsible: rl__safety_manager
   :approved_by: rl__technical_lead
   :input: wp__platform_mgmt, wp__issue_track_system, wp__sw_component_class
   :output: wp__module_safety_plan, wp__platform_safety_plan
   :contains: gd_guidl__saf_plan_definitions, gd_temp__feature_safety_wp, gd_temp__module_safety_plan
   :has: doc_concept__safety_management__process, doc_getstrt__safety_management__process

   | The Safety Manager is responsible for the planning and coordination of the safety activities for the platform.
   | The Safety Manager creates and maintains the safety plan.
   | For this a template exists to guide the creator of the safety plan.

.. workflow:: Create Component Classification
   :id: wf__cr_comp_class
   :status: valid
   :responsible: rl__committer
   :approved_by: rl__safety_manager
   :input: wp__platform_mgmt, wp__issue_track_system
   :output: wp__sw_component_class
   :contains: gd_guidl__component_classification, gd_temp__component_classification
   :has: doc_concept__safety_management__process, doc_getstrt__safety_management__process

   | The Safety Manager shall approve the OSS component classification performed by an expert on this component.

.. workflow:: Create/Maintain Safety Package
   :id: wf__cr_mt_safety_package
   :status: valid
   :responsible: rl__safety_manager
   :approved_by: rl__technical_lead
   :input: wp__module_safety_plan, wp__platform_safety_plan, wp__issue_track_system
   :output: wp__module_safety_package, wp__platform_safety_package
   :contains: gd_guidl__saf_package, gd_temp__feature_safety_wp, gd_temp__module_safety_plan
   :has: doc_concept__safety_management__process, doc_getstrt__safety_management__process

   | The Safety Manager in S-CORE is NOT responsible to provide the argument for the achievement of functional safety.
   | But the Safety Manager creates and maintains the safety package in the sense of a collection of safety related work products.
   | The generation and the maintainance of this draft safety package shall be automtated as much as possible.
   | It does not contain the final argumentation of the safety of the product.
   | As the safety package is only a collection of work products, the safety plan (template) can be used for documentation.

.. workflow:: Perform Safety Audit
   :id: wf__p_fs_audit
   :status: valid
   :responsible: rl__external_auditor
   :approved_by: rl__safety_manager
   :input: wp__module_safety_plan, wp__platform_safety_plan, wp__module_safety_package, wp__platform_safety_package
   :output: wp__audit_report
   :contains: gd_guidl__saf_plan_definitions
   :has: doc_concept__safety_management__process, doc_getstrt__safety_management__process

   | The external auditor is responsible to perform a safety audit.
   | The Safety Manager and the process community shall support the external auditor during this.
   | The Project Manager and and the Safety Manager shall approve the audit report.

.. workflow:: Perform Formal Reviews
   :id: wf__p_formal_rv
   :status: valid
   :responsible: rl__external_auditor
   :approved_by: rl__safety_manager
   :input: wp__module_safety_plan, wp__platform_safety_plan, wp__module_safety_package, wp__platform_safety_package
   :output: wp__fdr_reports
   :contains: gd_guidl__saf_plan_definitions, gd_chklst__safety_plan, gd_chklst__safety_package
   :has: doc_concept__safety_management__process, doc_getstrt__safety_management__process

   | The external auditor is responsible to perform the formal reviews on Safety plan and Safety Analysis.
   | The Safety Manager shall support the external auditor during the reviews.
   | The Project Manager and and the Safety Manager shall approve the formal reviews.
   | Therefore a checklists exist to guide the creator of the relevant safety documents.

.. workflow:: Create/Maintain Safety Manual
   :id: wf__cr_mt_safety_manual
   :status: valid
   :responsible: rl__safety_manager
   :approved_by: rl__technical_lead
   :input: wp__requirements__feat_aou, wp__requirements__feat, wp__feature_arch, wp__feature_safety_analysis, wp__feature_dfa, wp__requirements__comp_aou, wp__requirements__comp, wp__component_arch, wp__sw_component_safety_analysis, wp__sw_component_dfa
   :output: wp__platform_safety_manual, wp__module_safety_manual
   :contains: gd_guidl__saf_man, gd_temp__safety_manual
   :has: doc_concept__safety_management__process, doc_getstrt__safety_management__process

   | The Safety Manager collects the necessary input for the safety manuals on platform and module level and documents it.
   | He makes sure all items are in valid state for a release of the safety manual.
   | Also for the safety manual a template exists as a guidance.

.. workflow:: Monitor/Verify Safety
   :id: wf__mr_vy_safety
   :status: valid
   :responsible: rl__safety_manager
   :approved_by: rl__technical_lead
   :input: wp__module_safety_plan, wp__platform_safety_plan, wp__module_safety_package, wp__platform_safety_package, wp__audit_report, wp__fdr_reports
   :output: wp__issue_track_system, wp__module_sw_release_note, wp__platform_sw_release_note
   :contains: gd_guidl__saf_plan_definitions
   :has: doc_concept__safety_management__process, doc_getstrt__safety_management__process

   | The Safety Manager is responsible for the monitoring of the safety activities against the safety plan.
   | The Safety Manager is responsible to verify, that the preconditions for the "release for production", which are  part of the release notes, are fulfilled.
   | The Safety Manager is responsible to verify the correctness, completeness and consistency of the release notes.

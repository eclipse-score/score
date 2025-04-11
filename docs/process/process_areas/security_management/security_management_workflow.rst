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


Workflow Security Management
############################

.. workflow:: Create/Maintain Security Plan
   :id: wf__cr_mt_security_plan
   :status: valid
   :responsible: rl__security_manager
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager
   :input: wp__platform_mgmt, wp__issue_track_system, wp__tailoring
   :output: wp__module_security_plan, wp__platform_security_plan
   :contains: gd_guidl__security_plan_definitions, gd_temp__feature_security_wp, gd_temp__module_security_plan
   :has: doc_concept__security_management_process, doc_getstrt__security_management_process

   | The Security Manager is responsible for the planning and coordination of the security activities for the platform.
   | The Security Manager creates and maintains the security plan.
   | For this a template exists to guide the creator of the security plan.

.. workflow:: Create/Maintain Security Package
   :id: wf__cr_mt_security_package
   :status: valid
   :responsible: rl__security_manager
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager
   :input: wp__module_security_plan, wp__platform_security_plan, wp__issue_track_system
   :output: wp__module_security_package, wp__platform_security_package
   :contains: gd_guidl__security_package, gd_temp__feature_security_wp, gd_temp__module_security_plan, gd_guidl__security_plan_definitions
   :has: doc_concept__security_management_process, doc_getstrt__security_management_process

   | The Security Manager in S-CORE is NOT responsible to provide the argument for the achievement of security.
   | But the Security Manager creates and maintains the security package in the sense of a collection of security related work products.
   | The generation and the maintainance of this draft security package shall be automtated as much as possible.
   | It does not contain the final argumentation of the security of the product.
   | As the security package is only a collection of work products, the security plan (template) can be used for documentation.

.. workflow:: Perform Security Audit
   :id: wf__p_fs_audit_security
   :status: valid
   :responsible: rl__external_auditor
   :approved_by: rl__security_manager
   :supported_by: rl__safety_manager
   :input: wp__module_security_plan, wp__platform_security_plan, wp__module_security_package, wp__platform_security_package
   :output: wp__audit_report_security
   :contains: gd_guidl__security_plan_definitions
   :has: doc_concept__security_management_process, doc_getstrt__security_management_process

   | The external auditor is responsible to perform a security audit.
   | The Security Manager and the process community shall support the external auditor during this.
   | The Project Manager and and the Security Manager shall approve the audit report.
   |
   | This is currently tailored out (needs discussion).

.. workflow:: Perform Formal Security Reviews
   :id: wf__p_formal_security_rv
   :status: valid
   :responsible: rl__external_auditor
   :approved_by: rl__security_manager
   :supported_by: rl__safety_manager
   :input: wp__module_security_plan, wp__platform_security_plan, wp__module_security_package, wp__platform_security_package
   :output: wp__fdr_reports_security
   :contains: gd_guidl__security_plan_definitions, gd_chklst__security_plan, gd_chklst__security_package
   :has: doc_concept__security_management_process, doc_getstrt__security_management_process

   | The external auditor is responsible to perform the formal reviews on Security plan and Security Analysis.
   | The Security Manager shall support the external auditor during the reviews.
   | The Project Manager and and the Security Manager shall approve the formal reviews.
   | Therefore a checklists exist to guide the creator of the relevant security documents.
   |
   | This is currently tailored out (needs discussion).

.. workflow:: Create/Maintain Security Manual
   :id: wf__cr_mt_security_manual
   :status: valid
   :responsible: rl__security_manager
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager
   :input: wp__requirements__feat_aou, wp__requirements__feat, wp__feature_arch, wp__feature_safety_analysis, wp__feature_dfa, wp__requirements__comp_aou, wp__requirements__comp, wp__component_arch, wp__sw_component_safety_analysis, wp__sw_component_dfa
   :output: wp__platform_security_manual, wp__module_security_manual
   :contains: gd_guidl__security_manual, gd_temp__security_manual, gd_guidl__security_plan_definitions
   :has: doc_concept__security_management_process, doc_getstrt__security_management_process

   | The Security Manager collects the necessary input for the security manuals on platform and module level and documents it.
   | He makes sure all items are in valid state for a release of the security manual.
   | Also for the security manual a template exists as a guidance.

.. workflow:: Create/Maintain SBOM
   :id: wf__cr_mt_security_sbom
   :status: valid
   :responsible: rl__committer
   :approved_by: rl__security_manager, rl__technical_lead, rl__module_lead
   :supported_by: rl__infrastructure_tooling_community, rl__process_community, rl__security_team
   :input: wp__issue_track_system, wp__module_security_plan, wp__platform_security_plan, wp__module_security_package, wp__platform_security_package
   :output: wp__sw_platform_sbom, wp__sw_module_sbom
   :contains: gd_guidl__security_plan_definitions
   :has: doc_concept__security_management_process, doc_getstrt__security_management_process

   | The Committer is responsible to create and the maintain the SBOM for the platform/module.
   | The Committer makes sure all components and dependencies are identified and made available.

.. workflow:: Monitor/Verify Security
   :id: wf__mr_vy_security
   :status: valid
   :responsible: rl__security_manager
   :approved_by: rl__technical_lead
   :supported_by: rl__security_team
   :input: wp__issue_track_system, wp__module_security_plan, wp__platform_security_plan, wp__module_security_package, wp__platform_security_package, wp__audit_report, wp__fdr_reports, wp__sw_platform_sbom, wp__sw_module_sbom
   :output: wp__issue_track_system, wp__module_sw_release_note, wp__platform_sw_release_note
   :contains: gd_guidl__security_plan_definitions
   :has: doc_concept__security_management_process, doc_getstrt__security_management_process

   | The Security Manager is responsible for the monitoring of the security activities against the security plan.
   | The Security Manager is responsible to verify, that the preconditions for the "release for production", which are  part of the release notes, are fulfilled.
   | The Security Manager is responsible to verify the correctness, completeness and consistency of the release notes.
   | The Security Manager is repsponsible for the monitoring of security information as defined in the security plan.
   | The Security Manager is repsponsible to identify weaknesses and vulnerabilities based on received information, and to analyse and manage the vulnerabilities until closure.
   | Beside reporting vulnerabilities in the :need:`wp__issue_track_system`, also `Eclipse general vulnerability tracker <https://gitlab.eclipse.org/security>`_ may be used.

.. needextend:: "process_areas/security_management" in docname
   :+tags: security_management


RAS(IC) for Security Management:
********************************

.. needtable:: RASIC Overview for Security Management
   :tags: security_management
   :filter: "security_management" in tags and type == "workflow"
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30

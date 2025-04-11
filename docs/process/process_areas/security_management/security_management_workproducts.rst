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

Work Products Security Management
#################################

.. workproduct:: Platform Security Plan
   :id: wp__platform_security_plan
   :status: valid
   :complies: std_wp__isosae21434__prj_management_651, std_wp__isosae21434__maintenance_13331, std_wp__isosae21434__continual_8331, std_wp__isosae21434__continual_8332

   Plan to manage and guide the execution of the security activities of a project including dates, milestones, tasks, deliverables, responsibilities (including the Security Manager appointment)  and resources.

   This platform security plan also takes into accout the eclipse organization's rules relevant for security development.

   Guidelines on how an change impact analysis shall be concluded on each item or element involved together with it's connected items or elements.

   This is on following level:

   * Project/Platform (contains definitions how security planning is performed generally in the project)

.. workproduct:: Module Security Plan
   :id: wp__module_security_plan
   :status: valid
   :complies: std_wp__isosae21434__prj_management_651

   Plan to manage and guide the execution of the security activities of a project including dates, milestones, tasks, deliverables, responsibilities (including the Security Manager appointment) and resources.

   Guidelines on how an impact analysis shall be concluded on each item or element involved together with it's connected items or elements.

   This is on following level:

   * Module (contains activities planning based on a Change Request)

.. workproduct:: Platform Security Package
   :id: wp__platform_security_package
   :status: valid
   :complies: std_wp__isosae21434__prj_management_652

   Compiled Security Relevant Work Products. For Platform EooC.

   Note that the platform security package does not contain an argument that the platform is safe and secure.

.. workproduct:: Module Security Package
   :id: wp__module_security_package
   :status: valid
   :complies:

   Compiled Security Relevant Work Products. For Module EooC.

   Note that the module security package does not contain an argument that the module is safe and secure.

.. workproduct:: Formal Document Review Reports
   :id: wp__fdr_reports_security
   :status: valid
   :complies: std_wp__isosae21434__prj_management_654

   Review that a work product provides sufficient and convincing evidence of their contribution to the achievement of security considering the corresponding objectives and requirements of ISO SAE 21434.

   Will contain formal review report for Security Plan, Security Package, Security Analyses.

.. workproduct:: Process Security Audit Report
   :id: wp__audit_report_security
   :status: valid
   :complies: std_wp__isosae21434__org_management_555

   Examination of an implemented process with regard to the process objectives and that those match the ISO SAE 21434.
   (Currently tailored out, needs discussion)

.. workproduct:: Platform Security Manual
   :id: wp__platform_security_manual
   :status: valid
   :complies: std_wp__isosae21434__prj_management_654

   The security manual describes:

   * the Assumed Platform Requirements (Security related, including for post-development);
   * the security concept of the EooC (i.e. which attack paths are taken care of);
   * the Assumptions of Use (of the features);
   * a link to the user manual;
   * the reactions of the implemented functions under threatened operating conditions; and
   * a description of known vulnerabilities with corresponding workaround measures.

   This is on platform level. Only one manual for the entire platform.

.. workproduct:: Module Security Manual
   :id: wp__module_security_manual
   :status: valid
   :complies: std_wp__isosae21434__prj_management_654

   The security manual describes:

   * the Assumed Platform Requirements (Security related, including for post-development);
   * the security concept of the EooC (i.e. which attack paths are taken care of);
   * the Assumptions of Use (of the modules's components);
   * a link to the user manual;
   * the reactions of the implemented functions under threatened operating conditions; and
   * a description of known vulnerabilities with corresponding workaround measures.

   This is on module level. One manual per each module.

.. workproduct:: Feature Security Analysis
   :id: wp__feature_security_analysis
   :status: draft
   :complies: std_wp__isosae21434__development_1055, std_wp__isosae21434__assessment_15631, std_wp__isosae21434__assessment_15731, std_wp__isosae21434__assessment_15831, std_wp__isosae21434__assessment_15931

   Bottom-Up Security Analysis with e.g. FMEA method, verifies the feature architecture (as part of SW Security Concept)
   - Detection and prevention mitigations linked to Software Feature Requirements or Assumptions of Use

.. workproduct:: Component Security Analysis
   :id: wp__sw_component_security_analysis
   :status: draft
   :complies: std_wp__isosae21434__development_1055, std_wp__isosae21434__assessment_15631, std_wp__isosae21434__assessment_15731, std_wp__isosae21434__assessment_15831, std_wp__isosae21434__assessment_15931

   Bottom-Up Security Analysis with e.g. FMEA method, verifies the component architecture (as part of SW Security Concept)
   - Detection and prevention mitigations linked to Software Component Requirements or Assumptions of Use

.. workproduct:: Platform Software Bill of Material (SBOM)
   :id: wp__sw_platform_sbom
   :status: draft
   :complies:

   Platform Software Bill of Material
   - comprehensive inventory of software components to ensure security, integrity, and compliance.

.. workproduct:: Module Software Bill of Material (SBOM)
   :id: wp__sw_module_sbom
   :status: draft
   :complies:

   Module Software Bill of Material
   - comprehensive inventory of software components to ensure security, integrity, and compliance.

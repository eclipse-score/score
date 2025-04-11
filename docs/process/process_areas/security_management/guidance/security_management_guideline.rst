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

.. _guideline_security_management:

Security Management Guideline
=============================

.. gd_guidl:: Security plan definitions
   :id: gd_guidl__security_plan_definitions
   :status: valid
   :complies: std_req__isosae21434__org_management_5421, std_req__isosae21434__org_management_5422, std_req__isosae21434__org_management_5423, std_req__isosae21434__org_management_5443, std_req__isosae21434__org_management_5451, std_req__isosae21434__org_management_5461, std_req__isosae21434__continual_8321, std_req__isosae21434__continual_8322

   **Overall security management:**

   Security culture:

   Security culture is planned to grow in the SW platform.
   This shall be fostered by doing a lessons learned after each feature development completion,
   using the ISO SAE 21434 Annex B, Table B.1 as a questionnaire.
   This lessons learned is the main input for process improvement managed by :need:`wp__process_impr_report`
   As starting point for security culture we define a Committer selection process to already have
   professionals with security experience in the teams. Additionally the SW platform's processes
   are defined with experience of several companies already performing successful safe and secure
   SW development. This also improves independence of reviews for the process definitions.

   Quality Management:

   ASPICE standard is selected for quality management. Processes will always link to the
   :ref:`standard_isosae21434` standard and to the :ref:`standard_aspice_pam4` standard.

   Competence management:

   The :need:`rl__security_manager` on SW platform level is responsible to define a competence
   management for the whole platform. Expectation is that the security competence of the persons
   nominated for the roles is already given and only has to be checked. The exception from this
   are the committers, for these no security competence needs to be enforced.
   So the module security managers shall consult the :need:`doc__platform_security_plan` and
   perform accordingly in their module project.

   Communication:

   Development teams are interdisciplinary, so the regular (sprint) planning and review meetings
   enable communication (as defined in :need:`doc__project_mgt_plan`). Another main communication
   means are the Pull Request reviews. Also the standard Eclipse Foundation communication strategies
   are used (e.g. mailing lists)

   Security Weaknessess, Vulnerabilities:

   As the SW platform organization does not have own vehicles in the field, it relies on feedback
   from OEMs and Distributors on bugs discovered in the field. The need for this feedback is part
   of each security manual. But also during development of change requests to existing features,
   bug reporting by the Open Source community or integration of existing SW components into new
   features may lead to the discovery of new security weaknessess and vulnerabilities. Security
   weaknessess and vulnerabilities can also be deviations from the development process with impact
   on security. If these are known at the time of creation of a release they will be part of the
   :need:`wp__module_security_package` or :need:`wp__platform_security_package` for the EooC.
   Security weaknessess and vulnerabilities relevant for already delivered releases will be
   identified as such and communicated (as defined in Problem Resolution part of :need:`wp__platform_mgmt`)
   via the :need:`wp__issue_track_system` (which is also Open Source).


   **Tailoring security activities:**

   Main tailoring driver is that the SW platform is pure SW development and is provided as "EooC" -
   this explains mainly the generic, platform wide tailoring.
   Tailoring is done for the whole SW platform by defining only the relevant work products and an
   argumentation why the others are not needed in :ref:`standard_isosae21434` and
   :need:`doc__platform_security_plan`.
   But there may be also additional tailoring for each module EooC development to restrict further
   the work products. This is documented in every feature security plan. Here the usage of already
   existing components is the main tailoring driver.


   **Planning security activities:**

   In the security plan the nomination of the security manager and the project manager is documented.
   The planning of security activities is done using issues in the :need:`wp__issue_track_system`
   as specified in the :need:`doc__project_mgt_plan`

   It contains for each issue

   * objective - as part of the issue description
   * dependencies on other activities or information - by links to the respective issues
   * responsible person for the activity - as issue assignee
   * required resources for the activity - by selecting a team label (or "project") pointing to a team of committers dedicated to the issue resolution
   * duration in time, including start and end point - by selecting a milestone
   * UID of the resulting work products - stated in the issue title

   The planning of security activities is divided into the

   * platform EooC planning, dealing with all work products needed only once for the platform. This is included in :need:`wp__platform_security_plan`
   * module EooC planning, dealing with all work products needed for each module development (initiated by a contribution request), included in :need:`wp__module_security_plan`.

   A template exists to guide this: :need:`gd_temp__module_security_plan`.


   **Planning supporting processes:**

   Supporting processes (Requirements Management, Configuration Management, Change Management,
   Documentation Management, Tool Management) are planned within the :need:`wp__platform_mgmt`

   **Planning integration and verification:**

   Integration on the target hardware is not done in the scope of the SW platform project, but SW/SW
   integration up to the feature level is performed and its test results are part of the
   :need:`wp__verification__platform_ver_report`.
   The integration on the target hardware done by the distributor or OEM is supported by delivering
   a set of HW/SW integration tests which were already run successfully on a reference HW platform.

   This is planned by the respective work products:

   * :need:`wp__verification__feat_int_test`
   * :need:`wp__verification__platform_test`

   Verification planning is documented in :need:`wp__verification__plan`


   **Scheduling of reviews, audit and assessment:**

   Scheduling is done in the same way as for all work products definition by issues.
   The respective work products are :need:`wp__fdr_reports_security` and  :need:`wp__audit_report_security`


   **Planning of security analyses:**

   In cases where the components consist of sub-components there will be more than one architecture
   level. Security analysis will then be done on these multiple levels.

   See the respective work products:

   * feature level: :need:`wp__feature_security_analysis`
   * component level: :need:`wp__sw_component_security_analysis`

   Analyses shall be based on `STRIDE <https://en.wikipedia.org/wiki/STRIDE_model>`_ model.

   **Provision of the confidence in the use of software tools:**

   Tool Management planning is part of the :need:`wp__platform_mgmt`. The respective work product
   to be planned as an issue  of the generic security plan is the :need:`wp__tool_verification`,
   which contains tool evaluation and if applicable qualification of the SW platform toolchain.
   Components developed in C++ and Rust will have different toolchains. Both will be qualified
   once for the SW platform.

   **Provision of a Software Bill of Materials (SBOM) and Vulnerability Management**

   SBOMs provide a comprehensive inventory of all components and dependencies within a software
   project, thus they can be interpreted as configuration information.
   `Eclipse Project Handbook: Software Bill of Material <https://www.eclipse.org/projects/handbook/#sbom>`_
   recommends to generate SBOMs and contains also information how to generate SBOMs.
   SBOMs are used as sources for collection of information and as trigger for further investigations
   as identifying weaknesses and vulnerabilities.

   `Eclipse Foundation Security Team <https://www.eclipse.org/projects/handbook/#vulnerability-team>`_
   provides help and advice to Eclipse projects on security issues and is the first point of
   contact for handling security vulnerabilities. Nevertheless the all :need:`rl__contributor` and
   :need:`rl__committer` are responsible for following the `Eclipse Foundation Security Policy <https://www.eclipse.org/security/policy/>`_.
   The :need:`Security Team <rl__security_team>` is responsible for coordinating the resolution of
   vulnerabilities within the Project.

.. gd_guidl:: Security manual generation
   :id: gd_guidl__security_manual
   :status: valid
   :complies: std_req__isosae21434__prj_management_6491, std_req__isosae21434__prj_management_6492

   The security manual collects several work products and adds some additional content mainly to
   instruct the user of a EooC (in this project on platform and module level) to securely use it
   in the context of the user's own security element and requirements for post-development.
   Its main content is described in :need:`wp__platform_security_manual` and :need:`wp__module_security_manual`.
   A template exists to guide the definition of the security manual on platform and module level (:need:`gd_temp__security_manual`).

.. gd_guidl:: Security package automated generation
   :id: gd_guidl__security_package
   :status: valid
   :complies: std_req__isosae21434__prj_management_6471

   The security package shall be generated progressively and automatically compiling the work products.

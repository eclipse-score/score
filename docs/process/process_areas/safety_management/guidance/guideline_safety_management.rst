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

.. _guideline_safety_management:

Safety Management Guideline
===========================

.. gd_guidl:: Safety plan definitions
   :id: gd_guidl__saf_plan_definitions
   :status: valid
   :complies: std_req__iso26262__management_35, std_req__iso26262__management_36, std_req__iso26262__management_37, std_req__iso26262__management_38, std_req__iso26262__management_39

   | **Overall safety management:**
   | Safety culture:
   | Safety culture is planned to grow in the SW platform. This shall be fostered by doing a lessons learned after each feature development completion, using the ISO 26262-2 Table B.1 as a questionnaire.
   | This lessons learned is the main input for process improvement managed by :need:`wp__PROCESS_IMPR_REPORT`
   | As starting point for safety culture we define a Committer selection process to already have professionals with safety experience in the teams.
   | Additionally the SW platform's processes are defined with experience of several companies alrady performing successful safe SW development. This also improves independence of reviews for the process definitions.
   |
   | Quality Management:
   | ASPICE standard is selected for quality management. Processes will always link to the :ref:`standard_iso26262` standard and to the ASPICE (todo, add link) standard.
   |
   | Competence management:
   | The :need:`rl__safety_manager` on SW platform level is responsible to define a competence management for the whole platform.
   | Expectation is that the safety competence of the persons nominated for the roles is already given and only has to be checked.
   | The exception from this are the committers, for these no safety competence needs to be enforced.
   | So the module safety managers shall consult the :ref:`safety_management` and perform accordingly in their module project.
   |
   | Communication:
   | Development teams are interdisciplinary, so the regular (sprint) planning and review meetings enable communication (as defined in :ref:`project_management_plan`). Another main communication means are the Pull Request reviews.
   | Also the standard Eclipse Foundation communication strategies are used (e.g. mailing lists)
   |
   | Safety anomalies:
   | As the SW platform organization does not have own vehicles in the field, it relies on feedback from OEMs and Distributors on bugs discovered in the field. The need for this feedback is part of each safety manual.
   | But also during development of change requests to existing features, bug reporting by the Open Source community or integration of existing SW components into new features may lead to the discovery of new safety anomalies.
   | Safety anomalies can also be deviations from the development process with impact on safety.
   | If these are known at the time of creation of a release they will be part of the :need:`wp__module_safety_case` or :need:`wp__platform_safety_case` for the SEooC.
   | Safety anomalies relevant for already delivered releases will be identified as such and communicated (as defined in Problem Resolution part of :need:`wp__PLATFORM_MGMT`) via the :need:`wp__ISSUE_TRACK_SYSTEM` (which is also Open Source).
   |
   | **Tailoring safety activities:**
   | Main tailoring driver is that the SW platform is pure SW development and is provided as "SEooC" - this explains mainly the generic, platform wide tailoring.
   | Tailoring is done for the whole SW platform by defining only the relevant work products and an argumentation why the others are not needed in :ref:`standard_iso26262` and :ref:`safety_management`.
   | But there may be also additional tailoring for each module SEooC development to restrict further the work products. This is documented in every feature safety plan. Here the usage of already existing components is the main tailoring driver.
   |
   | **Planning safety activities:**
   | In the safety plan the nomination of the safety manager and the project manager is documented.
   | The planning of safety activities is done using issues in the :need:`wp__ISSUE_TRACK_SYSTEM` as specified in the :ref:`project_management_plan`
   | It contains for each issue
   | * objective - as part of the issue description
   | * dependencies on other activities or information - by links to the respective issues
   | * responsible person for the activity - as issue assignee
   | * required resources for the activity - by selecting a team label (or "project") pointing to a team of committers dedicated to the issue resolution
   | * duration in time, including start and end point - by selecting a milestone
   | * UID of the resulting work products - stated in the issue title
   |
   | The planning of safety activities is divided into the
   | * platform SEooC planning, dealing with all work products needed only once for the platform. This is included in :need:`wp__platform_safety_plan`
   | * module SEooC planning, dealing with all work products needed for each module development (initiated by a contribution request), included in :need:`wp__module_safety_plan`. This module safety planning also includes the planning of OSS component qualification based on :need:`gd_guidl__component_classification`.
   | A template exists to guide this: :need:`GD_TEMP__module_safety_plan`.
   |
   | **Planning supporting processes:**
   | Supporting processes (Requirements Management, Configuration Managment, Change Management, Documentation Management, Tool Management) are planned within the :need:`wp__PLATFORM_MGMT`
   |
   | **Planning integration and verification:**
   | Integration on the target hardware is not done in the scope of the SW platform project, but SW/SW integration up to the feature level is performed and its test results are part of the :need:`wp__PLATFORM_SW_VERIFICATION_REPORT`.
   | The integration on the target hardware done by the distributor or OEM is supported by delivering a set of HW/SW integration tests which were already run successfully on a reference HW platform.
   | This is planned by the respective work products:
   | * :need:`wp__FEATURE_INTEGRATION_TEST`
   | * :need:`wp__PLATFORM_TEST`
   | Verification planning is documented in :need:`wp__VERIFICATION_PLAN`
   |
   | **Scheduling of confirmation reviews, audit and assessment:**
   | Scheduling is done in the same way as for all work products definition by issues. The respective work products are :need:`wp__cmr_reports` and  :need:`wp__audit_report`
   |
   | **Planning of dependent failures and safety analyses:**
   | In cases where the components consist of sub-components there will be more than one architecture level. DFA and Safety analysis will then be done on these multiple levels. See the respective work products:
   | * feature level: :need:`wp__FEATURE_SAFETY_ANALYSES` and :need:`wp__FEATURE_DFA`
   | * component level: :need:`wp__SW_COMPONENT_SAFETY_ANALYSES` and :need:`wp__SW_COMPONENT_DFA`
   |
   | **Provision of the confidence in the use of software tools:**
   | Tool Management planning is part of the :need:`wp__PLATFORM_MGMT`. The respective work product to be planned as an issue of the generic safety plan is the :need:`wp__TOOL_EVAL`, which contains tool evaluation and if applicable qualification of the SW platform toolchain.
   | Components developed in C++ and Rust will have different toolchains. Both will be qualified once for the SW platform. Tool requirements will be documented in :need:`wp__TOOL_REQ`
   |
   | **(OSS) Component qualification planning:**
   | Based on the component classification as described in :need:`gd_guidl__component_classification`,
   | the qualification of the component is planned as part of the :need:`GD_TEMP__module_safety_plan`.
   | The template contains guidance how to do this and to document in the "OSS (sub-)component <name> Workproducts" list.

.. gd_guidl:: Safety manual generation
   :id: gd_guidl__saf_man
   :status: valid
   :complies: std_req__iso26262__system_1, std_req__iso26262__system_2, std_req__iso26262__system_3, std_req__iso26262__system_4, std_req__iso26262__system_5, std_req__iso26262__system_6, std_req__iso26262__software_4, std_req__iso26262__software_5, std_req__iso26262__software_8, std_req__iso26262__support_65

   | The safety manual collects several workproducts and adds some additional content mainly to instruct the user of
   | a SEooC (in this project on platform and module level) to safely use it in the context of the user's own safety
   | element.
   | Its main content is described in :need:`wp__platform_safety_manual` and :need:`wp__module_safety_manual`
   | A template exists to guide the definition of the safety manual on platform and module level (:need:`GD_TEMP__safety_manual`).

.. gd_guidl:: Safety case automated generation
   :id: gd_guidl__saf_case
   :status: valid
   :complies: std_req__iso26262__management_43, std_req__iso26262__management_44

   | The safety case shall be generated progressively and automatically compiling the work products.

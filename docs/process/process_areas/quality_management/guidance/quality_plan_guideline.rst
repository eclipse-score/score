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

.. _guideline_quality_plan:

Quality Management Plan Guideline
#################################

.. gd_guidl:: Quality Management Plan Definitions Guideline
   :id: gd_guidl__qlm_plan_definitions
   :status: valid
   :complies: std_wp__iso26262__management_553, std_req__iso26262__management_5423, std_req__aspice_40__SUP-1-BP1, std_req__aspice_40__SUP-1-BP2, std_req__aspice_40__SUP-1-BP3, std_req__aspice_40__SUP-1-BP4, std_req__aspice_40__SUP-1-BP7, std_req__aspice_40__PIM-3-BP1, std_req__aspice_40__PIM-3-BP2, std_req__aspice_40__PIM-3-BP3, std_req__aspice_40__PIM-3-BP4, std_req__aspice_40__PIM-3-BP5, std_req__aspice_40__PIM-3-BP6, std_req__aspice_40__PIM-3-BP7

   | **Overall quality management:**
   | Quality culture:
   | Quality as well as Safety and Security Culture is planned to grow in the SW platform. This shall be fostered by doing process conformance checks and work product reviews, as well as lessons learned after each feature development completion and a process audit after each platform/project release.
   | The main outcome is the :need:`wp__process_impr_report`, which is used to improve the processes for the platform/project.
   | As starting point for Quality Culture we define a Committer selection process to already have professionals with quality experience in the teams.
   |
   | Quality Management:
   | ASPICE 4.0 standard is selected for quality management. Processes will always link to the :ref:`standard_iso26262` standard, :ref:`standard_isopas8926` standard, :ref:`standard_isosae21434` and to the :ref:`standard_aspice_40` standard.
   |
   | Communication:
   | Cross functional teams are interdisciplinary, so the regular (sprint) planning and review meetings enable communication. The organization of the project is described in the Project Management Plan :need:`doc__project_mgt_plan`. Another main communication means are the Pull Request (PR) reviews.
   | Also the standard Eclipse Foundation communication strategies are used (e.g. mailing lists, Slack channel).
   |
   | Quality issues, non-conformances and improvements:
   | Feedback from the field, but also during development of change requests to existing features, bug reporting by the Open Source community or integration of existing SW components into new features may lead to the discovery of issues, non-conformances or improvements.
   | Non-conformance can also be deviations from the development process with impact on safety or security.
   | If these are known at the time of creation of a release they will be part of the :need:`wp__platform_sw_release_note` for the feature.
   | Other issues and non-conformances relevant for already delivered releases will be identified as such and communicated (as defined in Problem Resolution part of :need:`doc__project_mgt_plan`) via the :need:`wp__issue_track_system`.
   |
   | **Tailoring quality activities:**
   | Main tailoring driver is that the SW platform is pure SW development and is provided as "SW element" - this explains mainly the generic, platform wide tailoring.
   | Tailoring is done for the whole SW platform by defining only the relevant processes and their resulting outcomes and an argumentation why the others are not needed in :ref:`standard_aspice_40`.
   |
   | **Planning quality activities:**
   | In the Quality Management Plan the nomination of the quality manager and the project manager is documented.
   | The planning of quality activities is done using issues in the :need:`wp__issue_track_system` as specified in the Project Management part of :need:`doc__project_mgt_plan`
   | It contains for each issue
   | * objective - as part of the issue description
   | * dependencies on other activities or information - by links to the respective issues
   | * responsible person for the activity - as issue assignee
   | * required resources for the activity - by selecting a team label (or "project") pointing to a team of committers dedicated to the issue resolution
   | * duration in time, including start and end point - by selecting a milestone
   | * UID of the resulting work products - stated in the issue title
   |
   | The planning of quality activities is part of
   | * generic planning, dealing with all work products needed only once for the platform. This is included in :need:`doc__platform_quality_plan`
   |
   | **Planning supporting processes:**
   | Supporting processes (Requirements Management, Configuration Managment, Change Management, Documentation Management, Tool Management) are planned within the :need:`doc__project_mgt_plan`
   |
   | **Planning integration and verification:**
   | Integration on the target hardware is not done in the scope of the SW platform project, but SW/SW integration up to the feature level is performed and its test results are part of the :need:`wp__verification__platform_ver_report`.
   | The integration on the target hardware done by the distributor or OEM is supported by delivering a set of HW/SW integration tests which were already run successfully on a reference HW platform.
   | This is planned by the respective workproducts:
   | * :need:`wp__verification__feat_int_test`
   | * :need:`wp__verification__platform_test`
   | Verification planning is documented in :need:`wp__verification__plan`
   |
   | **Scheduling of audits, conformance checks, work product reviews, release verification and approval:**
   | Scheduling is done in the same way as for all work products definition by issues. The respective work products are listed :ref:`workproduct_list_quality_review` here.

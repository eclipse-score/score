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

Work products
-------------

.. workproduct:: Platform Safety Plan
   :id: WP__platform_safety_plan
   :status: valid
   :complies: STD_WP_ISO26262__management_1, STD_WP_ISO26262__management_2, STD_WP_ISO26262__management_7, STD_WP_ISO26262__support_9

   Plan to manage and guide the execution of the safety activities of a project including dates, milestones, tasks, deliverables, responsibilities (including the Safety Manager appointment)  and resources.

   This platform safety plan also takes into accout the eclipse organization's rules relevant for safety development.

   Guidelines on how an impact analysis shall be concluded on each item or element involved together with it's connected items or elements.

   This is on following level:

   * Project/Platform (contains definitions how safety planning is performed generally in the project)

.. workproduct:: Module Safety Plan
   :id: WP__module_safety_plan
   :status: valid
   :complies: STD_WP_ISO26262__management_2, STD_WP_ISO26262__management_7, STD_WP_ISO26262__support_9, STD_WP_ISO26262__support_18, STD_WP_ISO26262__support_19

   Plan to manage and guide the execution of the safety activities of a project including dates, milestones, tasks, deliverables, responsibilities (including the Safety Manager appointment) and resources.

   Guidelines on how an impact analysis shall be concluded on each item or element involved together with it's connected items or elements.

   This is on following level:

   * Module (contains activities planning based on a Contribution Request)

.. workproduct:: Platform Safety Case
   :id: WP__platform_safety_case
   :status: valid
   :complies: STD_WP_ISO26262__management_8

   Compiled Safety Relevant Work Products. For Platform SEooC.

   Note that the platform safety case does not contain the argument that the platform is safe.

.. workproduct:: Module Safety Case
   :id: WP__module_safety_case
   :status: valid
   :complies: STD_WP_ISO26262__management_8

   Compiled Safety Relevant Work Products. For Module SEooC.

   Note that the module safety case does not contain the argument that the module is safe.

.. workproduct:: Confirmation Review Reports
   :id: WP__cmr_reports
   :status: valid
   :complies: STD_WP_ISO26262__management_9

   Confirmation that a work product provides sufficient and convincing evidence of their contribution to the achievement of functional safety considering the corresponding objectives and requirements of ISO 26262.

   Will contain confirmation review report for Safety Plan, Safety Analyses and Dependent Failure Analyses (DFA)

.. workproduct:: Functional Safety Audit Report
   :id: WP__audit_report
   :status: valid
   :complies: STD_WP_ISO26262__management_9

   Examination of an implemented process with regard to the process objectives and that those match the ISO 26262.

.. workproduct:: Platform Safety Manual
   :id: WP__platform_safety_manual
   :status: valid
   :complies: STD_WP_ISO26262__software_2, STD_WP_ISO26262__system_1

   The safety manual describes:

   * The Assumed Platform Requirements (Safety related);
   * the safety concept of the SEooC (i.e. which faults are taken care of);
   * the Assumptions of Use (of the features);
   * a link to the user manual;
   * the reactions of the implemented functions under anomalous operating conditions; and
   * a description of known anomalies with corresponding workaround measures.

   This is on platform level. Only one manual for the entire platform.

.. workproduct:: Module Safety Manual
   :id: WP__module_safety_manual
   :status: valid
   :complies: STD_WP_ISO26262__software_2, STD_WP_ISO26262__system_1, STD_WP_ISO26262__support_18

   The safety manual describes:

   * The Assumed Platform Requirements (Safety related);
   * the safety concept of the SEooC (i.e. which faults are taken care of);
   * the Assumptions of Use (of the modules's components);
   * a link to the user manual;
   * the reactions of the implemented functions under anomalous operating conditions; and
   * a description of known anomalies with corresponding workaround measures.

   This is on module level. One manual per each module.

.. workproduct:: Software component classification
   :id: WP__sw_component_class
   :status: valid
   :complies: STD_WP_ISO26262__support_18

   The classification shall include:

   * the unique identification of the pre-developed software component;
   * the maximum ASIL of the safety requirements allocated to it;
   * a development processes analysis; and
   * a complexity analysis of the pre-developed SW component; and
   * finally a SW component classification as input for the safety planning (which is to cover the determined gaps, if any, by additional verification measures).

.. workproduct:: Tailoring Documents
   :id: WP_tailoring
   :status: valid
   :complies: STD_WP_ISO26262__management_7

   This work product argues why some work products are not needed in the project.

   It may have several levels:

   * Project/Platform
   * Feature/Component

   It belongs to the Safety Plan.

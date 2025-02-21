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

Module Safety Plan Template
===========================

.. gd_temp:: Module Safety Plan Template
   :id: gd_temp__module_safety_plan
   :status: valid
   :complies: std_req__iso26262__management_35, std_req__iso26262__management_36, std_req__iso26262__management_37, std_req__iso26262__management_38, std_req__iso26262__management_39

This document implements <add "need" link>


   | **1. Functional Safety Management Context**
   | This Safety Plan adds to the :ref:`safety_management` all the module development relevant workproducts needed for ISO 26262 conformity.
   |
   | **2. Functional Safety Management Scope**
   | This Safety Plan's scope is a SW module of the SW platform <link to module documentation in platform/modules/<modulename>/index.rst>.
   | The module consists of one or more SW components and will be qualified as a SEooC.
   |
   | **3. Functional Safety Management Roles**

   +---------------------------+--------------------------------------------------------+
   | Safety Manager            | <link to Module's Safety Manager assignment or name>   |
   +---------------------------+--------------------------------------------------------+
   | Project Manager           | <link to Module's Project Manager assignment or name>  |
   +---------------------------+--------------------------------------------------------+

   | **4. Tailoring**
   | Additional to the tailoring in the SW platform project as defined in the :ref:`safety_management` we define here the additional tailoring on module level.
   |
   | - Excluded for this module are additionally the following workproducts (and their related requirements):
   |   - <ISO 26262 reference>: <workproduct/requirement> - <Argumentation why it is not needed or replaced by another workproduct or activity.>
   |
   | **5. Functional Safety Module Workproducts**
   | One set of workproducts for the module and one set for each component of the module:

.. list-table:: Module Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - :need:`wp__module_safety_plan`
          - :ref:`guideline_safety_management`
          - <automated>
          - <Link to issue>
          - this document
          - see above

        * - :need:`wp__module_safety_case`
          - :ref:`guideline_safety_management`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__cmr_reports` (module Safety Plan)
          - :need:`gd_chklst__safety_plan`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__cmr_reports` (module Safety Case)
          - :need:`gd_chklst__safety_case`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__cmr_reports` (module's Safety Analyses & DFA)
          - Safety Analysis CMR tbd
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__audit_report`
          - performed by external experts
          - n/a
          - <Link to issue>
          - <Link to WP>
          - <WP status (manual)>

        * - :need:`wp__SW_COMPONENT_DFA`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__MODULE_SW_BUILD_CONFIG`
          - :ref:`sw_development`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__module_safety_manual`
          - :need:`gd_temp__safety_manual`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__MODULE_SW_VERIFICATION_REPORT`
          - :ref:`sw_verification`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__MODULE_SW_RELEASE_NOTE`
          - :ref:`release_management`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>


.. list-table:: Component <name> Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - :need:`wp__SW_COMPONENT_REQ`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__SW_COMPONENT_AOU`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__HSI`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__SW_REQ_INSPECT`
          - <Link to process>
          - <automated>
          - n/a
          - Checklist used in Pull Request Review
          - n/a

        * - :need:`wp__SW_COMPONENT_ARCHITECTURE`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__SW_COMPONENT_SAFETY_ANALYSES`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__SW_ARCH_VERIFICATION`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__SW_IMPLEMENTATION`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__SW_UNIT_TEST`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__SW_CODE_INSPECT`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__SW_COMPONENT_INTEGRATION_TEST`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__SW_COMPONENT_TEST`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_component_class`
          - :need:`gd_guidl__component_classification`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>


| **6. OSS (sub-)component qualification plan**
| For the selected OSS component the following workproducts will be implemented (and why):
| If the OSS element is classified as a
|    - component, then the below table shall match the above, adding the reasoning for tailoring of work products according to the OSS component classification.
|    - sub-component, then no workproducts additional to the component’s will be planned and activities below are part of the component’s issues.

.. list-table:: OSS (sub-)component <name> Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Link to issue
          - Reasoning for tailoring

        * - :need:`wp__SW_COMPONENT_REQ`
          - <Link to issue>
          - Always needed (for Q and QR classification) and also improves process Id 2

        * - :need:`wp__SW_COMPONENT_AOU`
          - <Link to issue>
          - Always needed (for Q and QR classification) and also improves process Id 5

        * - :need:`wp__HSI`
          - n/a
          - OSS needing special HW is an extreme exception.

        * - :need:`wp__SW_REQ_INSPECT`
          - n/a
          - Checklist used in Pull Request Review

        * - :need:`wp__SW_COMPONENT_ARCHITECTURE`
          - <Link to issue>
          - <Reasoning for tailoring, needed for example in case of deficits in process Id 3&4 and complexity Ids 1&4>

        * - :need:`wp__SW_COMPONENT_SAFETY_ANALYSES`
          - <Link to issue>
          - <Reasoning for tailoring, could help arguing too high cyclomatic complexity covered by safety mechanisms>

        * - :need:`wp__SW_ARCH_VERIFICATION`
          - <Link to issue>
          - <Reasoning for tailoring, needed if also wp__SW_COMPONENT_ARCHITECTURE is required>

        * - :need:`wp__SW_IMPLEMENTATION`
          - n/a
          - If source code is modified, this is not a OSS qualification any more.

        * - :need:`wp__SW_UNIT_TEST`
          - <Link to issue>
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 3>

        * - :need:`wp__SW_CODE_INSPECT`
          - <Link to issue>
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 2>

        * - :need:`wp__SW_COMPONENT_INTEGRATION_TEST`
          - <Link to issue>
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 3&5>

        * - :need:`wp__SW_COMPONENT_TEST`
          - <Link to issue>
          - Always needed (for Q and QR classification)

        * - :need:`wp__sw_component_class`
          - <Link to issue>
          - Always needed as basis for tailoring.

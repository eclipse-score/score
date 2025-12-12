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

Module Safety Plan
******************

.. document:: Persistency Safety Plan
   :id: doc__persistency_safety_plan
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__module_safety_plan
   :tags: persistency

Functional Safety Management Context
====================================

This Safety Plan adds to the :need:`gd_guidl__saf_plan_definitions` all the module development relevant workproducts needed for ISO 26262 conformity.

Functional Safety Management Scope
==================================

This Safety Plan's scope is a SW module of the SW platform :ref:`module_documentation`.
The module consists of one or more SW components and will be qualified as a SEooC.

Functional Safety Management Roles
==================================

.. list-table:: Module roles
        :header-rows: 1

        * - Role
          - Assignee

        * - Safety Manager
          - Volker Häussler

        * - Module Project Manager (= Feature team lead)
          - Lars Bauhofer

Tailoring
=========

Additional to the tailoring in the SW platform project as defined in the :need:`gd_guidl__saf_plan_definitions` we define here the additional tailoring on module level.

| - Excluded for this module are additionally the following workproducts (and their related requirements):
|   - No work products excluded

Functional Safety Module Workproducts
=====================================

One set of workproducts for the module and one set for each component of the module:

Module Workproducts List
------------------------

.. list-table:: Module Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Link to process
          - Process status
          - Link to WP

        * - :need:`wp__module_safety_plan`
          - :need:`gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='gd_guidl__saf_plan_definitions')`
          - this document

        * - :need:`wp__module_safety_package`
          - :need:`gd_guidl__saf_package`
          - :ndf:`copy('status', need_id='gd_guidl__saf_package')`
          - this document (including the linked documentation)

        * - :need:`wp__fdr_reports` (module Safety Plan)
          - :need:`gd_chklst__safety_plan`
          - :ndf:`copy('status', need_id='gd_chklst__safety_plan')`
          - :need:`doc__persistency_safety_plan_fdr`

        * - :need:`wp__fdr_reports` (module Safety Package)
          - :need:`gd_chklst__safety_package`
          - :ndf:`copy('status', need_id='gd_chklst__safety_package')`
          - :need:`doc__persistency_safety_package_fdr`

        * - :need:`wp__fdr_reports` (module's Safety Analyses & DFA)
          - :need:`gd_guidl__safety_analysis`
          - :ndf:`copy('status', need_id='gd_guidl__safety_analysis')`
          - <Link to WP>

        * - :need:`wp__audit_report`
          - performed by external experts
          - n/a
          - <Link to WP>

        * - :need:`wp__module_safety_manual`
          - :need:`gd_temp__safety_manual`
          - :ndf:`copy('status', need_id='gd_temp__safety_manual')`
          - :need:`doc__persistency_safety_manual`

        * - :need:`wp__verification_module_ver_report`
          - :need:`gd_temp__mod_ver_report`
          - :ndf:`copy('status', need_id='gd_temp__mod_ver_report')`
          - :need:`doc__persistency_verification_report`

        * - :need:`wp__module_sw_release_note`
          - :need:`gd_temp__rel_mod_rel_note`
          - :ndf:`copy('status', need_id='gd_temp__rel_mod_rel_note')`
          - :need:`doc__persistency_release_note`

Component KVS Workproducts List
-------------------------------

.. list-table:: Component KVS Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Link to process
          - Process status
          - Link to WP

        * - :need:`wp__requirements_comp`
          - :need:`gd_temp__req_comp_req`
          - :ndf:`copy('status', need_id='gd_temp__req_comp_req')`
          - :need:`doc__persistency_kvs_requirements`

        * - :need:`wp__requirements_comp_aou`
          - :need:`gd_temp__req_aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
          - :need:`doc__persistency_kvs_requirements`

        * - :need:`wp__requirements_inspect`
          - :need:`gd_chklst__req_inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
          - Checklist used in Pull Request Review

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch_comp`
          - :ndf:`copy('status', need_id='gd_temp__arch_comp')`
          - :need:`doc__persistency_kvs_architecture`

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
          - Checklist used in Pull Request Review

        * - :need:`wp__sw_component_fmea`
          - :need:`wp__sw_component_fmea`
          - :ndf:`copy('status', need_id='gd_guidl__safety_analysis')`
          - :need:`doc__persistency_kvs_fmea`

        * - :need:`wp__sw_component_dfa`
          - :need:`wp__sw_component_dfa`
          - :ndf:`copy('status', need_id='gd_guidl__safety_analysis')`
          - :need:`doc__persistency_kvs_dfa`

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - <Link to WP>

        * - :need:`wp__verification_sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - <Link to WP>

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - Checklist used in Pull Request Review

        * - :need:`wp__verification_comp_int_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - <Link to WP>

        * - :need:`wp__sw_component_class`
          - :need:`gd_guidl__component_classification`
          - :ndf:`copy('status', need_id='gd_guidl__component_classification')`
          - :need:`doc__persistency_component_classification`


OSS (sub-)component qualification plan
======================================

For the selected OSS component the following workproducts will be implemented (and why):

If the OSS element is classified as
    - component, then the below table shall match the above, adding the reasoning for tailoring of work products according to the OSS component classification.
    - lower level component, then no workproducts additional to the component’s will be planned and activities below are part of the component’s issues.

.. list-table:: OSS (sub-)component Tiny JSON Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Reasoning for tailoring

        * - :need:`wp__requirements_comp`
          - Always needed (for Q and QR classification) and also improves process Id 2

        * - :need:`wp__requirements_comp_aou`
          - Always needed (for Q and QR classification) and also improves process Id 5

        * - :need:`wp__requirements_inspect`
          - <Reasoning for tailoring>

        * - :need:`wf__cr_mt_comparch`
          - <Reasoning for tailoring, needed for example in case of deficits in process Id 3&4 and complexity Ids 1&4>

        * - :need:`wp__sw_component_fmea`
          - <Reasoning for tailoring, could help arguing too high cyclomatic complexity covered by safety mechanisms>

        * - :need:`wp__sw_arch_verification`
          - <Reasoning for tailoring, needed if also wf__cr_mt_comparch is required>

        * - :need:`wp__sw_implementation`
          - Tailored - If source code is modified, this is not a OSS qualification any more.

        * - :need:`wp__verification_sw_unit_test`
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 3>

        * - :need:`wp__sw_implementation_inspection`
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 2>

        * - :need:`wp__verification_comp_int_test`
          - Always needed (for Q and QR classification)

        * - :need:`wp__sw_component_class`
          - Always needed as basis for tailoring.

Module Safety Package
=====================

To create the safety package (according to :need:`gd_guidl__saf_package`) the following
documents and work products status have to go to "valid" (after the relevant verification were performed).

Module Documents Status
-----------------------

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See :ref:`documents_docs_modules_persistency_docs`

Component Documents Status
--------------------------

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See :ref:`documents_docs_modules_persistency_components`

Component Requirements Status
-----------------------------

.. needtable::
   :filter: docname is not None and "persistency" in docname and "requirements" in docname
   :style: table
   :types: comp_req
   :tags: kvs
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

Component AoU Status
--------------------

.. needtable::
   :filter: docname is not None and "persistency" in docname and "requirements" in docname
   :style: table
   :types: aou_req
   :tags: kvs
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

Component Architecture Status
-----------------------------

.. needtable::
   :filter: docname is not None and "persistency" in docname and "architecture" in docname
   :style: table
   :types: comp_arc_sta; comp_arc_dyn
   :tags: kvs
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

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
          - Link to issue
          - Link to WP
          - WP status

        * - :need:`wp__module_safety_plan`
          - :need:`gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='gd_guidl__saf_plan_definitions')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C963
          - this document
          - valid

        * - :need:`wp__module_safety_package`
          - :need:`gd_guidl__saf_package`
          - :ndf:`copy('status', need_id='gd_guidl__saf_package')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C963
          - this document (including the linked documentation)
          - valid

        * - :need:`wp__fdr_reports` (module Safety Plan)
          - :need:`gd_chklst__safety_plan`
          - :ndf:`copy('status', need_id='gd_chklst__safety_plan')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C963
          - :need:`doc__persistency_safety_plan_fdr`
          - :ndf:`copy('status', need_id='doc__persistency_safety_plan_fdr')`

        * - :need:`wp__fdr_reports` (module Safety Package)
          - :need:`gd_chklst__safety_package`
          - :ndf:`copy('status', need_id='gd_chklst__safety_package')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C963
          - :need:`doc__persistency_safety_package_fdr`
          - :ndf:`copy('status', need_id='doc__persistency_safety_package_fdr')`

        * - :need:`wp__fdr_reports` (module's Safety Analyses & DFA)
          - :need:`gd_guidl__safety_analysis`
          - :ndf:`copy('status', need_id='gd_guidl__safety_analysis')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C965
          - :need:`doc__persistency_kvs_fmea`
          - :ndf:`copy('status', need_id='doc__persistency_kvs_fmea')`

        * - :need:`wp__audit_report`
          - performed by external experts
          - n/a
          - <Link to issue>
          - <Link to WP>
          - <WP status (manual)>

        * - :need:`wp__module_sw_build_config`
          - `gd_temp__software_development_plan`
          - `copy('status', need_id='doc__software_development_plan')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__module_safety_manual`
          - :need:`gd_temp__safety_manual`
          - :ndf:`copy('status', need_id='gd_temp__safety_manual')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C963
          - :need:`doc__persistency_safety_manual`
          - :ndf:`copy('status', need_id='doc__persistency_safety_manual')`

        * - :need:`wp__verification_module_ver_report`
          - :need:`gd_temp__mod_ver_report`
          - :ndf:`copy('status', need_id='gd_temp__mod_ver_report')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C964
          - :need:`doc__persistency_verification_report`
          - :ndf:`copy('status', need_id='doc__persistency_verification_report')`

        * - :need:`wp__module_sw_release_note`
          - :need:`gd_temp__rel_mod_rel_note`
          - :ndf:`copy('status', need_id='gd_temp__rel_mod_rel_note')`
          - <Link to issue>
          - :need:`doc__persistency_release_note`
          - :ndf:`copy('status', need_id='doc__persistency_release_note')`

Component <name> Workproducts List
----------------------------------

.. list-table:: Component <name> Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP/doc status

        * - :need:`wp__requirements_comp`
          - :need:`gd_temp__req_comp_req`
          - :ndf:`copy('status', need_id='gd_temp__req_comp_req')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C960
          - :need:`doc__persistency_kvs_requirements`
          - :ndf:`copy('status', need_id='doc__persistency_kvs_requirements')` & WP below

        * - :need:`wp__requirements_comp_aou`
          - :need:`gd_temp__req_aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C960
          - :need:`doc__persistency_kvs_requirements`
          - :ndf:`copy('status', need_id='doc__persistency_kvs_requirements')` & WP below

        * - :need:`wp__requirements_inspect`
          - :need:`gd_chklst__req_inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
          - n/a
          - Checklist used in Pull Request Review
          - n/a

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch_comp`
          - :ndf:`copy('status', need_id='gd_temp__arch_comp')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C1020
          - :need:`doc__persistency_kvs_architecture`
          - :ndf:`copy('status', need_id='doc__persistency_kvs_architecture')` & WP below

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
          - n/a
          - Checklist used in Pull Request Review
          - n/a

        * - :need:`wp__sw_component_fmea`
          - :need:`wp__sw_component_fmea`
          - :ndf:`copy('status', need_id='gd_guidl__safety_analysis')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C965
          - :need:`doc__persistency_kvs_fmea`
          - :ndf:`copy('status', need_id='doc__persistency_kvs_fmea')` & WP below

        * - :need:`wp__sw_component_dfa`
          - :need:`wp__sw_component_dfa`
          - :ndf:`copy('status', need_id='gd_guidl__safety_analysis')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C965
          - :need:`doc__persistency_kvs_dfa`
          - :ndf:`copy('status', need_id='doc__persistency_kvs_dfa')` & WP below

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C961
          - <Link to WP>
          - <automated>

        * - :need:`wp__verification_sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C964
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - n/a
          - Checklist used in Pull Request Review
          - n/a

        * - :need:`wp__verification_comp_int_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C964
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_component_class`
          - :need:`gd_guidl__component_classification`
          - :ndf:`copy('status', need_id='gd_guidl__component_classification')`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C963
          - :need:`doc__persistency_component_classification`
          - :ndf:`copy('status', need_id='doc__persistency_component_classification')`

Note: In case the component is a new development, :need:`wp__sw_component_class` shall be removed from the above list (and also from the folders).
In case an OSS element is used in the module, part 6 has to be filled out.

OSS (sub-)component qualification plan
======================================

For the selected OSS component the following workproducts will be implemented (and why):

If the OSS element is classified as a
    - component, then the below table shall match the above, adding the reasoning for tailoring of work products according to the OSS component classification.
    - lower level component, then no workproducts additional to the component’s will be planned and activities below are part of the component’s issues.

.. list-table:: OSS (sub-)component Tiny JSON Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Link to issue
          - Reasoning for tailoring

        * - :need:`wp__requirements_comp`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C960
          - Always needed (for Q and QR classification) and also improves process Id 2

        * - :need:`wp__requirements_comp_aou`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C960
          - Always needed (for Q and QR classification) and also improves process Id 5

        * - :need:`wp__requirements_inspect`
          - n/a
          - Checklist used in Pull Request Review

        * - :need:`wf__cr_mt_comparch`
          - <Link to issue>
          - <Reasoning for tailoring, needed for example in case of deficits in process Id 3&4 and complexity Ids 1&4>

        * - :need:`wp__sw_component_fmea`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C965
          - <Reasoning for tailoring, could help arguing too high cyclomatic complexity covered by safety mechanisms>

        * - :need:`wp__sw_arch_verification`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C964
          - <Reasoning for tailoring, needed if also wf__cr_mt_comparch is required>

        * - :need:`wp__sw_implementation`
          - n/a
          - If source code is modified, this is not a OSS qualification any more.

        * - :need:`wp__verification_sw_unit_test`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C964
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 3>

        * - :need:`wp__sw_implementation_inspection`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C961
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 2>

        * - :need:`wp__verification_comp_int_test`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C964
          - Always needed (for Q and QR classification)

        * - :need:`wp__sw_component_class`
          - https://github.com/eclipse-score/score/issues/952?issue=eclipse-score%7Cscore%7C963
          - Always needed as basis for tailoring.

Work Product Status (for Safety Package)
========================================

Component Requirements Status
-----------------------------

.. needtable::
   :filter: docname is not None and "persistency" in docname and "requirements" in docname
   :style: table
   :types: comp_req
   :tags: persistencykvs
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

Component AoU Status
--------------------

.. needtable::
   :filter: docname is not None and "persistency" in docname and "requirements" in docname
   :style: table
   :types: aou_req
   :tags: persistencykvs
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

Component Architecture Status
-----------------------------

.. needtable::
   :filter: docname is not None and "persistency" in docname and "requirements" in docname
   :style: table
   :types: comp_arc_sta; comp_arc_dyn
   :tags: persistencykvs
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

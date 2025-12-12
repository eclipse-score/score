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

.. document:: Orchestrator Safety Plan
   :id: doc__orchestrator_safety_plan
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__module_safety_plan
   :tags: orchestrator

Functional Safety Management Context
====================================

This Safety Plan adds to the project's :need:`wp__platform_safety_plan` all the module development relevant work products needed for ISO 26262 conformity.

Functional Safety Management Scope
==================================

This Safety Plan's scope is a SW module of the SW platform <link to module documentation in platform/modules/<modulename>/index.rst>.
The module consists of one or more SW components and will be qualified as a SEooC.

Functional Safety Management Roles
==================================

.. list-table:: Module roles
        :header-rows: 1

        * - Role
          - Assignee

        * - Safety Manager
          - Volker Häussler

        * - Module Project Manager
          - Naveen Mohanan

Tailoring
=========

Additional to the tailoring in the SW platform project as defined in the project's :need:`wp__platform_safety_plan` we define here the additional tailoring on module level.

- Excluded for this module are additionally the following work products (and their related requirements):

  - <work product/requirement> - <Argumentation why it is not needed or replaced by another work product or activity.>

Functional Safety Module Work products
======================================

One set of work products for the module and one set for each component of the module:

Module Work products List
-------------------------

.. list-table:: Module Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - :need:`wp__module_safety_plan`
          - :need:`gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='gd_guidl__saf_plan_definitions')`
          - <Link to issue>
          - this document
          - see above

        * - :need:`wp__module_safety_package`
          - :need:`gd_guidl__saf_package`
          - :ndf:`copy('status', need_id='gd_guidl__saf_package')`
          - <Link to issue>
          - this document (including the linked documentation)
          - see above (and below)

        * - :need:`wp__fdr_reports` (module Safety Plan)
          - :need:`gd_chklst__safety_plan`
          - :ndf:`copy('status', need_id='gd_chklst__safety_plan')`
          - <Link to issue>
          - :need:`doc__module_name_safety_plan_fdr`
          - :ndf:`copy('status', need_id='doc__module_name_safety_plan_fdr')`

        * - :need:`wp__fdr_reports` (module Safety Package)
          - :need:`gd_chklst__safety_package`
          - :ndf:`copy('status', need_id='gd_chklst__safety_package')`
          - <Link to issue>
          - :need:`doc__module_name_safety_package_fdr`
          - :ndf:`copy('status', need_id='doc__module_name_safety_package_fdr')`

        * - :need:`wp__fdr_reports` (module's Safety Analyses & DFA)
          - Safety Analysis FDR tbd
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

        * - :need:`wp__module_safety_manual`
          - :need:`gd_temp__safety_manual`
          - :ndf:`copy('status', need_id='gd_temp__safety_manual')`
          - <Link to issue>
          - :need:`doc__module_name_safety_manual`
          - :ndf:`copy('status', need_id='doc__module_name_safety_manual')`

        * - :need:`wp__verification_module_ver_report`
          - :need:`gd_temp__mod_ver_report`
          - :ndf:`copy('status', need_id='gd_temp__mod_ver_report')`
          - <Link to issue>
          - :need:`doc__module_name_verification_report`
          - :ndf:`copy('status', need_id='doc__module_name_verification_report')`

        * - :need:`wp__module_sw_release_note`
          - :need:`gd_temp__rel_mod_rel_note`
          - :ndf:`copy('status', need_id='gd_temp__rel_mod_rel_note')`
          - <Link to issue>
          - :need:`doc__module_name_release_note`
          - :ndf:`copy('status', need_id='doc__module_name_release_note')`

Component <name> Work products List
-----------------------------------

.. list-table:: Component <name> Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP/doc status

        * - :need:`wp__requirements_comp`
          - :need:`gd_temp__req_comp_req`
          - :ndf:`copy('status', need_id='gd_temp__req_comp_req')`
          - <Link to issue>
          - :need:`doc__component_name_requirements`
          - doc :ndf:`copy('status', need_id='doc__component_name_requirements')` & WP below

        * - :need:`wp__requirements_comp_aou`
          - :need:`gd_temp__req_aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
          - <Link to issue>
          - :need:`doc__component_name_requirements`
          - doc :ndf:`copy('status', need_id='doc__component_name_requirements')` & WP below

        * - :need:`wp__requirements_inspect`
          - :need:`gd_chklst__req_inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
          - <link to issue>
          - :need:`doc__component_name_req_inspection`
          - :ndf:`copy('status', need_id='doc__component_name_req_inspection')`

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch_comp`
          - :ndf:`copy('status', need_id='gd_temp__arch_comp')`
          - <Link to issue>
          - :need:`doc__component_name_architecture`
          - doc :ndf:`copy('status', need_id='doc__component_name_architecture')` & WP below

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
          - <link to issue>
          - :need:`doc__component_name_arc_inspection`
          - :ndf:`copy('status', need_id='doc__component_name_arc_inspection')`

        * - :need:`wp__sw_component_fmea`
          - :need:`gd_temp__comp_saf_fmea`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_fmea')`
          - <Link to issue>
          - :need:`doc__component_name_fmea`
          - doc :ndf:`copy('status', need_id='doc__component_name_fmea')` & WP below

        * - :need:`wp__sw_component_dfa`
          - :need:`gd_temp__comp_saf_dfa`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_dfa')`
          - <Link to issue>
          - :need:`doc__component_name_dfa`
          - doc :ndf:`copy('status', need_id='doc__component_name_dfa')` & WP below

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__verification_sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__verification_comp_int_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_component_class`
          - :need:`gd_guidl__component_classification`
          - :ndf:`copy('status', need_id='gd_guidl__component_classification')`
          - <Link to issue>
          - :need:`doc__component_name_comp_class`
          - :ndf:`copy('status', need_id='doc__component_name_comp_class')`

Note: In case the component is a new development, :need:`wp__sw_component_class` shall be removed from the above list (and also from the folders).
In case an OSS element is used in the module, part 6 has to be filled out.

OSS (sub-)component qualification plan
======================================

For the selected OSS component the following work products will be implemented (and why):

If the OSS element is classified as a
    - component, then the below table shall match the above, adding the reasoning for tailoring of work products according to the OSS component classification.
    - lower level component, then no work products additional to the component’s will be planned and activities below are part of the component’s issues.

.. list-table:: OSS (sub-)component <name> Work products
        :header-rows: 1

        * - Work product Id
          - Link to issue
          - Reasoning for tailoring

        * - :need:`wp__requirements_comp`
          - <Link to issue>
          - Always needed (for Q and QR classification) and also improves process Id 2

        * - :need:`wp__requirements_comp_aou`
          - <Link to issue>
          - Always needed (for Q and QR classification) and also improves process Id 5

        * - :need:`wp__requirements_inspect`
          - n/a
          - Checklist used in Pull Request Review

        * - :need:`wf__cr_mt_comparch`
          - <Link to issue>
          - <Reasoning for tailoring, needed for example in case of deficits in process Id 3&4 and complexity Ids 1&4>

        * - :need:`wp__sw_component_fmea`
          - <Link to issue>
          - <Reasoning for tailoring, could help arguing too high cyclomatic complexity covered by safety mechanisms>

        * - :need:`wp__sw_arch_verification`
          - <Link to issue>
          - <Reasoning for tailoring, needed if also wf__cr_mt_comparch is required>

        * - :need:`wp__sw_implementation`
          - n/a
          - If source code is modified, this is not a OSS qualification any more.

        * - :need:`wp__verification_sw_unit_test`
          - <Link to issue>
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 3>

        * - :need:`wp__sw_implementation_inspection`
          - <Link to issue>
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 2>

        * - :need:`wp__verification_comp_int_test`
          - <Link to issue>
          - Always needed (for Q and QR classification)

        * - :need:`wp__sw_component_class`
          - <Link to issue>
          - Always needed as basis for tailoring.

Work Product Status (for Safety Package)
========================================

Component Requirements Status
-----------------------------

.. needtable::
   :filter: "orchestrator" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: comp_req
   :tags: orchestrator
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

Component AoU Status
--------------------

.. needtable::
   :filter: "orchestrator" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: aou_req
   :tags: orchestrator
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

Component Architecture Status
-----------------------------

.. needtable::
   :filter: "component_name" in docname and "architecture" in docname and docname is not None
   :style: table
   :types: comp_arc_sta; comp_arc_dyn
   :tags: orchestrator
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

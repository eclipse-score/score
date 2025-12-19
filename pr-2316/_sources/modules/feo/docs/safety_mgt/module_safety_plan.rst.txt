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

.. document:: FEO Module Safety Plan
   :id: doc__feo_safety_plan
   :status: valid
   :security: NO
   :safety: ASIL_B
   :realizes: wp__module_safety_plan
   :tags: module_feo


FEO Module Safety Plan
**********************

Functional Safety Management Context
====================================

This Safety Plan adds to the :need:`doc__platform_safety_plan` all the module development relevant work products needed for ISO 26262 conformity.

Functional Safety Management Scope
==================================

This Safety Plan's scope is a SW module :ref:`feo_module_documentation` of the SW platform.
The module consists of one or more SW components and will be qualified as a SEooC.

Functional Safety Management Roles
==================================

.. list-table:: Module roles
        :header-rows: 1

        * - Role
          - Assignee

        * - Safety Manager
          - Markus Schu

        * - Module Project Manager (= Feature team lead)
          - Johannes Glamsch

Tailoring
=========

Additional to the tailoring in the SW platform project as defined in the :need:`doc__platform_safety_plan` we define here the additional tailoring on module level.

- Excluded for this module are additionally the following work products (and their related requirements):
  - No work products excluded

Functional Safety Module Work Products
======================================

One set of work products for the module and one set for each component of the module:

FEO Module Work Products List
-----------------------------

.. list-table:: Module Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - :need:`wp__module_safety_plan`
          - :need:`gd_guidl__saf_plan_definitions`, :need:`gd_temp__module_safety_plan`
          - :ndf:`copy('status', need_id='gd_guidl__saf_plan_definitions')`
          - https://github.com/eclipse-score/score/issues/1658
          - this document
          - see above

        * - :need:`wp__module_safety_package`
          - :need:`gd_guidl__saf_package`
          - :ndf:`copy('status', need_id='gd_guidl__saf_package')`
          - https://github.com/eclipse-score/score/issues/1659
          - this document (including the linked documentation)
          - see above (and below), safety manual

        * - :need:`wp__fdr_reports` (module Safety Plan)
          - :need:`gd_chklst__safety_plan`
          - :ndf:`copy('status', need_id='gd_chklst__safety_plan')`
          - https://github.com/eclipse-score/score/issues/1660
          - :need:`doc__feo_safety_plan_fdr`
          - :ndf:`copy('status', need_id='doc__feo_safety_plan_fdr')`

        * - :need:`wp__fdr_reports` (module Safety Package)
          - :need:`gd_chklst__safety_package`
          - :ndf:`copy('status', need_id='gd_chklst__safety_package')`
          - https://github.com/eclipse-score/score/issues/1660
          - :need:`doc__feo_safety_package_fdr`
          - :ndf:`copy('status', need_id='doc__feo_safety_package_fdr')`

        * - :need:`wp__fdr_reports` (module's Safety Analyses & DFA)
          - :need:`gd_chklst__safety_analysis`
          - :ndf:`copy('status', need_id='gd_chklst__safety_analysis')`
          - https://github.com/eclipse-score/score/issues/1660
          - :need:`doc__safety_analysis_inspection_component_feo`
          - :ndf:`copy('status', need_id='doc__safety_analysis_inspection_component_feo')`

        * - :need:`wp__audit_report`
          - performed by external experts
          - n/a
          - https://github.com/eclipse-score/score/issues/1661
          - <Link to WP>
          - <WP status (manual)>

        * - :need:`wp__module_sw_build_config`
          - :need:`gd_temp__software_development_plan`
          - :ndf:`copy('status', need_id='gd_temp__software_development_plan')`
          - https://github.com/eclipse-score/score/issues/1662
          - <Link to WP>
          - <automated>

        * - :need:`wp__module_safety_manual`
          - :need:`gd_temp__safety_manual`
          - :ndf:`copy('status', need_id='gd_temp__safety_manual')`
          - https://github.com/eclipse-score/score/issues/1663
          - :need:`doc__feo_safety_manual`
          - :ndf:`copy('status', need_id='doc__feo_safety_manual')`

        * - :need:`wp__verification_module_ver_report`
          - :need:`gd_temp__mod_ver_report`
          - :ndf:`copy('status', need_id='gd_temp__mod_ver_report')`
          - https://github.com/eclipse-score/score/issues/1665
          - :need:`doc__feo_verification_report`
          - :ndf:`copy('status', need_id='doc__feo_verification_report')`

        * - :need:`wp__module_sw_release_note`
          - :need:`gd_temp__rel_mod_rel_note`
          - :ndf:`copy('status', need_id='gd_temp__rel_mod_rel_note')`
          - https://github.com/eclipse-score/score/issues/1666
          - :need:`doc__feo_release_note`
          - :ndf:`copy('status', need_id='doc__feo_release_note')`

FEO Component Work Products List
--------------------------------

.. list-table:: FEO Component Work Products List
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
          - https://github.com/eclipse-score/score/issues/1668
          - :need:`doc__component_feo_requirements`
          - doc :ndf:`copy('status', need_id='doc__component_feo_requirements')` & WP below

        * - :need:`wp__requirements_comp_aou`
          - :need:`gd_temp__req_aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
          - https://github.com/eclipse-score/score/issues/1669
          - :need:`doc__component_feo_aou_reqs`
          - doc :ndf:`copy('status', need_id='doc__component_feo_aou_reqs')` & WP below

        * - :need:`wp__requirements_inspect`
          - :need:`gd_chklst__req_inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
          - https://github.com/eclipse-score/score/issues/1670
          - :need:`doc__req_inspection_component_feo`
          - doc :ndf:`copy('status', need_id='doc__req_inspection_component_feo')`

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch_comp`
          - :ndf:`copy('status', need_id='gd_temp__arch_comp')`
          - https://github.com/eclipse-score/score/issues/1671
          - :need:`doc__component_feo_architecture`
          - doc :ndf:`copy('status', need_id='doc__component_feo_architecture')` & WP below

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
          - https://github.com/eclipse-score/score/issues/1672
          - :need:`doc__arch_inspection_component_feo`
          - doc :ndf:`copy('status', need_id='doc__arch_inspection_component_feo')`

        * - :need:`wp__sw_component_fmea`
          - :need:`gd_temp__comp_saf_fmea`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_fmea')`
          - https://github.com/eclipse-score/score/issues/1673
          - :need:`doc__component_feo_fmea`
          - doc :ndf:`copy('status', need_id='doc__component_feo_fmea')` & WP below

        * - :need:`wp__sw_component_dfa`
          - :need:`gd_temp__comp_saf_fmea`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_fmea')`
          - https://github.com/eclipse-score/score/issues/1674
          - :need:`doc__component_feo_dfa`
          - doc :ndf:`copy('status', need_id='doc__component_feo_dfa')` & WP below

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - https://github.com/eclipse-score/score/issues/1675
          - <Link to WP>
          - <automated>

        * - :need:`wp__verification_sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - https://github.com/eclipse-score/score/issues/1676
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - https://github.com/eclipse-score/score/issues/1677
          - :need:`doc__impl_inspection_component_feo`
          - :ndf:`copy('status', need_id='doc__impl_inspection_component_feo')`

        * - :need:`wp__verification_comp_int_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - https://github.com/eclipse-score/score/issues/1667
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_component_class`
          - :need:`gd_guidl__component_classification`
          - :ndf:`copy('status', need_id='gd_guidl__component_classification')`
          - https://github.com/eclipse-score/score/issues/1679
          - :need:`doc__feo_comp_class`
          - :ndf:`copy('status', need_id='doc__feo_comp_class')`

Note: In case the component is a new development, :need:`wp__sw_component_class` shall be removed from the above list (and also from the folders).
In case an OSS element is used in the module, part 6 has to be filled out, depending on the component classification results.

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
   :filter: docname is not None and "feo" in docname and "requirements" in docname
   :style: table
   :types: comp_req
   :tags: component_feo
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

Component AoU Status
--------------------

.. needtable::
   :filter: docname is not None and "feo" in docname and "requirements" in docname
   :style: table
   :types: aou_req
   :tags: component_feo
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

Component Architecture Status
-----------------------------

.. needtable::
   :filter: docname is not None and "feo" in docname and "architecture" in docname
   :style: table
   :types: comp_arc_sta; comp_arc_dyn
   :tags: component_feo
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

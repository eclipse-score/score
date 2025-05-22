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

.. note:: Document header

.. document:: [Your Module Name] Safety Plan
   :id: doc__module_name_safety_plan
   :status: draft
   :safety: ASIL_B
   :realizes: wp__module_safety_plan
   :tags: template

.. attention::
    The above directive must be updated according to your Module.

    - Modify ``Your Module Name`` to be your Module Name
    - Modify ``id`` to be your Module Name in upper snake case preceded by ``doc_`` and succeeded by ``safety_plan``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs


Functional Safety Management Context
====================================

This Safety Plan adds to the :ref:`process_safety_management` all the module development relevant workproducts needed for ISO 26262 conformity.

Functional Safety Management Scope
==================================

This Safety Plan's scope is a SW module of the SW platform <link to module documentation in platform/modules/<modulename>/index.rst>.
The module consists of one or more SW components and will be qualified as a SEooC.

Functional Safety Management Roles
==================================

+---------------------------+--------------------------------------------------------+
| Safety Manager            | <link to Module's Safety Manager assignment or name>   |
+---------------------------+--------------------------------------------------------+
| Project Manager           | <link to Module's Project Manager assignment or name>  |
+---------------------------+--------------------------------------------------------+

Tailoring
=========

Additional to the tailoring in the SW platform project as defined in the :ref:`process_safety_management` we define here the additional tailoring on module level.

- Excluded for this module are additionally the following workproducts (and their related requirements):
  - <ISO 26262 reference>: <workproduct/requirement> - <Argumentation why it is not needed or replaced by another workproduct or activity.>

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

        * - :need:`wp__module_sw_build_config`
          - :need:`doc__software_development_plan`
          - :ndf:`copy('status', need_id='doc__software_development_plan')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__module_safety_manual`
          - :need:`gd_temp__safety_manual`
          - :ndf:`copy('status', need_id='gd_temp__safety_manual')`
          - <Link to issue>
          - :need:`doc__module_name_safety_manual`
          - :ndf:`copy('status', need_id='doc__module_name_safety_manual')`

        * - :need:`wp__verification__module_ver_report`
          - :need:`gd_temp__mod_ver_report`
          - :ndf:`copy('status', need_id='gd_temp__mod_ver_report')`
          - <Link to issue>
          - :need:`doc__module_name_verification_report`
          - :ndf:`copy('status', need_id='doc__module_name_verification_report')`

        * - :need:`wp__module_sw_release_note`
          - :need:`gd_temp__rel__mod_rel_note`
          - :ndf:`copy('status', need_id='gd_temp__rel__mod_rel_note')`
          - <Link to issue>
          - :need:`doc__module_name_release_note`
          - :ndf:`copy('status', need_id='doc__module_name_release_note')`

Component <name> Workproducts List
----------------------------------

.. list-table:: Component <name> Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - :need:`wp__requirements__comp`
          - :need:`gd_temp__req__comp_req`
          - :ndf:`copy('status', need_id='gd_temp__req__comp_req')`
          - <Link to issue>
          - :doc:`../../component_name/docs/requirements/index`
          - see below

        * - :need:`wp__requirements__comp_aou`
          - :need:`gd_temp__req__aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req__aou_req')`
          - <Link to issue>
          - :doc:`../../component_name/docs/requirements/index`
          - see below

        * - :need:`wp__hsi`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__requirements__inspect`
          - :need:`gd_chklst__req__inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req__inspection')`
          - n/a
          - Checklist used in Pull Request Review
          - n/a

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch__comp`
          - :ndf:`copy('status', need_id='gd_temp__arch__comp')`
          - <Link to issue>
          - :doc:`../../component_name/docs/architecture/index`
          - see below

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch__inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch__inspection_checklist')`
          - n/a
          - Checklist used in Pull Request Review
          - n/a

        * - :need:`wp__sw_component_safety_analysis`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - :doc:`../../component_name/docs/safety_analysis/fmea`
          - <automated>

        * - :need:`wp__sw_component_dfa`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - :doc:`../../component_name/docs/safety_analysis/dfa`
          - <automated>

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__verification__sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - n/a
          - Checklist used in Pull Request Review
          - n/a

        * - :need:`wp__verification__comp_int_test`
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

For the selected OSS component the following workproducts will be implemented (and why):

If the OSS element is classified as a
    - component, then the below table shall match the above, adding the reasoning for tailoring of work products according to the OSS component classification.
    - lower level component, then no workproducts additional to the component’s will be planned and activities below are part of the component’s issues.

.. list-table:: OSS (sub-)component <name> Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Link to issue
          - Reasoning for tailoring

        * - :need:`wp__requirements__comp`
          - <Link to issue>
          - Always needed (for Q and QR classification) and also improves process Id 2

        * - :need:`wp__requirements__comp_aou`
          - <Link to issue>
          - Always needed (for Q and QR classification) and also improves process Id 5

        * - :need:`wp__hsi`
          - n/a
          - OSS needing special HW is an extreme exception.

        * - :need:`wp__requirements__inspect`
          - n/a
          - Checklist used in Pull Request Review

        * - :need:`wf__cr_mt_comparch`
          - <Link to issue>
          - <Reasoning for tailoring, needed for example in case of deficits in process Id 3&4 and complexity Ids 1&4>

        * - :need:`wp__sw_component_safety_analysis`
          - <Link to issue>
          - <Reasoning for tailoring, could help arguing too high cyclomatic complexity covered by safety mechanisms>

        * - :need:`wp__sw_arch_verification`
          - <Link to issue>
          - <Reasoning for tailoring, needed if also wf__cr_mt_comparch is required>

        * - :need:`wp__sw_implementation`
          - n/a
          - If source code is modified, this is not a OSS qualification any more.

        * - :need:`wp__verification__sw_unit_test`
          - <Link to issue>
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 3>

        * - :need:`wp__sw_implementation_inspection`
          - <Link to issue>
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 2>

        * - :need:`wp__verification__comp_int_test`
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
   :style: table
   :types: comp_req
   :tags: component_name
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

Component AoU Status
--------------------

.. needtable::
   :style: table
   :types: aou_req
   :tags: component_name
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

Component Architecture Status
-----------------------------

.. needtable::
   :style: table
   :types: comp_arc_sta; comp_arc_dyn
   :tags: component_name
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

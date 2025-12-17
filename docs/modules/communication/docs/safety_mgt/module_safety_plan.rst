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

.. document:: Communication Safety Plan
   :id: doc__communication_safety_plan
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__module_safety_plan



Functional Safety Management Context
====================================

This Safety Plan adds to the :need:`doc__score_platform_safety_plan` all the module development relevant work products needed for ISO 26262 conformity.

Functional Safety Management Scope
==================================

This Safety Plan's scope is a SW module of the SW platform :ref:`communication_module_docs`.
The module consists of one or more SW components and will be qualified as a SEooC.

Functional Safety Management Roles
==================================

.. list-table:: Module roles
        :header-rows: 1

        * - Role
          - Assignee

        * - Safety Manager
          - Alexander Schemmel

        * - Module Project Manager (= Feature team lead)
          - Committers of feature team see `Communication FT <https://github.com/eclipse-score/communication/blob/main/.github/CODEOWNERS>`_

Tailoring
=========

Additional to the tailoring in the SW platform project as defined in the :need:`doc__score_platform_safety_plan` we define here the additional tailoring on module level.

- Excluded for this module are additionally the following work products (and their related requirements):

  - :need:`wp__requirements_inspect`: in version 0.5 the inspections have to be done by the user
  - :need:`wp__sw_arch_verification`: in version 0.5 the inspections have to be done by the user
  - :need:`wp__fdr_reports` (module's Safety Analyses & DFA): in version 0.5 the reviews have to be done by the user

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
          - :need:`doc__communication_safety_plan_fdr`

        * - :need:`wp__fdr_reports` (module Safety Package)
          - :need:`gd_chklst__safety_package`
          - :ndf:`copy('status', need_id='gd_chklst__safety_package')`
          - :need:`doc__communication_safety_package_fdr`

        * - :need:`wp__fdr_reports` (module's Safety Analyses & DFA)
          - :need:`gd_chklst__safety_analysis`
          - :ndf:`copy('status', need_id='gd_chklst__safety_analysis')`
          - tailored

        * - :need:`wp__audit_report`
          - performed by external experts
          - n/a
          - <Link to WP>

        * - :need:`wp__module_safety_manual`
          - :need:`gd_temp__safety_manual`
          - :ndf:`copy('status', need_id='gd_temp__safety_manual')`
          - :need:`doc__communication_safety_manual`

        * - :need:`wp__verification_module_ver_report`
          - :need:`gd_temp__mod_ver_report`
          - :ndf:`copy('status', need_id='gd_temp__mod_ver_report')`
          - :need:`doc__communication_verification_report`

        * - :need:`wp__module_sw_release_note`
          - :need:`gd_temp__rel_mod_rel_note`
          - :ndf:`copy('status', need_id='gd_temp__rel_mod_rel_note')`
          - :need:`doc__communication_release_note`

Component lola Work products List
---------------------------------

.. list-table:: Component lola Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - :need:`wp__requirements_comp`
          - :need:`gd_temp__req_comp_req`
          - :ndf:`copy('status', need_id='gd_temp__req_comp_req')`
          - :need:`doc__lola_requirements`

        * - :need:`wp__requirements_comp_aou`
          - :need:`gd_temp__req_aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
          - :need:`doc__communication_aou`

        * - :need:`wp__requirements_inspect`
          - :need:`gd_chklst__req_inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
          - tailored

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch_comp`
          - :ndf:`copy('status', need_id='gd_temp__arch_comp')`
          - :need:`doc__lola_architecture`

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
          - tailored

        * - :need:`wp__sw_component_fmea`
          - :need:`gd_temp__comp_saf_fmea`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_fmea')`
          - :need:`doc__lola_fmea`

        * - :need:`wp__sw_component_dfa`
          - :need:`gd_temp__comp_saf_dfa`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_dfa')`
          - :need:`doc__lola_dfa`

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - `lola/.h/.cpp <https://github.com/eclipse-score/communication/blob/main/score/mw/com>`_, :need:`doc__lola_detailed_design`

        * - :need:`wp__verification_sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - `lola/test.cpp <https://github.com/eclipse-score/communication/blob/main/score/mw/com>`_

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - External process

        * - :need:`wp__verification_comp_int_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - <Link to WP>

        * - :need:`wp__sw_component_class`
          - :need:`gd_guidl__component_classification`
          - :ndf:`copy('status', need_id='gd_guidl__component_classification')`
          - :need:`doc__lola_comp_class`

Module Safety Package
=====================

To create the safety package (according to :need:`gd_guidl__saf_package`) the following
documents and work products status have to go to "valid" (after the relevant verification were performed).

Module Documents Status
-----------------------

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See :ref:`documents_docs_modules_communication_docs`

Component Documents Status
--------------------------

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See :ref:`documents_docs_modules_communication_components`

Component Requirements Status
-----------------------------

not documented as needs, `lola trlc <https://github.com/eclipse-score/communication/blob/main/score/mw/com/requirements/component_requirements/component_requirements_ipc.trlc>`_
shows no status attribute

Component AoU Status
--------------------

.. needtable::
   :filter: "communication" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: aou_req
   :tags: communication
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

Component Architecture Status
-----------------------------

see document link :need:`doc__lola_architecture` (as above)

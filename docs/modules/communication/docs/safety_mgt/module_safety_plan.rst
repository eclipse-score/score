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

.. document:: Communication Safety Plan
   :id: doc__communication_safety_plan
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__module_safety_plan



Functional Safety Management Context
====================================

This Safety Plan adds to the :need:`doc__platform_safety_plan` all the module development relevant work products needed for ISO 26262 conformity.

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

Additional to the tailoring in the SW platform project as defined in the :need:`doc__platform_safety_plan` we define here the additional tailoring on module level.

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
          - Link to issue
          - Link to WP
          - WP status

        * - :need:`wp__module_safety_plan`
          - :need:`gd_guidl__saf_plan_definitions`
          - :ndf:`copy('status', need_id='gd_guidl__saf_plan_definitions')`
          - n/a
          - this document
          - see above

        * - :need:`wp__module_safety_package`
          - :need:`gd_guidl__saf_package`
          - :ndf:`copy('status', need_id='gd_guidl__saf_package')`
          - n/a
          - this document (including the linked documentation)
          - see above (and below)

        * - :need:`wp__fdr_reports` (module Safety Plan)
          - :need:`gd_chklst__safety_plan`
          - :ndf:`copy('status', need_id='gd_chklst__safety_plan')`
          - <Link to issue>
          - :need:`doc__communication_safety_plan_fdr`
          - :ndf:`copy('status', need_id='doc__communication_safety_plan_fdr')`

        * - :need:`wp__fdr_reports` (module Safety Package)
          - :need:`gd_chklst__safety_package`
          - :ndf:`copy('status', need_id='gd_chklst__safety_package')`
          - <Link to issue>
          - :need:`doc__communication_safety_package_fdr`
          - :ndf:`copy('status', need_id='doc__communication_safety_package_fdr')`

        * - :need:`wp__fdr_reports` (module's Safety Analyses & DFA)
          - Safety Analysis FDR tbd
          - <automated>
          - tailored
          - n/a
          - n/a

        * - :need:`wp__audit_report`
          - performed by external experts
          - n/a
          - `#77 <https://github.com/eclipse-score/process_description/issues/77>`_
          - <Link to WP>
          - <WP status (manual)>

        * - :need:`wp__module_safety_manual`
          - :need:`gd_temp__safety_manual`
          - :ndf:`copy('status', need_id='gd_temp__safety_manual')`
          - <Link to issue>
          - :need:`doc__communication_safety_manual`
          - :ndf:`copy('status', need_id='doc__communication_safety_manual')`

        * - :need:`wp__verification_module_ver_report`
          - :need:`gd_temp__mod_ver_report`
          - :ndf:`copy('status', need_id='gd_temp__mod_ver_report')`
          - <Link to issue>
          - :need:`doc__communication_verification_report`
          - :ndf:`copy('status', need_id='doc__communication_verification_report')`

        * - :need:`wp__module_sw_release_note`
          - :need:`gd_temp__rel_mod_rel_note`
          - :ndf:`copy('status', need_id='gd_temp__rel_mod_rel_note')`
          - `#1925 <https://github.com/eclipse-score/score/issues/1925>`_
          - :need:`doc__communication_release_note`
          - :ndf:`copy('status', need_id='doc__communication_release_note')`

Component lola Work products List
---------------------------------

.. list-table:: Component lola Work products
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
          - n/a
          - `lola trlc <https://github.com/eclipse-score/communication/blob/main/score/mw/com/requirements/component_requirements/component_requirements_ipc.trlc>`_
          - valid

        * - :need:`wp__requirements_comp_aou`
          - :need:`gd_temp__req_aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
          - `#1987 <https://github.com/eclipse-score/score/pull/1987>`_
          - `lola/aou <https://github.com/eclipse-score/score/docs/modules/communication/docs/requirements/aou_req.rst>`_
          - in progress

        * - :need:`wp__requirements_inspect`
          - :need:`gd_chklst__req_inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
          - tailored
          - n/a
          - n/a

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch_comp`
          - :ndf:`copy('status', need_id='gd_temp__arch_comp')`
          - n/a
          - :need:`doc__lola_architecture`
          - :ndf:`copy('status', need_id='doc__lola_architecture')`

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
          - tailored
          - n/a
          - n/a

        * - :need:`wp__sw_component_fmea`
          - :need:`gd_temp__comp_saf_fmea`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_fmea')`
          - <Link to issue>
          - :need:`doc__lola_fmea`
          - :ndf:`copy('status', need_id='doc__lola_fmea')`

        * - :need:`wp__sw_component_dfa`
          - :need:`gd_temp__comp_saf_dfa`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_dfa')`
          - <Link to issue>
          - :need:`doc__lola_dfa`
          - :ndf:`copy('status', need_id='doc__lola_dfa')`

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - n/a
          - `lola/.h/.cpp <https://github.com/eclipse-score/communication/blob/main/score/mw/com>`_, `lola/design <https://github.com/eclipse-score/communication/blob/main/score/mw/com/design>`_
          - valid

        * - :need:`wp__verification_sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - n/a
          - `lola/test.cpp <https://github.com/eclipse-score/communication/blob/main/score/mw/com>`_
          - valid

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - n/a
          - External process
          - n/a

        * - :need:`wp__verification_comp_int_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_component_class`
          - :need:`gd_guidl__component_classification`
          - :ndf:`copy('status', need_id='gd_guidl__component_classification')`
          - n/a
          - :need:`doc__lola_comp_class`
          - :ndf:`copy('status', need_id='doc__lola_comp_class')`

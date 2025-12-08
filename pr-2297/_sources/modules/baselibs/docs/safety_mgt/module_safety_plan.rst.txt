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

.. document:: Baselibs Safety Plan
   :id: doc__baselibs_safety_plan
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__module_safety_plan


Functional Safety Management Context
====================================

This Safety Plan adds to the :need:`doc__platform_safety_plan` all the module development relevant work products needed for ISO 26262 conformity.

Functional Safety Management Scope
==================================

This Safety Plan's scope is a SW module of the SW platform :ref:`baselibs_module_docs`.
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
          - Andrey Babanin

Tailoring
=========

Additional to the tailoring in the SW platform project as defined in the :need:`doc__platform_safety_plan`  we define here the additional tailoring on module level.

- Excluded for this module are additionally the following work products (and their related requirements):
  - :need:`wp__module_sw_build_config` - Baselibs is a collection of libraries, so this work product is specific for every component.

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
          - `#1255 <https://github.com/eclipse-score/score/issues/1255>`_
          - this document
          - see above

        * - :need:`wp__module_safety_package`
          - :need:`gd_guidl__saf_package`
          - :ndf:`copy('status', need_id='gd_guidl__saf_package')`
          - `#1255 <https://github.com/eclipse-score/score/issues/1255>`_
          - this document (including the linked documentation)
          - see above (and below)

        * - :need:`wp__fdr_reports` (module Safety Plan)
          - :need:`gd_chklst__safety_plan`
          - :ndf:`copy('status', need_id='gd_chklst__safety_plan')`
          - `#1255 <https://github.com/eclipse-score/score/issues/1255>`_
          - :need:`doc__baselibs_safety_plan_fdr`
          - :ndf:`copy('status', need_id='doc__baselibs_safety_plan_fdr')`

        * - :need:`wp__fdr_reports` (module Safety Package)
          - :need:`gd_chklst__safety_package`
          - :ndf:`copy('status', need_id='gd_chklst__safety_package')`
          - `#1255 <https://github.com/eclipse-score/score/issues/1255>`_
          - :need:`doc__baselibs_safety_package_fdr`
          - :ndf:`copy('status', need_id='doc__baselibs_safety_package_fdr')`

        * - :need:`wp__fdr_reports` (module's Safety Analyses & DFA)
          - Safety Analysis FDR tbd
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__audit_report`
          - performed by external experts
          - n/a
          - `#77 <https://github.com/eclipse-score/process_description/issues/77>`_
          - <Link to WP>
          - <WP status (manual)>

        * - :need:`wp__module_safety_manual`
          - :need:`gd_temp__safety_manual`
          - :ndf:`copy('status', need_id='gd_temp__safety_manual')`
          - `#1255 <https://github.com/eclipse-score/score/issues/1255>`_
          - :need:`doc__baselibs_safety_manual`
          - :ndf:`copy('status', need_id='doc__baselibs_safety_manual')`

        * - :need:`wp__verification_module_ver_report`
          - :need:`gd_temp__mod_ver_report`
          - :ndf:`copy('status', need_id='gd_temp__mod_ver_report')`
          - `#1255 <https://github.com/eclipse-score/score/issues/1255>`_
          - :need:`doc__baselibs_verification_report`
          - :ndf:`copy('status', need_id='doc__baselibs_verification_report')`

        * - :need:`wp__module_sw_release_note`
          - :need:`gd_temp__rel_mod_rel_note`
          - :ndf:`copy('status', need_id='gd_temp__rel_mod_rel_note')`
          - `#1255 <https://github.com/eclipse-score/score/issues/1255>`_
          - :need:`doc__baselibs_release_note`
          - :ndf:`copy('status', need_id='doc__baselibs_release_note')`


Component bitmanipulation Work products List
--------------------------------------------

.. list-table:: Component bitmanipulation Work products
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
          - `#1719 <https://github.com/eclipse-score/score/issues/1719>`_
          - :need:`doc__bitmanipulation_requirements`
          - :ndf:`copy('status', need_id='doc__bitmanipulation_requirements')`

        * - :need:`wp__requirements_comp_aou`
          - :need:`gd_temp__req_aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
          - <Link to issue>
          - :need:`doc__bitmanipulation_requirements`
          - :ndf:`copy('status', need_id='doc__bitmanipulation_requirements')`

        * - :need:`wp__requirements_inspect`
          - :need:`gd_chklst__req_inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch_comp`
          - :ndf:`copy('status', need_id='gd_temp__arch_comp')`
          - `#1822 <https://github.com/eclipse-score/score/issues/1822>`_
          - :need:`doc__bitmanipulation_architecture`
          - :ndf:`copy('status', need_id='doc__bitmanipulation_architecture')`

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_component_fmea`
          - :need:`gd_temp__comp_saf_fmea`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_fmea')`
          - <Link to issue>
          - :need:`doc__bitmanipulation_fmea`
          - :ndf:`copy('status', need_id='doc__bitmanipulation_fmea')`

        * - :need:`wp__sw_component_dfa`
          - :need:`gd_temp__comp_saf_dfa`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_dfa')`
          - <Link to issue>
          - :need:`doc__bitmanipulation_dfa`
          - :ndf:`copy('status', need_id='doc__bitmanipulation_dfa')`

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - n/a
          - `.h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/bitmanipulation>`_, `design <https://github.com/eclipse-score/baselibs/tree/main/score/bitmanipulation/design>`_
          - valid

        * - :need:`wp__verification_sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - n/a
          - `test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/bitmanipulation>`_
          - valid

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - <Link to issue>
          - <Link to WP>
          - <manual>

        * - :need:`wp__verification_comp_int_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - n/a
          - component integration not needed (no sub-components and units are independent)
          - n/a

        * - :need:`wp__module_sw_build_config`
          - :need:`gd_temp__software_development_plan`
          - :ndf:`copy('status', need_id='gd_temp__software_development_plan')`
          - n/a
          - `BUILD <https://github.com/eclipse-score/baselibs/blob/main/score/bitmanipulation/BUILD>`_
          - valid


Component containers Work products List
---------------------------------------

.. list-table:: Component containers Work products
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
          - `#1718 <https://github.com/eclipse-score/score/issues/1718>`_
          - :need:`doc__containers_lib_requirements`
          - :ndf:`copy('status', need_id='doc__containers_lib_requirements')`

        * - :need:`wp__requirements_comp_aou`
          - :need:`gd_temp__req_aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
          - <Link to issue>
          - :need:`doc__containers_lib_requirements`
          - :ndf:`copy('status', need_id='doc__containers_lib_requirements')`

        * - :need:`wp__requirements_inspect`
          - :need:`gd_chklst__req_inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch_comp`
          - :ndf:`copy('status', need_id='gd_temp__arch_comp')`
          - `#1824 <https://github.com/eclipse-score/score/issues/1824>`_
          - :need:`doc__containers_architecture`
          - :ndf:`copy('status', need_id='doc__containers_architecture')`

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_component_fmea`
          - :need:`gd_temp__comp_saf_fmea`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_fmea')`
          - <Link to issue>
          - :need:`doc__containers_fmea`
          - :ndf:`copy('status', need_id='doc__containers_fmea')`

        * - :need:`wp__sw_component_dfa`
          - :need:`gd_temp__comp_saf_dfa`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_dfa')`
          - <Link to issue>
          - :need:`doc__containers_dfa`
          - :ndf:`copy('status', need_id='doc__containers_dfa')`

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - n/a
          - `containers .h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/containers>`_, `containers/design <https://github.com/eclipse-score/baselibs/tree/main/score/containers/design>`_
          - draft

        * - :need:`wp__verification_sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - n/a
          - `containers/test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/containers>`_
          - valid

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - <Link to issue>
          - <Link to WP>
          - <manual>

        * - :need:`wp__verification_comp_int_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - n/a
          - component integration not needed (no sub-components and units are independent)
          - n/a

        * - :need:`wp__module_sw_build_config`
          - :need:`gd_temp__software_development_plan`
          - :ndf:`copy('status', need_id='gd_temp__software_development_plan')`
          - n/a
          - `containers/BUILD <https://github.com/eclipse-score/baselibs/blob/main/score/containers/BUILD>`_
          - valid


Component filesystem Work products List
---------------------------------------

.. list-table:: Component filesystem Work products
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
          - `#1720 <https://github.com/eclipse-score/score/issues/1720>`_
          - :need:`doc__filesystem_lib_requirements`
          - :ndf:`copy('status', need_id='doc__filesystem_lib_requirements')`

        * - :need:`wp__requirements_comp_aou`
          - :need:`gd_temp__req_aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
          - <Link to issue>
          - :need:`doc__filesystem_lib_requirements`
          - :ndf:`copy('status', need_id='doc__filesystem_lib_requirements')`

        * - :need:`wp__requirements_inspect`
          - :need:`gd_chklst__req_inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch_comp`
          - :ndf:`copy('status', need_id='gd_temp__arch_comp')`
          - `#1823 <https://github.com/eclipse-score/score/issues/1823>`_
          - :need:`doc__filesystem_architecture`
          - :ndf:`copy('status', need_id='doc__filesystem_architecture')`

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_component_fmea`
          - :need:`gd_temp__comp_saf_fmea`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_fmea')`
          - <Link to issue>
          - :need:`doc__filesystem_fmea`
          - :ndf:`copy('status', need_id='doc__filesystem_fmea')`

        * - :need:`wp__sw_component_dfa`
          - :need:`gd_temp__comp_saf_dfa`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_dfa')`
          - <Link to issue>
          - :need:`doc__filesystem_dfa`
          - :ndf:`copy('status', need_id='doc__filesystem_dfa')`

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - n/a
          - `filesystem .h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/filesystem>`_, `filesystem/design <https://github.com/eclipse-score/baselibs/tree/main/score/filesystem/design>`_
          - valid

        * - :need:`wp__verification_sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - n/a
          - `filesystem/test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/filesystem>`_
          - valid

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - <Link to issue>
          - <Link to WP>
          - <manual>

        * - :need:`wp__verification_comp_int_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - n/a
          - component integration not needed (no sub-components and units are independent)
          - n/a

        * - :need:`wp__module_sw_build_config`
          - :need:`gd_temp__software_development_plan`
          - :ndf:`copy('status', need_id='gd_temp__software_development_plan')`
          - n/a
          - `filesystem/BUILD <https://github.com/eclipse-score/baselibs/blob/main/score/filesystem/BUILD>`_
          - valid


Component result Work products List
---------------------------------------

.. list-table:: Component result Work products
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
          - :need:`doc__result_lib_requirements`
          - :ndf:`copy('status', need_id='doc__result_lib_requirements')`

        * - :need:`wp__requirements_comp_aou`
          - :need:`gd_temp__req_aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
          - <Link to issue>
          - :need:`doc__result_lib_requirements`
          - :ndf:`copy('status', need_id='doc__result_lib_requirements')`

        * - :need:`wp__requirements_inspect`
          - :need:`gd_chklst__req_inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch_comp`
          - :ndf:`copy('status', need_id='gd_temp__arch_comp')`
          - `#1821 <https://github.com/eclipse-score/score/issues/1821>`_
          - :need:`doc__result_architecture`
          - :ndf:`copy('status', need_id='doc__result_architecture')`

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_component_fmea`
          - :need:`gd_temp__comp_saf_fmea`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_fmea')`
          - <Link to issue>
          - :need:`doc__result_fmea`
          - :ndf:`copy('status', need_id='doc__result_fmea')`

        * - :need:`wp__sw_component_dfa`
          - :need:`gd_temp__comp_saf_dfa`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_dfa')`
          - <Link to issue>
          - :need:`doc__result_dfa`
          - :ndf:`copy('status', need_id='doc__result_dfa')`

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - n/a
          - `result .h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/result>`_, `result/design <https://github.com/eclipse-score/baselibs/tree/main/score/result/design>`_
          - draft

        * - :need:`wp__verification_sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - n/a
          - `result/test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/result>`_
          - valid

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - <Link to issue>
          - <Link to WP>
          - <manual>

        * - :need:`wp__verification_comp_int_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - n/a
          - component integration not needed (no sub-components and units are independent)
          - n/a

        * - :need:`wp__module_sw_build_config`
          - :need:`gd_temp__software_development_plan`
          - :ndf:`copy('status', need_id='gd_temp__software_development_plan')`
          - n/a
          - `result/BUILD <https://github.com/eclipse-score/baselibs/blob/main/score/result/BUILD>`_
          - valid


Component json Work products List
---------------------------------------

.. list-table:: Component json Work products
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
          - `#1432 <https://github.com/eclipse-score/score/issues/1432>`_
          - :need:`doc__json_requirements`
          - :ndf:`copy('status', need_id='doc__json_requirements')`

        * - :need:`wp__requirements_comp_aou`
          - :need:`gd_temp__req_aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
          - <Link to issue>
          - :need:`doc__json_requirements`
          - :ndf:`copy('status', need_id='doc__json_requirements')`

        * - :need:`wp__requirements_inspect`
          - :need:`gd_chklst__req_inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch_comp`
          - :ndf:`copy('status', need_id='gd_temp__arch_comp')`
          - n/a
          - :need:`doc__json_architecture`
          - :ndf:`copy('status', need_id='doc__json_architecture')`

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_component_fmea`
          - :need:`gd_temp__comp_saf_fmea`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_fmea')`
          - <Link to issue>
          - :need:`doc__json_fmea`
          - :ndf:`copy('status', need_id='doc__json_fmea')`

        * - :need:`wp__sw_component_dfa`
          - :need:`gd_temp__comp_saf_dfa`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_dfa')`
          - <Link to issue>
          - :need:`doc__json_dfa`
          - :ndf:`copy('status', need_id='doc__json_dfa')`

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - n/a
          - `json .h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/json>`_, `json/design <https://github.com/eclipse-score/baselibs/tree/main/score/json/detailed_design>`_
          - valid

        * - :need:`wp__verification_sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - n/a
          - `json/test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/json>`_
          - valid

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - <Link to issue>
          - <Link to WP>
          - <manual>

        * - :need:`wp__verification_comp_int_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - <Link to issue>
          - <Link to WP>
          - <automatic>

        * - :need:`wp__module_sw_build_config`
          - :need:`gd_temp__software_development_plan`
          - :ndf:`copy('status', need_id='gd_temp__software_development_plan')`
          - n/a
          - `json/BUILD <https://github.com/eclipse-score/baselibs/blob/main/score/json/BUILD>`_
          - valid

        * - :need:`wp__sw_component_class`
          - :need:`tsf__trust__trustable-software`
          - :ndf:`copy('status', need_id='gd_guidl__component_classification')`
          - `#1460 <https://github.com/eclipse-score/score/issues/1460>`_
          - `TSF Report on nlohman/json <https://eclipse-score.github.io/inc_nlohmann_json/main/report.html>`_
          - draft

All other components of the baselibs module as released in the :need:`doc__baselibs_release_note`
are not planned to be qualifiable stand alone (as SEooC), but only in context, for example as they are used
in other S-CORE modules (e.g. communication). To be qualifiable in context those come with unit tests,
are implemented according to defined coding and detailed design guidelines, achieve the required structural coverage
and fulfill the AoUs of the reference OS (e.g. don’t use banned functions).

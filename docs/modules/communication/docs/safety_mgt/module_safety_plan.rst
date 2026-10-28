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
   :version: 2
   :safety: ASIL_B
   :security: NO
   :realizes: wp__module_safety_plan[version==1]



Functional Safety Management Context
====================================

This Safety Plan adds to the :need:`doc__score_platform_safety_plan` all the module development relevant work products needed for ISO 26262 conformity.

Functional Safety Management Scope
==================================

This Safety Plan's scope is a SW module of the SW platform: :ref:`communication_module_docs`.
The module consists of one or more SW components and will be developed as a SEooC in `S-CORE repository <https://github.com/eclipse-score/communication>`_
but with tooling and process different from S-CORE. It shall be used as a part of the S-CORE platform based on component classification.

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

- tailoring is as described in the work products lists based on the component classification.

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
          - :need:`doc__communication_safety_analysis_fdr`

        * - :need:`wp__audit_report`
          - performed by external experts
          - n/a
          - see platform safety plan

        * - :need:`wp__module_safety_manual`
          - :need:`gd_temp__safety_manual`
          - :ndf:`copy('status', need_id='gd_temp__safety_manual')`
          - :need:`doc__communication_safety_manual`

        * - :need:`wp__verification_module_ver_report`
          - :need:`gd_temp__mod_ver_report`
          - :ndf:`copy('status', need_id='gd_temp__mod_ver_report')`
          - `<https://eclipse-score.github.io/communication/latest/docs/sphinx/mw_com_index/traceability_report/index.html>`_

        * - :need:`wp__module_sw_release_note`
          - :need:`gd_temp__rel_mod_rel_note`
          - :ndf:`copy('status', need_id='gd_temp__rel_mod_rel_note')`
          - `<https://github.com/eclipse-score/communication/releases>`_

Component LoLa Work products List
---------------------------------

.. list-table:: Component LoLa Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - :need:`wp__requirements_comp`
          - :need:`gd_temp__req_comp_req`
          - :ndf:`copy('status', need_id='gd_temp__req_comp_req')`
          - `<https://github.com/eclipse-score/communication/tree/main/score/mw/com/dependability/requirements/component_requirements>`_

        * - :need:`wp__requirements_comp_aou`
          - :need:`gd_temp__req_aou_req`
          - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
          - same as for feature level

        * - :need:`wp__requirements_inspect`
          - :need:`gd_chklst__req_inspection`
          - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
          - partly tailored as several checks are automated, gap analysis tbd

        * - :need:`wp__component_arch`
          - :need:`gd_temp__arch_comp`
          - :ndf:`copy('status', need_id='gd_temp__arch_comp')`
          - `<https://github.com/eclipse-score/communication/tree/main/score/mw/com/dependability/software_architectural_design>`

        * - :need:`wp__sw_arch_verification`
          - :need:`gd_chklst__arch_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
          - partly tailored as several checks are automated, gap analysis tbd

        * - :need:`wp__sw_component_fmea`
          - :need:`gd_temp__comp_saf_fmea`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_fmea')`
          - same as for feature level

        * - :need:`wp__sw_component_dfa`
          - :need:`gd_temp__comp_saf_dfa`
          - :ndf:`copy('status', need_id='gd_temp__comp_saf_dfa')`
          - same as for feature level

        * - :need:`wp__sw_implementation`
          - :need:`gd_guidl__implementation`
          - :ndf:`copy('status', need_id='gd_guidl__implementation')`
          - `LoLa/.h/.cpp <https://github.com/eclipse-score/communication/blob/main/score/mw/com>`_, `LoLa/design <https://github.com/eclipse-score/communication/tree/main/score/mw/com/design>`_

        * - :need:`wp__verification_sw_unit_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - `LoLa/test.cpp <https://github.com/eclipse-score/communication/tree/main/score/mw/com/test>`_

        * - :need:`wp__sw_implementation_inspection`
          - :need:`gd_chklst__impl_inspection_checklist`
          - :ndf:`copy('status', need_id='gd_chklst__impl_inspection_checklist')`
          - partly tailored as several checks are automated, gap analysis tbd

        * - :need:`wp__verification_comp_int_test`
          - :need:`gd_guidl__verification_guide`
          - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
          - `LoLa/test <https://github.com/eclipse-score/communication/tree/main/score/mw/com/test>`_

        * - :need:`wp__sw_component_class`
          - :need:`gd_guidl__component_classification`
          - :ndf:`copy('status', need_id='gd_guidl__component_classification')`
          - :need:`doc__lola_comp_class`

Note: Name of the external component taken from `Readme <https://github.com/eclipse-score/communication/blob/main/README.md>`_
where it is stated as LoLa/mw::com but we abbreviate it to LoLa (as mw::com is mainly the namespace/api name).

Note2: Above links to communication repository are to the version as defined in reference integration.

Module Safety Package
=====================

To create the safety package (according to :need:`gd_guidl__saf_package`) the following
documents and work products status have to go to "valid" (after the relevant verification were performed).

Module Documents Status
-----------------------

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See :ref:`documents_docs_modules`

Component Documents Status
--------------------------

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See :ref:`documents_docs_modules`

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

Deviations from Module Safety Plan
----------------------------------

The following deviations from the module safety plan are present in the module safety package.
These are deviations from planned processes execution and/or work product results,
safety anomalies in the sense of known bugs in the software are reported in the release notes.

<Describe here the deviations, whether they have an impact on module's safety functions,
how these can be mitigated or argued and if and when a resolution is planned.>

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

.. _safety_planning_ipc:

IPC Safety Work Products List
#################################

.. document:: Communication IPC Safety WPs
   :id: doc__com_ipc_safety_wp
   :status: draft
   :version: 2
   :safety: ASIL_B
   :security: YES
   :realizes: wp__platform_safety_plan[version==1]


Tailoring
=========

Additional to the tailoring in the SW platform project as defined in the :need:`doc__platform_safety_plan` we define here the additional tailoring on feature level.

- The feature level artefacts are additionally partly tailored as in below list, as we use an "external" SEooC
  which provides the feature level artefacts as linked below.


Inter-process Communication Safety Work Products
================================================

.. list-table:: Feature Inter-process Communication Workproducts
    :header-rows: 1

    * - Workproduct Id
      - Link to process
      - Process status
      - Link to WP

    * - :need:`wp__feat_request`
      - :need:`gd_temp__change_feature_request`
      - :ndf:`copy('status', need_id='gd_temp__change_feature_request')`
      - :need:`doc__com_ipc`

    * - :need:`wp__requirements_feat`
      - :need:`gd_temp__req_feat_req`
      - :ndf:`copy('status', need_id='gd_temp__req_feat_req')`
      - `<https://eclipse-score.github.io/communication/latest/docs/sphinx/mw_com_index/feature_requirements/feature_requirements_ipc/requirements/feature_requirements/feature_requirements_ipc.html>`_

    * - :need:`wp__requirements_feat_aou`
      - :need:`gd_temp__req_aou_req`
      - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
      - `<https://eclipse-score.github.io/communication/latest/docs/sphinx/mw_com_index/assumptions_of_use/aous/aous.html>`_

    * - :need:`wp__feature_arch`
      - :need:`gd_temp__arch_feature`
      - :ndf:`copy('status', need_id='gd_temp__arch_feature')`
      - `<https://eclipse-score.github.io/communication/latest/docs/sphinx/mw_com_index/architectural_design/software_architectural_design/static/static_design/overall.html>`_

    * - :need:`wp__feature_fmea`
      - :need:`gd_temp__feat_saf_fmea`
      - :ndf:`copy('status', need_id='gd_temp__feat_saf_fmea')`
      - `<https://eclipse-score.github.io/communication/latest/docs/sphinx/mw_com_index/dependability_analysis/mw_com_dependability_analysis/safety_analysis.html>`_

    * - :need:`wp__feature_dfa`
      - :need:`gd_temp__feat_saf_dfa`
      - :ndf:`copy('status', need_id='gd_temp__feat_saf_dfa')`
      - covered by safety analysis link above

    * - :need:`wp__requirements_inspect`
      - :need:`gd_chklst__req_inspection`
      - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
      - partly tailored as several checks are automated, gap analysis tbd

    * - :need:`wp__sw_arch_verification`
      - :need:`gd_chklst__arch_inspection_checklist`
      - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
      - partly tailored as several checks are automated, gap analysis tbd

    * - :need:`wp__verification_feat_int_test`
      - :need:`gd_guidl__verification_guide`
      - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
      - <Link to WP>

Feature Safety Package
======================

To create the safety package (according to :need:`gd_guidl__saf_package`) the following
documents and work products status have to go to "valid" (after the relevant verification were performed).

Feature Documents Status
------------------------

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See :ref:`documents_docs_features_communication`

Feature Requirements Status
---------------------------

`<https://eclipse-score.github.io/communication/latest/docs/sphinx/mw_com_index/traceability_report/feature_requirements.html>`_

Feature AoU Status
------------------

no status is used for AoU, all AoU merged are implicitly in "valid" state.

Feature Architecture Status
---------------------------

no status is used for architecture elements, all architecture elements merged are implicitly in "valid" state.

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

- There is an overlap in two work products between the expectation formulated in the feature request,
  which defines feature requirements and interfaces and the work products provided in `Communication Repository <https://github.com/eclipse-score/communication>`_.
  Both versions are linked below. A comparison of these has to be performed and inconsistencies resolved as part of inspections - see `ticket <https://github.com/eclipse-score/communication/issues/1490>`_

- AoU in `Communication Repository <https://github.com/eclipse-score/communication>`_ are provided in a different format as needed by S-CORE documentation (e.g. the safety manual),
  so a copy of the AoU in docs_as-code format has to be provided.
  Original and Copy are linked below. It need to be confirmed that those are equal as part of inspections - see `ticket <https://github.com/eclipse-score/communication/issues/1490>`_

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
      - :need:`doc__com_ipc`, :need:`doc__com`

    * - :need:`wp__requirements_feat`
      - :need:`gd_temp__req_feat_req`
      - :ndf:`copy('status', need_id='gd_temp__req_feat_req')`
      - :need:`doc__ipc_requirements`, :need:`doc__communication_requirements`
        `<https://github.com/eclipse-score/communication/blob/main/score/mw/com/dependability/requirements/feature_requirements/feature_requirements_ipc.trlc>`_

    * - :need:`wp__requirements_feat_aou`
      - :need:`gd_temp__req_aou_req`
      - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
      - :need:`doc__communication_aou`,
        `<https://github.com/eclipse-score/communication/blob/main/score/mw/com/dependability/safety_analysis/aou.trlc>`_

    * - :need:`wp__feature_arch`
      - :need:`gd_temp__arch_feature`
      - :ndf:`copy('status', need_id='gd_temp__arch_feature')`
      - :need:`doc__communication_architecture`,
        `<https://github.com/eclipse-score/communication/tree/main/score/mw/com/dependability/architectural_design/static_design>`_

    * - :need:`wp__feature_fmea`
      - :need:`gd_temp__feat_saf_fmea`
      - :ndf:`copy('status', need_id='gd_temp__feat_saf_fmea')`
      - `<https://github.com/eclipse-score/communication/tree/main/score/mw/com/dependability/safety_analysis>`_

    * - :need:`wp__feature_dfa`
      - :need:`gd_temp__feat_saf_dfa`
      - :ndf:`copy('status', need_id='gd_temp__feat_saf_dfa')`
      - covered by safety analysis link above

    * - :need:`wp__requirements_inspect`
      - :need:`gd_chklst__req_inspection`
      - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
      - partly tailored as several checks are automated, gap analysis tbd, check score vs. communication repo

    * - :need:`wp__sw_arch_verification`
      - :need:`gd_chklst__arch_inspection_checklist`
      - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
      - partly tailored as several checks are automated, gap analysis tbd, check score vs. communication repo

    * - :need:`wp__verification_feat_int_test`
      - :need:`gd_guidl__verification_guide`
      - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
      - <Link to WP>

Note: Above links to communication repository are to the version as defined in reference integration.

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

.. needtable::
   :style: table
   :types: feat_req
   :tags: ipc
   :columns: id;status
   :colwidths: 25,25
   :sort: title

.. needtable::
   :style: table
   :types: feat_req
   :tags: com
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Test and traceability status in communication repository:
`<https://eclipse-score.github.io/communication/latest/docs/sphinx/mw_com_index/traceability_report/feature_requirements.html>`_

Feature AoU Status
------------------

.. needtable::
   :style: table
   :types: aou_req
   :tags: communication
   :columns: id;status
   :colwidths: 25,25
   :sort: title

The original AoUs are in communication repository and are not documented as sphinx-needs, these are "valid" as soon as merged.

Feature Architecture Status
---------------------------

.. needtable::
   :style: table
   :types: feat_arc_sta; feat_arc_dyn; logic_arc_int
   :tags: communication
   :columns: id;status
   :colwidths: 25,25
   :sort: title

The main architectural views are in communication repository and are not documented as sphinx-needs, these are "valid" as soon as merged.

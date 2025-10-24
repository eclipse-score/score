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


Feature Safety Planning
=======================

.. document:: Orchestration Safety WPs
   :id: doc__orchestration_safety_wp
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: PROCESS_wp__platform_safety_plan
   :tags: orchestration


.. list-table:: Feature Orchestration Work products
    :header-rows: 1

    * - Work product Id
      - Link to process
      - Process status
      - Link to issue
      - Link to WP
      - WP/doc status

    * - :need:`PROCESS_wp__feat_request`
      - :need:`PROCESS_gd_temp__change_feature_request`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__change_feature_request')`
      - https://github.com/eclipse-score/score/pull/1293
      - :need:`doc__orchestration`
      - :ndf:`copy('status', need_id='doc__orchestration')`

    * - :need:`PROCESS_wp__requirements_feat`
      - :need:`PROCESS_gd_temp__req_feat_req`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__req_feat_req')`
      - https://github.com/eclipse-score/score/pull/1293
      - :need:`doc__orchestration_requirements`
      - doc :ndf:`copy('status', need_id='doc__orchestration')` & WP below

    * - :need:`PROCESS_wp__requirements_feat_aou`
      - :need:`PROCESS_gd_temp__req_aou_req`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__req_aou_req')`
      - https://github.com/eclipse-score/score/pull/1293
      - :need:`doc__orchestration_requirements`
      - doc :ndf:`copy('status', need_id='doc__orchestration')` & WP below

    * - :need:`PROCESS_wp__feature_arch`
      - :need:`PROCESS_gd_temp__arch_feature`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__arch_feature')`
      - <link to issue>
      - :need:`doc__orchestration_architecture`
      - doc :ndf:`copy('status', need_id='doc__orchestration_architecture')` & WP below

    * - :need:`PROCESS_wp__feature_fmea`
      - :need:`PROCESS_gd_temp__feat_saf_fmea`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__feat_saf_fmea')`
      - <link to issue>
      - :need:`doc__orchestration_fmea`
      - doc :ndf:`copy('status', need_id='doc__orchestration_fmea')` & WP below

    * - :need:`PROCESS_wp__feature_dfa`
      - :need:`PROCESS_gd_temp__feat_saf_dfa`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__feat_saf_dfa')`
      - <Link to issue>
      - :need:`doc__orchestration_dfa`
      - doc :ndf:`copy('status', need_id='doc__orchestration_dfa')` & WP below

    * - :need:`PROCESS_wp__requirements_inspect`
      - :need:`PROCESS_gd_chklst__req_inspection`
      - :ndf:`copy('status', need_id='PROCESS_gd_chklst__req_inspection')`
      - n/a
      - Checklist used in Pull Request Review
      - n/a

    * - :need:`PROCESS_wp__sw_arch_verification`
      - :need:`PROCESS_gd_chklst__arch_inspection_checklist`
      - :ndf:`copy('status', need_id='PROCESS_gd_chklst__arch_inspection_checklist')`
      - n/a
      - Checklist used in Pull Request Review
      - n/a

    * - :need:`PROCESS_wp__verification_feat_int_test`
      - :need:`PROCESS_gd_guidl__verification_guide`
      - :ndf:`copy('status', need_id='PROCESS_gd_guidl__verification_guide')`
      - <link to issue>
      - <Link to WP>
      - <automated>


Feature Requirements Status
---------------------------

.. needtable::
   :filter: "orchestration" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: feat_req
   :tags: orchestration
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature AoU Status
------------------

.. needtable::
   :filter: "orchestration" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: aou_req
   :tags: orchestration
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature Architecture Status
---------------------------

.. needtable::
   :filter: "orchestration" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: orchestration
   :columns: id;status
   :colwidths: 25,25
   :sort: title

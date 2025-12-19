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

.. document:: Persistency KVS Safety WPs
   :id: doc__persistency_safety_wp
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__platform_safety_plan
   :tags: persistency


.. list-table:: Feature persistency Workproducts
    :header-rows: 1

    * - Workproduct Id
      - Link to process
      - Process status
      - Link to issue
      - Link to WP
      - WP status

    * - :need:`wp__feat_request`
      - :need:`gd_temp__change_feature_request`
      - :ndf:`copy('status', need_id='gd_temp__change_feature_request')`
      - https://github.com/eclipse-score/score/issues/760
      - :need:`doc__persistency_kvs`
      - :ndf:`copy('status', need_id='doc__persistency_kvs')`

    * - :need:`wp__requirements_feat`
      - :need:`gd_temp__req_feat_req`
      - :ndf:`copy('status', need_id='gd_temp__req_feat_req')`
      - https://github.com/eclipse-score/score/issues/960
      - :ref:`feature_requirements_PersistencyKvs`
      - valid

    * - :need:`wp__requirements_feat_aou`
      - :need:`gd_temp__req_aou_req`
      - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
      - https://github.com/eclipse-score/score/issues/960
      - :ref:`feature_requirements_PersistencyKvs`
      - valid

    * - :need:`wp__feature_arch`
      - :need:`gd_temp__arch_feature`
      - :ndf:`copy('status', need_id='gd_temp__arch_feature')`
      - https://github.com/eclipse-score/score/issues/1020
      - :ref:`feature_architecture_PersistencyKvs`
      - valid

    * - :need:`wp__feature_fmea`
      - :need:`gd_guidl__safety_analysis`
      - :ndf:`copy('status', need_id='gd_guidl__safety_analysis')`
      - https://github.com/eclipse-score/score/issues/965
      - :need:`doc__persistency_fmea`
      - valid

    * - :need:`wp__feature_dfa`
      - :need:`gd_guidl__safety_analysis`
      - :ndf:`copy('status', need_id='gd_guidl__safety_analysis')`
      - https://github.com/eclipse-score/score/issues/965
      - :need:`doc__persistency_dfa`
      - valid

    * - :need:`wp__requirements_inspect`
      - :need:`gd_chklst__req_inspection`
      - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
      - https://github.com/eclipse-score/score/issues/960
      - :need:`doc__req_inspection_persistency`
      - valid

    * - :need:`wp__sw_arch_verification`
      - :need:`gd_chklst__arch_inspection_checklist`
      - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
      - https://github.com/eclipse-score/score/issues/1020
      - Checklist used in Pull Request Review
      - n/a

    * - :need:`wp__verification_feat_int_test`
      - :need:`gd_guidl__verification_guide`
      - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
      - https://github.com/eclipse-score/score/issues/964
      - Checklist used in Pull Request Review
      - <automated>


Feature Requirements Status
---------------------------

.. needtable::
   :filter: "persistency" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: feat_req
   :tags: persistency
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature AoU Status
------------------

.. needtable::
   :filter: "persistency" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: aou_req
   :tags: persistency
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature Architecture Status
---------------------------

.. needtable::
   :filter: "persistency" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: persistency
   :columns: id;status
   :colwidths: 25,25
   :sort: title

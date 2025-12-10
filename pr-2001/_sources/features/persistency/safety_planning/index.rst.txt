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

Feature Safety Work Products List
=================================

.. document:: Persistency Safety WPs
   :id: doc__persistency_safety_wp
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__platform_safety_plan
   :tags: persistency


.. list-table:: Feature persistency workproducts
    :header-rows: 1

    * - Workproduct Id
      - Link to process
      - Process status
      - Link to WP

    * - :need:`wp__feat_request`
      - :need:`gd_temp__change_feature_request`
      - :ndf:`copy('status', need_id='gd_temp__change_feature_request')`
      - :need:`doc__persistency`

    * - :need:`wp__requirements_feat`
      - :need:`gd_temp__req_feat_req`
      - :ndf:`copy('status', need_id='gd_temp__req_feat_req')`
      - :need:`doc__feature_persistency_requirements`

    * - :need:`wp__requirements_feat_aou`
      - :need:`gd_temp__req_aou_req`
      - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
      - :need:`doc__feature_persistency_requirements`

    * - :need:`wp__feature_arch`
      - :need:`gd_temp__arch_feature`
      - :ndf:`copy('status', need_id='gd_temp__arch_feature')`
      - :need:`doc__persistency_architecture`

    * - :need:`wp__feature_fmea`
      - :need:`gd_guidl__safety_analysis`
      - :ndf:`copy('status', need_id='gd_guidl__safety_analysis')`
      - :need:`doc__persistency_fmea`

    * - :need:`wp__feature_dfa`
      - :need:`gd_guidl__safety_analysis`
      - :ndf:`copy('status', need_id='gd_guidl__safety_analysis')`
      - :need:`doc__persistency_dfa`

    * - :need:`wp__requirements_inspect`
      - :need:`gd_chklst__req_inspection`
      - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
      - :need:`doc__feature_persistency_requirements_chklst`

    * - :need:`wp__sw_arch_verification`
      - :need:`gd_chklst__arch_inspection_checklist`
      - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
      - :need:`doc__persistency_arc_inspection`

    * - :need:`wp__verification_feat_int_test`
      - :need:`gd_guidl__verification_guide`
      - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
      - <WP Link>


Feature Requirements Status
---------------------------

.. needtable::
   :filter: docname is not None and "persistency" in docname and "requirements" in docname
   :style: table
   :types: feat_req
   :tags: persistency
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature AoU Status
------------------

.. needtable::
   :filter: docname is not None and "persistency" in docname and "requirements" in docname
   :style: table
   :types: aou_req
   :tags: persistency
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature Architecture Status
---------------------------

.. needtable::
   :filter: docname is not None and "persistency" in docname and "architecture" in docname
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: persistency
   :columns: id;status
   :colwidths: 25,25
   :sort: title

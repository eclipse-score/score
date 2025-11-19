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


FEO Feature Safety Planning
===========================

.. document:: FEO Safety Work Products
   :id: doc__feo_safety_wp
   :status: valid
   :security: NO
   :safety: ASIL_B
   :realizes: wp__platform_safety_plan
   :tags: framework_feo


.. list-table:: FEO Feature Work Products
    :header-rows: 1

    * - Work product Id
      - Link to process
      - Process status
      - Link to issue
      - Link to WP
      - WP/doc status

    * - :need:`wp__feat_request`
      - :need:`gd_temp__change_feature_request`
      - :ndf:`copy('status', need_id='gd_temp__change_feature_request')`
      - https://github.com/eclipse-score/score/issues/1646
      - :need:`doc__frameworks_feo`
      - :ndf:`copy('status', need_id='doc__frameworks_feo')`

    * - :need:`wp__requirements_feat`
      - :need:`gd_temp__req_feat_req`
      - :ndf:`copy('status', need_id='gd_temp__req_feat_req')`
      - https://github.com/eclipse-score/score/issues/1647
      - :need:`doc__frameworks_feo_feat_reqs`
      - :ndf:`copy('status', need_id='doc__frameworks_feo_feat_reqs')`

    * - :need:`wp__requirements_feat_aou`
      - :need:`gd_temp__req_aou_req`
      - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
      - https://github.com/eclipse-score/score/issues/1648
      - :need:`doc__frameworks_feo_aou_reqs`
      - :ndf:`copy('status', need_id='doc__frameworks_feo_aou_reqs')`

    * - :need:`wp__feature_arch`
      - :need:`gd_temp__arch_feature`
      - :ndf:`copy('status', need_id='gd_temp__arch_feature')`
      - https://github.com/eclipse-score/score/issues/1649
      - :need:`doc__frameworks_feo_feat_arch`
      - :ndf:`copy('status', need_id='doc__frameworks_feo_feat_arch')`

    * - :need:`wp__feature_fmea`
      - :need:`gd_temp__feat_saf_fmea`
      - :ndf:`copy('status', need_id='gd_temp__feat_saf_fmea')`
      - https://github.com/eclipse-score/score/issues/1650
      - :need:`doc__frameworks_feo_fmea`
      - :ndf:`copy('status', need_id='doc__frameworks_feo_fmea')`

    * - :need:`wp__feature_dfa`
      - :need:`gd_temp__feat_saf_dfa`
      - :ndf:`copy('status', need_id='gd_temp__feat_saf_dfa')`
      - https://github.com/eclipse-score/score/issues/1651
      - :need:`doc__frameworks_feo_dfa`
      - :ndf:`copy('status', need_id='doc__frameworks_feo_dfa')`

    * - :need:`wp__fdr_reports` (Features's Safety Analyses & DFA)
      - :need:`gd_chklst__safety_analysis`
      - :ndf:`copy('status', need_id='gd_chklst__safety_analysis')`
      - https://github.com/eclipse-score/score/issues/1652
      - :need:`doc__saf_ana_inspec_frameworks_feo`
      - :ndf:`copy('status', need_id='doc__saf_ana_inspec_frameworks_feo')`

    * - :need:`wp__requirements_inspect`
      - :need:`gd_chklst__req_inspection`
      - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
      - https://github.com/eclipse-score/score/issues/1653
      - :need:`doc__req_inspection_frameworks_feo`
      - :ndf:`copy('status', need_id='doc__req_inspection_frameworks_feo')`

    * - :need:`wp__sw_arch_verification`
      - :need:`gd_chklst__arch_inspection_checklist`
      - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
      - https://github.com/eclipse-score/score/issues/1654
      - :need:`doc__arch_inspection_frameworks_feo`
      - :ndf:`copy('status', need_id='doc__arch_inspection_frameworks_feo')`

    * - :need:`wp__verification_feat_int_test`
      - :need:`gd_guidl__verification_guide`
      - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
      - https://github.com/eclipse-score/score/issues/1655
      - <Link to WP>
      - <automated>

FEO Requirements Status
-----------------------

.. needtable::
   :filter: "feo" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: feat_req
   :tags: frameworks_feo
   :columns: id;status
   :colwidths: 25,25
   :sort: title

FEO AoU Status
--------------

.. needtable::
   :filter: "feo" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: aou_req
   :tags: frameworks_feo
   :columns: id;status
   :colwidths: 25,25
   :sort: title

FEO Architecture Status
-----------------------

.. needtable::
   :filter: "feo" in docname and "architecture" in docname and docname is not None
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: frameworks_feo
   :columns: id;status
   :colwidths: 25,25
   :sort: title

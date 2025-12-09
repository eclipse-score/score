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
      - Link to WP

    * - :need:`wp__feat_request`
      - :need:`gd_temp__change_feature_request`
      - :ndf:`copy('status', need_id='gd_temp__change_feature_request')`
      - :need:`doc__frameworks_feo`

    * - :need:`wp__requirements_feat`
      - :need:`gd_temp__req_feat_req`
      - :ndf:`copy('status', need_id='gd_temp__req_feat_req')`
      - :need:`doc__frameworks_feo_feat_reqs`

    * - :need:`wp__requirements_feat_aou`
      - :need:`gd_temp__req_aou_req`
      - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
      - :need:`doc__frameworks_feo_aou_reqs`

    * - :need:`wp__feature_arch`
      - :need:`gd_temp__arch_feature`
      - :ndf:`copy('status', need_id='gd_temp__arch_feature')`
      - :need:`doc__frameworks_feo_feat_arch`

    * - :need:`wp__feature_fmea`
      - :need:`gd_temp__feat_saf_fmea`
      - :ndf:`copy('status', need_id='gd_temp__feat_saf_fmea')`
      - :need:`doc__frameworks_feo_fmea`

    * - :need:`wp__feature_dfa`
      - :need:`gd_temp__feat_saf_dfa`
      - :ndf:`copy('status', need_id='gd_temp__feat_saf_dfa')`
      - :need:`doc__frameworks_feo_dfa`

    * - :need:`wp__fdr_reports` (Features's Safety Analyses & DFA)
      - :need:`gd_chklst__safety_analysis`
      - :ndf:`copy('status', need_id='gd_chklst__safety_analysis')`
      - :need:`doc__saf_ana_inspec_frameworks_feo`

    * - :need:`wp__requirements_inspect`
      - :need:`gd_chklst__req_inspection`
      - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
      - :need:`doc__req_inspection_frameworks_feo`

    * - :need:`wp__sw_arch_verification`
      - :need:`gd_chklst__arch_inspection_checklist`
      - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
      - :need:`doc__arch_inspection_frameworks_feo`

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

See :ref:`documents_docs_features_frameworks`

FEO Requirements Status
-----------------------

.. needtable::
   :filter: docname is not None and "feo" in docname and "requirements" in docname
   :style: table
   :types: feat_req
   :tags: frameworks_feo
   :columns: id;status
   :colwidths: 25,25
   :sort: title

FEO AoU Status
--------------

.. needtable::
   :filter: docname is not None and "feo" in docname and "requirements" in docname
   :style: table
   :types: aou_req
   :tags: frameworks_feo
   :columns: id;status
   :colwidths: 25,25
   :sort: title

FEO Architecture Status
-----------------------

.. needtable::
   :filter: docname is not None and "feo" in docname and "architecture" in docname
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: frameworks_feo
   :columns: id;status
   :colwidths: 25,25
   :sort: title

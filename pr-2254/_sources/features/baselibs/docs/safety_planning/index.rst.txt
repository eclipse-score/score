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

.. document:: Baselibs Safety WPs
   :id: doc__baselibs_safety_wp
   :status: draft
   :safety: ASIL_B
   :realizes: wp__platform_safety_plan


.. list-table:: Feature Baselibs Work products
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
      - `#549 <https://github.com/eclipse-score/score/issues/549>`_
      - :need:`doc__baselibs`
      - :ndf:`copy('status', need_id='doc__baselibs')`

    * - :need:`wp__requirements_feat`
      - :need:`gd_temp__req_feat_req`
      - :ndf:`copy('status', need_id='gd_temp__req_feat_req')`
      - `#549 <https://github.com/eclipse-score/score/issues/549>`_
      - :need:`doc__baselibs_requirements`
      - doc :ndf:`copy('status', need_id='doc__baselibs_requirements')` & WP below

    * - :need:`wp__requirements_feat_aou`
      - :need:`gd_temp__req_aou_req`
      - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
      - <link to issue>
      - :need:`doc__baselibs_requirements`
      - doc :ndf:`copy('status', need_id='doc__baselibs_requirements')` & WP below

    * - :need:`wp__feature_arch`
      - :need:`gd_temp__arch_feature`
      - :ndf:`copy('status', need_id='gd_temp__arch_feature')`
      - `#1240 <https://github.com/eclipse-score/score/issues/1240>`_
      - :need:`doc__baselibs_architecture`
      - doc :ndf:`copy('status', need_id='doc__baselibs_architecture')` & WP below

    * - :need:`wp__feature_fmea`
      - :need:`gd_temp__feat_saf_fmea`
      - :ndf:`copy('status', need_id='gd_temp__feat_saf_fmea')`
      - <link to issue>
      - :need:`doc__baselibs_fmea`
      - doc :ndf:`copy('status', need_id='doc__baselibs_fmea')` & WP below

    * - :need:`wp__feature_dfa`
      - :need:`gd_temp__feat_saf_dfa`
      - :ndf:`copy('status', need_id='gd_temp__feat_saf_dfa')`
      - <Link to issue>
      - :need:`doc__baselibs_dfa`
      - doc :ndf:`copy('status', need_id='doc__baselibs_dfa')` & WP below

    * - :need:`wp__requirements_inspect`
      - :need:`gd_chklst__req_inspection`
      - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
      - <link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__sw_arch_verification`
      - :need:`gd_chklst__arch_inspection_checklist`
      - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
      - <link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__verification_feat_int_test`
      - :need:`gd_guidl__verification_guide`
      - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
      - <link to issue>
      - <Link to WP>
      - <automated>



Feature Requirements Status
---------------------------

.. needtable::
   :filter: "baselibs" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: feat_req
   :tags: baselibs
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature AoU Status
------------------

.. needtable::
   :filter: "baselibs" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: aou_req
   :tags: baselibs
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature Architecture Status
---------------------------

.. needtable::
   :filter: "baselibs" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: baselibs
   :columns: id;status
   :colwidths: 25,25
   :sort: title

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

.. _feature_safety_wp_template:

Feature Safety Planning
=======================

.. list-table:: Feature <feature> Workproducts
    :header-rows: 1

    * - Workproduct Id
      - Link to process
      - Process status
      - Link to issue
      - Link to WP
      - WP status

    * - :need:`PROCESS_wp__feat_request`
      - :need:`PROCESS_gd_temp__change__feature_request`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__change__feature_request')`
      - https://github.com/eclipse-score/score/issues/760
      - :need:`doc__persistency_kvs`
      - :ndf:`copy('status', need_id='doc__persistency_kvs')`

    * - :need:`PROCESS_wp__requirements__feat`
      - :need:`PROCESS_gd_temp__req__feat_req`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__req__feat_req')`
      - https://github.com/eclipse-score/score/issues/960
      - :doc:`../requirements/index`
      - see below

    * - :need:`PROCESS_wp__requirements__feat_aou`
      - :need:`PROCESS_gd_temp__req__aou_req`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__req__aou_req')`
      - https://github.com/eclipse-score/score/issues/960
      - :doc:`../requirements/index`
      - see below

    * - :need:`PROCESS_wp__feature_arch`
      - :need:`PROCESS_gd_temp__arch__feature`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__arch__feature')`
      - https://github.com/eclipse-score/score/issues/1020
      - :doc:`../architecture/index`
      - see below

    * - :need:`PROCESS_wp__feature_safety_analysis`
      - <link to process>
      - <automated>
      - https://github.com/eclipse-score/score/issues/965
      - :need:`doc__persistency_safety_analysis`
      - <automated>

    * - :need:`PROCESS_wp__feature_dfa`
      - <Link to process>
      - <Process status>
      - https://github.com/eclipse-score/score/issues/965
      - :need:`doc__persistency_dfa`
      - <automated>

    * - :need:`PROCESS_wp__requirements__inspect`
      - :need:`PROCESS_gd_chklst__req__inspection`
      - :ndf:`copy('status', need_id='PROCESS_gd_chklst__req__inspection')`
      - n/a
      - Checklist used in Pull Request Review
      - n/a

    * - :need:`PROCESS_wp__sw_arch_verification`
      - :need:`PROCESS_gd_chklst__arch__inspection_checklist`
      - :ndf:`copy('status', need_id='PROCESS_gd_chklst__arch__inspection_checklist')`
      - n/a
      - Checklist used in Pull Request Review
      - n/a

    * - :need:`PROCESS_wp__verification__feat_int_test`
      - :need:`PROCESS_gd_guidl__verification_guide`
      - :ndf:`copy('status', need_id='PROCESS_gd_guidl__verification_guide')`
      - <link to issue>
      - https://github.com/eclipse-score/score/issues/964
      - <automated>

.. attention::
    The above table must be updated according to your feature safety planning.

    - Create and link the issues to plan the work products (according to :need:`PROCESS_gd_guidl__saf_plan_definitions`)
    - Fill the work producs links and add their status (also possible below) to create the safety package (according to :need:`PROCESS_gd_guidl__saf_package`)

Feature Requirements Status
---------------------------

.. needtable::
   :style: table
   :types: feat_req
   :tags: feature_name
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature AoU Status
------------------

.. needtable::
   :style: table
   :types: aou_req
   :tags: feature_name
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature Architecture Status
---------------------------

.. needtable::
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: feature_name
   :columns: id;status
   :colwidths: 25,25
   :sort: title

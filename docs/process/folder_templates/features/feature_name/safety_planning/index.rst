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

    * - :need:`wp__feat_request`
      - :need:`gd_temp__change__feature_request`
      - :ndf:`copy('status', need_id='gd_temp__change__feature_request')`
      - <link to issue>
      - :need:`doc__feature_name`
      - :ndf:`copy('status', need_id='doc__feature_name')`

    * - :need:`wp__requirements__feat`
      - :need:`gd_temp__req__feat_req`
      - :ndf:`copy('status', need_id='gd_temp__req__feat_req')`
      - <link to issue>
      - :doc:`../requirements/index`
      - see below

    * - :need:`wp__requirements__feat_aou`
      - :need:`gd_temp__req__aou_req`
      - :ndf:`copy('status', need_id='gd_temp__req__aou_req')`
      - <link to issue>
      - :doc:`../requirements/index`
      - see below

    * - :need:`wp__feature_arch`
      - :need:`gd_temp__arch__feature`
      - :ndf:`copy('status', need_id='gd_temp__arch__feature')`
      - <link to issue>
      - :doc:`../architecture/index`
      - see below

    * - :need:`wp__feature_safety_analysis`
      - <link to process>
      - <automated>
      - <link to issue>
      - :doc:`../safety_analysis/fmea`
      - <automated>

    * - :need:`wp__feature_dfa`
      - <Link to process>
      - <Process status>
      - <Link to issue>
      - :doc:`../safety_analysis/dfa`
      - <automated>

    * - :need:`wp__requirements__inspect`
      - :need:`gd_chklst__req__inspection`
      - :ndf:`copy('status', need_id='gd_chklst__req__inspection')`
      - n/a
      - Checklist used in Pull Request Review
      - n/a

    * - :need:`wp__sw_arch_verification`
      - :need:`gd_chklst__arch__inspection_checklist`
      - :ndf:`copy('status', need_id='gd_chklst__arch__inspection_checklist')`
      - n/a
      - Checklist used in Pull Request Review
      - n/a

    * - :need:`wp__verification__feat_int_test`
      - :need:`gd_guidl__verification_guide`
      - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
      - <link to issue>
      - <Link to WP>
      - <automated>

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

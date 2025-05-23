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

Feature Safety Work Products Template
=====================================

.. gd_temp:: Feature Safety Work Products Template
   :id: gd_temp__feature_safety_wp
   :status: valid
   :complies: std_req__iso26262__management_6465, std_req__iso26262__management_6466, std_req__iso26262__management_6467, std_req__iso26262__management_6468, std_req__iso26262__management_6469


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
      - <Link to WP>
      - <automated>

    * - :need:`wp__requirements__feat`
      - :need:`gd_temp__req__feat_req`
      - :ndf:`copy('status', need_id='gd_temp__req__feat_req')`
      - <link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__requirements__feat_aou`
      - :need:`gd_temp__req__aou_req`
      - :ndf:`copy('status', need_id='gd_temp__req__aou_req')`
      - <link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wf__cr_mt_featarch`
      - :need:`gd_temp__arch__feature`
      - :ndf:`copy('status', need_id='gd_temp__arch__feature')`
      - <link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__feature_safety_analysis`
      - <link to process>
      - <automated>
      - <link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__requirements__inspect`
      - :need:`gd_chklst__req__inspection`
      - :ndf:`copy('status', need_id='gd_chklst__req__inspection')`
      - <link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__sw_arch_verification`
      - :need:`gd_chklst__arch__inspection_checklist`
      - :ndf:`copy('status', need_id='gd_chklst__arch__inspection_checklist')`
      - <link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`wp__verification__feat_int_test`
      - :need:`gd_guidl__verification_guide`
      - :ndf:`copy('status', need_id='gd_guidl__verification_guide')`
      - <link to issue>
      - <Link to WP>
      - <automated>

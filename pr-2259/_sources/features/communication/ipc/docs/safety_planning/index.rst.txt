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

Safety Planning
###############

Tailoring
=========

Additional to the tailoring in the SW platform project as defined in the :need:`doc__platform_safety_plan` we define here the additional tailoring on feature level.

- Excluded for this feature are additionally the following work products (and their related requirements):

  - :need:`wp__requirements_inspect`: in version 0.5 the inspections have to be done by the user
  - :need:`wp__sw_arch_verification`: in version 0.5 the inspections have to be done by the user


Inter-process Communication Safety Work Products
================================================

.. list-table:: Feature Inter-process Communication Workproducts
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
      - `#69 <https://github.com/eclipse-score/score/issues/69>`_
      - :need:`doc__com_ipc`
      - :ndf:`copy('status', need_id='doc__com_ipc')`

    * - :need:`wp__requirements_feat`
      - :need:`gd_temp__req_feat_req`
      - :ndf:`copy('status', need_id='gd_temp__req_feat_req')`
      - `#69 <https://github.com/eclipse-score/score/issues/69>`_
      - :need:`doc__ipc_requirements`, :need:`doc__communication_requirements`
      - :ndf:`copy('status', need_id='doc__ipc_requirements')`, :ndf:`copy('status', need_id='doc__communication_requirements')`

    * - :need:`wp__requirements_feat_aou`
      - :need:`gd_temp__req_aou_req`
      - :ndf:`copy('status', need_id='gd_temp__req_aou_req')`
      - <link to issue>
      - :need:`doc__ipc_requirements`, :need:`doc__communication_requirements`
      - :ndf:`copy('status', need_id='doc__ipc_requirements')`, :ndf:`copy('status', need_id='doc__communication_requirements')`

    * - :need:`wp__feature_arch`
      - :need:`gd_temp__arch_feature`
      - :ndf:`copy('status', need_id='gd_temp__arch_feature')`
      - `#388 <https://github.com/eclipse-score/score/issues/388>`_
      - :need:`doc__ipc_architecture`
      - :ndf:`copy('status', need_id='doc__ipc_architecture')`

    * - :need:`wp__feature_fmea`
      - :need:`gd_temp__feat_saf_fmea`
      - :ndf:`copy('status', need_id='gd_temp__feat_saf_fmea')`
      - <link to issue>
      - :need:`doc__ipc_fmea`
      - :ndf:`copy('status', need_id='doc__ipc_fmea')`

    * - :need:`wp__feature_dfa`
      - :need:`gd_temp__feat_saf_dfa`
      - :ndf:`copy('status', need_id='gd_temp__feat_saf_dfa')`
      - <link to issue>
      - :need:`doc__ipc_dfa`
      - :ndf:`copy('status', need_id='doc__ipc_dfa')`

    * - :need:`wp__requirements_inspect`
      - :need:`gd_chklst__req_inspection`
      - :ndf:`copy('status', need_id='gd_chklst__req_inspection')`
      - tailored
      - n/a
      - n/a

    * - :need:`wp__sw_arch_verification`
      - :need:`gd_chklst__arch_inspection_checklist`
      - :ndf:`copy('status', need_id='gd_chklst__arch_inspection_checklist')`
      - tailored
      - n/a
      - n/a

    * - :need:`wp__verification_feat_int_test`
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

Feature AoU Status
------------------

.. needtable::
   :style: table
   :types: aou_req
   :tags: ipc
   :columns: id;status
   :colwidths: 25,25
   :sort: title

.. needtable::
   :style: table
   :types: aou_req
   :tags: com
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature Architecture Status
---------------------------

.. needtable::
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: ipc
   :columns: id;status
   :colwidths: 25,25
   :sort: title

.. needtable::
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: com
   :columns: id;status
   :colwidths: 25,25
   :sort: title

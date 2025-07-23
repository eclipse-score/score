..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

Persistency Safety Analysis
###########################

.. document:: Safety Analysis
   :id: doc__persistency_safety_analysis
   :status: draft
   :safety: ASIL_B
   :tags: feature_persistency

   The FMEA is done by applying the fault model list. If a fault model doesn't apply, it is not listed here.
   Persistency is developed in a full deterministic way. A failure will lead to a specified reaction of the persistency feature.
   These failures must be handled by the application. Also failures that will lead to a unspecified usage of the feature
   like signals were corrupted or messages are not sent.

.. feat_saf_fmea:: Persistency
    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__message_nreived
    :violation_id: MF_01_01
    :violation_cause: Message is not received.
    :mitigates: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    User is not able to use the feature. Middleware cant be used.

.. feat_saf_fmea:: Persistency
    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__late_message
    :violation_id: MF_01_02
    :violation_cause: message received too late.
    :mitigates: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    User is not able to use the feature. Middleware cant be used.

.. feat_saf_fmea:: Persistency
    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__corrupted_message
    :violation_id: MF_01_05
    :violation_cause: message is corrupted.
    :mitigates: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    Covered by MF_01_01

.. feat_saf_fmea:: Persistency
    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__not_sent
    :violation_id: MF_01_06
    :violation_cause: message is not sent.
    :mitigates: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    Covered by MF_01_01

.. feat_saf_fmea:: Persistency
    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__unintendend
    :violation_id: MF_01_07
    :violation_cause: message is unintended sent.
    :mitigates: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    Covered by MF_01_01

.. feat_saf_fmea:: Persistency
    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__calc_wrong
    :violation_id: EX_01_01
    :violation_cause: Process calculates wrong result(s).
    :mitigates: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    User is not able to use the feature. Middleware cant be used.

.. feat_saf_fmea:: Persistency
    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__too_slow
    :violation_id: EX_01_02
    :violation_cause: processing too slow.
    :mitigates: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    User is not able to use the feature. Middleware cant be used.

.. feat_saf_fmea:: Persistency
    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__too_fast
    :violation_id: EX_01_03
    :violation_cause: processing too fast.
    :mitigates: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    User is not able to use the feature. Middleware cant be used.

.. feat_saf_fmea:: Persistency
    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__err_handl
    :violation_id: EX_01_04
    :violation_cause: loss of execution.
    :mitigates: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    User is not able to use the feature. Middleware cant be used.

.. feat_saf_fmea:: Persistency
    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__arbitrary
    :violation_id: EX_01_05
    :violation_cause: processing changes to arbitrary process.
    :mitigates: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    User is not able to use the feature. Middleware cant be used.

.. feat_saf_fmea:: Persistency
    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__infinite
    :violation_id: EX_01_06
    :violation_cause: processing is not complete (infinite loop).
    :mitigates: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    User is not able to use the feature. Middleware cant be used.

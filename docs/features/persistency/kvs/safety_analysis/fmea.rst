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

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_MF_01_01
   |    :failure_mode: MF_01_01
   |    :failure_effect: Message is not received.
   |    :mitigation: aou_req__persistency__error_handling
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: User is not able to use the feature. Middleware cant be used.
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_MF_01_02
   |    :failure_mode: MF_01_02
   |    :failure_effect: message received too late.
   |    :mitigation: aou_req__persistency__error_handling
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: User is not able to use the feature. Middleware cant be used.
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |   :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |   :id: feat_saf_FMEA__persistency_MF_01_03
   |   :failure_mode: MF_01_03
   |   :failure_effect: message received too early.
   |   :mitigation: NONE
   |   :mitigation_issue: None
   |   :sufficient: yes
   |   :argument: No impact / feature reacts only if triggered on the trigger.
   |   :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_MF_01_04
   |    :failure_mode: MF_01_04
   |    :failure_effect: message not received correctly by all recipients (different messages or messages partly lost).
   |    :mitigation: NONE
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: Failure mode not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_MF_01_05
   |    :failure_mode: MF_01_05
   |    :failure_effect: message is corrupted.
   |    :mitigation: NONE
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: Covered by MF_01_01
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_MF_01_06
   |    :failure_mode: MF_01_06
   |    :failure_effect: message is not sent.
   |    :mitigation: NONE
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: Covered by MF_01_01
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_MF_01_07
   |    :failure_mode: MF_01_07
   |    :failure_effect: message is unintended sent.
   |    :mitigation: NONE
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: Covered by MF_01_01
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_CO_01_01
   |    :failure_mode: CO_01_01
   |    :failure_effect: minimum constraint boundary is violated.
   |    :mitigation: NONE
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: Failure mode not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_CO_01_02
   |    :failure_mode: CO_01_02
   |    :failure_effect: maximum constraint boundary is violated.
   |    :mitigation: NONE
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: Failure mode not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_EX_01_01
   |    :failure_mode: EX_01_01
   |    :failure_effect: Process calculates wrong result(s).
   |    :mitigation: aou_req__persistency__error_handling
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: User is not able to use the feature. Middleware cant be used.
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_EX_01_02
   |    :failure_mode: EX_01_02
   |    :failure_effect: processing too slow.
   |    :mitigation: aou_req__persistency__error_handling
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: User is not able to use the feature. Middleware cant be used.
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_EX_01_03
   |    :failure_mode: EX_01_03
   |    :failure_effect: processing too fast.
   |    :mitigation: NONE
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: Failure mode not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_EX_01_04
   |    :failure_mode: EX_01_04
   |    :failure_effect: loss of execution.
   |    :mitigation: aou_req__persistency__error_handling
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: User is not able to use the feature. Middleware cant be used.
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_EX_01_05
   |    :failure_mode: EX_01_05
   |    :failure_effect: processing changes to arbitrary process.
   |    :mitigation: NONE
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: Failure mode not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_fmea:: Persistency
   |    :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
   |    :id: feat_saf_FMEA__persistency_EX_01_06
   |    :failure_mode: EX_01_06
   |    :failure_effect: processing is not complete (infinite loop).
   |    :mitigation: aou_req__persistency__error_handling
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: User is not able to use the feature. Middleware cant be used.
   |    :status: valid

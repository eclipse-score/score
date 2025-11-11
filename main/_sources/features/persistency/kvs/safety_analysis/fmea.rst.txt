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

Persistency FMEA
################

.. document:: FMEA
   :id: doc__persistency_fmea
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__feature_fmea
   :tags: persistency

For the FMEA analysis where the fault models :need:`gd_guidl__fault_models` are used.
The following fault models doesn't apply to the persistency feature:

Fault models
    - MF_01_03: Message received too early: Failure initiator not applicable at persistency, so no mitigation is needed.
    - MF_01_04: message not received correctly by all recipients (different messages or messages partly lost): Failure initiator not applicable at persistency, so no mitigation is needed.
    - MF_01_07: Message is unintended sent: Failure initiator not applicable at persistency. Feature developed fully deterministic, so no unintended messages are expected.
    - CO_01_01: Minimum constraint boundary is violated: Failure initiator not applicable at persistency, so no mitigation is needed.
    - CO_01_02: Maximum constraint boundary is violated: Failure initiator not applicable at persistency, so no mitigation is needed.
    - EX_01_01: Process calculates wrong result(s): Failure initiator not applicable at persistency, so no mitigation is needed. The feature is developed fully deterministic, so no wrong results are expected caused by persistency
    - EX_01_02: Processing too slow: Failure initiator not applicable at persistency. The feature is developed fully deterministic, so no processing too slow is expected caused by persistency.
    - EX_01_03: Processing too fast: Failure initiator not applicable at persistency, so no mitigation is needed. The feature is developed fully deterministic, so no processing too fast is expected caused by persistency.
    - EX_01_04: Loss of execution: Failure initiator not applicable at persistency, so no mitigation is needed. The feature is developed fully deterministic, so no loss of execution is expected caused by persistency.
    - EX_01_05: Processing changes to arbitrary process: Failure initiator not applicable at persistency, so no mitigation is needed.
    - EX_01_06: Processing is not complete (infinite loop): Failure initiator not applicable at persistency, so no mitigation is needed. The feature is developed fully deterministic, so no infinite loop is expected caused by persistency.


.. feat_saf_fmea:: Persistency
    :violates: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__message_nreived
    :fault_id: MF_01_01
    :failure_effect: Message is not received so the feature persistency is not available.
    :mitigated_by: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    User is not able to use the feature. Middleware cant be used. User is not able to use the feature. Middleware cant be used. Loss of execution can only be caused by the application, not by the persistency feature itself.
    Failure handling is addressed to the application by the aou_req__persistency__error_handling.

.. feat_saf_fmea:: Persistency
    :violates: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__late_message
    :fault_id: MF_01_02
    :failure_effect: message received too late.
    :mitigated_by: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    Subset of MF_01_01 if the delay is to long.

.. feat_saf_fmea:: Persistency
    :violates: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__corrupted_message
    :fault_id: MF_01_05
    :failure_effect: message is corrupted so the feature persistency is not available.
    :mitigated_by: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    Covered by MF_01_01

.. feat_saf_fmea:: Persistency
    :violates: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__not_sent
    :fault_id: MF_01_06
    :failure_effect: message is not sent so the feature persistency is not available.
    :mitigated_by: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    Covered by MF_01_01 because the violation cause is the same.

.. feat_saf_fmea:: Persistency
    :violates: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
    :id: feat_saf_fmea__persistency__err_handl
    :fault_id: EX_01_04
    :failure_effect: loss of execution will lead to an unavailability of the persistency feature.
    :mitigated_by: aou_req__persistency__error_handling
    :sufficient: yes
    :status: valid

    User is not able to use the feature. Middleware cant be used. Loss of execution can only be caused by the application, not by the persistency feature itself.
    Failure handling is addressed to the application by the aou_req__persistency__error_handling.

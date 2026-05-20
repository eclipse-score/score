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

FMEA (Failure Modes and Effects Analysis)
#########################################

.. document:: Persistency FMEA
   :id: doc__persistency_fmea
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__feature_fmea
   :tags: persistency


The FMEA for the feature Persistency is performed. To show evidence that all failure initiators are considered, the applicability has to be filled out in the
following tables. For all applicable failure initiators, the FMEA has to be performed.

Failure Mode List
-----------------

Fault Models for sequence diagrams
  .. list-table:: Fault Models for sequence diagrams
     :header-rows: 1
     :widths: 10,20,10,20

    * - ID
      - Failure Mode
      - Applicability
      - Rationale
    * - MF_01_01
      - message is not received (is a subset/more precise description of MF_01_05)
      - yes
      - :need:`feat_saf_fmea__persistency__message_nreived`
    * - MF_01_02
      - message received too late (only relevant if delay is a realistic fault)
      - yes
      - :need:`feat_saf_fmea__persistency__late_message`
    * - MF_01_03
      - message received too early (usually not a problem)
      - no
      - Failure initiator not applicable at persistency, so no mitigation is needed.
    * - MF_01_04
      - message not received correctly by all recipients (different messages or messages partly lost). Only relevant if the same message goes to multiple recipients.
      - no
      - Failure initiator not applicable at persistency, so no mitigation is needed.
    * - MF_01_05
      - message is corrupted
      - yes
      - :need:`feat_saf_fmea__persistency__corrupted_message`
    * - MF_01_06
      - message is not sent
      - yes
      - :need:`feat_saf_fmea__persistency__not_sent`
    * - MF_01_07
      - message is unintended sent
      - no
      - Failure initiator not applicable at persistency. Feature developed fully deterministic, so no unintended messages are expected.
    * - CO_01_01
      - minimum constraint boundary is violated
      - no
      - Failure initiator not applicable at persistency, so no mitigation is needed.
    * - CO_01_02
      - maximum constraint boundary is violated
      - no
      - Failure initiator not applicable at persistency, so no mitigation is needed.
    * - EX_01_01
      - Process calculates wrong result(s) (is a subset/more precise description of MF_01_05 or MF_01_04). This failure mode is related to the analysis if e.g. internal safety mechanisms are required (level 2 function, plausibility check of the output, …) because of the size / complexity of the feature.
      - no
      - Failure initiator not applicable at persistency, so no mitigation is needed. The feature is developed fully deterministic, so no wrong results are expected caused by persistency
    * - EX_01_02
      - processing too slow (only relevant if timing is considered)
      - no
      - Failure initiator not applicable at persistency. The feature is developed fully deterministic, so no processing too slow is expected caused by persistency.
    * - EX_01_03
      - processing too fast (only relevant if timing is considered)
      - no
      - Failure initiator not applicable at persistency, so no mitigation is needed. The feature is developed fully deterministic, so no processing too fast is expected caused by persistency.
    * - EX_01_04
      - loss of execution
      - yes
      - :need:`feat_saf_fmea__persistency__err_handl`
    * - EX_01_05
      - processing changes to arbitrary process
      - no
      - Failure initiator not applicable at persistency, so no mitigation is needed.
    * - EX_01_06
      - processing is not complete (infinite loop)
      - no
      - Failure initiator not applicable at persistency, so no mitigation is needed. The feature is developed fully deterministic, so no infinite loop is expected caused by persistency.

FMEA
----
For all identified applicable failure initiators, the FMEA is performed in the following section.

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

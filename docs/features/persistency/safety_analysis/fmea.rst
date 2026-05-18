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

Failure Mode List
-----------------

.. needimport:: fmea.json
   :hide:

.. needtable::
   :types: feat_saf_fmea
   :columns: id;violates;fault_id;failure_effect;mitigated_by;sufficient;status;content

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


Failure Mode List
-----------------

.. needimport:: fmea.json
   :hide:

.. needtable::
   :types: feat_saf_fmea
   :columns: id;violates;fault_id;failure_effect;mitigated_by;sufficient;status;content

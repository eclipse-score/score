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


FMEA (Failure Modes and Effects Analysis)
=========================================

.. document:: result FMEA
   :id: doc__result_fmea
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__sw_component_fmea

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
      - no
      - If set result was not received before the get value/error are called, this will lead to an exception/terminate. In case of the get value user defined defaults are provided.
    * - MF_01_02
      - message received too late (only relevant if delay is a realistic fault)
      - no
      - Do not see this as a problem for result lib, would lead to the same consideration as in MF_01_01
    * - MF_01_03
      - message received too early (usually not a problem)
      - no
      - No problem for result lib
    * - MF_01_04
      - message not received correctly by all recipients (different messages or messages partly lost). Only relevant if the same message goes to multiple recipients.
      - no
      - No multiple recipients (maybe from different threads?)
    * - MF_01_05
      - message is corrupted
      - yes
      - Error message string is destroyed before accessing it by the user - see :need:`comp_saf_fmea__result__error_message_unavail`
    * - MF_01_06
      - message is not sent
      - yes
      - Value or error are not returned - see :need:`comp_saf_fmea__result__no_return`
    * - MF_01_07
      - message is unintended sent
      - no
      - not applicable for a library
    * - CO_01_01
      - minimum constraint boundary is violated
      - yes
      - Used enum types may not match - see :need:`comp_saf_fmea__result__enum_type_mismatch`
    * - CO_01_02
      - maximum constraint boundary is violated
      - yes
      - same as above
    * - EX_01_01
      - Process calculates wrong result(s) (is a subset/more precise description of MF_01_05 or MF_01_04). This failure mode is related to the analysis if e.g. internal safety mechanisms are required (level 2 function, plausibility check of the output, …) because of the size / complexity of the feature.
      - no
      - Due to low complexity of the component this error is completely eliminated by testing. Low complex architecture according to criteria in :need:`gd_chklst__arch_inspection_checklist` ARC_03_03 and design complexity below numbers as in :need:`gd_req__impl_complexity_analysis`
    * - EX_01_02
      - processing too slow (only relevant if timing is considered)
      - no
      - Due to the small functionality, being too slow is no likely issue.
    * - EX_01_03
      - processing too fast (only relevant if timing is considered)
      - no
      - Get functions only deliver data when called, no "too fast" is possible.
    * - EX_01_04
      - loss of execution
      - yes
      - Loss of execution leads to the same error as MF_01_06
    * - EX_01_05
      - processing changes to arbitrary process
      - no
      - Not a problem of result lib as this is a libray and not a process
    * - EX_01_06
      - processing is not complete (infinite loop)
      - yes
      - User gives back a function as return which induces stop of user execution - see :need:`comp_saf_fmea__result__stop_user`

FMEA
----
For all identified applicable failure initiators, the FMEA is performed in the following section.

.. comp_saf_fmea:: Result Enum Type Mismatch
   :violates: comp_arc_dyn__baselibs__result
   :id: comp_saf_fmea__result__enum_type_mismatch
   :fault_id: CO_01_01
   :failure_effect: User would understand a wrong error type (based on different error domains)
   :mitigation_issue: https://github.com/eclipse-score/score/issues/2880
   :sufficient: no
   :status: valid

   Only if the user would use the error information not only for debug reasons but for selecting the
   type of error reaction this error may have an error impact. We need to make the user aware of this.

.. comp_saf_fmea:: Result Error Message Unavailability
   :violates: comp_arc_dyn__baselibs__result
   :id: comp_saf_fmea__result__error_message_unavail
   :fault_id: MF_01_05
   :failure_effect: Accessing error message could result in undefined behaviour
   :mitigated_by: aou_req__result__resource_lifetime
   :mitigation_issue: https://github.com/eclipse-score/score/issues/2880
   :sufficient: no
   :status: valid

   The linked AoU cares about unavailability of other return objects, but also the error message may be unavailable.

.. comp_saf_fmea:: Result No Return
   :violates: comp_arc_dyn__baselibs__result
   :id: comp_saf_fmea__result__no_return
   :fault_id: MF_01_06
   :failure_effect: Accessing value object could result in undefined behaviour (e.g. usage of wrong value)
   :mitigated_by: aou_req__result__value_handling, aou_req__result__error_reaction
   :sufficient: yes
   :status: valid

   If a value or a error is not returned this will be noticed by the user and reacted upon. This is ensured
   additionally by the provided AoU.

.. comp_saf_fmea:: Result Stop User
   :violates: comp_arc_dyn__baselibs__result
   :id: comp_saf_fmea__result__stop_user
   :fault_id: EX_01_06
   :failure_effect: User could be stopped by a function provided as a result from another user
   :mitigated_by: aou_req__platform__flow_monitoring
   :sufficient: yes
   :status: valid

   Stopping its own execution has to be managed by the user via program flow monitoring, see AoU.

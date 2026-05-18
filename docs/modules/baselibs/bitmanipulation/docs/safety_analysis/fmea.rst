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

.. document:: bitmanipulation FMEA
   :id: doc__bitmanipulation_fmea
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
      - yes
      - If a bit manipulation request is not received there is also no return "ok", this should be covered by the user. See :need:`comp_saf_fmea__bitmanipulation__no_return`
    * - MF_01_02
      - message received too late (only relevant if delay is a realistic fault)
      - yes
      - If a bit manipulation request is received too late, also the return is too late, this should be covered by the user. See :need:`comp_saf_fmea__bitmanipulation__late_return`
    * - MF_01_03
      - message received too early (usually not a problem)
      - no
      - Do not see where this is a problem.
    * - MF_01_04
      - message not received correctly by all recipients (different messages or messages partly lost). Only relevant if the same message goes to multiple recipients.
      - no
      - No multiple recipients, one library per user.
    * - MF_01_05
      - message is corrupted
      - yes
      - Corruption of a message is not applicable in a function call, but a corrupt input (by wrong understanding of the user) of bit locations is. See :need:`comp_saf_fmea__bitmanipulation__wrong_input`
    * - MF_01_06
      - message is not sent
      - yes
      - If bitmanipulation does not return a success status, this should be observed by the user. See :need:`comp_saf_fmea__bitmanipulation__no_return`
    * - MF_01_07
      - message is unintended sent
      - no
      - Error would be to return "Success" when there is no action done. Due to low complexity of the component this error is completely eliminated by testing. See also EX_01_01.
    * - CO_01_01
      - minimum constraint boundary is violated.
      - yes
      - :need:`comp_saf_fmea__bitmanipulation__constraints`
    * - CO_01_02
      - maximum constraint boundary is violated,
      - yes
      - :need:`comp_saf_fmea__bitmanipulation__constraints`
    * - EX_01_01
      - Process calculates wrong result(s) (is a subset/more precise description of MF_01_05 or MF_01_04). This failure mode is related to the analysis if e.g. internal safety mechanisms are required (level 2 function, plausibility check of the output, …) because of the size / complexity of the feature.
      - no
      - Due to low complexity of the component this error is completely eliminated by testing. Low complex architecture according to criteria in :need:`gd_chklst__arch_inspection_checklist` ARC_03_03 and design complexity below numbers as in :need:`gd_req__impl_complexity_analysis`
    * - EX_01_02
      - processing too slow (only relevant if timing is considered)
      - no
      - Bitmanipulation is not expected to be slow due to low functional content.
    * - EX_01_03
      - processing too fast (only relevant if timing is considered)
      - no
      - No problem seen.
    * - EX_01_04
      - loss of execution
      - yes
      - If bitmanipulation execution is lost, it does not return, this should be observed by the user. See :need:`comp_saf_fmea__bitmanipulation__no_return`
    * - EX_01_05
      - processing changes to arbitrary process
      - no
      - Not a bitmanipulation problem as it is a library and not a process.
    * - EX_01_06
      - processing is not complete (infinite loop)
      - yes
      - If bitmanipulation stalls, also the user process may stall, so this should be covered by external safety mechanism. See :need:`comp_saf_fmea__bitmanipulation__late_return`

FMEA
----
For all identified applicable failure initiators, the FMEA is performed in the following section.

.. comp_saf_fmea:: Bitmanipulation No Return
   :violates: comp_arc_dyn__baselibs__bit_manipulation
   :id: comp_saf_fmea__bitmanipulation__no_return
   :fault_id: MF_01_01,MF_01_06,EX_01_04
   :failure_effect: Bitmanipulation is not executed, if safety function relies on this there may be violation of the safety requirements.
   :mitigated_by: aou_req__platform__error_reaction
   :mitigation_issue: https://github.com/eclipse-score/score/issues/2837
   :sufficient: no
   :status: valid

   There is already an aou on platform level which states that a user has to use the return values,
   so the error mode of no return should be covered, but there is no explicit mention that a "success"
   return is needed.

.. comp_saf_fmea:: Bitmanipulation Late Return
   :violates: comp_arc_dyn__baselibs__bit_manipulation
   :id: comp_saf_fmea__bitmanipulation__late_return
   :fault_id: MF_01_02,EX_01_06
   :failure_effect: Bitmanipulation is executed too late or stalls, so there may be violation of its safety requirements.
   :mitigated_by: aou_req__platform__flow_monitoring
   :sufficient: yes
   :status: valid

   There is already an aou on platform level which states that a user has to use program flow monitoring

.. comp_saf_fmea:: Bitmanipulation Constraints
   :violates: comp_arc_dyn__baselibs__bit_manipulation
   :id: comp_saf_fmea__bitmanipulation__constraints
   :fault_id: CO_01_01,CO_01_02
   :failure_effect: If constraints are violated there may be out-of bounds memory corruption.
   :mitigated_by: comp_req__bitmanipulation__bounds_safety
   :sufficient: yes
   :status: valid

   Constraints are checked, see mitigation requirement.

.. comp_saf_fmea:: Bitmanipulation Wrong Input
   :violates: comp_arc_dyn__baselibs__bit_manipulation
   :id: comp_saf_fmea__bitmanipulation__wrong_input
   :fault_id: MF_01_05
   :failure_effect: If enums are wrongly defined, the expectation of what bit(s) are set will not be met.
   :mitigated_by: aou_req__bitmanipulation__enum_constraints
   :sufficient: yes
   :status: valid

   Wrongly defined Enum values are not checked by Bitmanipulation component, the output of the action may be unexpected.
   So the user has to make sure this is done in a right way, covered by the linked AoU.

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
      - The error message carried within the error object does not own the underlying data. If the data source is destroyed before the error message is accessed by the user, the message reference becomes invalid (see :need:`comp_saf_fmea__result__error_message_life`).
    * - MF_01_06
      - message is not sent
      - yes
      - Value or error are not returned - see :need:`comp_saf_fmea__result__unchecked`
    * - MF_01_07
      - message is unintended sent
      - no
      - not applicable for a library
    * - CO_01_01
      - minimum constraint boundary is violated
      - yes
      - The error code returned is not bound to a specific error domain at the type level. A user may interpret the code against the wrong domain, violating the constraint that error codes are only meaningful within their originating domain (see :need:`comp_saf_fmea__result__error_code`).
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
      - Not a problem of result lib as this is a library and not a process
    * - EX_01_06
      - processing is not complete (infinite loop)
      - yes
      - The Result library accepts user-provided operations for value and error transformation. If such an operation does not complete, the calling execution is halted (see :need:`comp_saf_fmea__result__stop_user`).

FMEA
----
For all identified applicable failure initiators, the FMEA is performed in the following section.

.. comp_saf_fmea:: Result Error Code Cross-Domain Misinterpretation
   :violates: comp_arc_dyn__baselibs__result
   :id: comp_saf_fmea__result__error_code
   :fault_id: CO_01_01
   :failure_effect: When retrieving error information, the error code is returned as a domain-agnostic integer. If the user interprets this code under a different error domain than the one that produced it, the error is misidentified, potentially leading to incorrect error reaction.
   :mitigation_issue: https://github.com/eclipse-score/score/issues/2880
   :sufficient: no
   :status: valid

   If the user relies on the error code not only for diagnostic purposes but for selecting an error reaction path,
   misinterpreting the code under a wrong domain could lead to an incorrect safety-relevant decision.
   An Assumption of Use shall ensure the user verifies the error domain before interpreting the error code.

.. comp_saf_fmea:: Result Error Message Lifetime Violation
   :violates: comp_arc_dyn__baselibs__result
   :id: comp_saf_fmea__result__error_message_life
   :fault_id: MF_01_05
   :failure_effect: The error message provided during error construction is stored as a non-owning reference. If the referenced data is no longer valid when the user retrieves the error message, accessing it results in undefined behavior.
   :mitigated_by: aou_req__result__resource_lifetime
   :mitigation_issue: https://github.com/eclipse-score/score/issues/2880
   :sufficient: no
   :status: valid

   The existing Assumption of Use for resource lifetime addresses the validity of error domain objects
   and referenced resources. However, it does not explicitly cover the user-provided error message,
   which is equally subject to lifetime constraints. The AoU should be extended to explicitly include the error message data,
   or a separate AoU should be established for it.

.. comp_saf_fmea:: Result Unchecked Value or Error Access
   :violates: comp_arc_dyn__baselibs__result
   :id: comp_saf_fmea__result__unchecked
   :fault_id: MF_01_06
   :failure_effect: If the user calls value without the result containing a value, or calls error without the result containing an error, the program will terminate. This may occur when the user does not check the state of the result before accessing it.
   :mitigated_by: aou_req__result__value_handling, aou_req__result__error_reaction
   :sufficient: yes
   :status: valid

   If the user accesses the value or the error without first verifying the state of the result,
   the program will deterministically terminate. The provided Assumptions of Use require the user to check and handle both states before access.

.. comp_saf_fmea:: Result Stop User
   :violates: comp_arc_dyn__baselibs__result
   :id: comp_saf_fmea__result__stop_user
   :fault_id: EX_01_06
   :failure_effect: The user provides a transformation or error handling operation to the Result library. If this operation does not terminate (e.g., infinite loop), the calling execution is blocked indefinitely.
   :mitigated_by: aou_req__platform__flow_monitoring
   :sufficient: yes
   :status: valid

   The Result library invokes user-provided operations synchronously during transformation of values or errors.
   Ensuring these operations terminate is outside the scope of the library and is the responsibility of the user via program flow monitoring,
   as covered by the referenced platform-level Assumption of Use.

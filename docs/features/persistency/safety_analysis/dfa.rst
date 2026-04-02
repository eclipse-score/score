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

DFA (Dependent Failure Analysis)
################################

.. document:: Persistency DFA
   :id: doc__persistency_dfa
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__feature_dfa
   :tags: persistency


The DFA for the feature Persistency is performed. To show evidence that all failure initiators are considered, the applicability has to be filled out in the
following tables. For all applicable failure initiators, the DFA has to be performed.

Dependent Failure Initiators
----------------------------

2.1 Shared resources

| 2.2 Communication between the two elements:
| Receiving function is affected by information that is false, lost, sent multiple times, or in the wrong order etc. from the sender.

.. list-table:: DFA communication between elements
  :header-rows: 1
  :widths: 10,20,10,20

  * - ID
    - Violation cause communication between elements
    - Applicability
    - Rationale
  * - CO_01_01
    - Information passed via argument through a function call, or via writing/reading a variable being global to the two software functions (data flow)
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed.
  * - CO_01_02
    - Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information
    - no
    - Persistency is developed fully deterministic. So no corruption, repetition, loss, delay, masquerading or incorrect addressing of information is expected.
  * - CO_01_03
    - Insertion / sequence of information
    - no
    - Subset of CO_01_02.
  * - CO_01_04
    - Corruption of information, inconsistent data
    - no
    - Subset of CO_01_02.
  * - CO_01_05
    - Asymmetric information sent from a sender to multiple receivers, so that not all defined receivers have the same information
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed.
  * - CO_01_06
    - Information from a sender received by only a subset of the receivers
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed.
  * - CO_01_07
    - Blocking access to a communication channel
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed.


| 2.3 Shared information inputs
| Same information input used by multiple functions.

.. list-table:: DFA shared information inputs
  :header-rows: 1
  :widths: 10,20,10,20

  * - ID
    - Violation cause shared information inputs
    - Applicability
    - Rationale
  * - SI_01_02
    - Configuration data
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed.
  * - SI_01_03
    - Constants, or variables, being global to the two software functions
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed.
  * - SI_01_04
    - Basic software passes data (read from hardware register and converted into logical information) to two applications software functions
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed.
  * - SI_01_05
    - Data / function parameter arguments / messages delivered by software function to more than one other function
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed.


| 2.4 Unintended impact
| Unintended impacts to function due to various failures.

.. list-table:: DFA unintended impact
  :header-rows: 1
  :widths: 10,20,10,20

  * - ID
    - Violation cause unintended impact
    - Applicability
    - Rationale
  * - UI_01_01
    - Memory miss-allocation and leaks
    - no
    - Will be considered at the platform DFA.
  * - UI_01_02
    - Read/Write access to memory allocated to another software element
    - no
    - Will be considered at the platform DFA.
  * - UI_01_03
    - Stack/Buffer under-/overflow
    - no
    - Might happens but very unlikely in RUST. Will be considered at the platform DFA.
  * - UI_01_04
    - Deadlocks
    - no
    - Deadlocks are not caused by the KVS, but by the application.
  * - UI_01_05
    - Livelocks
    - no
    - Same consideration as done in UI_01_04.
  * - UI_01_06
    - Blocking of execution
    - yes
    - :need:`feat_saf_dfa__persistency__execution_blocking`
  * - UI_01_07
    - Incorrect allocation of execution time
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed.
  * - UI_01_08
    - Incorrect execution flow
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed.
  * - UI_01_09
    - Incorrect synchronization between software elements
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed.
  * - UI_01_10
    - CPU time depletion
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed. Will be anylysed at the platform DFA.
  * - UI_01_11
    - Memory depletion
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed. Will be anylysed at the platform DFA.
  * - UI_01_12
    - Other HW unavailability
    - no
    - Failure initiator not applicable at persistency, so no mitigation is needed.


DFA
---
For all identified applicable failure initiators, the DFA is performed in the following section.

.. feat_saf_dfa:: Persistency execution blocking
   :violates: feat_arc_sta__persistency__static
   :id: feat_saf_dfa__persistency__execution_blocking
   :failure_id: UI_01_06
   :failure_effect: Blocking of execution. This will lead to a unavailability of the persistency feature.
   :mitigated_by: aou_req__persistency__appl_exec
   :mitigation_issue:
   :sufficient: yes
   :status: valid

   Execution blocking will make persistency not available.

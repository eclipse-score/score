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

Persistency DFA
###############

.. document:: DFA
   :id: doc__persistency_dfa
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__feature_dfa
   :tags: persistency

For the DFA analysis where the failure initiators :need:`gd_guidl__dfa_failure_initiators` are used. The analysis is done before the platform DFA is done.
Safety mechanisms that are used by many features are not considered here, but at the platform DFA. The analysis is only done for the needs of the persistency feature.
The components KVS and JSON will also be considered at the platform DFA. No additional violations within the persistency feature are expected.

The following failure initiators doesn't apply to the persistency feature:

Shared resources
   - SR_01_01: Reused software module: No reused software modules are used.
   - SR_01_02: Library: The file system fs is a library. It will be considered at the platform DFA. Same argument is used for the JSON library.
   - SR_01_04: Basic software: No basic software is used.
   - SR_01_05: Operating system including scheduler: Might be considered at the platform DFA or is out of scope.
   - SR_01_06: Any service stack, e.g. communication stack: No service stack is used.
   - SR_01_09: Execution time: There is no timing impact at persistency, so no mitigation is needed.
   - SR_01_10: Allocated memory: Will be considered at the platform DFA. JSON can effect it, but it should not be allowed.

Communication between the two elements
   - CO_01_01: Information passed via argument through a function call, or via writing/reading a variable being global to the two software functions (data flow): Failure initiator not applicable at persistency, so no mitigation is needed.
   - CO_01_02: Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information: Persistency is developed fully deterministic. So no corruption, repetition, loss, delay, masquerading or incorrect addressing of information is expected.
   - CO_01_03: Insertion / sequence of information: Subset of CO_01_02.
   - CO_01_04: Corruption of information, inconsistent data: Subset of CO_01_02.
   - CO_01_05: Asymmetric information sent from a sender to multiple receivers, so that not all defined receivers have the same informations: Failure initiator not applicable at persistency, so no mitigation is needed.
   - CO_01_06: Information from a sender received by only a subset of the receivers: Failure initiator not applicable at persistency, so no mitigation is needed.
   - CO_01_07: Blocking access to a communication channel: Failure initiator not applicable at persistency, so no mitigation is needed.

Shared information inputs
   - SI_01_02: Configuration data: Failure initiator not applicable at persistency, so no mitigation is needed.
   - SI_01_03: Constants, or variables, being global to the two software functions: Failure initiator not applicable at persistency, so no mitigation is needed.
   - SI_01_04: Basic software passes data (read from hardware register and converted into logical information) to two applications software functions: Failure initiator not applicable at persistency, so no mitigation is needed.
   - SI_01_05: Data / function parameter arguments / messages delivered by software function to more than one other function: Failure initiator not applicable at persistency, so no mitigation is needed.

Unintended impact
   - UI_01_01: Memory miss-allocation and leaks: Will be considered at the platform DFA.
   - UI_01_02: Read/Write access to memory allocated to another software element: Will be considered at the platform DFA.
   - UI_01_03: Stack/Buffer under-/overflow: Might happens but very unlikely in RUST. Will be considered at the platform DFA.
   - UI_01_04: Deadlocks: Deadlocks are not caused by the KVS, but by the application.
   - UI_01_05: Livelocks: Same consideration as done in UI_01_04.
   - UI_01_07: Incorrect allocation of execution time: Failure initiator not applicable at persistency, so no mitigation is needed.
   - UI_01_08: Incorrect execution flow: Failure initiator not applicable at persistency, so no mitigation is needed.
   - UI_01_09: Incorrect synchronization between software elements: Failure initiator not applicable at persistency, so no mitigation is needed.
   - UI_01_10: CPU time depletion: Failure initiator not applicable at persistency, so no mitigation is needed. Will be anylysed at the platform DFA.
   - UI_01_11: Memory depletion: Failure initiator not applicable at persistency, so no mitigation is needed. Will be anylysed at the platform DFA.
   - UI_01_12: Other HW unavailability: Failure initiator not applicable at persistency, so no mitigation is needed.

Development failure initiators
   - SC_01_02: Same development approaches (e.g. IDE, programming and/or modelling language): Will be considered at feature platform DFA.
   - SC_01_03: Same personal: Will be considered at feature platform DFA.
   - SC_01_04: Same social-cultural context (even if different personnel): Will be considered at feature platform DFA.
   - SC_01_05: Development fault (e.g. human error, insufficient qualification, insufficient methods): Will be considered at feature platform DFA.


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

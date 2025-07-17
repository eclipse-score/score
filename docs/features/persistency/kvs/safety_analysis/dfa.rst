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
   :status: draft
   :safety: ASIL_B
   :tags: feature_persistency

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SR_01_01
   |    :violation_id: SR_01_01
   |    :violation_cause: Reused software module
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: There are no reused software modules, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SR_01_02
   |    :violation_id: SR_01_02
   |    :violation_cause: Library fs
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: The file system fs is a library. No mitigation for persistency is needed, because is an elementary library without the functionalites of S-CORE are not availabe.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SR_01_02
   |    :violation_id: SR_01_02
   |    :violation_cause: Library json
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: JSON is a library. A mitigation might be needed but it will not be considered at persistency.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SR_01_04
   |    :violation_id: SR_01_04
   |    :violation_cause: Basic software
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: There are no basic software within persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SR_01_05
   |    :violation_id: SR_01_05
   |    :violation_cause: Operating system including scheduler
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Will be considered at feature platform DFA. Mitigation can't be handled at middleware.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SR_01_06
   |    :violation_id: SR_01_06
   |    :violation_cause: Any service stack, e.g. communication stack
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: There is no service stack at persistency used, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SR_01_07
   |    :violation_id: SR_01_07
   |    :violation_cause: Configuration data. Return values might be falsified.
   |    :mitigation: Integritry check feat_req__persistency__integrity_check
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Integrity check will fail, so the failure will be detected.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SR_01_09
   |    :violation_id: SR_01_09
   |    :violation_cause: Execution time.
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: There is timing impact at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SR_01_10
   |    :violation_id: SR_01_10
   |    :violation_cause: Allocated memory.
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :sufficient: <yes|no>
   |    :argument: Acutally discussed in feature community. JSON can do it, but it should not be allowed.
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__CO_01_01
   |    :violation_id: CO_01_01
   |    :violation_cause: Information passed via argument through a function call, or via writing/reading a variable being global to the two software functions (data flow)
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__CO_01_02
   |    :violation_id: CO_01_02
   |    :violation_cause: Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information.
   |    :mitigation: < NONE|ID from Feature Requirement>  feat_req__persistency__integrity_check? Maybe mitigation is needed. Persistency will be not available or be falsified executed.
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__CO_01_03
   |    :violation_id: CO_01_03
   |    :violation_cause: Insertion / sequence of information
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Subset of feat_saf_DFA__persistency__static CO_01_02
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__CO_01_04
   |    :violation_id: CO_01_04
   |    :violation_cause: Corruption of information, inconsistent data
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Subset of feat_saf_DFA__persistency__static CO_01_02
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__CO_01_05
   |    :violation_id: CO_01_05
   |    :violation_cause: Asymmetric information sent from a sender to multiple receivers, so that not all defined receivers have the same informations
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__CO_01_06
   |    :violation_id: CO_01_06
   |    :violation_cause: Information from a sender received by only a subset of the receivers.
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__CO_01_07
   |    :violation_id: CO_01_07
   |    :violation_cause: Blocking access to a communication channel
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SI_01_02
   |    :violation_id: SI_01_02
   |    :violation_cause: Configuration data.
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SI_01_03
   |    :violation_id: SI_01_03
   |    :violation_cause: Constants, or variables, being global to the two software functions.
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SI_01_04
   |    :violation_id: SI_01_04
   |    :violation_cause: Basic software passes data (read from hardware register and converted into logical information) to two applications software functions.
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SI_01_05
   |    :violation_id: SI_01_05
   |    :violation_cause: Data / function parameter arguments / messages delivered by software function to more than one other function.
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__UI_01_01
   |    :violation_id: UI_01_01
   |    :violation_cause: Memory miss-allocation and leaks.
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Will be considered at feature platform DFA.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__UI_01_02
   |    :violation_id: UI_01_02
   |    :violation_cause: Read/Write access to memory allocated to another software element.
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Will be considered at feature platform DFA.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__UI_01_03
   |    :violation_id: UI_01_03
   |    :violation_cause: Stack/Buffer under-/overflow. Might happens but very unlikely in RUST. Recursive functions could be the violation cause.
   |    :mitigation: < NONE|ID from Feature Requirement> Compilerüberwachung / AoU
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__UI_01_04
   |    :violation_id: UI_01_04
   |    :violation_cause: Deadlocks.
   |    :mitigation: aou_req__persistency__appl_design
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: Deadlocks are not caused by the KVS, but by the application.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__UI_01_05
   |    :violation_id: UI_01_05
   |    :violation_cause: Livelocks
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Same consideration as done in feat_saf_DFA__persistency__static UI_01_04
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__UI_01_06
   |    :violation_id: UI_01_06
   |    :violation_cause: Blocking of execution.
   |    :mitigation: aou_req__persistency__appl_exec
   |    :mitigation_issue: None
   |    :sufficient: yes
   |    :argument: Execution blocking will make persistency not available.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__UI_01_07
   |    :violation_id: UI_01_07
   |    :violation_cause: Incorrect allocation of execution time.
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__UI_01_08
   |    :violation_id: UI_01_08
   |    :violation_cause: Incorrect execution flow
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__UI_01_09
   |    :violation_id: UI_01_09
   |    :violation_cause: Incorrect synchronization between software elements
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__UI_01_10
   |    :violation_id: UI_01_10
   |    :violation_cause: CPU time depletion
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__UI_01_11
   |    :violation_id: UI_01_11
   |    :violation_cause: Memory depletion
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__UI_01_12
   |    :violation_id: UI_01_12
   |    :violation_cause: Other HW unavailability
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Failure initiator not applicable at persistency, so no mitigation is needed.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SC_01_02
   |    :violation_id: SC_01_02
   |    :violation_cause: Same development approaches (e.g. IDE, programming and/or modelling language)
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Will be considered at feature platform DFA.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SC_01_03
   |    :violation_id: SC_01_03
   |    :violation_cause: Same personal
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Will be considered at feature platform DFA.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SC_01_04
   |    :violation_id: SC_01_04
   |    :violation_cause: Same social-cultural context (even if different personnel). Only applicable if diverse development is needed.
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Will be considered at feature platform DFA.
   |    :status: valid

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_sta__persistency__static
   |    :id: feat_saf_DFA__persistency__SC_01_05
   |    :violation_id: SC_01_05
   |    :violation_cause: Development fault (e.g. human error, insufficient qualification, insufficient methods). Only applicable if diverse development is needed.
   |    :mitigation: NONE
   |    :mitigation_issue: NONE
   |    :sufficient: yes
   |    :argument: Will be considered at feature platform DFA.
   |    :status: valid

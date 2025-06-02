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
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SR_01_01
   |    :violation_cause: Reused software module. N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SR_01_02
   |    :violation_cause: Libraries. . N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SR_01_04
   |    :violation_cause: Basic software. N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SR_01_05
   |    :violation_cause: Operating system including scheduler. Platformebene. Nicht von Middleware handlebar
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>      

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SR_01_06
   |    :violation_cause: Any service stack, e.g. communication stack. N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SR_01_07
   |    :violation_cause: Configuration data. Return values might be falsified.
   |    :mitigation: < NONE|ID from Feature Requirement> Integritry check feat_req__kvs__integrity_check
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SR_01_09
   |    :violation_cause: Execution time. N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SR_01_10
   |    :violation_cause: Allocated memory. Diskussion aktuell in Feature-Community. JSON kann das, sollte aber eigentlich nicht erlaubt sein
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: CO_01_01
   |    :violation_cause: Information passed via argument through a function call, or via writing/reading a variable being global to the two software functions (data flow)   <- Checken ob das Fehlerbild überhaupt passt. 1. Satzteil nicht passen zu 2.>
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: CO_01_02
   |    :violation_cause: Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information. Fehlerhafte ausführung oder nichtverfügbarkeit vom feature
   |    :mitigation: < NONE|ID from Feature Requirement>  feat_req__kvs__integrity_check
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: CO_01_03
   |    :violation_cause: Insertion / sequence of information   wie CO_01_02
   |    :mitigation: < NONE|ID from Feature Requirement> feat_req__kvs__integrity_check
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: CO_01_04
   |    :violation_cause: Corruption of information, inconsistent data    wie CO_01_02
   |    :mitigation: < NONE|ID from Feature Requirement> keine Erkennung
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: CO_01_05
   |    :violation_cause: Asymmetric information sent from a sender to multiple receivers, so that not all defined receivers have the same informations  N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: CO_01_06
   |    :violation_cause: Information from a sender received by only a subset of the receivers. N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: CO_01_07
   |    :violation_cause: Blocking access to a communication channel N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SI_01_02
   |    :violation_cause: Configuration data. N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SI_01_03
   |    :violation_cause: Constants, or variables, being global to the two software functions. N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SI_01_04
   |    :violation_cause: Basic software passes data (read from hardware register and converted into logical information) to two applications software functions. N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SI_01_05
   |    :violation_cause: Data / function parameter arguments / messages delivered by software function to more than one other function. Unklar was das Fehlerbild ist
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: UI_01_01
   |    :violation_cause: Memory miss-allocation and leaks. Platformebene
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: UI_01_02
   |    :violation_cause: Read/Write access to memory allocated to another software element. Platformebene
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: UI_01_03
   |    :violation_cause: Stack/Buffer under-/overflow. Könnte passieren, ist aber unwahrscheinlich in RUST. Recursive Funktionen könnten die Ursache sein.
   |    :mitigation: < NONE|ID from Feature Requirement> Compilerüberwachung / AoU
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: UI_01_04
   |    :violation_cause: Deadlocks. Könnten auftreten. Würde von Applikation verursacht werden. KVS kann da nichts machen
   |    :mitigation: < NONE|ID from Feature Requirement> AoU
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: UI_01_05
   |    :violation_cause: Livelocks wie UI_01_04
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: UI_01_06
   |    :violation_cause: Blocking of execution. Feature is not available.
   |    :mitigation: < NONE|ID from Feature Requirement> AoU 
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: UI_01_07
   |    :violation_cause: Incorrect allocation of execution time. N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: UI_01_08
   |    :violation_cause: Incorrect execution flow N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: UI_01_09
   |    :violation_cause: Incorrect synchronization between software elements N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: UI_01_10
   |    :violation_cause: CPU time depletion N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: UI_01_11
   |    :violation_cause: Memory depletion N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: UI_01_12
   |    :violation_cause: Other HW unavailability N/A
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SC_01_02
   |    :violation_cause: Same development approaches (e.g. IDE, programming and/or modelling language)
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SC_01_03
   |    :violation_cause: Same personal
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SC_01_04
   |    :violation_cause: Same social-cultural context (even if different personnel). Only applicable if diverse development is needed.
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: Persistency
   |    :verifies: feat_arc_dyn__kvs__check_key_default
   |    :id: feat_saf_DFA__persistency__check_key_default
   |    :violation_id: SC_01_05
   |    :violation_cause: Development fault (e.g. human error, insufficient qualification, insufficient methods). Only applicable if diverse development is needed.
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>







   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SR_01_01
   |    :violation_cause: Reused software modules
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SR_01_02
   |    :violation_cause: Libraries
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SR_01_04
   |    :violation_cause: Basic software
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SR_01_05
   |    :violation_cause: Operating system including scheduler
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>      

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SR_01_06
   |    :violation_cause: Any service stack, e.g. communication stack
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SR_01_07
   |    :violation_cause: Configuration data
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SR_01_09
   |    :violation_cause: Execution time
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SR_01_10
   |    :violation_cause: Allocated memory
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: CO_01_01
   |    :violation_cause: Information passed via argument through a function call, or via writing/reading a variable being global to the two software functions (data flow)
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: CO_01_02
   |    :violation_cause: Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: CO_01_03
   |    :violation_cause: Insertion / sequence of information
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: CO_01_04
   |    :violation_cause: Corruption of information, inconsistent data
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: CO_01_05
   |    :violation_cause: Asymmetric information sent from a sender to multiple receivers, so that not all defined receivers have the same informations
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: CO_01_06
   |    :violation_cause: Information from a sender received by only a subset of the receivers
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: CO_01_07
   |    :violation_cause: Blocking access to a communication channel
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SI_01_02
   |    :violation_cause: Configuration data
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SI_01_03
   |    :violation_cause: Constants, or variables, being global to the two software functions
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SI_01_04
   |    :violation_cause: Basic software passes data (read from hardware register and converted into logical information) to two applications software functions
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SI_01_05
   |    :violation_cause: Data / function parameter arguments / messages delivered by software function to more than one other function
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: UI_01_01
   |    :violation_cause: Memory miss-allocation and leaks
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: UI_01_02
   |    :violation_cause: Read/Write access to memory allocated to another software element
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: UI_01_03
   |    :violation_cause: Stack/Buffer under-/overflow
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: UI_01_04
   |    :violation_cause: Deadlocks
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: UI_01_05
   |    :violation_cause: Livelocks
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: UI_01_06
   |    :violation_cause: Blocking of execution
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: UI_01_07
   |    :violation_cause: Incorrect allocation of execution time
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: UI_01_08
   |    :violation_cause: Incorrect execution flow
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: UI_01_09
   |    :violation_cause: Incorrect synchronization between software elements
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: UI_01_10
   |    :violation_cause: CPU time depletion
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: UI_01_11
   |    :violation_cause: Memory depletion
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: UI_01_12
   |    :violation_cause: Other HW unavailability
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SC_01_02
   |    :violation_cause: Same development approaches (e.g. IDE, programming and/or modelling language)
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>    

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SC_01_03
   |    :violation_cause: Same personal
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SC_01_04
   |    :violation_cause: Same social-cultural context (even if different personnel). Only applicable if diverse development is needed.
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: SC_01_05
   |    :violation_cause: Development fault (e.g. human error, insufficient qualification, insufficient methods). Only applicable if diverse development is needed.
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

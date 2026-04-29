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


DFA (Dependent Failure Analysis)
================================

.. document:: Baselibs DFA
   :id: doc__baselibs_dfa
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feature_dfa


Dependent Failure Initiators
----------------------------

The DFA for the feature baselibs is performed. To show evidence that all failure initiators are considered, the applicability has to be filled out in the
following tables. For all applicable failure initiators, the DFA has to be performed.

Dependent Failure Initiators
----------------------------

Shared resources
^^^^^^^^^^^^^^^^

.. list-table:: DFA shared resources (used for Platform DFA)
  :header-rows: 1
  :widths: 10,20,10,20

  * - ID
    - Violation cause shared resources
    - Applicability
    - Rationale
  * - SR_01_01
    - Reused software modules
    - no
    - Baselibs only uses libraries and not other executable modules.
  * - SR_01_02
    - Libraries
    - yes
    - Baselibs filesystem component may suffer from concurrent access to a file, :need:`feat_saf_dfa__baselibs__conc_file_access`
  * - SR_01_04
    - Basic software
    - no
    - Not a baselibs specific topic, covered on platform level.
  * - SR_01_05
    - Operating system including scheduler
    - no
    - Not a baselibs specific topic, covered on platform level.
  * - SR_01_06
    - Any service stack, e.g. communication stack
    - no
    - Not a baselibs specific topic, covered on platform level.
  * - SR_01_07
    - Configuration data
    - no
    - No shared configuration data for baselibs.
  * - SR_01_09
    - Execution time
    - no
    - Not a baselibs specific topic, covered on platform level.
  * - SR_01_10
    - Allocated memory
    - yes
    - Bitmanipulation component may operate on the same memory, :need:`feat_saf_dfa__baselibs__conc_memory_access`

Communication between the two elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Receiving function is affected by information that is false, lost, sent multiple times, or in the wrong order etc. from the sender.

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
    - According to its architecture shown in :need:`feat_arc_sta__baselibs__static_view_arch` baselibs do not rely on common input.
  * - CO_01_02
    - Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information
    - no
    - Baselibs are not sending messages between their components.
  * - CO_01_03
    - Insertion / sequence of information
    - no
    - Baselibs are not sending messages between their components.
  * - CO_01_04
    - Corruption of information, inconsistent data
    - no
    - Baselibs are not sending messages between their components. Data eventually shared by function calls are covered by FMEA already.
  * - CO_01_05
    - Asymmetric information sent from a sender to multiple receivers, so that not all defined receivers have the same information
    - no
    - Asymmetric information sending is not done in baselibs.
  * - CO_01_06
    - Information from a sender received by only a subset of the receivers
    - no
    - This is not done in baselibs.
  * - CO_01_07
    - Blocking access to a communication channel
    - no
    - There are no communication channels in baselibs.

Shared information inputs
^^^^^^^^^^^^^^^^^^^^^^^^^

Same information input used by multiple functions.

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
    - There is no shared config data in baselibs.
  * - SI_01_03
    - Constants, or variables, being global to the two software functions
    - no
    - No global variables are used in baselibs.
  * - SI_01_04
    - Basic software passes data (read from hardware register and converted into logical information) to two applications software functions
    - no
    - No shared low level data are used between baselibs.
  * - SI_01_05
    - Data / function parameter arguments / messages delivered by software function to more than one other function
    - no
    - No common input can be seen in architecture of baselibs.

Unintended impact
^^^^^^^^^^^^^^^^^

Unintended impacts to function due to various failures.

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
    - Not a specific baselibs topic, therefore covered at platform DFA.
  * - UI_01_02
    - Read/Write access to memory allocated to another software element
    - yes
    - As baselibs are in context of a application, they may access their memory, :need:`feat_saf_dfa__baselibs__memory_access`
  * - UI_01_03
    - Stack/Buffer under-/overflow
    - no
    - Not a specific baselibs topic, therefore covered at platform DFA.
  * - UI_01_04
    - Deadlocks
    - yes
    - shared memory or file access may lead to deadlock, :need:`feat_saf_dfa__baselibs__locked_ressource`
  * - UI_01_05
    - Livelocks
    - no
    - Should be covered together with deadlock.
  * - UI_01_06
    - Blocking of execution
    - yes
    - As baselibs are in context of a application, they may block execution, :need:`feat_saf_dfa__baselibs__blocked_execution`
  * - UI_01_07
    - Incorrect allocation of execution time
    - no
    - Execution time allocated by (external) OS on platform level, should be covered centrally at platform level.
  * - UI_01_08
    - Incorrect execution flow
    - no
    - Execution flow controlled by (external) OS on platform level, should be covered centrally at platform level.
  * - UI_01_09
    - Incorrect synchronization between software elements
    - no
    - There is no need for synchronization for baselibs.
  * - UI_01_10
    - CPU time depletion
    - yes
    - Baselibs may deplete or suffer from depletion, :need:`feat_saf_dfa__baselibs__cpu_starvation`
  * - UI_01_11
    - Memory depletion
    - no
    - Not a specific baselibs topic, therefore covered at platform DFA.
  * - UI_01_12
    - Other HW unavailability
    - no
    - No special HW used for baselibs.


DFA
===

For all identified applicable failure initiators, the DFA is performed in the following section.

.. feat_saf_dfa:: memory access
   :violates: feat_arc_sta__baselibs__static_view_arch
   :id: feat_saf_dfa__baselibs__memory_access
   :failure_id: UI_01_02
   :failure_effect: memory of using component may be corrupted leading to safety requirement violation
   :mitigation_issue: https://github.com/eclipse-score/score/issues/2816
   :sufficient: no
   :status: valid

   All the baselibs components have to be developed to ASIL_B standard to maintain Freedom From Interference,
   out of bounds access should be detected by unit testing/sanitizers.

.. feat_saf_dfa:: locked ressource
   :violates: feat_arc_sta__baselibs__static_view_arch
   :id: feat_saf_dfa__baselibs__locked_ressource
   :failure_id: UI_01_04
   :failure_effect: Deadlock/Livelock leads to stalling of the execution
   :mitigated_by: feat_req__baselibs__memory_library,aou_req__platform__flow_monitoring
   :sufficient: yes
   :status: valid

   Only components "filesystem" and "memory_shared" should have the problem ("bitmanipulation" should not be affected due to shortness of execution)
   "memory_shared" cares for this by above linked feature requirement and :need:`comp_req__memory__atomic_ops`.
   "filesystem" component may fail on this but this is covered by common platform aou linked above.

.. feat_saf_dfa:: concurrent file access
   :violates: feat_arc_sta__baselibs__static_view_arch
   :id: feat_saf_dfa__baselibs__conc_file_access
   :failure_id: SR_01_02
   :failure_effect: Concurrent file access may lead to corruption of the file
   :mitigated_by: aou_req__filesystem__thread_safety
   :sufficient: yes
   :status: valid

   The user has to care for concurrent file access. This is not covered by the filesytem library.

.. feat_saf_dfa:: concurrent memory access
   :violates: feat_arc_sta__baselibs__static_view_arch
   :id: feat_saf_dfa__baselibs__conc_memory_access
   :failure_id: SR_01_10
   :failure_effect: Concurrent memory access may lead to corruption of the memory
   :mitigated_by: aou_req__bitmanipulation__concurrent_access
   :sufficient: yes
   :status: valid

   The user has to care for concurrent memory access. This is not covered by the bitmanipulation library.

.. feat_saf_dfa:: blocked execution
   :violates: feat_arc_sta__baselibs__static_view_arch
   :id: feat_saf_dfa__baselibs__blocked_execution
   :failure_id: UI_01_06
   :failure_effect: Using application is blocked from execution and thus cannot fulfill its safety function
   :mitigation_issue: https://github.com/eclipse-score/score/issues/2816
   :sufficient: no
   :status: valid

   All the baselibs components have to be developed to ASIL_B standard to maintain Freedom From Interference,
   all blocks should be detected by unit testing.

.. feat_saf_dfa:: CPU starvation
   :violates: feat_arc_sta__baselibs__static_view_arch
   :id: feat_saf_dfa__baselibs__cpu_starvation
   :failure_id: UI_01_10
   :failure_effect: CPU starvation leads to delayed execution and may violate safety timing requirements.
   :mitigated_by: aou_req__platform__flow_monitoring
   :sufficient: yes
   :status: valid

   Some care is taken to avoid using too much CPU time, but this cannot be covered fully.
   Platform level AoU asks applications with timing requirements to cover this by program flow monitoring.

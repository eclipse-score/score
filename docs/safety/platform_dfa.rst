..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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


Platform DFA (Dependent Failure Analysis)
=========================================

.. document:: Platform DFA
   :id: doc__score_platform_dfa
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: NO
   :realizes: wp__platform_dfa[version==1]
   :tags:

.. note:: The platform DFA is only performed once at platform level to analyse the dependencies between the features of the platform.
          The results shall be used as an input for the safety analysis so that general safety mechanisms are only defined once and not in every single safety analysis.

.. note:: Use the content of the document to describe e.g. why a fault model is not applicable for the diagram.


The DFA for the platform is performed based on :need:`doc__platform_architecture`.
To show evidence that all failure initiators are considered, the applicability has to be filled out in the
following tables. For all applicable failure initiators, the DFA has to be performed.

Dependent Failure Initiators
----------------------------

Shared resources
^^^^^^^^^^^^^^^^

.. note:: Shared libraries is only then applicable as a shared resource if the feature and the related safety mechanisms are using this specific library. If the library is not used by the feature or the related safety mechanisms, it is not applicable as shared resource at the end.


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
    - There is no feature in S-CORE platform which is the safety mechanism for another feature. So eventual reuse would not be a problem.
  * - SR_01_02
    - Libraries
    - yes
    - :need:`plat_saf_dfa__safety__shared_lib`
  * - SR_01_04
    - Basic software
    - no
    - Assumption is that the "basic software" relates to HW near SW, if this is relevant for a feature may only be analyzed on feature/component level.
  * - SR_01_05
    - Operating system including scheduler
    - yes
    - :need:`plat_saf_dfa__safety__os_failures`
  * - SR_01_06
    - Any service stack, e.g. communication stack
    - yes
    - :need:`plat_saf_dfa__safety__stack_failure`
  * - SR_01_07
    - Configuration data
    - no
    - S-CORE featues do not share configuration data
  * - SR_01_09
    - Execution time
    - yes
    - :need:`plat_saf_dfa__safety__execution_timing`
  * - SR_01_10
    - Allocated memory
    - yes
    - :need:`plat_saf_dfa__safety__memory_overwrites`


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
    - yes
    - :need:`plat_saf_dfa__safety__wrong_data`, global variables are not used
  * - CO_01_02
    - Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information
    - yes
    - :need:`plat_saf_dfa__safety__communication_errors`
  * - CO_01_03
    - Insertion / sequence of information
    - yes
    - :need:`plat_saf_dfa__safety__communication_errors`
  * - CO_01_04
    - Corruption of information, inconsistent data
    - yes
    - :need:`plat_saf_dfa__safety__communication_errors`
  * - CO_01_05
    - Asymmetric information sent from a sender to multiple receivers, so that not all defined receivers have the same information
    - no
    - This should be covered on feature and component level.
  * - CO_01_06
    - Information from a sender received by only a subset of the receivers
    - no
    - This should be covered on feature and component level.
  * - CO_01_07
    - Blocking access to a communication channel
    - no
    - Blocking execution is already covered in other questions (UI_01_06), not receiving information is covered in feature/components FMEAs

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
    - S-CORE featues do not share configuration data
  * - SI_01_03
    - Constants, or variables, being global to the two software functions
    - no
    - Shared memory is only used between components using communication feature, this is covered in the respective safety analysis.
  * - SI_01_04
    - Basic software passes data (read from hardware register and converted into logical information) to two applications software functions
    - no
    - no shared HW register access known for S-CORE features
  * - SI_01_05
    - Data / function parameter arguments / messages delivered by software function to more than one other function
    - no
    - no data sent from one feature to more than one other feature

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
    - yes
    - :need:`plat_saf_dfa__safety__memory_overwrites`
  * - UI_01_02
    - Read/Write access to memory allocated to another software element
    - yes
    - :need:`plat_saf_dfa__safety__memory_overwrites`
  * - UI_01_03
    - Stack/Buffer under-/overflow
    - yes
    - :need:`plat_saf_dfa__safety__over_underflow`
  * - UI_01_04
    - Deadlocks
    - yes
    - :need:`plat_saf_dfa__safety__execution_timing`
  * - UI_01_05
    - Livelocks
    - yes
    - :need:`plat_saf_dfa__safety__execution_timing`
  * - UI_01_06
    - Blocking of execution
    - yes
    - :need:`plat_saf_dfa__safety__execution_timing`
  * - UI_01_07
    - Incorrect allocation of execution time
    - yes
    - :need:`plat_saf_dfa__safety__execution_flow`
  * - UI_01_08
    - Incorrect execution flow
    - yes
    - :need:`plat_saf_dfa__safety__execution_flow`
  * - UI_01_09
    - Incorrect synchronization between software elements
    - no
    - This is not a platform level analysis item, should be covered on feature/component level. Do not see synchronization need between features.
  * - UI_01_10
    - CPU time depletion
    - yes
    - :need:`plat_saf_dfa__safety__execution_timing`
  * - UI_01_11
    - Memory depletion
    - yes
    - :need:`plat_saf_dfa__safety__exception_memory`, :need:`plat_saf_dfa__safety__dyn_memory`
  * - UI_01_12
    - Other HW unavailability
    - yes
    - :need:`plat_saf_dfa__safety__hw_errors`

Development failure initiators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Section is **only applicable if a diverse SW development is needed** due to decomposition.

.. note::

  Section shall be applied only once to analyse all dependencies of the features. Results shall be checked during of the analysis of new features if this is applicable to the feature.

.. list-table:: DFA development failure initiators (Platform DFA)
  :header-rows: 1
  :widths: 10,20,10,20

  * - ID
    - Violation cause development failure initiators
    - Applicability
    - Rationale
  * - SC_01_02
    - Same development approaches (e.g. IDE, programming and/or modelling language)
    - no
    - no diverse SW development is needed
  * - SC_01_03
    - Same personal
    - no
    - no diverse SW development is needed
  * - SC_01_04
    - Same social-cultural context (even if different personnel). Only applicable if diverse development is needed.
    - no
    - no diverse SW development is needed
  * - SC_01_05
    - Development fault (e.g. human error, insufficient qualification, insufficient methods). Only applicable if diverse development is needed.
    - no
    - no diverse SW development is needed


DFA
===

For all identified applicable failure initiators, the DFA is performed in the following section.


.. plat_saf_dfa:: Memory overflow by exceptions
   :violates: feat_arc_sta__all__platform
   :id: plat_saf_dfa__safety__exception_memory
   :failure_id: UI_01_11
   :failure_effect: allocating memory for exception handling may exceed memory limits and cause unspecified effects also to safety relevant functions
   :safety_relevant: yes
   :mitigated_by: aou_req__platform__no_exceptions[version==1]
   :sufficient: yes
   :status: valid
   :version: 1

   As exceptions are not allowed, the error should not happen.

.. plat_saf_dfa:: Dynamic Memory overflow
   :violates: feat_arc_sta__all__platform
   :id: plat_saf_dfa__safety__dyn_memory
   :failure_id: UI_01_11
   :failure_effect: allocating dynamic memory may exceed memory limits and cause unspecified effects also to safety relevant functions
   :safety_relevant: yes
   :mitigated_by: aou_req__platform__no_heap_alloc_after_init[version==1]
   :sufficient: yes
   :status: valid
   :version: 1

   As dynamic memory allocation is not allowed after initialization (which is expected to happen before safety functions are started), the error should not happen.

.. plat_saf_dfa:: Wrong data in function call
   :violates: feat_arc_sta__all__platform
   :id: plat_saf_dfa__safety__wrong_data
   :failure_id: CO_01_01
   :failure_effect: using wrong or stale data returned may impact the using application's safety function
   :safety_relevant: yes
   :mitigated_by: aou_req__platform__success_expected[version==1], aou_req__platform__no_mixed_asil[version==1], stkh_req__dependability__error_reaction[version==1]
   :sufficient: yes
   :status: valid
   :version: 1

   As the S-CORE platform SW always returns a success/failed status (if successful/failed), applications can avoid using stale or wrong data.
   A check of the ASIL level of the used libraries of any platform SW and application SW should avoid using "QM" data.

.. plat_saf_dfa:: execution timing
   :violates: feat_arc_sta__all__platform
   :id: plat_saf_dfa__safety__execution_timing
   :failure_id: UI_01_10,SR_01_09,UI_01_04,UI_01_05,UI_01_06
   :failure_effect: any QM component could use up CPU time or cause dead/livelocks and thus delay or block safety applications
   :safety_relevant: yes
   :mitigated_by: aou_req__platform__flow_monitoring[version==1], stkh_req__dependability__flow_monitoring[version==1], aou_req__platform__external_health_management[version==1], stkh_req__dependability__health_management[version==1], stkh_req__dependability__safe_state[version==1]
   :sufficient: yes
   :status: valid
   :version: 1

   The S-CORE safety concept is not to avoid the CPU time depletion but to detect it by using alive monitoring.
   If even the alive monitoring is blocked from execution, an external monitor should detect this.

.. plat_saf_dfa:: execution flow
   :violates: feat_arc_sta__all__platform
   :id: plat_saf_dfa__safety__execution_flow
   :failure_id: UI_01_07,UI_01_08
   :failure_effect: if safety applications have requirements on execution sequence or timing, these could be violated by misallocation of execution time (too little time budget, wrong sequence)
   :safety_relevant: yes
   :mitigated_by: stkh_req__dependability__health_management[version==1]
   :sufficient: yes
   :status: valid
   :version: 1

   Deadline and logical monitoring detect the execution flow errors.

.. plat_saf_dfa:: memory overwrites
   :violates: feat_arc_sta__all__platform
   :id: plat_saf_dfa__safety__memory_overwrites
   :failure_id: UI_01_01,UI_01_02,SR_01_10
   :failure_effect: if the memory of a safety application is overwritten by another application this will cause unspecified effects also to safety relevant functions
   :safety_relevant: yes
   :mitigated_by: aou_req__platform__process_isolation[version==1], aou_req__platform__no_mixed_asil[version==1], aou_req__platform__hardware_safety[version==1], aou_req__platform__os_safety_functions[version==1], stkh_req__dependability__no_mixed_asil[version==1]
   :sufficient: yes
   :status: valid
   :version: 1

   Processes memory should be isolated against each other (by OS, Hypervisor and HW means) and if running within the same process SW components should avoid writing into the wrong memory by
   having the same quality (ASIL level) as the using applications.

.. plat_saf_dfa:: OS failures
   :violates: feat_arc_sta__all__platform
   :id: plat_saf_dfa__safety__os_failures
   :failure_id: SR_01_05
   :failure_effect: OS failures may lead to unspecified reactions of the safety functions
   :safety_relevant: yes
   :mitigated_by: aou_req__platform__os_safety_functions[version==1],aou_req__os__safe_fctn_use[version==1],aou_req__platform__safety_integration[version==1]
   :sufficient: yes
   :status: valid
   :version: 1

   Operating system functions may be a common cause for decomposed safety functions. The current safety concept does not expect diverse OS but the relevant OS functions are required in ASIL quality and OS AoU to be followed.

.. plat_saf_dfa:: shared libraries
   :violates: feat_arc_sta__all__platform
   :id: plat_saf_dfa__safety__shared_lib
   :failure_id: SR_01_02
   :failure_effect: Libraries failures may lead to unspecified reactions of the safety functions
   :safety_relevant: yes
   :mitigated_by: aou_req__platform__safety_integration[version==1],aou_req__platform__safety_matching[version==1],stkh_req__functional_req__safe_config[version==1],stkh_req__functional_req__base_libraries[version==1]
   :sufficient: yes
   :status: valid
   :version: 1

   Main libraries used by all S-CORE features for safety functions, apart from the OS provided ones, are Baselibs and Configuration.
   User has to make sure he integrates only libraries of sufficient ASIL and follows their AoU.

   Note: :need:`stkh_req__functional_req__base_libraries` is QM because only a selection of Baselibs Components are ASIL_B, user has to check.

.. plat_saf_dfa:: service stack failures
   :violates: feat_arc_sta__all__platform
   :id: plat_saf_dfa__safety__stack_failure
   :failure_id: SR_01_02
   :failure_effect: Stack failures may lead to unspecified reactions of the safety functions
   :safety_relevant: yes
   :mitigated_by: stkh_req__dependability__e2eprotection[version==1],stkh_req__functional_req__support_of_store[version==1]
   :sufficient: yes
   :status: valid
   :version: 1

   The following service stacks (HW and SW) are considered (according to S-CORE architecture):
   Ethernet communication (potentially ASIL), diagnostics (QM), crypto (QM), time (potentially ASIL), persistency (potentially ASIL)

.. plat_saf_dfa:: stack over underflow
   :violates: feat_arc_sta__all__platform
   :id: plat_saf_dfa__safety__over_underflow
   :failure_id: SR_01_03
   :failure_effect: Stack overflow or underflow may lead to unspecified reactions of the safety functions
   :safety_relevant: yes
   :mitigation_issue: https://github.com/eclipse-score/score/issues/2655
   :sufficient: no
   :status: invalid
   :version: 1

   Stack over/underflow should be avoided or detected by a safety mechanism. ToDo: require this safety mechanism.

.. plat_saf_dfa:: HW errors
   :violates: feat_arc_sta__all__platform
   :id: plat_saf_dfa__safety__hw_errors
   :failure_id: UI_01_12
   :failure_effect: HW errors may corrupt entire SW platform including the safety functions
   :safety_relevant: yes
   :mitigated_by: aou_req__platform__hardware_safety[version==1]
   :sufficient: yes
   :status: valid
   :version: 1

   S-CORE requires a HW safety concept for the HW it is used on.

.. plat_saf_dfa:: Communication errors
   :violates: feat_arc_sta__all__platform
   :id: plat_saf_dfa__safety__communication_errors
   :failure_id: CO_01_02,CO_01_03,CO_01_04
   :failure_effect: Communication errors may invalidate any action by safety functions
   :safety_relevant: yes
   :mitigated_by: stkh_req__dependability__e2eprotection[version==1]
   :mitigation_issue: https://github.com/eclipse-score/score/issues/2655
   :sufficient: no
   :status: valid
   :version: 1

   For the IPC communication the feature's safety analysis covers the error modes, for Some/IP this is covered by an End-to-End protection mechanism. ToDo: Need to make sure all error modes are covered.

.. feat_arc_sta:: Platform Static View
   :id: feat_arc_sta__all__platform
   :security: YES
   :safety: ASIL_B
   :status: invalid
   :version: 1
   :includes: logic_arc_int__baselibs__json[version==1]
   :belongs_to: feat__baselibs[version==1]

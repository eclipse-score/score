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

.. _dfa failure initiators:

DFA failure initiators
======================

.. gd_guidl:: DFA failure initiators
  :id: gd_guidl__dfa_failure_initiators
  :status: valid
  :complies: std_wp__iso26262__software_751, std_wp__iso26262__software_753


:note: Use the failure initiators to ensure a structured analysis. If a failure doesn't apply, please fill in a short desciption in the violation cause of the analysis so it could be recognized that the analysis is done. If there are additional failure initiators needed, please enlage the list of fault models.

**Purpose**

In order to identify all cascading and common cause failures, which may initiated from your feature or components to the platform, other features, components, etc.,
use the following framework of dependent failure initiators to check your completeness of the analysis.

DFA failure initiators
======================

2.1 Shared resources

.. list-table:: DFA shared resources
  :header-rows: 1
  :widths: 10,30,30,30

  * - ID
    - Violation cause shared resources
    - Simplification
    - Importance (can be used for priorisation)
  * - SR_01_01
    - Reused software modules
    -
    - Medium
  * - SR_01_02
    - Libraries
    - SR_01_01
    - Medium
  * - SR_01_04
    - Basic software
    - 
    - Medium
  * - SR_01_05
    - Operating system including scheduler
    -
    - Medium
  * - SR_01_06
    - Any service stack, e.g. communication stack
    -
    - Medium
  * - SR_01_07
    - Configuration data
    -
    - Medium
  * - SR_01_09
    - Execution time
    -
    - Medium
  * - SR_01_10
    - Allocated memory
    -
    - Medium


| 2.2 Communication between the two elements:
| Receiving function is affected by information that is false, lost, sent multiple times, or in the wrong order etc. from the sender.

.. list-table:: DFA communication between elements
  :header-rows: 1
  :widths: 10,30,30,30

  * - ID
    - Violation cause communication between elements
    - Simplification
    - Importance (can be used for priorisation)
  * - CO_01_01
    - Information passed via argument through a function call, or via writing/reading a variable being global to the two software functions (data flow)
    -
    - Medium
  * - CO_01_02
    - Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information
    -
    - Medium
  * - CO_01_03
    - Insertion / sequence of information
    -
    - Medium
  * - CO_01_04
    - Corruption of information, inconsistent data
    -
    - Medium
  * - CO_01_05
    - Asymmetric information sent from a sender to multiple receivers, so that not all defined receivers have the same informations
    -
    - Medium
  * - CO_01_06
    - Information from a sender received by only a subset of the receivers
    -
    - Medium
  * - CO_01_07
    - Blocking access to a communication channel
    -
    - Medium

| 2.3 Shared information inputs
| Same information input used by multiple functions.

.. list-table:: DFA shared information inputs
  :header-rows: 1
  :widths: 10,30,30,30

  * - ID
    - Violation cause shared information inputs
    - Simplification
    - Importance (can be used for priorisation)
  * - SI_01_02
    - Configuration data
    -
    - Medium
  * - SI_01_03
    - Constants, or variables, being global to the two software functions
    -
    - Medium
  * - SI_01_04
    - Basic software passes data (read from hardware register and converted into logical information) to two applications software functions
    -
    - Medium
  * - SI_01_05
    - Data / function parameter arguments / messages delivered by software function to more than one other function
    -
    - Medium

| 2.4 Unintended impact
| Unintended impacts to function due to various failures.

.. list-table:: DFA unintended impact
  :header-rows: 1
  :widths: 10,30,30,30

  * - ID
    - Violation cause unintended impact
    - Simplification
    - Importance (can be used for priorisation)
  * - UI_01_01
    - Memory miss-allocation and leaks
    -
    - Medium
  * - UI_01_02
    - Read/Write access to memory allocated to another software element
    -
    - Medium
  * - UI_01_03
    - Stack/Buffer under-/overflow
    -
    - Medium
  * - UI_01_04
    - Deadlocks
    - 
    - Medium
  * - UI_01_05
    - Livelocks
    -
    - Medium
  * - UI_01_06
    - Blocking of execution
    -
    - Medium
  * - UI_01_07
    - Incorrect allocation of execution time
    -
    - Medium
  * - UI_01_08
    - Incorrect execution flow
    -
    - Medium
  * - UI_01_09
    - Incorrect synchronization between software elements
    -
    - Medium
  * - UI_01_10
    - CPU time depletion
    -
    - Medium
  * - UI_01_11
    - Memory depletion
    -
    - Medium
  * - UI_01_12
    - Other HW unavailability
    -         
    - Medium

| Development failure initiators
| Secition is **only aplicable if a divers SW development is needed** due to decomposition.

:note: Section shall be applied on platform level. Results shall be implemented in general to the S-CORE development definitions.

.. list-table:: DFA development failure initiators
  :header-rows: 1
  :widths: 10,30,30,30

  * - ID
    - Violation cause development failure initiators
    - Simplification
    - Importance (can be used for priorisation)
  * - SC_01_02
    - Same development approaches (e.g. IDE, programming and/or modelling language)
    -
    - Medium
  * - SC_01_03
    - Same personal
    -
    - Medium
  * - SC_01_04
    - Same social-cultural context (even if different personnel). Only applicable if diverse development is needed.
    -
    - Medium
  * - SC_01_05
    - Development fault (e.g. human error, insufficient qualification, insufficient methods). Only applicable if diverse development is needed.
    -
    - Medium

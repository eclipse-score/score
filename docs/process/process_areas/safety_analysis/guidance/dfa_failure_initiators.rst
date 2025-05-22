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


:note: Use the failure initiators to ensure a structed analysis. If a fault model doesn't apply, please fill in a short desciption in the
       violation cause so it could be recognized that the analysis is done. If there are additional failure initiators needed, please
       enlage the list of fault models.

    **Purpose**

    In order to identify all cascading and common cause failures, which may initiated from your feature or components to the platform, other features, components, etc.,
    use the following framework of dependent failure initiators to check your completeness of the analysis.

    **DFA failure initiators**

    | 2.1 Shared resources

    .. list-table:: DFA shared resources
       :header-rows: 1
       :widths: 10,30,30,30

      * - ID
        - Violation cause shared resource used by several components
        - Avoidance, or detection and mitigation of the fault
        - Comment
      * - SR_01_01
        - Reused standard software modules
        -
        -
      * - SR_01_02
        - Libraries
        -
        -
      * - SR_01_03
        - Middleware
        -
        -
      * - SR_01_04
        - Basic software
        -
        -
      * - SR_01_05
        - Operating system including scheduler
        -
        -
      * - SR_01_06
        - Any service stack, e.g. communication stack
        -
        -
      * - SR_01_07
        - Configuration data
        -
        -
      * - SR_01_09
        - Execution time
        -
        -
      * - SR_01_10
        - Allocated memory
        -
        -

    | 2.2 Communication between the two elements:
    | Receiving function is affected by information that is false, lost, sent multiple times, or in the wrong order etc. from the sender.

    .. list-table:: DFA communication between elements
       :header-rows: 1
       :widths: 10,30,30,30

      * - ID
        - Violation cause
          communication between elements
        - Avoidance, or detection and mitigation of the fault
        - Comment
      * - CO_01_01
        - Information passed via argument through a function call,
          or via writing/reading a variable being global to the
          two software functions (data flow)
        -
        -
      * - CO_01_02
        - Data or message corruption / repetition (*) / loss (*) /
          delay (*) / masquerading or incorrect addressing of
          information (*)
        -
        -
      * - CO_01_03
        - Insertion (*) / sequence of information (*)
        -
        -
      * - CO_01_04
        - Corruption of information, inconsistent data (*)
        -
        -
      * - CO_01_05
        - Asymmetric information sent from a sender to multiple
          receivers (*)
        -
        -
      * - CO_01_06
        - Information from a sender received by only a subset of the
          receivers (*)
        -
        -
      * - CO_01_07
        - Blocking access to a communication channel (*)
        -
        -

    | (*) These issues are taken from the arguments on freedom from interference between software elements.
    |     In that respect, the dependent failure initiators Unintended Impact and Communication represent causes of violation of freedom from interference for software.

    | 2.3 Shared information inputs
    | Same information consumed by the two functions even in absence of shared resources, i.e. from a functional perspective.

    .. list-table:: DFA shared information inputs
       :header-rows: 1
       :widths: 10,30,30,30

      * - ID
        - Violation cause
          Shared resource used by several components
        - Avoidance, or detection and mitigation of the fault
        - Comment
      * - SI_01_02
        - Configuration data
        -
        -
      * - SI_01_03
        - Constants, or variables, being global to the two software
          functions
        -
        -
      * - SI_01_04
        - Basic software passes data (read from hardware register and
          converted into logical information) to two applications
          software functions
        -
        -
      * - SI_01_05
        - Data / function parameter arguments / messages delivered by
          software function to more than one other function
        -
        -

    | 2.4 Unintended impact
    | Two functions affecting each other’s elements directly via an implicit, that is unintended, interface.

    .. list-table:: DFA unintended impact
       :header-rows: 1
       :widths: 10,30,30,30

      * - ID
        - Violation cause
          Shared resources used by several components
        - Avoidance, or detection and mitigation of the fault
        - Comment
      * - UI_01_01
        - Memory miss-allocation and leaks
        -
        -
      * - UI_01_02
        - Read/Write access to memory allocated to another software
          element (*)
        -
        -
      * - UI_01_03
        - Stack/Buffer under-/overflow (*)
        -
        -
      * - UI_01_04
        - Deadlocks (*)
        -
        -
      * - UI_01_05
        - Livelocks (*)
        -
        -
      * - UI_01_06
        - Blocking of execution (*)
        -
        -
      * - UI_01_07
        - Incorrect allocation of execution time (*)
        -
        -
      * - UI_01_08
        - Incorrect synchronization between software elements (*)
        -
        -

    | (*) These issues are taken from the arguments on freedom from interference between software elements.
    |     In that respect, the dependent failure initiators Unintended Impact and Communication represent causes of violation of freedom from interference for software.

    | 2.5 Systematic coupling

    .. list-table:: DFA systematic coupling
       :header-rows: 1
       :widths: 10,30,30,30

      * - ID
        - Violation cause
          Shared resources used by several components
        - Avoidance, or detection and mitigation of the fault
        - Comment
      * - SC_01_02
        - Non-diverse development approaches including:
          - same software tools (e.g. IDE, compiler, linker)
          - same algorithms
          - same programming and/or modelling language used
        -
        -
      * - SC_01_03
        - Same personal
        -
        -
      * - SC_01_04
        - Same social-cultural context (even if different personnel)
        -
        -
      * - SC_01_05
        - Development fault, e.g.
          - human error
          - insufficiently qualified personnel
          - process weaknesses
          - insufficient methods
        -
        -

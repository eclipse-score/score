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

.. _dfa checklist:

DFA Checklist
=============

.. gd_chklst:: DFA Checklist
    :id: gd_chklst__dfa
    :status: valid
    :tags: safety analysis

    **Purpose**

    In order to identify all cascading and common cause failures, which may initiated from your feature or components to the platform, other features, components, etc.,
    use the following framework of dependent failure initiators to check your completeness of the analysis.

    **Checklist**

    | 2.1 Shared resources
    | Same software element instance used by the two functions which are therefore affected by the failure or unavailability of that shared resource.

    .. list-table:: Requirement Inspection Checklist
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
      * - SR_01_08
        - Calibration data
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

    .. list-table:: Requirement Inspection Checklist
       :header-rows: 1
       :widths: 10,30,30,30

      * - ID
        - Violation cause
          Shared resource used by several components
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

    | 2.3 Shared information inputs
    | Same information consumed by the two functions even in absence of shared resources, i.e. from a functional perspective.

    .. list-table:: Requirement Inspection Checklist
       :header-rows: 1
       :widths: 10,30,30,30

      * - ID
        - Violation cause
          Shared resource used by several components
        - Avoidance, or detection and mitigation of the fault
        - Comment
      * - SI_01_01
        - Calibration data
        -
        -
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

    .. list-table:: Requirement Inspection Checklist
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
    | Systematic causes from human or tool errors can lead to the simultaneous failure of more than one function.

    .. list-table:: Requirement Inspection Checklist
       :header-rows: 1
       :widths: 10,30,30,30

      * - ID
        - Violation cause
          Shared resources used by several components
        - Avoidance, or detection and mitigation of the fault
        - Comment
      * - SC_01_01
        - Manufacturing fault / repair fault (e.g. false flashing,
          false calibration reference for sensors)
        -
        -
      * - SC_01_02
        - Non-diverse development approaches including:
          - same software tools (e.g. IDE, compiler, linker)
          - same algorithms
          - same programming and/or modelling language used
          - same complier/linker used
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

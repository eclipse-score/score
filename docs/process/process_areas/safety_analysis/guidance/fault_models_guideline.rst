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

Fault Models
============

.. gd_guidl:: Fault Models
   :id: gd_guidl__fault_models
   :status: valid
   :complies: std_wp__iso26262__software_752, std_req__iso26262__analysis_846

    Fault Models for activity diagrams

    .. list-table:: Fault Models for activity diagrams
       :header-rows: 1
       :widths: 15,6,30,30,15

      * - Element
        - ID
        - Failure Mode
        - Simplification
        - Importance
      * - data storage
        - DS_01_01
        - stored data changed
          (before read operation)
        -
        - High
      * - data storage
        - DS_01_02
        - new data not stored (keeps old data)
          / stuck-at (specific value)
        -
        - High
      * - data flow
        - DF_01_01
        - transferred data changed
        - DS_01_01 if there is one data flow to the data store
        - Medium
      * - data flow
        - DF_01_02
        - transferred data lost
        - DS_01_02 if there is one data flow to the data store
        - Medium
      * - data flow
        - DF_01_03
        - transferred to wrong data store
        - DS_01_01 unless point in time of change is important
        - Low
      * - data flow
        - DF_01_04
        - data stored at wrong location in data store
        - relevant only for arrays/complex types
        - High
      * - processing
        - PS_01_01
        - process calculates wrong result(s)
        - DS_01_01 unless process affects multiple data stores
        - High
      * - processing
        - PS_01_02
        - processing too slow/fast
        - relevant only if timing is considered, infinite loop->CF01_01
        - Low
      * - control flow
        - CF_01_01
        - control flow stops
        -
        - High
      * - control flow
        - CF_01_02
        - control flow skips process
        - PS_01_01 and PS_01_02
        - Medium
      * - control flow
        - CF_01_03
        - control flow proceeds to wrong process
        - CF_01_02 or limited to specific process
        - Low
      * - fork
        - FK_01_01
        - some but not all outgoing concurrent processes are triggered
        -
        - Medium
      * - fork
        - FK_01_02
        - concurrent processes are triggered despite incoming process has not yet been completed
        - similar to CF_01_02
        - Low
      * - fork
        - FK_01_03
        - none of the outgoing concurrent processes is triggered
        - similar to CF_01_01
        - Low
      * - join
        - JF_01_01
        - execution proceeds before all joining processes have been completed
        - similar to CF_01_02
        - High
      * - join
        - JF_01_02
        - execution does not proceed despite all joining processes have been completed
        - similar to CF_01_01
        - Medium


   | Fault Model for sequence diagrams

    .. list-table:: Fault Models for sequence diagrams
       :header-rows: 1
       :widths: 15,6,30,30,15

      * - Element
        - ID
        - Failure Mode
        - Simplification
        - Importance
      * - message
        - MF_01_01
        - message is not received
        - MF_01_05
        - Low
      * - message
        - MF_01_02
        - message received too late
        - relevant only if delay is a realistic fault
        - Medium
      * - message
        - MF_01_03
        - message received too early
        - usually not a problem
        - Low
      * - message
        - MF_01_04
        - message not received correctly by all recipients (different messages or messages partly lost)
        - only relevant if the same message goes to multiple recipients
        - Low
      * - message
        - MF_01_05
        - message is corrupted
        -
        - High
      * - duration/time constraint
        - CO_01_01
        - minimum constraint boundary is violated
        -
        - Medium
      * - duration/time constraint
        - CO_01_02
        - maximum constraint boundary is violated
        -
        - High
      * - execution
        - EX_01_01
        - Process calculates wrong result(s)
        - MF_01_05 or MF_01_04
        - High
      * - execution
        - EX_01_02
        - processing too slow/fast
        - relevant only if timing is considered
        - Low
      * - execution
        - EX_01_03
        - processing changes to arbitrary process
        -
        - Low
      * - execution
        - EX_01_04
        - processing is not complete (infinite loop)
        -
        - Low
      * - frame (*)
        - FE_01_01
        - frame not entered as specified
        -
        - Medium
      * - frame (*)
        - FE_01_02
        - frame not exited as specified
        -
        - Medium
      * - frame (*)
        - FE_01_03
        - frame entered differently than specified
        -
        - Medium
      * - frame (*)
        - FE_01_04
        - frame exited differently than specified
        -
        - Medium

   | (*) frame is a reference to another diagram, which describes more detailed aspects. Entry- and Exit points define the order of transitions.

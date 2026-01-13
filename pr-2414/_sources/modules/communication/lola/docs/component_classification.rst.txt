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

Component Classification
========================

.. note:: Document header

.. document:: lola Component Classification
   :id: doc__lola_comp_class
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__sw_component_class

| Classification of lola
|
| `Lola IPC <https://github.com/eclipse-score/communication>`_ v0.1.1
|
| Additional documentation considered:
| :need:`doc__com` and :need:`doc__com_ipc`


Step 1: Determine (P): the uncertainty of the Processes applied
---------------------------------------------------------------

| Apply the process measures to determine (P).
| The result of a process measure shall have as outcome [HE, PE, NE]
| - HE: High Evidence
| - PE: Partly Evidence but Manageable
| - NE: No Evidence

.. list-table:: Determine (P)
        :header-rows: 1

        * - Id
          - Indicator for applying process
          - Result
          - Rationale for result

        * - 1
          - Are rules, state-of-the art processes applied for the design, implementation and verification?
          - PE
          - The component was already qualified as part of an OEM SW platform safety case, but not all work products are available open source.

        * - 2
          - Are requirements available?
          - PE
          - See `lola trlc <https://github.com/eclipse-score/communication/blob/main/score/mw/com/requirements>`_ available but not according to S-CORE process - perform content centric inspection of component requirements and also checking matching of S-CORE and lola feature requirements

        * - 3
          - Are specifications for functionalities and properties available (architecture)?
          - HE
          - Created using S-CORE process: :need:`mod_view_sta__com__communication`

        * - 4
          - Are design specifications available?
          - PE
          - `lola/design <https://github.com/eclipse-score/communication/blob/main/score/mw/com/design/README.md>`_ available but not according to S-CORE process - perform content centric inspection inclusive the matching of S-CORE feature architecture with lola design

        * - 5
          - Are configuration specification and data available, if applicable?
          - HE
          - See `lola/design/configuration <https://github.com/eclipse-score/communication/tree/main/score/mw/com/design/configuration>`_

        * - 6
          - Are verification measures including tests and reports available?
          - PE
          - Unit tests available and configured failure blocks the merge of any lola pull request, evidences links TBD, need to check for integration testing


| (P=1) shall be selected when none of the determined process measures indicate PE or NE.
| (P=2) shall be selected when at least one of the determined process measures indicate PE or NE, but the gaps evaluated are acceptable, means
|       the risk of systematic faults due to these gaps is sufficiently low or manageable by mitigating the gaps.
| (P=3) in all other cases.

lola is determined as P=2


Step 2: Determine (C): the uncertainty of finding systematic faults based on the Complexity
-------------------------------------------------------------------------------------------

| Apply the complexity measures to determine (C).
| The result of a complexity measure shall have as outcome [NH, HM, NM]
| - NH: Not High
| - HM: High but Manageable
| - NM: high and Not Manageable
|
| **Complexity measure for programming language: C++**

.. list-table:: Determine (C) for C++
    :header-rows: 1

    * - Id
      - Indicator for high Complexity
      - Complexity measure Tool
      - Result
      - Number

    * - 1
      - High amount of Lines of Code
      - Lines of Code (without comments) (generated code is excluded)
      - HM
      - <Number>

    * - 2
      - Cyclomatic complexity
      - Static Code Analysis tooling
      - NH
      - <Number>

    * - 3
      - | Test exists / Coverage (Function, Line)
        | (maybe better: testability, but how to measure?)
      - Existing Tests Coverage
      - NH
      - <Number>

    * - 4
      - High amount of public function interfaces
      - Number of public function interfaces
      - NH
      - <Number>

    * - 5
      - High amount of function parameters
      - Number of parameters
      - NH
      - <Number>


| (C=1) shall be selected when none of the determined complexity measures indicate HM or NM.
| (C=2) shall be selected when at least one of the determined complexity measures indicate HM or NM, but the gaps evaluated are acceptable, means
|       the risk of systematic faults due to these gaps is sufficiently low in the context of the project or manageable by mitigating the gaps.
| (C=3) in all other cases.
|

lola is determined as C=2


Step 3: Determine (CLAS_OUT): the classification outcome
--------------------------------------------------------

| Select CLAS_OUT depending on the determined values of (C) and (P)

+-------+-----------------------+
| ( C ) | ( P )                 |
+-------+-------+-------+-------+
|       |  1    |  2    |  3    |
+=======+=======+=======+=======+
| 1     |  Q    |  Q    | QR    |
+-------+-------+-------+-------+
| 2     |  QR   | QR    | QR    |
+-------+-------+-------+-------+
| 3     |  QR   | QR    | NQ    |
+-------+-------+-------+-------+

lola is classified as CLAS_OUT=QR


Step 4: Document all results and rationale for choosing (P) and (C) and (CLAS_OUT)
----------------------------------------------------------------------------------
This document


Step 5: Based on (CLAS_OUT) select the activities
-------------------------------------------------

| As soon as the change request containing this is in status "Accepted", the module safety plan for the component development is adapted based on the following: (select according to above result)
| - Q: Follow the processes for qualification of software components in a safety context.
| - QR: Follow the process for pre-existing software architectural elements
| - NQ: Do no use this element in safety context

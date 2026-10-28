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

.. document:: LoLa Component Classification
   :id: doc__lola_comp_class
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: NO
   :realizes: wp__sw_component_class[version==1]

| Classification of LoLa
|
| `LoLa <https://github.com/eclipse-score/communication>`_ version is as stated in the current reference integration's release note.
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
          - See `LoLa trlc <https://github.com/eclipse-score/communication/tree/main/score/mw/com/dependability/requirements>`_ available but not inspected according to S-CORE process - check inspection checklist delta and re-perform if needed

        * - 3
          - Are specifications for functionalities and properties available (architecture)?
          - PE
          - See `LoLa arc <https://github.com/eclipse-score/communication/tree/main/score/mw/com/dependability/architectural_design/static_design>`_
            and `LoLa SW arc <https://github.com/eclipse-score/communication/tree/main/score/mw/com/dependability/software_architectural_design>`_
            available but not inspected according to S-CORE process - check inspection checklist delta and re-perform if needed

        * - 4
          - Are design specifications available?
          - PE
          - `LoLa/design <https://github.com/eclipse-score/communication/tree/main/score/mw/com/design>`_
            available but not inspected according to S-CORE process - check inspection checklist delta and re-perform if needed

        * - 5
          - Are configuration specification and data available, if applicable?
          - HE
          - Configuration is done by the user by json files, explained in `tutorial <https://eclipse-score.github.io/communication/latest/score/mw/com/doc/tutorial/README.html>`_

        * - 6
          - Are verification measures including tests and reports available?
          - PE
          - Unit and integration tests available and configured failure blocks the merge of any lola pull request, evidences links see `q-report <https://eclipse-score.github.io/communication/latest/quality_reports.html>`_ and `feat_req test report <https://eclipse-score.github.io/communication/latest/docs/sphinx/mw_com_index/traceability_report/feature_requirements.html>`_ - need to find component test report
            Safety Analysis performed and documented in `<https://eclipse-score.github.io/communication/latest/docs/sphinx/mw_com_index/dependability_analysis/mw_com_dependability_analysis/safety_analysis.html>`_


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
      - >1000

    * - 2
      - Cyclomatic complexity
      - Static Code Analysis tooling
      - HM
      - was determined in external project and did not block qualification

    * - 3
      - Test exists / Coverage (Function, Line)
      - Existing Tests Coverage
      - NH
      - See `coverage <https://eclipse-score.github.io/communication/latest/quality/coverage/index.html>`_ - missing coverage gaps in mw/com to be resolved

    * - 4
      - High amount of public function interfaces
      - Number of public function interfaces
      - HM
      - See `<https://eclipse-score.github.io/communication/latest/generated/api_index.html>`_ - interface is comparable to AUTOSAR standard, check if safety analysis full covers interface in :need:`doc__communication_safety_analysis_fdr`

    * - 5
      - High amount of function parameters
      - Number of parameters
      - NH
      - see above


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

LoLa is classified as CLAS_OUT=QR


Step 4: Document all results and rationale for choosing (P) and (C) and (CLAS_OUT)
----------------------------------------------------------------------------------
This document


Step 5: Based on (CLAS_OUT) select the activities
-------------------------------------------------

| As soon as the change request containing this is in status "Accepted", the module safety plan for the component development is adapted based on the following: (select according to above result)
| - Q: Follow the processes for qualification of software components in a safety context.
| - QR: Follow the process for pre-existing software architectural elements
| - NQ: Do no use this element in safety context

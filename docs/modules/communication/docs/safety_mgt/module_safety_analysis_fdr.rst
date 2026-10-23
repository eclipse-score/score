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


Communication Safety Analysis Checklist
=======================================

.. document:: Communication Safety Analysis Checklist
  :id: doc__communication_safety_analysis_fdr
  :status: draft
  :version: 1
  :safety: ASIL_B
  :security: YES
  :realizes: wp__fdr_reports

**Purpose**

The purpose of this Safety Analysis (DFA and FMEA) formal review report template is to collect the topics to be checked during verification of the Safety Analysis.

**Conduct**

As described in :need:`wf__p_formal_rv`, the formal document review is performed by an "external" safety manager:

- reviewer: **<committer with safety manager skills explicitly named here>**
- scope: **<describe the scope of the review here, e.g. "the safety analysis of the module and its results">**

**Checklist**

Please note that it is mandatory to fill in the "passed" column with "yes" or "no" for each checklist item and additional to add in the remarks why it is passed or not passed. In case of "no" an issue link to the issue tracking system has to be added in the last column. See also :need:`doc_concept__wp_inspections` for further information about reviews in general and inspection in particular.


.. list-table:: General Checklist
      :header-rows: 1
      :widths: 10,30,10,30,20

      * - ID
        - Safety analysis activity
        - Compliant to ISO 26262?
        - Reference
        - Comment

      * - Gen 1
        - Are the safety analysis performed according to the defined process and templates? See :need:`gd_req__saf_structure` and also :need:`gd_temp__feat_saf_fmea` and :need:`gd_temp__feat_saf_dfa`
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_841>`, :need:`[[title]] <std_req__iso26262__analysis_849>`, :need:`[[title]] <std_req__iso26262__analysis_8410>`, :need:`[[title]] <std_req__iso26262__analysis_748>`
        - <Rationale for result>

      * - Gen 2
        - Are the safety analysis performed in a systematic way to identify the potential dependent failures / failure modes and their effects? Are the failure effect and the mitigation described?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_849>`, :need:`[[title]] <std_req__iso26262__analysis_8410>`
        - <Ensured and checked by application of the defined templates and processes>

      * - Gen 3
        - Is the result of the safety analysis indicate if the safety requirements are complied?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_842>`
        - <Rationale for result>

      * - Gen 4
        - Are the mitigations effective and implemented?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_844>`
        - <Rationale for result>

      * - Gen 5
        - Are all AoU's that are used as mitigation's created and covered in the safety manual?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_845>`
        - <Rationale for result>

      * - Gen 6
        - Are additional safety-related test cases determined by potential results of the safety analyses?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_847>`
        - <Rationale for result>


.. list-table:: DFA Checklist
      :header-rows: 1
      :widths: 10,30,10,30,20

      * - ID
        - Safety analysis activity
        - Compliant to ISO 26262?
        - Reference
        - Comment

      * - DFA 1
        - Are the potential dependent failures identified by performing a DFA?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_741>`
        - <Rationale for result>

      * - DFA 2
        - Is it plausible that each potential identified dependent failure that has been identified, will lead to a dependent failure which cause a violation of FFI?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_742>`
        - <Rationale for result>

      * - DFA 3
        - Are applicable operational situations and operating modes considered?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_743>`
        - <Rationale for result>

      * - DFA 4
        - Are the failure initiators :need:`[[title]] <gd_guidl__dfa_failure_initiators>` suitable and applied?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_744>`
        - <Rationale for result>

      * - DFA 5
        - Is a rationale provided for each identified potential dependent failure?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_745>`
        - <Rationale for result>

      * - DFA 6
        - Are measures defined to resolve the identified potential dependent failures?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_746>`, :need:`[[title]] <std_req__iso26262__analysis_747>`, :need:`[[title]] <std_req__iso26262__analysis_843>`
        - <Rationale for result>

      * - DFA 7
        - Can be the required level of independence shown for the identified potential dependent failures?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_748>`
        - <Rationale for result>


.. list-table:: FMEA Checklist
      :header-rows: 1
      :widths: 10,30,10,30,20

      * - ID
        - Safety analysis activity
        - Compliant to ISO 26262?
        - Reference
        - Comment

      * - FMEA 1
        - Are the fault models suitable and applied for the FMEA? See :need:`gd_guidl__fault_models` and also :need:`gd_req__saf_structure`
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_846>`
        - <Rationale for result>

      * - FMEA 2
        - Are measures defined to resolve the identified faults?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_843>`
        - <Rationale for result>

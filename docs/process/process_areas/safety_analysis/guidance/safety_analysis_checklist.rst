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


Checklist for Safety Analysis
================================

.. gd_chklst:: Safety Analysis Checklist Template
   :id: gd_chklst__safety_analysis
   :status: valid
   :tags: safety_analysis

   **Purpose**
   The purpose of this safety analysis checklist template is to collect the topics to be checked during verification of the safety analysis.

   **Checklist**

   .. list-table:: Safety Analysis Checklist
      :header-rows: 1
      :widths: 10,30,30,15,8,8

      * - Review ID
        - Acceptance Criteria
        - Guidance
        - Passed
        - Remarks
        - Issue link
      * - REQ_01_01
        - Is / are the safety analysis is / are finished?
        - 
        - No open topics in safety analysis report.
        - <yes|no>
        -
      * - REQ_01_02
        - Are the templates for DFA or / and Safety Analysis used?
        - see :need:`gd_temp__plat_saf_dfa` / :need:`gd_temp__feat_saf_fmea`
        - Templates are used to generate the DFA or / and Safety Analysis.
        - <yes|no>
        -
      * - REQ_01_03
        - Were the failure initiators / fault models applied?
        - see :need:`gd_guidl__dfa_failure_initiators` / :need:`gd_guidl__fault_models`
        - The items of the failure initiators / fault models are used to ensure a structured analysis.
        - <yes|no>
        - 
      * - REQ_01_04
        - Is the vialation cause described completly and in an easily understandable manner?
        - 
        - The cause of the violation is described completly. The cause can be recognized easily.
        - <yes|no>
        -        
      * - REQ_01_05
        - Is the mitigation described completly and in an easily understandable manner?
        - 
        - The mitigation is described completly and can be recognized easily.
        - <yes|no>
        -          
      * - REQ_01_06
        - Is the overall result of the safety analysis described in the report?
        - 
        - The results of the safety analysis are described in the report. The report is available :need:`wp__saf_analysis_report`.
        - <yes|no>
        -          
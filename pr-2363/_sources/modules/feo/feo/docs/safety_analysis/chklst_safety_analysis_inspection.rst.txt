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

.. document:: FEO Safety Analysis Inspection Checklist
   :id: doc__safety_analysis_inspection_component_feo
   :status: draft
   :security: NO
   :safety: ASIL_B
   :tags: component_feo
   :realizes: wp__training_path

FEO Component Safety Analysis Checklist
=======================================

   **Purpose**
   The purpose of this safety analysis (DFA and FMEA) checklist template is to collect the topics to be checked during verification of the safety analysis.

   **Checklist**

   .. list-table:: FEO Component Safety Analysis Checklist
      :header-rows: 1
      :widths: 10,30,30,15,8,8

      * - Review ID
        - Acceptance Criteria
        - Guidance
        - Passed
        - Remarks
        - Issue link
      * - REQ_01_01
        - Is / are the attribute sufficient set correctly?
        - The mitigations shall have a direct influence ont the violation by prevention, detection or mitigation to reduce the risk to an acceptable level.
        - The mitigations are sufficient.
        - <yes|no>
        -
      * - REQ_01_02
        - Are the templates for DFA and/or FMEA used?
        - See :need:`gd_temp__comp_saf_dfa` / :need:`gd_temp__comp_saf_fmea` and also :need:`gd_req__saf_structure`
        - Templates are used to generate the DFA or / and FMEA.
        - <yes|no>
        -
      * - REQ_01_03
        - Were the failure initiators / fault models applied?
        - See :need:`gd_guidl__dfa_failure_initiators` / :need:`gd_guidl__fault_models`
        - The applicable items of the failure initiators / fault models are used to ensure a structured analysis. For all not applicable items an argument shall be given in the content of the document.
        - <yes|no>
        -
      * - REQ_01_04
        - Are the failure effects clearly and completely described?
        - Use the generic failure effect descriptions and enlarge the description if it's applicable to the considered element.
        - The effects of the failure is described completely. The effect can be recognized easily.
        - <yes|no>
        -
      * - REQ_01_06
        - Is the attribute "mitigated by" linked correct?
        - Check if the correct failure effect is linked via "mitigated by".
        - The "mitigated by" link is correct.
        - <yes|no>
        -
      * - REQ_01_07
        - Is the sufficiency of the "mitigated by" (prevention, detection or mitigation) described or can it be recognized easily?
        - The sufficiency of the "mitigated by" is described in the content of the document. It can be recognized easily.
        - The "mitigated by" shows clearly that a fault / failure can be mitigated by the linked requirement by prevention, detection or mitigation. It shall be described in the contend.
        - <yes|no>
        -
      * - REQ_01_08
        - Is the overall result of the safety analysis described in the report?
        - It shall be shown in the report if the safety analysis are finished and if all artifacts are "valid" and "sufficient".
        - The results of the safety analysis are described in the report. The report is available :need:`wp__verification_platform_ver_report`.
        - <yes|no>
        -

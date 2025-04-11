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


Guidelines
##########

.. gd_guidl:: Safety Analysis Guideline
   :id: gd_guidl__safety_analysis
   :status: valid
   :complies: std_req__iso26262__analysis_841, std_req__iso26262__analysis_842, std_req__iso26262__analysis_843, std_req__iso26262__analysis_844, std_req__iso26262__analysis_847, std_req__iso26262__analysis_848, std_req__iso26262__analysis_849, std_req__iso26262__analysis_8410, std_wp__iso26262__analysis_851

This document describes the general guidances for Safety Analysis based on the concept which is defined :need:`[[title]]<doc_concept__safety__analysis>`.

Workflow for Safety Analysis
============================

Detailed description which steps are need for implementation.

#. To analyse the Feature Architecture a Safety Analysis and a DFA shall be executed.
#. Perform Safety Analysis on the feature.
#. Perform DFA on the feature.
#. To analyse the Architecture a Safety Analysis and a DFA shall be executed.
#. Perform Safety Analysis on the component.
#. Perform DFA on the component.
#. The performance of the Safety Analysis and DFA shall be monitored and verified.
#. Open issues like from the Safety Analysis and DFA shall be monitored by the Issue Tracking system.
#. The verification of the Architecture is completed when Safety Analysis and DFA are completed by using the checklist and all open issues are closed.


Step-by-Step-approach DFA:
^^^^^^^^^^^^^^^^^^^^^^^^^^

The analysis is done by using the template <:need:`gd_temp__dfa`> on the feature or component architectural diagrams using a checklist <:need:`gd_chklst__dfa`>.

**Step 1:**
For each identified violation assign the violation by ID from the DFA checklist and document it as a sphinx-needs directive.
Document the resulting violation causes and effect and the violated safety requirement.
Document safety measure/mechanism to avoid or control the violation.

**Step 2:**
Judge if this is sufficient. If not, request to update the requirements with additional safety measure/mechanism to come to a sufficient outcome.
The analysis is finished, if for each identified violation a mechanism/measure exists.
Unless the attribute sufficient is yes, measure and argument attribute can be still empty.

Alternatively the checklist template can be used. It can be filled out and is then the DFA report.

**Example:**

| .. feat_saf_dfa:: <Element descriptor>
|    :id: feat_saf_DFA__<Feature>__<Element descriptor>
|    :violation_id: "SR_01_05"
|    :violation_cause: "Operating system including scheduler"
|    :violates: FEAT_REQ__persistency_key_val_storage__creation
|    :measure:
|    :sufficient: no
|    :argument:
|    :status: valid


Step-by-Step-approach Safety Analysis:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The analysis is done by using the template <:need:`gd_temp__safety_analysis`> on the feature or component architectural diagrams
(activity and/or sequence diagrams) using a diagram specific applied fault model <:need:`gd_guidl__fault_models`>.
The analysis considers single faults that can violate a safety requirement.

**Step 1:**
For each affected design element in scope of each diagram, assign the faults by ID from the fault model applicable and document it as a sphinx-needs directive.
Document the resulting failure mode and effect and the violated safety requirement.
Document safety measure/mechanism to avoid or control the failure.

**Step 2:**
Judge if this is sufficient. If not, request to update the diagram and the requirements with additional safety measure/mechanism to come to a sufficient outcome.
The analysis is finished, if for each identified faults a mechanism/measure exists.
Unless the attribute sufficient is yes, measure and argument attribute can be still empty.

**Examples:**


| .. feat_saf_fmea:: OpenKVS
|    :id: FEAT_SAF_FMEA__KVS__OpenKVS
|    :failure_node: "MF_01_05"
|    :failure_effect: "message from calling app is corrupted"
|    :violates: FEAT_REQ_persistency_key_val_storage__interface
|    :measure:
|    :sufficient: no
|    :argument:
|    :status: valid

| .. feat_saf_fmea:: GetKeyValue
|    :id: FEAT_SAF_FMEA__KVS__GetKeyValue
|    :failure_node: "MF_01_05"
|    :failure_effect: "message is corrupted due to corrupted call open to OSAL"
|    :violates: FEAT_REQ_persistency_key_val_storage__interface
|    :measure: FEAT_REQ_persistency_key_val_storage__error
|    :sufficient: yes
|    :argument: "Calling app gets error information"
|    :status: valid

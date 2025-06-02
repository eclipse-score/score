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
   :complies: std_req__iso26262__analysis_841, std_req__iso26262__analysis_842, std_req__iso26262__analysis_843, std_req__iso26262__analysis_844, std_req__iso26262__analysis_847, std_req__iso26262__analysis_848, std_req__iso26262__analysis_849, std_req__iso26262__analysis_8410, std_req__isopas8926__44431, std_req__isopas8926__44432

This document describes the general guidances for Safety Analysis based on the concept which is defined :need:`[[title]]<doc_concept__safety__analysis>`.

Workflow for Safety Analysis
============================

Detailed description which steps are need for a safety analysis. In general the workflow is shown in :ref:`safety_analysis_workflow_fig`

#. To analyse the Platform Architecture DFA shall be executed.
#. Perform DFA on the Platform Architecture.
#. To analyse the Feature Architecture a Safety Analysis and a DFA shall be executed.
#. Perform Safety Analysis on the Feature Architecture.
#. Perform DFA on the Feature Architecture.
#. To analyse the Component Architecture a Safety Analysis and a DFA shall be executed. This only applies if the component architecture is not already covered by the feature architecture.
#. Perform Safety Analysis on the Component Architecture.
#. Perform DFA on the Component Architecture.
#. The performance of the Safety Analysis and DFA (Feature and Component) shall be monitored.
#. For open issues like from the Safety Analysis and DFA and Issue shall be created in the Issue Tracking system. For safety relevant issues types a ``safety`` label is used. Until there are open issues the safety analysis is "valid" and "not sufficient".
#. If the analysis is completed, a verification of the analysis shall be done and a report therfore shall be created.

Step-by-Step-approach Safety Analysis:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The analysis is done by using the template :ref:`safety_analysis_templates` on the feature or component architectural diagrams
(activity and/or sequence diagrams) using a diagram specific applied fault model <:need:`gd_guidl__fault_models`>. Apply the fault
model to the diagram and document the results in the template. If a fault model is not applicable, fill in a short remark in the
vialoation cause that it's not apllicable. So it could be shown that the analysis was done and no fault model is applicable.
The analysis considers single faults that can mitigate a safety requirement.

**Steps:**

* For each affected design element in scope of each diagram, assign the faults by ID from the fault model and document it as a sphinx-needs directive.
* Document the resulting failure mode and effect and the mitigated safety requirement. 
* Document safety mitigation to avoid or control the failure.
* The mitigation coverage shall be estimated in percent. 
* The attributes of the template are described in :ref:`process_requirements_safety_analysis_attributes`.
* Judge if this is sufficient. 
* If not, request to update the diagram and the requirements with additional safety mitigation to come to a sufficient outcome by creating an issue.
* The analysis is finished, if for each identified faults a sufficient mitigation exists. 
* Unless the attribute sufficient is yes, mitigation and argument attribute can be still empty.
* Coninue the analysis until all gault models are checked.
* The verification is done by appling the safety analysis checklist :need:`gd_chklst__safety_analysis`.

**Examples:**


| .. feat_saf_fmea:: OpenKVS
|    :verifies: <Feature architecture>
|    :id: FEAT_SAF_FMEA__KVS__OpenKVS
|    :failure_mode: "MF_01_05"
|    :failure_effect: "message from calling app is corrupted"
|    :mitigation:
|    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
|    :mitigation_coverage: <0..100%>
|    :sufficient: no
|    :argument:
|    :status: valid

| .. feat_saf_fmea:: GetKeyValue
|    :verifies: <Feature architecture>
|    :id: FEAT_SAF_FMEA__KVS__GetKeyValue
|    :failure_mode: "MF_01_05"
|    :failure_effect: "message is corrupted due to corrupted call open to OSAL"
|    :mitigation: FEAT_REQ_persistency_key_val_storage__error
|    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
|    :mitigation_coverage: <0..100%>
|    :sufficient: yes
|    :argument: "Calling app gets error information"
|    :status: valid

The example is also used in the building blocks <:ref:`building_block_example`>.


Step-by-Step-approach DFA:
^^^^^^^^^^^^^^^^^^^^^^^^^^

The analysis is done by using the template :ref:`dfa_templates` on the feature or component architectural diagrams using a list of DFA failure initiators <:need:`gd_guidl__dfa_failure_initiators`>.
If a element of the failure initiators is not applicable, fill in a short remark in the vialoation cause that it's not apllicable.
So it could be shown that the analysis was done and no fault model is applicable.

**Steps:**

* For each failure initiator assign the violation by ID from the DFA failure initiators and document it as a sphinx-needs directive.
* Document the resulting violation causes and effect and the mitigated safety requirement. 
* The mitigation coverage shall be estimated in percent.
* The attributes of the template are described in :ref:`process_requirements_safety_analysis_attributes`.
* Judge if the mitigation is sufficient. If not, request to update the requirements with additional safety mitigation to come to a sufficient outcome.
* The analysis is finished, if for each identified violation a mitigation exists.
* Unless the attribute "sufficient" is "yes", mitigation and argument attribute can be still empty.
* Coninue the analysis until all failure initiators are checked.
* The verification is done by appling the safety analysis checklist :need:`gd_chklst__safety_analysis`.

**Examples:**

| .. feat_saf_dfa:: <Element descriptor>
|    :verifies: <Feature architecture>
|    :id: feat_saf_DFA__<Feature>__<Element descriptor>
|    :violation_id: "SR_01_05"
|    :violation_cause: "Operating system including scheduler"
|    :mitigation:
|    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
|    :mitigation_coverage: <0..100%>
|    :sufficient: no
|    :argument:
|    :status: valid

The example is also used in the concept description <:ref:`safety_analysis_feature_example`> and also in the building blocks <:ref:`building_block_example`>.

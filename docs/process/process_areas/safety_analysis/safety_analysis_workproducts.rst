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

Workproducts Safety Analysis
############################

.. workproduct:: Platform DFA
   :id: wp__platform_dfa
   :status: valid
   :complies: std_wp__iso26262__software_751, std_wp__iso26262__software_753, std_wp__isopas8926__4524

   | Dependent Failure Analysis on platform level
   | - Detection and prevention mitigations linked to Software Platform Requirements
   | Perform analysis on interactions between safety related and non-safety related modules or modules with different ASIL of the platform.


.. workproduct:: Feature Safety Analysis
   :id: wp__feature_safety_analysis
   :status: valid
   :complies: std_wp__iso26262__software_751, std_wp__iso26262__analysis_851, std_wp__isopas8926__4524

   | Bottom-Up Safety Analysis with e.g. FMEA method, verifies the feature architecture (as part of SW Safety Concept)
   | - Detection and prevention mitigations linked to Software Feature Requirements or Feature Assumptions of Use

.. workproduct:: Feature DFA
   :id: wp__feature_dfa
   :status: valid
   :complies: std_wp__iso26262__software_751, std_wp__iso26262__software_753, std_wp__isopas8926__4524

   | Dependent Failure Analysis on feature level
   | - Detection and prevention mitigations linked to Software Feature Requirements or Feature Assumptions of Use
   | Perform analysis on interactions between safety related and non-safety related modules or modules with different ASIL of one feature. Including potential influences from other features in the platform.

.. workproduct:: Component Safety Analysis
   :id: wp__sw_component_safety_analysis
   :status: valid
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__analysis_851, std_wp__isopas8926__4524

   | Bottom-Up Safety Analysis with e.g. FMEA method, verifies the component architecture (as part of SW Safety Concept)
   | - Detection and prevention mitigations linked to Software Component Requirements or Assumptions of Use

.. workproduct:: Component DFA
   :id: wp__sw_component_dfa
   :status: valid
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__software_753, std_wp__isopas8926__4524

   | Dependent Failure Analysis on component/module level
   | - Detection and prevention mitigations linked to Software Component Requirements or Assumptions of Use
   | Perform analysis of safety related and non-safety related sub-elements or sub-elements with different ASIL.
   | Perform analysis on interactions between safety related and non-safety related sub-components or sub-components with different ASIL of one component. Including potential influences from the other components in the component's module.

.. workproduct:: Feature Safety Analysis Report
   :id: wp__saf_analysis_report
   :status: valid
   :complies: std_wp__iso26262__analysis_851, std_wp__iso26262__software_752, std_wp__iso26262__analysis_752, std_wp__iso26262__software_753, std_wp__isopas8926__4524

   | Report of the safety analysis and DFA for the feature. For every feature architecture a report for safety analysis and DFA shall be created.
   | The report shall include:
   | - Coverage of mitigations for the feature architecture (none will also be count as one mitigation)
   | - Number of sufficient mitigations
   | - Number of insufficient mitigations
   | - Number of valid mitigations
   | - Number of invalid mitigations

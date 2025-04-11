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

.. workproduct:: Feature Safety Analysis
   :id: wp__feature_safety_analysis
   :status: valid
   :complies: std_wp__iso26262__analysis_851, std_wp__iso26262__software_752

   Bottom-Up Safety Analysis with e.g. FMEA method, verifies the feature architecture (as part of SW Safety Concept)
   - Detection and prevention mitigations linked to Software Feature Requirements or Assumptions of Use

.. workproduct:: Feature DFA
   :id: wp__feature_dfa
   :status: valid
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__software_753

   Dependent Failure Analysis on platform/feature level
   - Detection and prevention mitigations linked to Software Feature Requirements or Assumptions of Use
   Perform analysis on interactions between safety related and non-safety related modules or modules with different ASIL of one feature. Including potential influences from the rest of the SW platform.

.. workproduct:: Component Safety Analysis
   :id: wp__sw_component_safety_analysis
   :status: valid
   :complies: std_wp__iso26262__analysis_851, std_wp__iso26262__software_752

   Bottom-Up Safety Analysis with e.g. FMEA method, verifies the component architecture (as part of SW Safety Concept)
   - Detection and prevention mitigations linked to Software Component Requirements or Assumptions of Use

.. workproduct:: Component DFA
   :id: wp__sw_component_dfa
   :status: valid
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__software_753

   Dependent Failure Analysis on component/module level
   - Detection and prevention mitigations linked to Software Component Requirements or Assumptions of Use
   Perform analysis of safety related and non-safety related sub-elements or sub-elements with different ASIL.
   Perform analysis on interactions between safety related and non-safety related sub-components or sub-components with different ASIL of one component. Including potential influences from the other components in the component's module.

.. workproduct:: Architecture Verification
   :id: wp__sw_arch_verification
   :status: valid
   :complies: std_wp__iso26262__software_754

   Depends on architecture, FMEA and DFA tooling.
   May include several methods like inspection, modelling ... Which are selected in SW Development Plan.

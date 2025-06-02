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

.. _safety_analysis_templates:

Safety Analysis Templates
=========================

.. gd_temp:: Feature Safety Analysis Template
   :id: gd_temp__feat_saf_fmea
   :status: valid
   :complies: std_wp__iso26262__analysis_851, std_wp__iso26262__software_752, std_wp__isopas8926__4524, std_req__iso26262__software_7410, std_req__iso26262__software_7412, std_req__iso26262__analysis_841, std_req__iso26262__analysis_842, std_req__iso26262__analysis_843, std_req__iso26262__analysis_844, std_req__iso26262__analysis_845, std_req__iso26262__analysis_846, std_req__iso26262__analysis_847, std_req__iso26262__analysis_848, std_req__iso26262__analysis_849, std_req__iso26262__analysis_8410, std_req__isopas8926__44431

   | .. feat_saf_fmea:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_FMEA__<Feature>__<Element descriptor>
   |    :failure_mode: <ID from fault model :need:`gd_guidl__fault_models`>
   |    :failure_effect: "description of failure effect of the failure initiator on the element"
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>


.. gd_temp:: Component Safety Analysis Template
   :id: gd_temp__comp_saf_fmea
   :status: valid
   :complies: std_wp__iso26262__analysis_851, std_wp__iso26262__software_752, std_wp__isopas8926__4524, std_req__iso26262__software_7410, std_req__iso26262__software_7412, std_req__iso26262__analysis_841, std_req__iso26262__analysis_842, std_req__iso26262__analysis_843, std_req__iso26262__analysis_844, std_req__iso26262__analysis_845, std_req__iso26262__analysis_846, std_req__iso26262__analysis_847, std_req__iso26262__analysis_848, std_req__iso26262__analysis_849, std_req__iso26262__analysis_8410, std_req__isopas8926__44431

   | .. comp_saf_fmea:: <Element descriptor>
   |    :verifies: <Component architecture>
   |    :id: comp_saf_FMEA__<Component>__<Element descriptor>
   |    :failure_mode: <ID from fault model :need:`gd_guidl__fault_models`>
   |    :failure_effect: "description of failure effect of the failure initiator on the element"
   |    :mitigation: < NONE|ID from Component Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

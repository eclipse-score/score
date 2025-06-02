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

.. _dfa_templates:

DFA Templates
=============

.. gd_temp:: Platform DFA Templates
   :id: gd_temp__plat_saf_dfa
   :status: valid
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__software_753, std_wp__isopas8926__4524, std_req__iso26262__software_7411, std_req__iso26262__analysis_741, std_req__iso26262__analysis_742, std_req__iso26262__analysis_743, std_req__iso26262__analysis_745, std_req__iso26262__analysis_746, std_req__iso26262__analysis_747, std_req__iso26262__analysis_748, std_req__iso26262__analysis_749, std_req__isopas8926__44432

   | .. plat_saf_dfa:: <Element descriptor>
   |    :verifies: <Platform architecture>
   |    :id: plat_saf_DFA__<Platform>__<Element descriptor>
   |    :violation_id: <ID from DFA failure initiators :need:`gd_guidl__dfa_failure_initiators`>
   |    :violation_cause: "description of failure effect of the failure initiator on the element"
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

.. gd_temp:: Feature DFA Templates
   :id: gd_temp__feat_saf_dfa
   :status: valid
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__software_753, std_wp__isopas8926__4524, std_req__iso26262__software_7411, std_req__iso26262__analysis_741, std_req__iso26262__analysis_742, std_req__iso26262__analysis_743, std_req__iso26262__analysis_745, std_req__iso26262__analysis_746, std_req__iso26262__analysis_747, std_req__iso26262__analysis_748, std_req__iso26262__analysis_749, std_req__isopas8926__44432

   | .. feat_saf_dfa:: <Element descriptor>
   |    :verifies: <Feature architecture>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: <ID from DFA failure initiators :need:`gd_guidl__dfa_failure_initiators`>
   |    :violation_cause: "description of failure effect of the failure initiator on the element"
   |    :mitigation: < NONE|ID from Feature Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>


.. gd_temp:: Component DFA Templates
   :id: gd_temp__comp_saf_dfa
   :status: valid
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__software_753, std_wp__isopas8926__4524, std_req__iso26262__software_7411, std_req__iso26262__analysis_741, std_req__iso26262__analysis_742, std_req__iso26262__analysis_743, std_req__iso26262__analysis_745, std_req__iso26262__analysis_746, std_req__iso26262__analysis_747, std_req__iso26262__analysis_748, std_req__iso26262__analysis_749, std_req__isopas8926__44432

   | .. comp_saf_dfa:: <Element descriptor>
   |    :verifies: <Component architecture>
   |    :id: comp_saf_DFA__<Component>__<Element descriptor>
   |    :violation_id: <ID from DFA failure initiators :need:`gd_guidl__dfa_failure_initiators`>
   |    :violation_cause: "description of failure effect of the failure initiator on the element"
   |    :mitigation: < NONE|ID from Component Requirement>
   |    :mitigation_issue: <ID from Issue Tracker| None if no issue needed>
   |    :mitigation_coverage: <0..100%>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why mitigation is sufficient>
   |    :status: <valid|invalid>

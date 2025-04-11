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


Safety Analysis Template
========================

.. gd_temp:: Safety Analysis Templates
   :id: gd_temp__safety_analysis
   :status: valid
   :complies: std_wp__iso26262__analysis_851, std_wp__iso26262__software_752, std_req__iso26262__software_7410, std_req__iso26262__software_7412, std_req__iso26262__analysis_841, std_req__iso26262__analysis_842, std_req__iso26262__analysis_843, std_req__iso26262__analysis_844, std_req__iso26262__analysis_845, std_req__iso26262__analysis_846, std_req__iso26262__analysis_847, std_req__iso26262__analysis_848, std_req__iso26262__analysis_849, std_req__iso26262__analysis_8410

   | .. feat_saf_fmea:: <Element descriptor>
   |    :id: feat_saf_FMEA__<Feature>__<Element descriptor>
   |    :failure_mode: <ID from fault model :need:`gd_guidl__fault_models`>
   |    :failure_effect: "Failure mode similar to :need:`gd_guidl__fault_models`"
   |    :violates: <ID from Feature Requirement>
   |    :measure: < NONE|ID from Feature Requirement>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why measure is sufficient>
   |    :status: <valid|invalid>

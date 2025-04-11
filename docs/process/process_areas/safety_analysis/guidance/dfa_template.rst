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


DFA Template
============

.. gd_temp:: DFA Templates
   :id: gd_temp__dfa
   :status: valid
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__software_753, std_req__iso26262__software_7411, std_req__iso26262__analysis_741, std_req__iso26262__analysis_742, std_req__iso26262__analysis_743, std_req__iso26262__analysis_745, std_req__iso26262__analysis_746, std_req__iso26262__analysis_747, std_req__iso26262__analysis_748, std_req__iso26262__analysis_749

   | .. feat_saf_dfa:: <Element descriptor>
   |    :id: feat_saf_DFA__<Feature>__<Element descriptor>
   |    :violation_id: <ID from dfa checklist :need:`gd_chklst__dfa`>
   |    :violation_cause: "Failure mode similar to :need:`gd_chklst__dfa`"
   |    :violates: <ID from Feature Requirement>
   |    :measure: < NONE|ID from Feature Requirement>
   |    :sufficient: <yes|no>
   |    :argument: <text to argument why measure is sufficient>
   |    :status: <valid|invalid>

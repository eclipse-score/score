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


DFA (Dependent Failure Analysis)
================================

.. document:: Orchestration DFA
   :id: doc__orchestration_dfa
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feature_dfa
   :tags: orchestration


Dependent Failure Initiators
----------------------------

.. code-block:: rst

    .. feat_saf_dfa:: <Title>
       :violates: <Feature architecture>
       :id: feat_saf_dfa__<Feature>__<Element descriptor>
       :failure_id: <ID from DFA failure initiators :need:`gd_guidl__dfa_failure_initiators`>
       :failure_effect: "description of failure effect of the failure initiator on the element"
       :mitigated_by: <ID from Feature Requirement | ID from AoU Feature Requirement>
       :mitigation_issue: <ID from Issue Tracker>
       :sufficient: <yes|no>
       :status: <valid|invalid>

 .. note::   argument is inside the 'content'. Therefore content is mandatory

.. attention::
    The above directive must be updated according to your feature DFA.

    - The above "code-block" directive must be updated
    - Fill in all the needed information in the <brackets>

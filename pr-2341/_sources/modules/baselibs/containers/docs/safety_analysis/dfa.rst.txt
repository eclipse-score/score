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

.. document:: containers DFA
   :id: doc__containers_dfa
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__sw_component_dfa

.. note:: Use the content of the document to describe e.g. why a fault model is not applicable for the diagram.


Dependent Failure Initiators
----------------------------

.. code-block:: rst

    .. comp_saf_dfa:: <Title>
       :violates: <Component architecture>
       :id: comp_saf_dfa__<Component>__<Element descriptor>
       :failure_id: <ID from DFA failure initiators :need:`gd_guidl__dfa_failure_initiators`>
       :failure_effect: "description of failure effect of the failure initiator on the element"
       :mitigated_by: <ID from Component Requirement | ID from AoU Component Requirement>
       :mitigation_issue: <ID from Issue Tracker>
       :sufficient: <yes|no>
       :status: <valid|invalid>

.. note::   argument is inside the 'content'. Therefore content is mandatory

.. attention::
    The above directive must be updated according to your component DFA.

    - The above "code-block" directive must be updated
    - Fill in all the needed information in the <brackets>

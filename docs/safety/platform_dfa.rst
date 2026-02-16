..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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


Platform DFA (Dependent Failure Analysis)
=========================================

.. document:: Platform DFA
   :id: doc__score_platform_dfa
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__platform_dfa
   :tags:

.. note:: The platform DFA is only performed once at platform level to analyse the dependencies between the features of the platform.
          The results shall be used as an input for the safety analysis so that general safety mechanisms are only defined once and not in every single safety analysis.

.. note:: Use the content of the document to describe e.g. why a fault model is not applicable for the diagram.


Dependent Failure Initiators
----------------------------

.. code-block:: rst

    .. plat_saf_dfa:: <Title>
       :violates: <Feature architecture>
       :id: plat_saf_DFA__<Feature>__<Element descriptor>
       :failure_id: <ID from DFA failure initiators :need:`gd_guidl__dfa_failure_initiators`>
       :failure_effect: "description of failure effect of the failure initiator on the element"
       :mitigated_by: <ID from Feature Requirement | ID from AoU Feature Requirement>
       :mitigation_issue: <ID from Issue Tracker>
       :sufficient: <yes|no>
       :status: <valid|invalid>
.. note::   Argument is inside the 'content'. Therefore content is mandatory.

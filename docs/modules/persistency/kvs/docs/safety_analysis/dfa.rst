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


Dependent Failure Analysis
==========================

.. document:: [Your Component Name] DFA
   :id: doc__component_name_dfa
   :status: draft
   :safety: ASIL_D
   :realizes: wp__sw_component_dfa
   :tags: template

.. attention::
    The above directive must be updated according to your Component.

    - Modify ``Your Component Name`` to be your Component Name
    - Modify ``id`` to be your Component Name in upper snake case preceded by ``doc__`` and succeeded by ``_dfa``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

Dependent Failure Intitiators
-----------------------------

.. code-block:: rst

   .. comp_saf_dfa:: <Element descriptor>
      :id: comp_saf_DFA__<Component>__<Element descriptor>
      :violation_id: <ID from Dependent Failure Initiators list :need:`gd_guidl__dfi`>
      :violation_effect: <Effect caused by the initiator (leading to a violation of a safety goal)>
      :verifies: <ID from Component Architecture>
      :mitigated_by: < NONE|ID from Component Requirement>
      :sufficient: <yes|no>
      :argument: <text to argument why measure is sufficient>
      :status: <valid|invalid>

.. attention::
    The above directive must be updated according to your component DFA.

    - Remove the ``code-block``
    - Fill in all the needed information in the <brackets>

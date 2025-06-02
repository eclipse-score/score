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

Requirements
############

.. document:: [Your Component Name] Requirements
   :id: doc__component_name_requirements
   :status: draft
   :safety: ASIL_D
   :realizes: wp__requirements__comp
   :tags: template

.. attention::
    The above directive must be updated according to your Component.

    - Modify ``Your Component Name`` to be your Component Name
    - Modify ``id`` to be your Component Name in upper snake case preceded by ``doc__`` and followed by ``_requirements``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

<Headlines (for the list of requirements if structuring is needed)>
===================================================================

.. comp_req:: Some Title
   :id: comp_req__component_name__some_title
   :reqtype: Process
   :security: YES
   :safety: ASIL_D
   :satisfies: feat_req__feature_name__some_title
   :status: invalid

   The Component shall do xyz to another component to bring it to this condition at this time

   Note: (optional, not to be verified)

.. attention::
    The above directive must be updated according to your component requirements.

    - Replace the example content by the real content for your first requirement
    - Set the status to valid and start the review/merge process
    - Add other needed requirements for your component

.. aou_req:: Next Title
   :id: aou_req__component_name__next_title
   :reqtype: Process
   :security: YES
   :safety: ASIL_D
   :status: invalid

   The Component User shall do xyz to use the component safely

.. attention::
    The above directives must be updated according to your feature requirements.

    - Replace the example content by the real content for your first requirement (according to :need:`gd_guidl__req__engineering`)
    - Set the status to valid and start the review/merge process
    - Add other needed requirements for your feature

.. needextend:: "component_name" in id
   :+tags: component_name

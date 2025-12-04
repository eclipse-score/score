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

.. document:: [Your Feature Name] Requirements
   :id: doc__feature_name_requirements
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__requirements_feat
   :tags: template

.. attention::
    The above directive must be updated according to your Feature.

    - Modify ``Your Feature Name`` to be your Feature Name
    - Modify ``id`` to be your Feature Name in upper snake case preceded by ``doc__`` and followed by ``_requirements``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

<Headlines (for the list of requirements if structuring is needed)>
===================================================================

.. stkh_req:: Template
   :id: stkh_req__requirements__template
   :reqtype: Non-Functional
   :safety: ASIL_B
   :security: YES
   :rationale: Exists just for the template example
   :status: invalid

   The platform shall ...

.. attention::
    The above stakeholder requirement must be removed, it just serves as a link target for this template.

.. feat_req:: Some Title
   :id: feat_req__feature_name__some_title
   :reqtype: Process
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__requirements__template
   :status: invalid

   The Feature shall do xyz to the user to bring him to this condition at this time

   Note: (optional, not to be verified)

.. aou_req:: Some Other Title
   :id: aou_req__feature_name__some_other_title
   :reqtype: Process
   :security: YES
   :safety: ASIL_B
   :status: invalid

   The Feature User shall do xyz to use the feature safely

.. attention::
    The above directives must be updated according to your feature requirements.

    - Replace the example content by the real content for your first requirement (according to :need:`gd_guidl__req_engineering`)
    - Set the status to valid and start the review/merge process
    - Add other needed requirements for your feature

.. needextend:: docname is not None and "feature_name" in id
   :+tags: feature_name

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

<Headlines (for the list of requirements if structuring is needed)>
===================================================================

.. feat_req:: Some Title
   :id: feat_req__feature_name__some_title
   :reqtype: Process
   :security: YES
   :safety: ASIL_D
   :satisfies: stkh_req__requirements__as_code
   :status: invalid

   The Feature shall do xyz to the user to bring him to this condition at this time

   Note: (optional, not to be verified)

.. aou_req:: Some Other Title
   :id: aou_req__feature_name__some_other_title
   :reqtype: Process
   :security: YES
   :safety: ASIL_D
   :status: invalid

   The Feature User shall do xyz to use the feature safely

.. attention::
    The above directives must be updated according to your feature requirements.

    - Replace the example content by the real content for your first requirement
    - Set the status to valid and start the review/merge process
    - Add other needed requirements for your feature

.. needextend:: "feature_name/requirements" in docname
   :+tags: feature_name

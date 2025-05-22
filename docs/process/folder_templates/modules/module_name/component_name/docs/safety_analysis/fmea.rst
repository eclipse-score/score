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


Safety Analysis : FMEA
======================

.. code-block:: rst

   .. comp_saf_fmea:: <Element descriptor>
      :id: comp_saf_FMEA__<Component>__<Element descriptor>
      :failure_mode: <ID from fault model :need:`gd_guidl__fault_models`>
      :failure_effect: <Effect caused by the failure (leading to a violation of a safety goal)>
      :verifies: <ID from Component Architecture>
      :mitigated_by: < NONE|ID from Component Requirement>
      :sufficient: <yes|no>
      :argument: <text to argument why measure is sufficient>
      :status: <valid|invalid>

.. attention::
    The above directive must be updated according to your component FMEA.

    - Remove the ``code-block``
    - Fill in all the needed information in the <brackets>

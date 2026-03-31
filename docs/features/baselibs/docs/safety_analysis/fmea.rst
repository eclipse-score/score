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


FMEA (Failure Modes and Effects Analysis)
=========================================

.. document:: Baselibs FMEA
   :id: doc__baselibs_fmea
   :status: valid
   :safety: ASIL_B
   :security: NO
   :realizes: wp__feature_fmea

The feature baselibs consists of multiple components which provide very different functionality.
They are also low-complex (i.e. no component architecture is documented). In consequence the function's
failure modes are discussed and documented in the components FMEA's for better readability.

Below failure mode is just one example which is present in every baselibs components FMEA.

Failure Mode List
-----------------

.. feat_saf_fmea:: Baselibs Feature
   :violates: feat_arc_dyn__baselibs__dynamic_view_arch
   :id: feat_saf_fmea__baselibs__components
   :fault_id: EX_01_04
   :failure_effect: any of the baselibs components execution is lost due to systematic SW error
   :mitigated_by: feat_req__baselibs__safety
   :sufficient: yes
   :status: valid

   SW development is required in ASIL_B quality and each individual baselibs component has low complexity.

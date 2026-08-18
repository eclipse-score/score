
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

.. document:: Time Assumption of Use Requirements
   :id: doc__feature_time_aou_reqs
   :status: draft
   :version: 1
   :security: NO
   :safety: ASIL_B
   :realizes: wp__requirements_feat_aou[version==1]

Time Feature Assumption of Use Requirements
===========================================

.. aou_req:: Vehicle time end-to-end integrity
   :id: aou_req__feature__veh_time_e2e_integrity
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   If the system using the S-CORE Time feature has the safety goal to achive end-to-end integrity of
   the vehicle time information, the involved external components (like grand master clock, any
   intermediate master clock, and time-aware bridges/switches) must support respective measures for
   the integrity protection.

   Note: If this assumption is violated, the data integrity level of the vehicle time information will fall
         back to QM and must be marked accordingly in the respective project documentation.

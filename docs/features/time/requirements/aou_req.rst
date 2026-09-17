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

.. document:: Time Assumption of Use Requirements
   :id: doc__feature_time_aou_reqs
   :status: draft
   :version: 1
   :security: NO
   :safety: ASIL_B
   :realizes: wp__requirements_feat_aou[version==1]

Time Feature Assumption of Use Requirements
===========================================

.. aou_req:: Vehicle time value integrity
   :id: aou_req__feature_time__veh_time_integrity
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   The integrity of the vehicle time *value* is not guaranteed by :term:`score::time` alone. If the
   system using :term:`score::time` has the safety goal to treat the vehicle time as ASIL-B data, the
   system integrator shall establish end-to-end integrity by suitable measures, e.g.:

   * integrity protection along the time-distribution chain (grand master, intermediate masters,
     time-aware bridges/switches), and/or
   * a receiver-side qualification/monitoring mechanism that evaluates the qualifiers provided by
     :term:`score::time` (see :need:`feat_req__time__vehicle_time_time_pt_qual`,
     :need:`feat_req__time__vehicle_time_acc_qual_api`) and reacts per the project safety concept.

   Note 1: :term:`score::time` provides the qualifier/detection hooks; the concrete integrity
   mechanism, its redundancy, the safety reaction and the end-to-end safety argument are
   project-specific and outside the scope of the :term:`score::time` SEooC.

   Note 2: If this assumption is not fulfilled, the vehicle time value integrity falls back to QM
   and must be marked accordingly in the project documentation.

.. aou_req:: Vehicle time integrity result reflected in qualifier
   :id: aou_req__feature_time__veh_time_qual_reflect
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   Where the integrity check for the vehicle time is realized as a :term:`score::time` extension, the
   system integrator shall ensure its result is reflected in the :term:`time point qualifier`
   (see :need:`feat_req__time__vehicle_time_time_pt_qual`).

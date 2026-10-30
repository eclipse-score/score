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

Time Feature Assumption of Use Requirements
###########################################

.. document:: Time Assumption of Use Requirements
   :id: doc__feature_time_aou_reqs
   :status: draft
   :version: 1
   :security: NO
   :safety: ASIL_B
   :realizes: wp__requirements_feat_aou[version==1]

Assumptions of Use
==================

Vehicle Time Integration
------------------------

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
     :term:`score::time` (see :need:`feat_req__time__vehicle_time_time_pt_qual`) and reacts per the project safety concept.

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
   :version: 3

   Where the integrity check for the vehicle time is realized as a :term:`score::time` extension, the
   system integrator shall ensure its result is reflected in the :term:`time point qualifier`
   (see :need:`feat_req__time__vehicle_time_time_pt_qual`).

.. aou_req:: Scheduling configuration of score::time
   :id: aou_req__feature_time__veh_sched_config
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   The system integrator shall configure the scheduling of :term:`score::time` and provide CPU time so that the
   time synchronization data and the :term:`Vehicle Time status` reach their consumers within the time budget
   derived from the fault tolerant time interval of the consuming functions.

   Note: the scheduling configuration covers e.g. the priorities, the core assignment and the CPU time budget of the
   processes of score::time.

.. aou_req:: Vehicle Time gPTP domain configuration
   :id: aou_req__feature_time__veh_domain_config
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :status: valid
   :version: 1

   The system integrator shall configure the gPTP domain of the :term:`Vehicle Time` according to the
   project-specific requirements (see :need:`feat_req__time__veh_gptp_slave`).

   Note: the domain selects the gPTP synchronization domain used for the :term:`Vehicle Time`.

.. aou_req:: Vehicle Time slave port configuration
   :id: aou_req__feature_time__veh_port_config
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :status: valid
   :version: 1

   The system integrator shall configure the network interface of the gPTP slave port according to the
   project-specific requirements (see :need:`feat_req__time__veh_gptp_slave`).

   Note: the network interface selects the slave port used to exchange gPTP messages.

.. aou_req:: Local hardware clock configuration
   :id: aou_req__feature_time__veh_hw_clock_config
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :status: valid
   :version: 1

   The system integrator shall configure the local hardware clocks that are synchronized to the
   :term:`Vehicle Time` according to the project-specific requirements
   (see :need:`feat_req__time__hw_clock_sync`).

   Note: this selection identifies the local hardware clocks that are synchronized to the :term:`Vehicle Time`.

.. aou_req:: Follow_Up receipt timeout configuration
   :id: aou_req__feature_time__veh_fup_tmo_config
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :status: valid
   :version: 1

   The system integrator shall configure the Follow_Up receipt timeout according to the project-specific
   requirements (see :need:`feat_req__time__veh_fup_timeout`).

   Note: the timeout controls how long after the reception of a Sync message its Follow_Up message is awaited.

.. aou_req:: Peer delay request interval configuration
   :id: aou_req__feature_time__veh_pdelay_int_config
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :status: valid
   :version: 1

   The system integrator shall configure the Pdelay_Req interval according to the project-specific requirements
   (see :need:`feat_req__time__veh_pdelay_interval`).

   Note: the interval controls the time between consecutive Pdelay_Req messages.

.. aou_req:: Peer delay discard threshold configuration
   :id: aou_req__feature_time__veh_pdelay_disc_config
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :status: valid
   :version: 1

   The system integrator shall configure the peer delay discard threshold according to the project-specific
   requirements (see :need:`feat_req__time__veh_pdelay_discard`).

   Note: the threshold controls the calculated peer delay above which a peer delay measurement is discarded.

.. aou_req:: Vehicle Time synchronization timeout configuration
   :id: aou_req__feature_time__veh_timeout_config
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 2

   The system integrator shall configure the synchronization timeout period according to the project-specific
   requirements (see :need:`feat_req__time__veh_status_timeout`).

   Note: the period controls how long after the last reception of time synchronization information a timeout is
   indicated if no further information is received.

.. aou_req:: Vehicle Time startup timeout configuration
   :id: aou_req__feature_time__veh_start_tmo_config
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   The system integrator shall configure the startup timeout period according to the project-specific
   requirements (see :need:`feat_req__time__veh_startup_timeout`).

   Note: the period controls how long after the feature starts a timeout is indicated if no time synchronization
   information has been received.

.. aou_req:: Vehicle Time leap to the future threshold configuration
   :id: aou_req__feature_time__veh_leap_fut_config
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 2

   The system integrator shall configure the time leap to the future threshold according to the project-specific
   requirements (see :need:`feat_req__time__veh_status_leap_fut`).

   Note: the threshold controls how far the updated Vehicle Time may be ahead of the time predicted for the Sync
   ingress instant before a time leap to the future is indicated, when leap evaluation is enabled.

.. aou_req:: Vehicle Time leap to the past threshold configuration
   :id: aou_req__feature_time__veh_leap_past_config
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 2

   The system integrator shall configure the time leap to the past threshold according to the project-specific
   requirements (see :need:`feat_req__time__veh_status_leap_past`).

   Note: the threshold controls how far the updated Vehicle Time may be behind the time predicted for the Sync
   ingress instant before a time leap to the past is indicated, when leap evaluation is enabled.

.. aou_req:: Time leap debounce period configuration
   :id: aou_req__feature_time__veh_debounce_config
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   The system integrator shall configure the time leap debounce period after the first synchronization according to
   the project-specific requirements (see :need:`feat_req__time__veh_leap_debounce`).

   Note: the period controls how long leap evaluation is skipped after the first synchronization. With a period
   of zero, only the first synchronization is excluded.

.. aou_req:: Time leap indication healing count configuration
   :id: aou_req__feature_time__veh_heal_count_config
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   The system integrator shall configure the common number of consecutive time synchronization updates required
   to clear each time leap indication according to the project-specific requirements
   (see :need:`feat_req__time__veh_leap_heal` and :need:`feat_req__time__veh_leap_past_heal`).

   Note: the count controls how many consecutive updates without a leap in a given direction clear that direction's
   indication. Both directions use the same configured count, but their progress is counted independently.

.. aou_req:: Time leap evaluation after timeout configuration
   :id: aou_req__feature_time__veh_leap_tmo_config
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   The system integrator shall configure whether the first time synchronization update received after a timeout
   is evaluated for a time leap according to the project-specific requirements
   (see :need:`feat_req__time__veh_leap_after_timeout`).

   Note: this choice controls whether leap evaluation is skipped or performed for the first synchronization update
   received after a timeout.

Vehicle Time Usage
------------------

A Vehicle Time :term:`Snapshot` carries two independent pieces of information about its :term:`TimePoint`:
the :term:`Vehicle Time status` tells whether the TimePoint is meaningful, and the :term:`time point qualifier`
tells whether the TimePoint may be treated as ASIL-B data. The following assumptions describe how the user
combines both.

.. aou_req:: Elapsed time measurement
   :id: aou_req__feature_time__elapsed_time_clock
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   The user shall measure elapsed time within one ECU with the :term:`Steady Clock`.

   Note: the :term:`Vehicle Time` is not :term:`monotonic`; a time synchronization update may decrease it.

.. aou_req:: Vehicle Time status evaluation
   :id: aou_req__feature_time__veh_status_eval
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   The user shall use a :term:`TimePoint` only if the :term:`Vehicle Time status` of the same :term:`Snapshot`
   fulfils the requirements of the user's use case.

.. aou_req:: Vehicle Time time point qualifier evaluation
   :id: aou_req__feature_time__veh_tpq_eval
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   The user shall treat a :term:`TimePoint` as ASIL-B data only if the :term:`time point qualifier` of the same
   :term:`Snapshot` indicates ASIL-B data.

Absolute Time Integration
-------------------------

.. aou_req:: Absolute Time qualifier evaluation
   :id: aou_req__feature_time__abs_qual_eval
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid
   :version: 1

   The user shall use an :term:`Absolute Time` :term:`TimePoint` only if the :term:`accuracy qualifier` and the
   :term:`security qualifier` of the same :term:`Snapshot` fulfil the requirements of the user's use case.

   Note: the security qualifier depends on external conditions, e.g. the connectivity to a secure time source.

.. aou_req:: Absolute Time accuracy validity period configuration
   :id: aou_req__feature_time__abs_acc_period_config
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid
   :version: 1

   The system integrator shall configure the period after which the accuracy qualifier of the Absolute Time
   indicates "Inaccuracy not available" according to the project-specific requirements
   (see :need:`feat_req__time__abs_acc_degrade`).

   Note: the period controls how long after the last Absolute Time sample was processed the accuracy qualifier
   changes to "Inaccuracy not available".

.. aou_req:: Absolute Time security degradation period configuration
   :id: aou_req__feature_time__abs_sec_period_config
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid
   :version: 1

   The system integrator shall configure the period after which the security qualifier "Time very trustworthy"
   degrades to "Time trustworthy" according to the project-specific requirements
   (see :need:`feat_req__time__abs_sec_degrade`).

   Note: the period controls how long after the last sample with "Time very trustworthy" was processed the security
   qualifier degrades to "Time trustworthy".

.. aou_req:: System Clock setting threshold configuration
   :id: aou_req__feature_time__sys_threshold_config
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid
   :version: 1

   The system integrator shall configure the difference between the System Clock and the Absolute Time above which
   the System Clock is set according to the project-specific requirements
   (see :need:`feat_req__time__sys_clock_step`).

   Note: the threshold controls the difference between the System Clock and the Absolute Time above which the
   System Clock is set, subject to the minimum accuracy and security level.

.. aou_req:: System Clock minimum accuracy configuration
   :id: aou_req__feature_time__sys_min_acc_config
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid
   :version: 1

   The system integrator shall configure the minimum accuracy of the Absolute Time for setting the System Clock
   according to the project-specific requirements (see :need:`feat_req__time__sys_clock_min_acc`).

   Note: the limit controls which accuracy qualifiers permit setting the System Clock: the indicated inaccuracy
   must be less than the limit.

.. aou_req:: System Clock minimum security level configuration
   :id: aou_req__feature_time__sys_min_sec_config
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid
   :version: 1

   The system integrator shall configure the minimum security level of the Absolute Time for setting the System
   Clock according to the project-specific requirements (see :need:`feat_req__time__sys_clock_min_sec`).

   Note: the minimum level controls which security qualifiers permit setting the System Clock; a lower level
   prevents setting it.

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

.. document:: Time Requirements
   :id: doc__time_requirements
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: NO
   :realizes: wp__requirements_feat[version==1]

Vehicle Time
============

Synchronization
---------------

.. feat_req:: Vehicle Time synchronization
   :id: feat_req__time__vehicle_time_sync
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall synchronize the :term:`Vehicle Time` to the :term:`Grand Master` using :term:`gPTP` (IEEE 802.1AS).

.. feat_req:: gPTP slave operation
   :id: feat_req__time__veh_gptp_slave
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall synchronize the :term:`Vehicle Time` as a :term:`gPTP` time-aware end
   station according to IEEE 802.1AS and the Avnu automotive profile, unless specified otherwise by the requirements
   of this feature, with a statically configured slave port on the configured gPTP domain and without executing the
   best master clock algorithm.

   Note: static port roles and no passive ports follow from the automotive profile. The gPTP domain of the
   :term:`Vehicle Time` is typically domain 0.

.. feat_req:: gPTP message addressing
   :id: feat_req__time__veh_gptp_frame_addr
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall send its :term:`gPTP` messages untagged to the MAC group address
   01:80:C2:00:00:0E with the Ethertype 0x88F7.

.. feat_req:: Follow_Up receipt timeout
   :id: feat_req__time__veh_fup_timeout
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall discard a received Sync message when its Follow_Up message is not received
   within a configured Follow_Up receipt timeout after the reception of the Sync message.

.. feat_req:: Time synchronization information out of range
   :id: feat_req__time__veh_drop_out_of_range
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall discard received time synchronization information whose
   ``preciseOriginTimestamp`` has a seconds field greater than 2^32 - 1 or a nanoseconds field greater than
   999 999 999.

.. feat_req:: Sequence identifier jumps
   :id: feat_req__time__veh_no_seq_jump_check
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall process received time synchronization messages independent of the
   difference between their ``sequenceId`` and the ``sequenceId`` of the previously received message.

.. feat_req:: Signaling messages
   :id: feat_req__time__veh_signaling_ignore
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall ignore :term:`gPTP` Signaling messages received on its slave port.

.. feat_req:: Rate deviation compensation
   :id: feat_req__time__veh_rate_comp
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall compensate the measured rate deviation between the
   :term:`Local Reference Time` and the :term:`Grand Master` when deriving the :term:`Vehicle Time` between two time
   synchronization updates.

.. feat_req:: Application of synchronization updates
   :id: feat_req__time__veh_apply_update
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall apply every valid time synchronization update to the :term:`Vehicle Time`,
   independent of the time leap thresholds.

   Note: a correction can decrease the Vehicle Time; the Vehicle Time is not :term:`monotonic`.
   Measure elapsed time within one ECU with the :term:`Steady Clock`
   (see :need:`aou_req__feature_time__elapsed_time_clock`).

.. feat_req:: HW clock synchronization to Vehicle Time
   :id: feat_req__time__hw_clock_sync
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 3
   :valid_from: v1.0.0

   The :term:`score::time` feature shall synchronize each configured local hardware clock to the
   :term:`Vehicle Time`.

   Note: a local hardware clock is e.g. the PTP hardware clock (PHC) of a network interface. The synchronized clock
   may also supply the timestamps of time synchronization and peer delay messages.
   The ownership of the HW clock discipline (score::time vs. the network/gPTP stack) is a system design choice.

Peer Delay Measurement
----------------------

.. feat_req:: Peer delay requester
   :id: feat_req__time__veh_pdelay_requester
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall act as peer delay requester on its :term:`gPTP` slave port.

.. feat_req:: Peer delay request interval
   :id: feat_req__time__veh_pdelay_interval
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall transmit Pdelay_Req messages with a configured interval, with each time
   between two consecutive Pdelay_Req messages within ±25 % of the configured interval, measured with its local clock.

.. feat_req:: Link delay compensation
   :id: feat_req__time__veh_pdelay_comp
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall compensate the link propagation delay measured with the :term:`gPTP` peer
   delay mechanism when synchronizing the :term:`Vehicle Time`.

.. feat_req:: Peer delay discard threshold
   :id: feat_req__time__veh_pdelay_discard
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall discard a peer delay measurement whose calculated peer delay exceeds a
   configured discard threshold.

.. feat_req:: Peer delay after restart
   :id: feat_req__time__veh_pdelay_persist
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall store the last calculated peer delay persistently and use it after a
   restart until a new peer delay measurement is available.

.. feat_req:: Peer delay responder
   :id: feat_req__time__veh_pdelay_responder
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall answer Pdelay_Req messages received on its :term:`gPTP` slave port with
   Pdelay_Resp and Pdelay_Resp_Follow_Up messages.

.. feat_req:: Synchronization without peer delay response
   :id: feat_req__time__veh_sync_no_pdelay
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall keep ``asCapable`` (IEEE 802.1AS) of its :term:`gPTP` slave port ``TRUE``
   and synchronize the :term:`Vehicle Time` when no Pdelay_Resp message is received for its Pdelay_Req messages or
   no valid peer delay measurement is available.

.. feat_req:: Synchronization independent of peer delay thresholds
   :id: feat_req__time__veh_ascapable_thresh
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall keep ``asCapable`` (IEEE 802.1AS) of its :term:`gPTP` slave port ``TRUE``
   and synchronize the :term:`Vehicle Time` when the measured ``neighborPropDelay`` exceeds
   ``neighborPropDelayThresh`` (Avnu) or the peer delay limit of a :term:`Vehicle Time` integrity check.

Synchronization Performance
---------------------------

.. feat_req:: Vehicle Time synchronization precision
   :id: feat_req__time__vehicle_time_sync_prec
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall keep the deviation of the :term:`Vehicle Time` from the :term:`Grand Master`
   time within a project-specific precision bound while the :term:`Vehicle Time status` indicates neither a timeout
   nor a time leap.

   Note: informative reference values for the deviation from the :term:`Grand Master`:

   * AVB nodes (hardware timestamping, time-aware bridges): around 1 µs.
   * non-AVB nodes: around 200-500 µs.

.. feat_req:: Readiness for time synchronization
   :id: feat_req__time__veh_startup_ready
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__execution_model__startup_perf[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall be ready to process received Sync and Follow_Up messages within one
   synchronization interval specified for the network after the network interface used for the time synchronization
   has started communication, provided that the feature has been started before.

.. feat_req:: First peer delay request after start
   :id: feat_req__time__veh_startup_pdelay
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__execution_model__startup_perf[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall transmit its first Pdelay_Req message within one synchronization interval
   specified for the network after the network interface used for the time synchronization has started
   communication, provided that the feature has been started before.

.. feat_req:: Synchronization latency
   :id: feat_req__time__veh_sync_latency
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__execution_model__startup_perf[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v2.0.0

   The :term:`score::time` feature shall provide the :term:`Vehicle Time` synchronized to the :term:`Grand Master`,
   with the :term:`synchronized` indication in the :term:`Vehicle Time status`, to its users less than one
   synchronization interval specified for the network after the reception of the first valid time synchronization
   information.

Vehicle Time Status
-------------------

.. feat_req:: Initial Vehicle Time status
   :id: feat_req__time__veh_status_init
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall start with a :term:`Vehicle Time status` that indicates neither
   :term:`synchronized`, nor a timeout, nor a time leap to the future, nor a time leap to the past.

.. feat_req:: Vehicle Time synchronized indication
   :id: feat_req__time__veh_status_sync
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall indicate in the :term:`Vehicle Time status` that the :term:`Vehicle Time`
   has been synchronized to the :term:`Grand Master`, from the first synchronization until the end of the
   feature lifecycle.

   Note: a later loss of synchronization does not reset this indication; it is indicated by the timeout
   (see :need:`feat_req__time__veh_status_timeout`). The synchronization state is reported by the :term:`gPTP` stack.

.. feat_req:: Vehicle Time timeout indication
   :id: feat_req__time__veh_status_timeout
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall indicate a timeout in the :term:`Vehicle Time status` when no time
   synchronization information from the :term:`Grand Master` has been received for longer than a configured timeout
   period since the last reception, measured by the :term:`Local Reference Time`.

.. feat_req:: Vehicle Time startup timeout indication
   :id: feat_req__time__veh_startup_timeout
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall indicate a timeout in the :term:`Vehicle Time status` when no time
   synchronization information from the :term:`Grand Master` has been received within a configured startup timeout
   period after the start of the feature.

   Note: as the :term:`synchronized` indication is not set yet, users can distinguish this timeout from a timeout
   after a synchronization.

.. feat_req:: Timeout indication healing
   :id: feat_req__time__veh_timeout_heal
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall clear the timeout indication in the :term:`Vehicle Time status` with the
   first valid time synchronization update received after the timeout.

.. feat_req:: Vehicle Time leap to the future indication
   :id: feat_req__time__veh_status_leap_fut
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 3
   :valid_from: v1.0.0

   The :term:`score::time` feature shall indicate a time leap to the future in the :term:`Vehicle Time status` when
   the :term:`Vehicle Time` after a time synchronization update is ahead of the Vehicle Time predicted for the Sync
   ingress instant before the update (see :need:`feat_req__time__veh_sync_data`) by more than a configured
   threshold, unless the time leap evaluation of the update is skipped (see :need:`feat_req__time__veh_leap_debounce`
   and :need:`feat_req__time__veh_leap_after_timeout`).

.. feat_req:: Vehicle Time leap to the past indication
   :id: feat_req__time__veh_status_leap_past
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 3
   :valid_from: v1.0.0

   The :term:`score::time` feature shall indicate a time leap to the past in the :term:`Vehicle Time status` when
   the :term:`Vehicle Time` after a time synchronization update is behind the Vehicle Time predicted for the Sync
   ingress instant before the update (see :need:`feat_req__time__veh_sync_data`) by more than a configured
   threshold, unless the time leap evaluation of the update is skipped (see :need:`feat_req__time__veh_leap_debounce`
   and :need:`feat_req__time__veh_leap_after_timeout`).

.. feat_req:: Time leap debounce after the first synchronization
   :id: feat_req__time__veh_leap_debounce
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall skip the time leap evaluation of the time synchronization updates received
   from the first synchronization until a configured debounce period after it.

   Note: with a debounce period of zero, only the first synchronization is not evaluated.

.. feat_req:: Time leap evaluation after a timeout
   :id: feat_req__time__veh_leap_after_timeout
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall skip the time leap evaluation of the first time synchronization update
   received after a timeout, unless configured otherwise.

   Note: the timeout indication already marks the discontinuity after a timeout.

.. feat_req:: Time leap to the future indication healing
   :id: feat_req__time__veh_leap_heal
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall clear the time leap to the future indication in the
   :term:`Vehicle Time status` after a configured number of consecutive time synchronization updates without a time
   leap to the future.

   Note: the time leap to the past indication is cleared independently
   (see :need:`feat_req__time__veh_leap_past_heal`); both indications can be active at the same time. A repeated
   delivery of the same update does not count.

.. feat_req:: Time leap to the past indication healing
   :id: feat_req__time__veh_leap_past_heal
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall clear the time leap to the past indication in the
   :term:`Vehicle Time status` after the same configured number of consecutive time synchronization updates
   without a time leap to the past as used for healing the time leap to the future indication
   (see :need:`feat_req__time__veh_leap_heal`).

   Note: the time leap to the future indication is cleared independently
   (see :need:`feat_req__time__veh_leap_heal`). A repeated delivery of the same update does not count.

.. feat_req:: Rate deviation indication
   :id: feat_req__time__veh_rate_dev
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall indicate in the :term:`Vehicle Time status` the measured rate deviation
   between the :term:`Local Reference Time` and the :term:`Grand Master`.

.. feat_req:: Rate deviation before the first measurement
   :id: feat_req__time__veh_rate_dev_init
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall indicate in the :term:`Vehicle Time status` that no rate deviation has been
   measured, from its start until it has measured the first rate deviation.

.. feat_req:: Notification of Vehicle Time status changes
   :id: feat_req__time__veh_status_notify
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_status[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall notify subscribed users of every change of the
   :term:`Vehicle Time status`.

   Note: diagnostic trouble codes of a project (e.g. "time base not in sync") can be derived from these
   notifications.

Vehicle Time Access
-------------------

.. feat_req:: Vehicle Time base API
   :id: feat_req__time__vehicle_time_time_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall provide an API to access the :term:`Vehicle Time`.

   Note: ASIL_B applies to the API, so that ASIL-B applications can use it; whether the delivered
   :term:`TimePoint` is ASIL-B or QM data is indicated by the :term:`time point qualifier`
   (see :need:`feat_req__time__vehicle_time_time_pt_qual`).

.. feat_req:: Vehicle Time value range
   :id: feat_req__time__veh_tp_format
   :reqtype: Interface
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall provide the :term:`Vehicle Time` in the time scale of the
   :term:`Grand Master`, in the range from 0 s to less than 2^32 s with a resolution of 1 ns.

   Note: :term:`score::time` does not interpret the epoch of the Grand Master time scale; it can be arbitrary, e.g.
   the start of a free-running counter of the Grand Master. The range of more than 136 years corresponds to the 4
   least significant bytes of the seconds field of the IEEE 802.1AS Timestamp.

.. feat_req:: Vehicle Time Snapshot consistency
   :id: feat_req__time__veh_snapshot_cons
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall deliver each Vehicle Time :term:`Snapshot` with a :term:`TimePoint` and a
   :term:`Vehicle Time status` determined from the same synchronization state.

.. feat_req:: Non-blocking Vehicle Time read
   :id: feat_req__time__vehicle_time_ctrl_flow
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall return a Vehicle Time :term:`Snapshot` to a reading application without
   blocking the application on another process.

   Note: blocking means that the application waits until another process, e.g. the process that synchronizes the
   :term:`Vehicle Time`, releases a lock or replies. A bounded number of read retries does not block
   (API: :need:`feat_req__time__vehicle_time_time_api`).

   *Use case:* frequent access to the current synchronized time and its metadata by multiple clients within one ECU.

Safe Vehicle Time
-----------------

.. feat_req:: Vehicle Time base time point qualifier
   :id: feat_req__time__vehicle_time_time_pt_qual
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__vehicle_time_status[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 3
   :valid_from: v1.0.0

   The :term:`score::time` feature shall indicate in the :term:`Vehicle Time status`, with the :term:`time point qualifier`,
   whether the :term:`TimePoint` of the same :term:`Snapshot` may be treated as ASIL-B data or only as QM data.

   Note: the qualifier indicates QM data unless an integrity check has confirmed the TimePoint
   (see :need:`feat_req__time__veh_tpq_default`).
   This verdict comes from the integrity check established for the vehicle time
   (see :need:`aou_req__feature_time__veh_time_integrity`).
   If that integrity check is integrated into :term:`score::time`, its verdict is delivered through this qualifier
   (see :need:`feat_req__time__veh_integrity_verdict` and :need:`aou_req__feature_time__veh_time_qual_reflect`).

.. feat_req:: Vehicle Time time point qualifier default
   :id: feat_req__time__veh_tpq_default
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall report the :term:`time point qualifier` as QM unless an integrity check has
   confirmed the :term:`TimePoint` as ASIL-B data.

.. feat_req:: Integration of a Vehicle Time integrity check
   :id: feat_req__time__veh_integrity_verdict
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__safe_vehicle_time[version==2]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall reflect the verdict of an integrated :term:`Vehicle Time` integrity check
   in the :term:`time point qualifier` of every :term:`Snapshot` delivered after the verdict.

   Note: the integrity check can be integrated e.g. as an additional validation stage of the feature. If the check
   runs outside :term:`score::time`, the time point qualifier stays QM (see :need:`feat_req__time__veh_tpq_default`)
   and the check informs its users itself.

Time Synchronization Data
-------------------------

The following requirements provide the information that project-specific diagnostics (e.g. diagnostic jobs and
trouble codes) and an independent validation of the :term:`Vehicle Time` (e.g. Safe Car Time, integrated as a
validation stage or running on top of the :term:`score::time` API) need.

.. feat_req:: Time synchronization data
   :id: feat_req__time__veh_sync_data
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__safe_vehicle_time[version==2], stkh_req__time__vehicle_time_sync_data[version==1], stkh_req__time__vehicle_time_status[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v2.0.0

   The :term:`score::time` feature shall provide the following data for each received time synchronization update,
   with all local timestamps in nanoseconds:

   * ``sequenceId``
   * ``sourcePortIdentity``
   * ``preciseOriginTimestamp``
   * ``correctionField``
   * the local Sync ingress timestamp
   * the :term:`Vehicle Time` predicted for the Sync ingress instant before the update
   * the applied peer delay and its validity
   * the :term:`Vehicle Time` after the update
   * the local time after the update
   * the :term:`Vehicle Time status` after the update

   Note: as the local timestamps are provided in nanoseconds, no frequency or scaling factor of the timestamp clock
   is needed to convert them.

.. feat_req:: Peer delay measurement data
   :id: feat_req__time__veh_pdelay_data
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__safe_vehicle_time[version==2], stkh_req__time__vehicle_time_sync_data[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v2.0.0

   The :term:`score::time` feature shall provide the following data for each completed peer delay measurement, with
   all local timestamps in nanoseconds:

   * ``sequenceId``
   * the requester port identity
   * the responder port identity
   * the local Pdelay_Req transmission timestamp
   * ``requestReceiptTimestamp``
   * ``responseOriginTimestamp``
   * the local Pdelay_Resp reception timestamp
   * the resulting peer delay
   * the :term:`Vehicle Time` at the Pdelay_Req transmission
   * the :term:`Vehicle Time` at the Pdelay_Resp reception

.. feat_req:: Notification of time synchronization updates
   :id: feat_req__time__veh_data_notify
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__dependability__automotive_safety[version==1], stkh_req__time__vehicle_time_sync_data[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v2.0.0

   The :term:`score::time` feature shall notify subscribed users of every time synchronization update.

   Note: every update is delivered exactly once, so that users can keep a history of the updates.

.. feat_req:: Notification of peer delay measurements
   :id: feat_req__time__veh_pdelay_notify
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__dependability__automotive_safety[version==1], stkh_req__time__vehicle_time_sync_data[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall notify subscribed users of every completed peer delay measurement.

   Note: every measurement is delivered exactly once.

Absolute Time
=============

Synchronization to External Time Sources
----------------------------------------

.. feat_req:: Absolute Time synchronization
   :id: feat_req__time__abs_sync
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall synchronize the :term:`Absolute Time` to every received
   :term:`Absolute Time sample`.

   Note: the time source follows an external reference, e.g. :term:`UTC` from GNSS. A sample can move the Absolute
   Time forward or backward, e.g. after the time source has resynchronized to its reference.

.. feat_req:: Transmission delay compensation
   :id: feat_req__time__abs_delay_comp
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall provide as :term:`TimePoint` of an Absolute Time :term:`Snapshot` the
   time value of the last processed :term:`Absolute Time sample` plus the :term:`Vehicle Time` elapsed since the
   :term:`Delay Tag` of that sample, when both of the following conditions are met:

   * the Delay Tag of that sample is not marked as invalid, and
   * when the Absolute Time is read, the :term:`Vehicle Time status` indicates :term:`synchronized` and neither a
     timeout nor a time leap.

   Note: the compensation is calculated at each read with the Vehicle Time and its status at that moment.

.. feat_req:: Advancing the Absolute Time without delay compensation
   :id: feat_req__time__abs_advance
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall provide as :term:`TimePoint` of an Absolute Time :term:`Snapshot` the
   time value of the last processed :term:`Absolute Time sample` plus the :term:`Steady Clock` time elapsed since
   the processing of that sample, when at least one of the following conditions is met:

   * the :term:`Delay Tag` of that sample is marked as invalid, or
   * when the Absolute Time is read, the :term:`Vehicle Time status` indicates not :term:`synchronized`, a timeout
     or a time leap.

   Note: this is the complementary case of :need:`feat_req__time__abs_delay_comp`; the transmission delay of the
   sample is not compensated.

.. feat_req:: Accuracy qualifier without delay compensation
   :id: feat_req__time__abs_no_delay_comp
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__time__absolute_time_accuracy[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall indicate the :term:`accuracy qualifier` "Inaccuracy not available" in an
   Absolute Time :term:`Snapshot` whose :term:`TimePoint` it provides without delay compensation
   (see :need:`feat_req__time__abs_advance`).

.. feat_req:: Initial Absolute Time value
   :id: feat_req__time__abs_initial_value
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall provide the :term:`Unix time` 0 as :term:`Absolute Time` from its start
   until it has processed the first :term:`Absolute Time sample`.

Absolute Time Status
--------------------

.. feat_req:: Absolute Time base accuracy qualifier
   :id: feat_req__time__abs_acc_qual
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__time__absolute_time_accuracy[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 3
   :valid_from: v1.0.0

   The :term:`score::time` feature shall indicate the inaccuracy of the :term:`TimePoint` of each
   :term:`Absolute Time` :term:`Snapshot` with one of the following steps of the :term:`accuracy qualifier`:

   * Inaccuracy higher than 24 h
   * Inaccuracy less than 24 h
   * Inaccuracy less than 1 h
   * Inaccuracy less than 15 min
   * Inaccuracy less than 60 s
   * Inaccuracy less than 10 s
   * Inaccuracy less than 1 s
   * Inaccuracy less than 500 ms
   * Inaccuracy less than 100 ms
   * Inaccuracy less than 50 ms
   * Inaccuracy less than 10 ms
   * Inaccuracy not available

   Note: the steps "Inaccuracy higher than 24 h" and "Inaccuracy not available" give no upper bound of the inaccuracy.

.. feat_req:: Absolute Time base security qualifier
   :id: feat_req__time__abs_sec_qual
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__time__absolute_time_trust[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 3
   :valid_from: v1.0.0

   The :term:`score::time` feature shall indicate the :term:`security qualifier` of each :term:`Absolute Time`
   :term:`Snapshot` as one of the following steps, listed in ascending order of the security level:

   * No time available
   * Time not trustworthy
   * Time trustworthy
   * Time very trustworthy

   Note: the component that provides the Absolute Time samples determines the step of each sample
   (see :need:`feat_req__time__abs_sec_from_sample`).

.. feat_req:: Initial Absolute Time accuracy qualifier
   :id: feat_req__time__abs_initial_qual
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__time__absolute_time_accuracy[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall indicate the :term:`accuracy qualifier` "Inaccuracy higher than 24 h" from
   its start until it has processed the first :term:`Absolute Time sample`.

.. feat_req:: Accuracy qualifier of the time source
   :id: feat_req__time__abs_acc_from_sample
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__time__absolute_time_accuracy[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall indicate the :term:`accuracy qualifier` of the last processed
   :term:`Absolute Time sample`, unless another step applies (see :need:`feat_req__time__abs_no_delay_comp` and
   :need:`feat_req__time__abs_acc_degrade`).

.. feat_req:: Accuracy qualifier of an outdated sample
   :id: feat_req__time__abs_acc_degrade
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__time__absolute_time_accuracy[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall indicate the :term:`accuracy qualifier` "Inaccuracy not available" in an
   Absolute Time :term:`Snapshot` when the last :term:`Absolute Time sample` was processed longer ago than a
   configured period.

   Note: e.g. when the time source no longer delivers samples. The project chooses the period so that the accuracy
   of the last sample still holds, taking the rate deviation of the Vehicle Time into account.

.. feat_req:: Initial Absolute Time security qualifier
   :id: feat_req__time__abs_initial_sec_qual
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__time__absolute_time_trust[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall indicate the :term:`security qualifier` "No time available" from its start
   until it has processed the first :term:`Absolute Time sample`.

.. feat_req:: Security qualifier of the Absolute Time sample
   :id: feat_req__time__abs_sec_from_sample
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__time__absolute_time_trust[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall indicate the :term:`security qualifier` of the last processed
   :term:`Absolute Time sample`, unless it is degraded (see :need:`feat_req__time__abs_sec_degrade`).

.. feat_req:: Degradation of the security qualifier
   :id: feat_req__time__abs_sec_degrade
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__time__absolute_time_trust[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall degrade the :term:`security qualifier` "Time very trustworthy" to
   "Time trustworthy" when the last :term:`Absolute Time sample` with "Time very trustworthy" was processed longer
   ago than a configured period.

Absolute Time Access
--------------------

.. feat_req:: Absolute Time base API
   :id: feat_req__time__abs_base_api
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall provide an API to read the :term:`Absolute Time`.

   Note: ASIL_B applies to the API, so that ASIL-B applications can use it; the Absolute Time it delivers is QM
   data.

.. feat_req:: Non-blocking Absolute Time read
   :id: feat_req__time__abs_ctrl_flow
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall return an Absolute Time :term:`Snapshot` to a reading application without
   blocking the application on another process.

   Note: blocking means that the application waits until another process, e.g. the process that processes the
   :term:`Absolute Time sample`, releases a lock or replies. A bounded number of read retries does not block
   (API: :need:`feat_req__time__abs_base_api`). This requirement does not specify a read latency bound or upgrade
   the Absolute Time data from QM to ASIL_B.

.. feat_req:: Absolute Time value range
   :id: feat_req__time__abs_tp_format
   :reqtype: Interface
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall provide the :term:`Absolute Time` as :term:`Unix time` with a resolution of
   1 ns, covering at least the years 1970 to 2199.

   Note: standard calendar functions convert Unix time into the date and time format (year, month, day, hour,
   minute, second, nanosecond).

System Clock Synchronization
----------------------------

.. feat_req:: Setting the System Clock
   :id: feat_req__time__sys_clock_step
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall set the :term:`System Clock` to the :term:`Absolute Time` after processing
   an :term:`Absolute Time sample` when their difference exceeds a configured threshold, unless the accuracy or the
   security qualifier of the Absolute Time is below its configured minimum
   (see :need:`feat_req__time__sys_clock_min_acc` and :need:`feat_req__time__sys_clock_min_sec`).

   Note: a difference up to the threshold is left as it is. Until the first Absolute Time sample is processed, the
   System Clock keeps the time set by the operating system.

.. feat_req:: Minimum accuracy for the System Clock
   :id: feat_req__time__sys_clock_min_acc
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__time__absolute_time_accuracy[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall leave the :term:`System Clock` unchanged after processing an
   :term:`Absolute Time sample` when the :term:`accuracy qualifier` of the Absolute Time does not indicate an
   inaccuracy less than a configured limit.

   Note: e.g. when the Absolute Time is provided without delay compensation ("Inaccuracy not available",
   see :need:`feat_req__time__abs_no_delay_comp`).

.. feat_req:: Minimum security level for the System Clock
   :id: feat_req__time__sys_clock_min_sec
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__absolute_time_sync[version==1], stkh_req__time__absolute_time_trust[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall leave the :term:`System Clock` unchanged after processing an
   :term:`Absolute Time sample` when the :term:`security qualifier` of the Absolute Time indicates a lower security
   level than a configured step.

Local Time
==========

.. feat_req:: High resolution clock API
   :id: feat_req__time__high_res_clock_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__high_res_time[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The :term:`score::time` feature shall provide an API to read the :term:`High-Resolution Steady Clock` in nanoseconds resolution.

   Note: to which clock the high resolution clock is mapped, depends on the system design.

   *Use case:* such clocks might be used for time-critical applications, such as audio/video streaming, event logging, and diagnostics.

.. feat_req:: Monotonic clock API
   :id: feat_req__time__monotonic_clock_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from: stkh_req__time__monotonic_time[version==2], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall provide an API to read the :term:`Steady Clock`.

   Note: to which clock the Steady Clock is mapped depends on the system design.

Configuration
=============

.. feat_req:: Project-specific configuration
   :id: feat_req__time__config_params
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__time__vehicle_time_sync[version==1], stkh_req__time__absolute_time_sync[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The :term:`score::time` feature shall allow the system integrator to set the value of every parameter that its
   requirements call configured without modifying the source code of :term:`score::time`.

   Note: the values can e.g. be read from a configuration file at start-up or be set at build time. The integrator
   parts are the configuration AoUs (aou_req__feature_time__*_config).

Testability
===========

.. feat_req:: score::time mocking APIs implementation
   :id: feat_req__time__mocking_apis
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__dev_experience__mockup_public_apis[version==1]
   :satisfied_by: feat__time[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0

   The :term:`score::time` feature shall provide a mock for each of its public interfaces.

   Note: with a mock, a test of an application defines the time values, status and notifications that the
   application receives, e.g. in unit, component and integration tests.

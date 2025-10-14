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

Time Synchronization
^^^^^^^^^^^^^^^^^^^^

.. feat_req:: Vehicle Time synchronization
   :id: feat_req__time__vehicle_time_sync
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__time__vehicle_time_sync
   :status: valid

   The **score::time feature** shall synchronize the local clock with an external **Time Master** using the gPTP protocol (IEEE 802.1AS).

.. feat_req:: Vehicle Time synchronization precision
   :id: feat_req__time__vehicle_time_sync_prec
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__time__vehicle_time_sync
   :status: valid

   The **score::time feature** shall synchronize the local time, see feat_req__time__vehicle_time__sync, base with **Time Master** within a defined
   precision, based on the system setup.

   Note:

   * the particular target precision depends on the system setup
   * for AVB nodes the maximum difference in the synchronized time between two AVB ports/ECUs while
      both are in state SYNC, and could be 1 usec
   * for non-AVB node the precision is relaxed, and could be 200-500 usec

.. feat_req:: Vehicle Time base API
   :id: feat_req__time__vehicle_time_time_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__time__vehicle_time_api
   :status: valid

   The **score::time feature** shall provide an API to access the synchronized vehicle time.

.. feat_req:: Vehicle Time base accuracy qualifier
   :id: feat_req__time__vehicle_time_acc_qual_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__time__vehicle_time_api
   :status: valid

   The **score::time feature** shall provide an API to read the accuracy qualifier of the local synchronized time base.

   Note: qualifier shall reflect the accuracy of the local time base, e.g.

   * if it is synchronized to an external time source or not,
   * are there any instabilities, like time jumps to the past or to the future
   * does the time increase in a monotonic manner.

.. feat_req:: Vehicle Time base time point qualifier
   :id: feat_req__time__vehicle_time_time_pt_qual
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__time__vehicle_time_api
   :status: valid

   The **score::time feature** shall provide an API to read the time point qualifier of the local synchronized time base.

   Note: qualifier shall reflect if the time point could be treated as ASIL-B data or QM data

.. feat_req:: Vehicle Time control flow
   :id: feat_req__time__vehicle_time_ctrl_flow
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__time__vehicle_time_api
   :status: valid

   The **score::time feature** shall provide an access its data via specified APIs in a fast and very efficient manner,
   avoiding, if possible, kernel calls, resource manager involvement and so on.

   For APIs see:

   * feat_req__time__vehicle_time__time_api
   * feat_req__time__vehicle_time__acc_qual_api
   * feat_req__time__vehicle_time__time_pt_qual

   *Use case:* frequent access to the current synchronized time and its metadata by multiple clients within one ECU.

.. feat_req:: Vehicle Time synchronization logging
   :id: feat_req__time__vehicle_time_sync_log
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__debugging
   :status: valid

   The **score::time feature** shall provide a mechanism to log the internal state of the synchronization process,
   to be able to debug and diagnose the synchronization process.

   *Use case:* Debugging and diagnostics of the time synchronization process.


Time Synchronization to absolute external sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. feat_req:: score::time external synchronization
   :id: feat_req__time__abs_sync
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__time__absolute_time_sync
   :status: valid

   The **score::time feature** shall support synchronization with external time sources, such as UTC time from GPS.

.. feat_req:: Absolute Time base API
   :id: feat_req__time__abs_base_api
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__time__absolute_time_api
   :status: valid

   The **score::time feature** shall provide an API to read the absolute time base, synchronized to external time sources.

.. feat_req:: Absolute Time base accuracy qualifier
   :id: feat_req__time__abs_acc_qual
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__time__absolute_time_api
   :status: valid

   The **score::time feature** shall provide an API to read accuracy qualifier of the absolute time base, synchronized to external time sources.

   Note: the inaccuracy could be indicated in the following manner

   * Inaccuracy higher than 24h
   * Inaccuracy less than 24h
   * Inaccuracy less than 1h
   * Inaccuracy less than 15min
   * Inaccuracy less than 60s
   * Inaccuracy less than 10s
   * Inaccuracy less than 1s
   * Inaccuracy less than 500ms
   * Inaccuracy less than 100ms
   * Inaccuracy less than 50ms
   * Inaccuracy less than 10ms
   * Inaccuracy not available

.. feat_req:: Absolute Time base security qualifier
   :id: feat_req__time__abs_sec_qual
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__time__absolute_time_api
   :status: valid

   The **score::time feature** shall provide an API to read security qualifier of the absolute time base, synchronized to external time sources.

   Note: the security level might be indicated in the following steps

   * No time available
   * Time not trustworthy
   * Time trustworthy
   * Time very trustworthy

.. feat_req:: Absolute Time synchronization status log
   :id: feat_req__time__abs_sync_log
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__debugging
   :status: valid

   The **score::time feature** shall provide a mechanism to log the internal state of the absolute time synchronization process,
   to be able to debug and diagnose the synchronization process.

Local Clock
^^^^^^^^^^^^^^^^^^^^

.. feat_req:: High precision clock API
   :id: feat_req__time__high_prec_clock_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__time__high_precision_clock_api
   :status: valid

   The **score::time feature** shall provide an API to read the high precision clock in nanoseconds precision.

   Note: to which clock the high precision clock is mapped, depends on the system design.

   *Use case:* such clocks might be used for time-critical applications, such as audio/video streaming, event logging, and diagnostics.

.. feat_req:: Monotonic clock API
   :id: feat_req__time__monotonic_clock_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__time__monotonic_clock_api
   :status: valid

   The **score::time feature** shall provide an API to read monotonic, not adjustable clock value.

Testability
^^^^^^^^^^^^

.. feat_req:: score::time mocking APIs implementation
   :id: feat_req__time__mocking_apis
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__mockup_public_apis
   :status: valid

   The **score::time feature** shall provide support for mocking its public interfaces, enabling unit,
   component and integration testing of applications.

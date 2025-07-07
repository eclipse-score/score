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

.. feat_req:: Time client PTP sync
   :id: feat_req__time__trec_external_sync_ptp
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The **time client**, as part of score::time feature, shall synchronize the local clock with an external **time host** using the PTP protocol (IEEE 802.1AS).

.. feat_req:: score::time metadata
   :id: feat_req__time__time_metadata
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The score::time shall get the current synchronized time and its metadata from the **time host**.

.. feat_req:: score::time validation
   :id: feat_req__time__time_validataion
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The score::time shall validate the current synchronized time, which was received from the **time host** and reflect the validation results in the time point status accordingly.
   
   Validation of the current synchronized time includes:
   * checking the time point for loss of synchronization
   * checking the time point for monotonicity
   * checking the time point for instability, like time jumps to the past or to the future

.. feat_req:: score::time multiple applications
   :id: feat_req__time__multiple_applications
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The score::time feature shall provide a mechanism to access (read only) to the synchronized time and its status across multiple applications within one ECU.

.. feat_req:: score::time efficiency
   :id: feat_req__time__client_efficiency
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The score::time feature shall provide an access to the synchronized time and its status, see feat_req__time__multiple_applications, in an efficient way without any additional overhead, like kernel calls, Resource manager involvement and so on.
   *Use case:* frequent access to the current synchronized time and its metadata by multiple clients within one ECU.


.. feat_req:: score::time synchronization process metadata
   :id: feat_req__time__sync_process_metadata
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The score::time feature shall provide a mechanism to access (read only) to the internal state of the synchronization process, see **Synchronization process metadata**, across multiple applications within one ECU.

.. feat_req:: score::time synchronization stat logging
   :id: feat_req__time__sync_stat_logging
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The score::time shall provide a mechanism to log the internal state of the synchronization process, see **Synchronization process metadata**, to be able to debug and diagnose the time synchronization process.
   *Use case:* Debugging and diagnostics of the time synchronization process.


External Time Synchronization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. feat_req:: score::time external synchronization
   :id: feat_req__time__external_sync
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The score::time feature shall support synchronization with external time sources, such as GPS, based on SOME/IP messages.

.. feat_req:: score::time external synchronization status
   :id: feat_req__time__external_sync_status
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The score::time shall maintain the current synchronized time and its synchronization status, to be able to provide the latest values by clients request.

.. feat_req:: score::time external synchronization time
   :id: feat_req__time__external_sync_time
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The score::time feature shall provide a mechanism to access (read only) the current synchronized time from external time sources and its synchronization status.

.. feat_req:: score::time external synchronization status log
   :id: feat_req__time__external_sync_status_log
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The score::time feature shall provide a mechanism to log the internal state of the external time synchronization process, to be able to debug and diagnose the synchronization process.


High precision Clock
^^^^^^^^^^^^^^^^^^^^

.. feat_req:: score::time high precision clock
   :id: feat_req__time__high_precision_clock
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The score::time feature shall provide a mechanism to access (read only) the high precision clock in nanoseconds precision.
   *Use case:* such clocks might be used for time-critical applications, such as audio/video streaming, event logging, and diagnostics.


Monotonic Clock
^^^^^^^^^^^^^^^

.. feat_req:: score::time monotonic clock
   :id: feat_req__time__monotonic_clock
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies:
   :status: valid

   The score::time feature shall provide a mechanism to access (read only) to monotonic, not adjustable clock value, which is mapped from the known OS or HW clock.

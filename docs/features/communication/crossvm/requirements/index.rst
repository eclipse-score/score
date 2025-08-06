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

.. feat_req:: One-way data sharing into a VM
   :id: feat_req__crossvm__one_way_sharing
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   The system shall support one-way data sharing into a VM for vehicle state read-only for the VM (snapshot state).

.. feat_req:: Read-only access for VM
   :id: feat_req__crossvm__readonly_vm
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   The consumer (VM) shall have read-only access to the shared data.

.. feat_req:: Consistent data-sets
   :id: feat_req__crossvm__consistent_data
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   The system shall support consistent data-sets, allowing the consumer to obtain a consistent version of related data items.

.. feat_req:: Lock-free access
   :id: feat_req__crossvm__lock_free_access
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   Consistent access to data must be lock-free.

.. feat_req:: Producer time stamps
   :id: feat_req__crossvm__producer_timestamps
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   Producer time stamps shall be available for related data-sets.

.. feat_req:: Streamed data based on shared queues
   :id: feat_req__crossvm__streamed_data
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   The system shall support streamed data based on shared queues (stream of events or data).

.. feat_req:: Configurable queues
   :id: feat_req__crossvm__configurable_queues
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   Queues shall be configurable by the client (VM), including the number of elements and buffer allocation.

.. feat_req:: Lock-free queue access
   :id: feat_req__crossvm__lock_free_queue
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   Queues shall support lock-free access to data elements.

.. feat_req:: Bi-directional communication
   :id: feat_req__crossvm__bi_directional_comm
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   The system shall support bi-directional communication via writable data elements by the client.

.. feat_req:: Asynchronous support
   :id: feat_req__crossvm__async_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   The system shall provide asynchronous bi-directional support via multiple queues.

.. feat_req:: Shared memory chunks
   :id: feat_req__crossvm__shared_memory
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   The system shall support multiple chunks of shared memory to allow required access control.

.. feat_req:: Data update notifications
   :id: feat_req__crossvm__data_notifications
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   Notifications for data updates shall be available (virtual IRQs in a VM).

.. feat_req:: Configurable notifications
   :id: feat_req__crossvm__config_notifications
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__vm
   :status: valid

   Notifications shall be configurable by consumers of data (using flags or watermarks in shared memory from client to producer).

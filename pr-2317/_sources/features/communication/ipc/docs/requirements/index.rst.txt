..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

.. _ipc_requirements:

Requirements
============

.. document:: IPC Requirements
   :id: doc__ipc_requirements
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_feat

.. feat_req:: Zero-Copy Approach
   :id: feat_req__ipc__zero_copy
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__inter_process,stkh_req__app_architectures__support_data
   :status: valid

   IPC communication shall be possible without copying to-be-transferred data.

.. feat_req:: IPC Confidentiality
   :id: feat_req__ipc__confidentiality
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The IPC binding shall ensure confidentiality of its communication.

.. feat_req:: IPC Integrity
   :id: feat_req__ipc__integrity
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The IPC binding shall ensure integrity of its communication.

.. feat_req:: IPC Availability
   :id: feat_req__ipc__availability
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__communication__inter_process
   :status: valid

   The IPC binding shall ensure availability of its communication, so that the availability is independent per
   criticality level.

.. needextend:: "__ipc" in id
   :+tags: ipc

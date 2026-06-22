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
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_feat[version==1]

.. feat_req:: Zero-Copy Approach
   :id: feat_req__ipc__zero_copy
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1], stkh_req__app_architectures__support_data[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1

   IPC communication shall be possible without copying to-be-transferred data.

.. feat_req:: IPC Confidentiality
   :id: feat_req__ipc__confidentiality
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1

   The IPC binding shall ensure confidentiality of its communication.

.. feat_req:: IPC Integrity
   :id: feat_req__ipc__integrity
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1

   The IPC binding shall ensure integrity of its communication.

.. feat_req:: IPC Availability
   :id: feat_req__ipc__availability
   :reqtype: Functional
   :security: YES
   :safety: QM
   :derived_from: stkh_req__communication__inter_process[version==1]
   :satisfied_by: feat__com_communication[version==1]
   :status: valid
   :version: 1

   The IPC binding shall ensure availability of its communication, so that the availability is independent per
   criticality level.

.. needextend:: is_external == False and "__ipc" in id
   :+tags: ipc

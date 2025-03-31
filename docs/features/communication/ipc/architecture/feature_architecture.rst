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

Feature Architecture
####################

Static Architecture
*******************

.. feat_arc_sta:: Static Architecture
   :id: feat_arc_sta__communication__ipc
   :security: YES
   :status: valid
   :safety: ASIL_B
   :fulfils: feat_req__ipc__data_loss, feat_req__ipc__time_based_arch, feat_req__ipc__data_driven_arch, feat_req__ipc__request_driven_arch, feat_req__ipc__event_type, feat_req__ipc__method, feat_req__ipc__signal, feat_req__ipc__producer_consumer, feat_req__ipc__service_instance, feat_req__ipc__service_instance_names, feat_req__ipc__versioning, feat_req__ipc__service_location_transparency, feat_req__ipc__stateless_communication, feat_req__ipc__service_instance_granularity, feat_req__ipc__service_discovery, feat_req__ipc__safe_communication, feat_req__ipc__data_corruption, feat_req__ipc__data_reordering, feat_req__ipc__data_repetition, feat_req__ipc__data_loss, feat_req__ipc__asil
   :includes: feat_arc_int__communication__ipc

   .. uml:: _assets/stat_arch.puml
      :scale: 50
      :align: center

Dynamic Architecture
********************

.. feat_arc_dyn:: Dynamic Architecture
   :id: feat_arc_dyn__communication__ipc
   :security: YES
   :status: valid
   :safety: ASIL_B
   :fulfils: feat_req__ipc__depl_config_runtime

   .. uml:: _assets/dyn_arch.puml
      :scale: 50
      :align: center

Interfaces
**********

.. feat_arc_int:: Logical Interface
   :id: feat_arc_int__communication__ipc
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__ipc__interfaces

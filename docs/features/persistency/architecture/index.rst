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

.. _feature_architecture_persistency:

Architecture
============

.. document:: Persistency KVS Feature Architecture
   :id: doc__persistency_architecture
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: NO
   :realizes: wp__feature_arch[version==1]
   :tags: persistency


.. feat:: Persistency
   :id: feat__persistency
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :provides: logic_arc_int__persistency__interface


Logical Interfaces
------------------

.. logic_arc_int:: Ikvs
   :id: logic_arc_int__persistency__interface
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__persistency__async_api[version==1]
   :status: valid
   :version: 1

   .. uml:: _assets/kvs_interface.puml

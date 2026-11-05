..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

.. _tracing_architecture:

Tracing Architecture
####################

.. document:: Tracing Architecture
   :id: doc__tracing_architecture
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feature_arch[version==1]


Tracing Feature
---------------

.. feat:: Tracing
   :id: feat__tracing
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

Logical Interfaces
------------------

.. logic_arc_int:: Tracing
   :id: logic_arc_int__tracing__tracing
   :included_by: feat__tracing
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__com__tracing[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: Trace
   :id: logic_arc_int_op__tracing__trace
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__tracing__tracing

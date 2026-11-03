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

.. _logtrace_architecture:
.. _logging_architecture:
.. _tracing_architecture:

Log and Trace Architecture
==========================

.. document:: Log and Trace Architecture
   :id: doc__logging_architecture
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feature_arch[version==1]

.. feat:: Log and Trace
   :id: feat__logtrace
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :uses: logic_arc_int__baselibs__json[version==1], logic_arc_int__baselibs__filesystem[version==1]

Interfaces
----------

.. logic_arc_int:: Logging
   :id: logic_arc_int__log_cpp__logging
   :included_by: feat__logtrace
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1


.. logic_arc_int:: Logging Rust
   :id: logic_arc_int__log_rust__logging_rust
   :included_by: feat__logtrace
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int_op:: Log
   :id: logic_arc_int_op__logging__log
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__log_cpp__logging

.. logic_arc_int:: Tracing
   :id: logic_arc_int__tracing__tracing
   :included_by: feat__logtrace
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
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__tracing__tracing

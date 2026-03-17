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

.. _logging_architecture:

Logging Architecture
====================

.. feat:: Logging
   :id: feat__logging
   :security: YES
   :safety: ASIL_B
   :status: valid
   :provides: logic_arc_int__log_cpp__logging, logic_arc_int__log_rust__logging_rust
   :uses: logic_arc_int__baselibs__json, logic_arc_int__baselibs__filesystem


.. logic_arc_int:: Logging
   :id: logic_arc_int__log_cpp__logging
   :security: YES
   :safety: ASIL_B
   :status: valid


.. logic_arc_int:: Logging Rust
   :id: logic_arc_int__log_rust__logging_rust
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Log
   :id: logic_arc_int_op__logging__log
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__log_cpp__logging

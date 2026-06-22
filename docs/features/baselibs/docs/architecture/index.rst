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
.. _baselibs_architecture:

Architecture
=====================

.. document:: Baselibs Architecture
   :id: doc__baselibs_architecture
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feature_arch[version==1]

.. feat:: Baselibs
   :id: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :provides: logic_arc_int__baselibs__json, logic_arc_int__baselibs__memory_shared, logic_arc_int__com__message_passing, logic_arc_int__baselibs__result, logic_arc_int__baselibs__bit_manipulation, logic_arc_int__baselibs__bit_mask_operator, logic_arc_int__baselibs__dynamic_array, logic_arc_int__baselibs__intrusive_list, logic_arc_int__baselibs__filesystem, logic_arc_int__baselibs__utils_base64, logic_arc_int__baselibs__utils_scoped_op, logic_arc_int__baselibs__promise, logic_arc_int__baselibs__future, logic_arc_int__baselibs__shared_future, logic_arc_int__baselibs__executor, logic_arc_int__baselibs__task, logic_arc_int__baselibs__task_result, logic_arc_int__baselibs__synchronized_queue, logic_arc_int__baselibs__condition_variable, logic_arc_int__baselibs__aborts_upon_ex, logic_arc_int__baselibs__coverage_termination, logic_arc_int__baselibs__safemath, logic_arc_int__baselibs__safeatomics, logic_arc_int__baselibs__scoped_function, logic_arc_int__baselibs__string_view, logic_arc_int__baselibs__static_reflection, logic_arc_int__baselibs__generic_serial, logic_arc_int__baselibs__log_serial

Interfaces
----------

.. logic_arc_int:: Bit Manipulation
   :id: logic_arc_int__baselibs__bit_manipulation
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Bit Mask Operator
   :id: logic_arc_int__baselibs__bit_mask_operator
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: IJson
   :id: logic_arc_int__baselibs__json
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Memory Shared
   :id: logic_arc_int__baselibs__memory_shared
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Result
   :id: logic_arc_int__baselibs__result
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Dynamic Array
   :id: logic_arc_int__baselibs__dynamic_array
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Intrusive List
   :id: logic_arc_int__baselibs__intrusive_list
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Filesystem
   :id: logic_arc_int__baselibs__filesystem
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Base64
   :id: logic_arc_int__baselibs__utils_base64
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Scoped Operation
   :id: logic_arc_int__baselibs__utils_scoped_op
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Promise
   :id: logic_arc_int__baselibs__promise
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Future
   :id: logic_arc_int__baselibs__future
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Shared Future
   :id: logic_arc_int__baselibs__shared_future
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Executor
   :id: logic_arc_int__baselibs__executor
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Task
   :id: logic_arc_int__baselibs__task
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Task Result
   :id: logic_arc_int__baselibs__task_result
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Synchronized Queue
   :id: logic_arc_int__baselibs__synchronized_queue
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Condition Variable
   :id: logic_arc_int__baselibs__condition_variable
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Aborts Upon Exception
   :id: logic_arc_int__baselibs__aborts_upon_ex
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Coverage Termination Handler
   :id: logic_arc_int__baselibs__coverage_termination
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Safe Math
   :id: logic_arc_int__baselibs__safemath
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Safe Atomics
   :id: logic_arc_int__baselibs__safeatomics
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Scoped Function
   :id: logic_arc_int__baselibs__scoped_function
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: String View
   :id: logic_arc_int__baselibs__string_view
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Static Reflection
   :id: logic_arc_int__baselibs__static_reflection
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Generic Serialization
   :id: logic_arc_int__baselibs__generic_serial
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Logging Serialization
   :id: logic_arc_int__baselibs__log_serial
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

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

Interfaces
----------

.. logic_arc_int:: Bit Manipulation
   :id: logic_arc_int__baselibs__bit_manipulation
   :included_by: feat__baselibs
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Bit Mask Operator
   :id: logic_arc_int__baselibs__bit_mask_operator
   :included_by: feat__baselibs
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: IJson
   :id: logic_arc_int__baselibs__json
   :included_by: feat__baselibs
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Memory Shared
   :id: logic_arc_int__baselibs__memory_shared
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Result
   :id: logic_arc_int__baselibs__result
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Dynamic Array
   :id: logic_arc_int__baselibs__dynamic_array
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Intrusive List
   :id: logic_arc_int__baselibs__intrusive_list
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Filesystem
   :id: logic_arc_int__baselibs__filesystem
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Base64
   :id: logic_arc_int__baselibs__utils_base64
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Scoped Operation
   :id: logic_arc_int__baselibs__utils_scoped_op
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Promise
   :id: logic_arc_int__baselibs__promise
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Future
   :id: logic_arc_int__baselibs__future
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Shared Future
   :id: logic_arc_int__baselibs__shared_future
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Executor
   :id: logic_arc_int__baselibs__executor
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Task
   :id: logic_arc_int__baselibs__task
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Task Result
   :id: logic_arc_int__baselibs__task_result
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Synchronized Queue
   :id: logic_arc_int__baselibs__synchronized_queue
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Condition Variable
   :id: logic_arc_int__baselibs__condition_variable
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Aborts Upon Exception
   :id: logic_arc_int__baselibs__aborts_upon_ex
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Coverage Termination Handler
   :id: logic_arc_int__baselibs__coverage_termination
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Safe Math
   :id: logic_arc_int__baselibs__safemath
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Safe Atomics
   :id: logic_arc_int__baselibs__safeatomics
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Scoped Function
   :id: logic_arc_int__baselibs__scoped_function
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: String View
   :id: logic_arc_int__baselibs__string_view
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Static Reflection
   :id: logic_arc_int__baselibs__static_reflection
   :included_by: feat__baselibs
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Generic Serialization
   :id: logic_arc_int__baselibs__generic_serial
   :included_by: feat__baselibs
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

.. logic_arc_int:: Logging Serialization
   :id: logic_arc_int__baselibs__log_serial
   :included_by: feat__baselibs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

.. needextend:: "c.this_doc()"
   :+tags: baselibs

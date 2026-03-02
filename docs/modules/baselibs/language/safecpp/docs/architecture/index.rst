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

Safecpp Component Architecture
********************************

.. document:: Safecpp Architecture
   :id: doc__safecpp_architecture
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__component_arch

Overview/Description
--------------------

see :need:`doc__safecpp_architecture`

Static Architecture
-------------------

.. comp:: SafeCpp
   :id: comp__baselibs_safecpp
   :security: YES
   :safety: ASIL_B
   :status: valid
   :tags: baselibs_safecpp
   :implements: logic_arc_int__safecpp__aborts_upon_ex, logic_arc_int__safecpp__coverage_termination, logic_arc_int__baselibs__safemath, logic_arc_int__baselibs__safeatomics, logic_arc_int__baselibs__scoped_function, logic_arc_int__baselibs__string_view

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

Interfaces
----------
.. logic_arc_int:: Aborts Upon Exception
   :id: logic_arc_int__safecpp__aborts_upon_ex
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Allocate exception
   :id: logic_arc_int_op__safecpp__allocate_exception
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__safecpp__aborts_upon_ex

.. logic_arc_int:: Coverage Termination Handler
   :id: logic_arc_int__safecpp__coverage_termination
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Terminate_handler
   :id: logic_arc_int_op__safecpp__terminate_handler
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__safecpp__coverage_termination

.. logic_arc_int_op:: Signal_handler
   :id: logic_arc_int_op__safecpp__signal_handler
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__safecpp__coverage_termination

.. logic_arc_int:: Safe Math
   :id: logic_arc_int__baselibs__safemath
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Add
   :id: logic_arc_int_op__safecpp__safemath_add
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int_op:: Subtract
   :id: logic_arc_int_op__safecpp__safemath_subtract
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int_op:: Multiply
   :id: logic_arc_int_op__safecpp__safemath_multiply
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int_op:: Divide
   :id: logic_arc_int_op__safecpp__safemath_divide
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int_op:: Negate
   :id: logic_arc_int_op__safecpp__safemath_negate
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int_op:: Abs
   :id: logic_arc_int_op__safecpp__safemath_abs
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int_op:: Cast
   :id: logic_arc_int_op__safecpp__safemath_cast
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int_op:: Less
   :id: logic_arc_int_op__safecpp__safemath_less
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int_op:: Greater
   :id: logic_arc_int_op__safecpp__safemath_greater
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int_op:: Equal
   :id: logic_arc_int_op__safecpp__safemath_equal
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int_op:: Notequal
   :id: logic_arc_int_op__safecpp__safemath_notequal
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int_op:: Lessequal
   :id: logic_arc_int_op__safecpp__safemath_lessequal
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int_op:: Greaterequal
   :id: logic_arc_int_op__safecpp__safemath_greatereq
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safemath

.. logic_arc_int:: Safe Atomics
   :id: logic_arc_int__baselibs__safeatomics
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Atomic Add
   :id: logic_arc_int_op__safecpp__safeatomics_atomic
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__safeatomics

.. logic_arc_int:: Scoped Function
   :id: logic_arc_int__baselibs__scoped_function
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Move Only Scoped Function
   :id: logic_arc_int_op__safecpp__scoped_function_mo
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__scoped_function

.. logic_arc_int_op:: Copyable Scoped Function
   :id: logic_arc_int_op__safecpp__scoped_function_co
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__scoped_function

.. logic_arc_int_op:: Expire
   :id: logic_arc_int_op__safecpp__scoped_function_ex
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__scoped_function

.. logic_arc_int:: String View
   :id: logic_arc_int__baselibs__string_view
   :security: YES
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Null Termination Check
   :id: logic_arc_int_op__safecpp__string_view_null
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__string_view

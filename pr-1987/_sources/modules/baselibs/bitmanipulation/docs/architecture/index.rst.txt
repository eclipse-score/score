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

Bit Manipulation Component Architecture
***************************************

.. comp_arc_sta:: Bit Manipulation
   :id: comp_arc_sta__baselibs__bit_manipulation
   :security: NO
   :safety: ASIL_B
   :status: valid
   :tags: baselibs_bit_manipulation
   :implements: logic_arc_int__baselibs__bit_manipulation,logic_arc_int__baselibs__bit_mask_operator

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}


.. logic_arc_int:: Bit Manipulation
   :id: logic_arc_int__baselibs__bit_manipulation
   :security: NO
   :safety: ASIL_B
   :status: valid

.. logic_arc_int:: Bit Mask Opearator
   :id: logic_arc_int__baselibs__bit_mask_operator
   :security: NO
   :safety: ASIL_B
   :status: valid

.. logic_arc_int_op:: Set Bit
   :id: logic_arc_int_op__baselibs__set_bit
   :security: NO
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__bit_manipulation

.. logic_arc_int_op:: Clear Bit
   :id: logic_arc_int_op__baselibs__clear_bit
   :security: NO
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__bit_manipulation

.. logic_arc_int_op:: Toggle Bit
   :id: logic_arc_int_op__baselibs__toggle_bit
   :security: NO
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__bit_manipulation

.. logic_arc_int_op:: Test Bit
   :id: logic_arc_int_op__baselibs__test_bit
   :security: NO
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__bit_manipulation

.. logic_arc_int_op:: OR operator
   :id: logic_arc_int_op__baselibs__bitmask_or
   :security: NO
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__bit_mask_operator

.. logic_arc_int_op:: AND operator
   :id: logic_arc_int_op__baselibs__bitmask_and
   :security: NO
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__bit_mask_operator

.. logic_arc_int_op:: XOR operator
   :id: logic_arc_int_op__baselibs__bitmask_xor
   :security: NO
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__bit_mask_operator

.. logic_arc_int_op:: Complement operator
   :id: logic_arc_int_op__baselibs__bitmask_not
   :security: NO
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__bit_mask_operator

.. logic_arc_int_op:: Assignment Operators
   :id: logic_arc_int_op__baselibs__bitmask_assignmnt
   :security: NO
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__bit_mask_operator

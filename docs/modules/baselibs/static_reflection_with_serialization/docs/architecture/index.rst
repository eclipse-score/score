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

Static Reflection with Serialization Component Architecture
************************************************************

.. document:: static_reflection_with_serialization Architecture
   :id: doc__static_refl_with_serial_arch
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__component_arch

Overview/Description
--------------------

see :need:`doc__static_reflection_with_serialization`

Static Architecture
-------------------

.. comp:: Static Reflection with Serialization
   :id: comp__baselibs_static_reflection_with_serial
   :security: YES
   :safety: ASIL_B
   :status: valid
   :tags: baselibs_static_reflection_serialization
   :implements: logic_arc_int__baselibs__static_reflection,logic_arc_int__baselibs__generic_serial,logic_arc_int__baselibs__log_serial
   :belongs_to: feat__baselibs

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

Interfaces
----------

.. logic_arc_int:: Static Reflection
   :id: logic_arc_int__baselibs__static_reflection
   :security: NO
   :safety: ASIL_B
   :status: valid

.. logic_arc_int:: Generic Serialization
   :id: logic_arc_int__baselibs__generic_serial
   :security: NO
   :safety: ASIL_B
   :status: valid

.. logic_arc_int:: Logging Serialization
   :id: logic_arc_int__baselibs__log_serial
   :security: YES
   :safety: ASIL_B
   :status: valid

Static Reflection Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. logic_arc_int_op:: Visit
   :id: logic_arc_int_op__baselibs__visit
   :security: NO
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__static_reflection

.. logic_arc_int_op:: Declare Struct Visitable
   :id: logic_arc_int_op__baselibs__decl_struct_visit
   :security: NO
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__static_reflection

.. logic_arc_int_op:: Struct Introspection
   :id: logic_arc_int_op__baselibs__struct_intro
   :security: NO
   :safety:  ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__static_reflection

Generic Serialization Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. logic_arc_int_op:: Serialize
   :id: logic_arc_int_op__baselibs__serialize
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__generic_serial

.. logic_arc_int_op:: Deserialize
   :id: logic_arc_int_op__baselibs__deserialize
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__generic_serial

.. logic_arc_int_op:: Get Serialized Size
   :id: logic_arc_int_op__baselibs__get_serial_size
   :security: NO
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__generic_serial

Logging Serialization Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. logic_arc_int_op:: Serialize
   :id: logic_arc_int_op__baselibs__log_ser
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__log_serial

.. logic_arc_int_op:: Deserialize
   :id: logic_arc_int_op__baselibs__log_deser
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__log_serial

.. logic_arc_int_op:: Get Serialized Size
   :id: logic_arc_int_op__baselibs__get_log_ser_size
   :security: NO
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__baselibs__log_serial

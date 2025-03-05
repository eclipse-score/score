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

Detailed Design for Component: component1
=========================================

Description
-----------

 - component is split into two units unit1 and unit2 based on single responsibility principle.
 - unit2 is injected to unit1 one via dependency injection for testability.


Static Diagrams for Unit Interactions
-------------------------------------

.. unit_dd_sta:: dd example static
    :id: unit_dd_sta__dd_example_static
    :security: NO
    :safety: ASIL_B
    :status: valid

.. uml:: dd_example_ex_sta.puml

Dynamic Diagrams for Unit Interactions
--------------------------------------

.. unit_dd_dyn:: dd example dynamic
    :id: unit_dd_dyn__dd_example_dynamic
    :security: NO
    :safety: ASIL_B
    :status: valid

.. uml:: dd_example_ex_dyn.puml

Units within the Component
--------------------------

.. unit_dd:: unit1
    :id: unit_dd__unit1
    :security: NO
    :safety: ASIL_B
    :status: valid

Interface
*********

.. unit_dd_int:: int1
    :id: unit_dd_int__unit1_int1
    :security: NO
    :safety: ASIL_B
    :status: valid

.. unit_dd:: unit2
    :id: unit_dd__unit2
    :security: NO
    :safety: ASIL_B
    :status: valid

Interface
*********

.. unit_dd_int:: int2
    :id: unit_dd_int__unit2_int2
    :security: NO
    :safety: ASIL_B
    :status: valid


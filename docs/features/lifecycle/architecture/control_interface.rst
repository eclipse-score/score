..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

Control Interface
#################


It's foreseen ECU projects will need a custom state management to fulfill ECU-project specific requirements.  THe S-Core will offer a framework to control application lifecycle, but will not specify the State Manager.

The `Launch Manager` shall provide an interface, which allows an external State Manager application to request the `Launch Manager` to start, stop or restart applications or groups of applications,
which allows the implementation of a state management applications to support dynamic state control.


Static Architecture
===================


.. logic_arc_int:: Control Interface
   :id: logic_arc_int__lifecycle__controlif
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces



Use cases
=========

The following use cases are supported by the `ControlInterface` provided by the `Launch Manager`.

Starting a component (or a group of components)
-----------------------------------------------

When a request to start component(s) is received via the `ControlInterface`, the `Launch Manager` shall first evaluate if the conditions are correct for the launching of the component. At least the following conditions must be valid:

- The component exists in the model
- If the component has dependencies, the dependencies must be valid

If the pre-conditions are valid, then the components are started in the order defined in the dependency tree. (See : TODO, add link to the documentation about the dependencies).

If all components were successfully started, the respond to the caller with a status indicating success.
If any of the components failed to start, respond to the caller with a status indicating a failure.

Stopping a component (or a group of components)
-----------------------------------------------


Getting the status of a component (or a group of components)
------------------------------------------------------------

The `Launch Manager` shall provide an interface to requery of the status of a component or a group of components.


Dynamic Architecture
====================

.. feat_arc_dyn:: Control interface dynamic architecture start of components
   :id: feat_arc_dyn__lifecycle__control_if_start
   :security: YES
   :status: valid
   :safety: ASIL_B
   :fulfils: feat_req__lifecycle__control_commands, feat_req__lifecycle__request_group_launch
   :includes: 

   .. uml:: _assets/control_interface_start_sequence.puml
      :scale: 50
      :align: center

.. feat_arc_dyn:: Control interface dynamic architecture stop of components
   :id: feat_arc_dyn__lifecycle__control_if_stop
   :security: YES
   :status: valid
   :safety: ASIL_B
   :fulfils: feat_req__lifecycle__control_commands, feat_req__lifecycle__request_group_stop
   :includes: 

   .. uml:: _assets/control_interface_stop_sequence.puml
      :scale: 50
      :align: center



Requirements
============

- :need:`feat_req__lifecycle__control_commands`
- :need:`feat_req__lifecycle__query_commands`
- :need:`feat_req__lifecycle__request_group_launch`
- :need:`feat_req__lifecycle__request_group_stop`
- :need:`feat_req__lifecycle__request_group_restart`

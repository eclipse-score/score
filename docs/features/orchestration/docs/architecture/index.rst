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

.. document:: Orchestration Architecture
   :id: doc__orch_architecture
   :status: valid
   :safety: ASIL_B
   :tags: feature_request

Overview
--------

An brief overview of orchestration is described.

Description
-----------

A description of the orchestration module is located.

.. _orch_static_architecture:

Static Architecture
-------------------

 The overall architecture of the orchestration framework is layered. Orchestration uses the runtime component which abstracts execution
 specific details like threads.

.. feat_arc_sta:: Feature Architecture Orchestration
   :id: feat_arc_sta__orch__orchestration
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces
   :includes: logic_arc_int__orchestration__user, logic_arc_int__orchestration__design, logic_arc_int__orchestration__deployment

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}


API Components
^^^^^^^^^^^^^^

The API is split into three key components:

1. **Design**
   - Provides a way to register all application callables (functions, async functions, objects, etc.)
   - Allows the creation of an application task flow in the `config-by-code` case

2. **Deployment**
   - Provides a way to bind specific application actions to concrete implementations in the current system:

      #. Binding events to Local/Remote/Timers
      #. Configuring certain threads for callables

3. **Orchestration**
   - Acts as the central API for managing designs and transitioning them into a deployment-ready state
   - Handles the creation of programs and their orchestration

Purpose of Orchestration, Design, and Deployment Split
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The split between **Orchestration**, **Design**, and **Deployment** is intentional and reflects
a separation of concerns in the orchestration process:

- **Design**: Focuses on the **definition** of the system's components, encapsulating configuration
  and metadata for specific parts of the system.

- **Deployment**: Focuses on the **execution** of the designs, handling specific details of the
  given system.

- **Orchestration**: Acts as the **entry point** for managing designs and transitioning them into
  deployment, bridging the gap between the design phase and the deployment phase.

This separation ensures that each phase of the orchestration process is modular, testable, and maintainable.


Interface Description
^^^^^^^^^^^^^^^^^^^^^

The public API for the frontend is defined as:

.. logic_arc_int:: Orchestration Interface
   :id: logic_arc_int__orchestration__user
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int:: Design Interface
   :id: logic_arc_int__orchestration__design
   :security: YES
   :safety: ASIL_B
   :status: valid

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int:: Deployment Interface
   :id: logic_arc_int__orchestration__deployment
   :security: YES
   :safety: ASIL_B
   :status: valid


   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

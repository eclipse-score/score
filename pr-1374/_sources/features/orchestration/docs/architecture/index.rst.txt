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

.. _orch_architecture:

Architecture
============

Overview
--------

An brief overview of orchestration is described .

Description
-----------

A description of the orchestration module is located.

.. _orch_static_architecture:

Static Architecture
-------------------

As discussed in :ref:`com_rationale`, the overall architecture of the communication framework must be layered. This is required, to separate the frontend from the underlying communication mechanisms (also called bindings).

This ensures a stable public API, independent of the underlying binding(s). At the same time, the communication framework can support many different communication protocols in a flexible manner.

.. feat_arc_sta:: Feature Architecture Orchestration
   :id: feat_arc_sta__orch__orchestration
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces
   :includes: logic_arc_int__orchestration__user

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}

In the following sections we will look on the different architectural elements of the communication framework in more
detail.


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


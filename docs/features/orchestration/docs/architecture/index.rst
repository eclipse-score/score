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

 The overall architecture of the orchestration framework is to be layered.Orchestration uses the runtime component which abstracts

 execution specific details like threads.

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

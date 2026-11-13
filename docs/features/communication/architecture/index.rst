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

.. _com_architecture:

Communication Architecture
==========================

.. document:: Communication Architecture
   :id: doc__communication_architecture
   :status: valid
   :version: 2
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feature_arch[version==1]

Overview
--------

An brief overview of communication is described :ref:`here <com_abstract>`.

Description
-----------

A description of the communication module is located :ref:`here <com_rationale>`

.. _com_static_architecture:

Static Architecture
-------------------

As discussed in :ref:`com_rationale`, the overall architecture of the communication framework must be layered. This is required, to separate the frontend from the underlying communication mechanisms (also called bindings).

This ensures a stable public API, independent of the underlying binding(s). At the same time, the communication framework can support many different communication protocols in a flexible manner.

.. feat:: Communication Feature
   :id: feat__com_communication
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :version: 1

Interface Description
^^^^^^^^^^^^^^^^^^^^^

The public API for communication is defined as:

.. logic_arc_int:: Communication User Interface
   :id: logic_arc_int__communication__user
   :included_by: feat__com_communication
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__com__interfaces[version==1]
   :tags: communication

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: Initialize
   :id: logic_arc_int_op__com__initialize
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: Offer Service
   :id: logic_arc_int_op__com__offer_service
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: Update
   :id: logic_arc_int_op__com__update
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: Send
   :id: logic_arc_int_op__com__send
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: StartFindService
   :id: logic_arc_int_op__com__startfindserv
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: CreateProxy
   :id: logic_arc_int_op__com__createproxy
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: Subscribe
   :id: logic_arc_int_op__com__subscribe
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__communication__user

.. logic_arc_int_op:: GetNewSamples
   :id: logic_arc_int_op__com__getnewsamples
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__communication__user

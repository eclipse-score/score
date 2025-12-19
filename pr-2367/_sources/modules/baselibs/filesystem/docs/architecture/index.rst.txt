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

Component Architecture
======================

.. document:: Filesystem Architecture
   :id: doc__filesystem_architecture
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__component_arch

Overview/Description
--------------------
see :need:`doc__filesystem`

Static Architecture
-------------------

The components are designed to cover the expectations from the feature architecture
(i.e. if already exists a definition it should be taken over and enriched).

.. code-block:: rst

   .. comp_arc_sta:: Component Name (Static View)
      :id: comp_arc_sta__component_name__static_view
      :security: YES
      :safety: ASIL_B
      :status: invalid
      :implements: logic_arc_int__feature_name__interface_name
      :fulfils: comp_req__component_name__some_title
      :includes: comp_arc_sta__component_name__2

      .. needarch::
         :scale: 50
         :align: center

         {{ draw_component(need(), needs) }}

Dynamic Architecture
--------------------

.. code-block:: rst

   .. comp_arc_dyn:: Dynamic View
      :id: comp_arc_dyn__component_name__dynamic_view
      :security: YES
      :safety: ASIL_B
      :status: invalid
      :fulfils: comp_req__component_name__some_title

      put here a sequence diagram


Interfaces
----------

.. code-block:: rst

   .. real_arc_int:: <Title>
      :id: real_arc_int__<component>__<Title>
      :security: <YES|NO>
      :safety: <QM|ASIL_B>
      :fulfils: <link to component requirement id>
      :language: cpp

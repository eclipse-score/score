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

.. _logging_architecture:

Architecture
============

Overview
--------


Description
-----------


Static Architecture
-------------------

.. feat_arc_sta:: Feature Architecture Communication
   :id: feat_arc_sta__log__logging
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :fulfils:
   :includes: logic_arc_int__log__logging

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}


Architecture draft from CFT discussion
--------------------------------------

.. figure:: ../../_assets/feat_arc_sta__log__logging.drawio.svg
   :align: center
   :name: fr_logging_arc

   Architecture draft from CFT discussion

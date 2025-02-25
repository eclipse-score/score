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

Component Architecture Template
###############################

.. gd_temp:: Component Architecture Templates
    :id: gd_temp__arch__comp
    :status: valid
    :tags: architecture_design
    :complies: std_wp__iso26262__software_5

Component Architecture : <Component>/<sub-component>
====================================================

Overview
--------
Brief summary

Requirements Linked to Component Architecture
---------------------------------------------

.. code-block:: none

   .. needtable:: Overview of Component Requirements
      :style: table
      :columns: title;id
      :filter: search("comp_arch_sta__archdes$", "fulfils_back")
      :colwidths: 70,30

Description
-----------

General Description

Design Decisions

Design Constraints

Rationale Behind Architecture Decomposition
*******************************************
mandatory: a motivation for the decomposition or reason for not further splitting it into sub components.

.. note:: Common decisions across components / cross cutting concepts is at the higher level.

Static Architecture
-------------------

.. code-block:: rst

   .. comp_arc_sta:: <Title>
      :id: comp_arc_sta__<component>__<Title>
      :security: <YES|NO>
      :safety: <QM|ASIL_B|ASIL_D>
      :fulfils: <link to component requirement id>



Dynamic Architecture
--------------------

.. code-block:: rst

   .. comp_arc_dyn:: <Title>
      :id: comp_arc_dyn__<component>__<Title>
      :security: <YES|NO>
      :safety: <QM|ASIL_B|ASIL_D>
      :fulfils: <link to component requirement id>


Interfaces
----------

.. code-block:: rst

   .. comp_arc_int:: <Title>
      :id: comp_arc_int__<component>__<Title>
      :security: <YES|NO>
      :safety: <QM|ASIL_B|ASIL_D>
      :fulfils: <link to component requirement id>

.. note::
   Architecture can be split into multiple files. At component level the public interfaces to be used by the user and tester to be shown.


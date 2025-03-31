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

Feature Architecture Template
#############################

.. gd_temp:: Feature Architecture Templates
    :id: gd_temp__arch__feature
    :status: valid
    :complies: std_req__iso26262__software_741, std_req__iso26262__software_742, std_req__iso26262__software_743

Feature Architecture : <Feature>/<sub-feature>
==================================================

Overview
--------
Brief summary

Description
-----------

General Description

Design Decisions

Design Constraints

Requirements
------------

.. code-block:: none

   .. needtable:: Overview of Component Requirements
      :style: table
      :columns: title;id
      :filter: search("feat_arch_sta__archdes$", "fulfils_back")
      :colwidths: 70,30


Rationale Behind Architecture Decomposition
*******************************************
mandatory: a motivation for the decomposition

.. note:: Common decisions across features / cross cutting concepts is at the high level.

Static Architecture
-------------------

.. code-block:: rst

   .. feat_arc_sta:: <Title>
      :id: feat_arc_sta__<feature>__<Title>
      :security: <YES|NO>
      :safety: <QM|ASIL_B|ASIL_D>
      :fulfils: <link to feature requirement id>

Dynamic Architecture
--------------------

.. code-block:: rst

   .. feat_arc_dyn:: <Title>
      :id: feat_arc_dyn__<feature>__<Title>
      :security: <YES|NO>
      :safety: <QM|ASIL_B|ASIL_D>
      :fulfils: <link to feature requirement id>

Logical Interfaces
------------------

.. code-block:: rst

   .. feat_arc_int:: <Title>
      :id: feat_arc_int__<feature>__<Title>
      :security: <YES|NO>
      :safety: <QM|ASIL_B|ASIL_D>
      :fulfils: <link to feature requirement id>

.. note::
   Architecture can be split into multiple files,it is an High level architecture_design which can be shown without actual c++/rust interfaces and data types ,and there will be link to lower level architecture till code to get actual api descriptions.

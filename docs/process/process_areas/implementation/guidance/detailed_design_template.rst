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


Detailed Design Template
########################

.. gd_temp:: Detailed Design Templates
   :id: gd_temp__detailed_design
   :status: valid
   :complies: std_req__iso26262__software_2, std_req__iso26262__support_1, std_req__iso26262__support_2, std_req__iso26262__support_6

Detailed Design for Component: <Component Name>
===============================================

Description
-----------

| Design Decisions
| Design Constraints

Rationale Behind Decomposition into Units
******************************************
| mandatory: a motivation for the decomposition into one or more units.

.. note:: Reason for split into multiple units could be-
	    - Based on design principles like SOLID,DRY etc
	    - Based on design pattern's etc.

Static Diagrams for Unit Interactions
-------------------------------------

    | .. unit_dd_sta:: <Title>
    |    :id: unit_dd_sta__<Title>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :status: <valid|invalid>
    |    :implements: <link to component requirement id>
    | .. image:: <link to drawio image> or .. uml:: <link to plantuml>

Dynamic Diagrams for Unit Interactions
--------------------------------------

    | .. unit_dd_dyn:: <Title>
    |    :id: unit_dd_dyn__<Title>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :status: <valid|invalid>
    |    :implements: <link to component requirement id>
    | .. image:: <link to drawio image> or .. uml:: <link to plantuml>

Units within the Component
--------------------------

    | .. unit_dd:: <Unit>
    |    :id: unit_dd__<Unit>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :status: <valid|invalid>
    |    :implements: <link to component requirement id>

Interface
*********

    | .. unit_dd_int:: <Title>
    |    :id: unit_dd_int__<Unit>_<Title>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :status: <valid|invalid>
    |    :implements: <link to component requirement id>


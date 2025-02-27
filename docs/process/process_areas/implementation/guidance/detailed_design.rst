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

.. gd_temp:: Stakeholder Requirements Templates
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
    |    :id: UNIT_DD_STA__<Component>__<Title>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :satisfies: <link to component requirement id>
    | .. image:: <link to drawio image> or .. uml:: <link to plantuml>

Dynamic Diagrams for Unit Interactions
--------------------------------------

    | .. unit_dd_dyn:: <Title>
    |    :id: UNIT_DD_DYN__<Component>__<Title>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :satisfies: <link to component requirement id>
    | .. image:: <link to drawio image> or .. uml:: <link to plantuml>

Units within the Component
--------------------------

    | .. unit_dd:: <Unit Name>
    |    :id: UNIT_DD__<Unit>__<Unit Name>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :satisfies: <link to component requirement id>

Interface
*********

    | .. unit_dd_int:: <Title>
    |    :id: UNIT_DD_INT__<Unit>__<Unit Name>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :satisfies: <link to component requirement id>
    | .. image:: <link to drawio image> or .. uml:: <link to plantuml>


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

Detailed Design
###############

.. document:: Executor Detailed Design
   :id: doc__executor_detailed_design
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_implementation
   :tags: executor


Detailed Design for Component: Orchestrator
===========================================

Description
-----------

| Design Decisions - For the documentation of the decision the :need:`gd_temp__change_decision_record` can be used.
| Design Constraints

Rationale Behind Decomposition into Units
******************************************
| mandatory: a motivation for the decomposition into one or more units.

.. note:: Reason for split into multiple units could be-
	    - Based on design principles like SOLID,DRY etc
	    - Based on design pattern's etc.

Static Diagrams for Unit Interactions
-------------------------------------
.. code-block:: rst

   .. dd_sta:: <Title>
      :id: dd_sta__<Feature>__<Title>
      :security: <YES|NO>
      :safety: <QM|ASIL_B>
      :status: <valid|invalid>
      :implements: <link to component requirement id>
      :satisfies: <link to component architecture id>

        .. image:: <link to drawio image> or .. uml:: <link to plantuml>

Dynamic Diagrams for Unit Interactions
--------------------------------------
.. code-block:: rst

   .. dd_dyn:: <Title>
      :id: dd_dyn__<Feature>__<Title>
      :security: <YES|NO>
      :safety: <QM|ASIL_B>
      :status: <valid|invalid>
      :implements: <link to component requirement id>
      :satisfies: <link to component architecture id>

        .. image:: <link to drawio image> or .. uml:: <link to plantuml>

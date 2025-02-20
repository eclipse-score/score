..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

Requirement Templates
~~~~~~~~~~~~~~~~~~~~~

todo: add links to standards

.. gd_temp:: Stakeholder Requirements Template
  :id: gd_temp__stakeholder_requirements_template
  :status: draft
  :tags: requirements_management

    | .. stkh_req:: <Title>
    |    :id: sthk_req__<title>
    |    :reqtype: <Functional|Interface|Process|Legal|Non-Functional>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :rational: <The rationale provides the reason that the requirement is needed.>
    |    :status: <valid|invalid>


.. gd_temp:: Feature Requirements Template
    :id: gd_temp__feature_requirements_template
    :status: draft
    :tags: safety

    | .. feat_req:: <Title>
    |    :id: feat_req__<feature>__<title>
    |    :reqtype: <Functional|Interface|Process|Legal|Non-Functional>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :satisfies: <link to stakeholder requirement id>
    |    :status: <valid|invalid>


.. gd_temp:: Component Requirements Template
    :id: gd_temp__component_requirements_template
    :status: draft
    :tags: safety

    | .. comp_req:: <Title>
    |    :id: comp_req__<component>__<title>
    |    :reqtype: <Functional|Interface|Process|Legal|Non-Functional>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :satisfies: <link to feature requirement id>
    |    :status: <valid|invalid>


.. gd_temp:: Tool Requirements Template
  :id: gd_temp__tool_requirements_template
  :status: draft
  :tags: safety

    | .. tool_req:: <Title>
    |    :id: tool_req__<tool>__<title>
    |    :reqtype: <Functional|Interface|Process|Legal|Non-Functional>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :satisfies: <link to stakeholder id>
    |    :status: <valid|invalid>


.. gd_temp:: Requirement Formulation Template
   :id: gd_temp__requirement_formulation
   :status: valid
   :tags: safety

   Requirements shall be specified according to the following schema:

   <The SW Platform|Feature|Component> shall <main verb> <object> <parameter> <temporal/logical conjunction>

   <Note: (optional, not to be verified)>

   .. list-table:: Sentence Table
      :header-rows: 1

      * - Addressee of the requirement (subject)
        - shall
        - main verb
        - object of the requirement
        - parameter of the requirement
        - temporal/logical conjunction
      * - The development object (who/what)
        - shall
        - do something
        - for whom or what
        - which target value/condition
        - when, under which conditions
      * - The parking brake (general example)
        - shall
        - hold
        - the vehicle
        - up to a inclination of 20 deg
        - under all conditions (weather, …)
      * - The software platform (from our stakeholder requirements)
        - shall
        - enable
        - users
        - to ensure the compatibility of application software
        - across vehicle variants and vehicle software releases.


   .. note::
      Of the last three columns of the above sentence template table, filling one is mandatory the others are optional.



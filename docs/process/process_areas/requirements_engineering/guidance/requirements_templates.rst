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

.. _requirement templates:

Templates
=========

.. gd_temp:: Stakeholder Requirements Templates
   :id: gd_temp__req__stkh_req
   :status: valid
   :complies: std_wp__iso26262__software_2, std_wp__iso26262__support_1, std_wp__iso26262__support_2, std_wp__iso26262__support_6

   .. code-block:: rst

      .. stkh_req:: <Title>
         :id: stkh_req__<Title>
         :reqtype: <Functional|Interface|Process|Legal|Non-Functional>
         :safety: <QM|ASIL_B|ASIL_D>
         :rational: <The rationale provides the reason that the requirement is needed.>
         :status: <valid|invalid>

.. gd_temp:: Feature Requirements Templates
   :id: gd_temp__req__feat_req
   :status: valid
   :complies: std_wp__iso26262__software_2, std_wp__iso26262__support_1, std_wp__iso26262__support_2, std_wp__iso26262__support_6

   .. code-block:: rst

      .. feat_req:: <Title>
        :id: feat_req__<Feature>__<Title>
        :reqtype: <Functional|Interface|Process|Legal|Non-Functional>
        :security: <YES|NO>
        :safety: <QM|ASIL_B|ASIL_D>
        :satisfies: <link to stakeholder requirement id>
        :status: <valid|invalid>

.. gd_temp:: Component Requirements Templates
   :id: gd_temp__req__comp_req
   :status: valid
   :complies: std_wp__iso26262__software_2, std_wp__iso26262__support_1, std_wp__iso26262__support_2, std_wp__iso26262__support_6

   .. code-block:: rst

      .. comp_req:: <Title>
         :id: comp_req__<Component>__<Title>
         :reqtype: <Functional|Interface|Process|Legal|Non-Functional>
         :security: <YES|NO>
         :safety: <QM|ASIL_B|ASIL_D>
         :satisfies: <link to feature requirement id>
         :status: <valid|invalid>

.. gd_temp:: AoU Requirement Templates
   :id: gd_temp__req__aou_req
   :status: valid
   :complies: std_wp__iso26262__software_2, std_wp__iso26262__support_1, std_wp__iso26262__support_2, std_wp__iso26262__support_6

   .. code-block:: rst

      .. aou_req:: <Title>
         :id: aou_req__<Component>__<Title>
         :reqtype: <Functional|Interface|Process|Legal|Non-Functional>
         :security: <YES|NO>
         :safety: <QM|ASIL_B|ASIL_D>
         :status: <valid|invalid>
         :mitigates: <link to safety analysis>

.. gd_temp:: Process Requirements Templates
   :id: gd_temp__req__process_req
   :status: valid
   :complies: std_wp__iso26262__software_2, std_wp__iso26262__support_1, std_wp__iso26262__support_2, std_wp__iso26262__support_6

   .. code-block:: rst

      .. gd_req:: <Title>
         :id: gd_req__<Tool>__<Title>
         :satisfies: <link to guidance id>
         :status: <valid|invalid>

.. gd_temp:: Requirement Formulation Template
   :id: gd_temp__req__formulation
   :status: valid
   :complies: std_wp__iso26262__software_2, std_wp__iso26262__support_1, std_wp__iso26262__support_2, std_wp__iso26262__support_6

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
      * - Example 1: The component
        - shall
        - detect
        - if a key-value pair got corrupted
        - and set its status to INVALID
        - during every restart of the SW platform.
      * - Example 2: The software platform
        - shall
        - enable
        - users
        - to ensure the compatibility of application software
        - across vehicle variants and vehicle software releases.
      * - Example 3: The linter-tool
        - shall
        - check
        - correctness of .rst files format
        -
        - upon each commit.


   .. note::
      Of the last three columns of the above sentence template table, filling one is mandatory the others are optional.

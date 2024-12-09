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

.. _stakeholder_requirements_template:

Stakeholder Requirements Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    | .. stkh_req:: <Title>
    |    :id: STHK_REQ__<Title>
    |    :reqtype: <Functional|Interface|Process|Legal|Non-Functional>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :rational: <The rationale provides the reason that the requirement is needed.>
    |    :status: <valid|invalid>

    |  <The SW Platform|Feature|Component> shall <main verb> <object> <parameter> <temporal/logical conjunction>
    |  <Note: (optional, not to be verified)>

    | Sentence template:

       +----------------------------------------+-------+-----------------------+---------------------------+-------------------------------+-------------------------------------+
       | Addressee of the requirement (subject) | shall | main verb             | object of the requirement | parameter of the requirement  | temporal/logical conjunction        |
       +========================================+=======+=======================+===========================+===============================+=====================================+
       | The development object (who/what)      | shall | do someting           | for whom or what          | which target value/condition  | when, under which conditions        |
       +----------------------------------------+-------+-----------------------+---------------------------+-------------------------------+-------------------------------------+
       | The parking brake                      | shall | hold                  | the vehicle               | up to a inclination of 20 deg | under all conditions (weather, ...) |
       | (general example)                      |       |                       |                           |                               |                                     |
       +----------------------------------------+-------+-----------------------+---------------------------+-------------------------------+-------------------------------------+
       | The software platform                  | shall | enable                | users                     | to ensure the compatibility   | across vehicle variants and         |
       | (from our stakeholder requirements)    |       |                       |                           | of application software       | vehicle software releases.          |
       +----------------------------------------+-------+-----------------------+---------------------------+-------------------------------+-------------------------------------+

    .. note::
       Of the last three columns of the above sentence template table, filling one is mandatory the others are optional.

Tool Requirements Template
~~~~~~~~~~~~~~~~~~~~~~~~~~

    | .. tool_req:: <Title>
    |    :id: TOOL_REQ__<Tool>__<Title>
    |    :reqtype: <Functional|Interface|Process|Legal|Non-Functional>
    |    :security: <YES|NO>
    |    :safety: <QM|ASIL_B|ASIL_D>
    |    :satisfies: <link to stakeholder id>
    |    :status: <valid|invalid>

    |  <The Tool> shall <main verb> <object> <parameter> <temporal/logical conjunction>
    |  <Note: (optional, not to be verified)>

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

.. _adr-template:

======================================
ADR Template
======================================

This template is used to create new Architecture Decision Records (ADRs) for S-CORE. Each ADR should be stored in the `docs/requirements/adr/index.rst` directory and should use the sphinx needs type adr.

In each ADR file, include the following sections:

.. adr:: ADR Template
   :id: adr__001
   :title: Provide a descriptive and concise title. Summarizing the decision.
   :status: proposed
   :context: Describe the issue or motivation behind this decision or change.
   :decision: Detail the proposed change or decision.
   :consequences: Explain the impact of this change, including what becomes easier or more difficult.


.. container:: adr-template

    +--------------------------------------------------+
    | **ID**                                           |
    | Unique id for the ADR in format ADR-{uint8}      |
    +--------------------------------------------------+
    | **Title**                                        |
    | Provide a descriptive and concise title          |
    | summarizing the decision.                        |
    +--------------------------------------------------+
    | **Status**                                       |
    | Indicate the current status, such as proposed,   |
    | proposed, accepted, deprecated, rejected,        |
    | superseded                                       |
    +--------------------------------------------------+
    | **Context**                                      |
    | Describe the issue or motivation behind this     |
    | decision or change.                              |
    +--------------------------------------------------+
    | **Decision**                                     |
    | Detail the proposed change or decision.          |
    +--------------------------------------------------+
    | **Consequences**                                 |
    | Explain the impact of this change, including     |
    | what becomes easier or more difficult.           |
    +--------------------------------------------------+

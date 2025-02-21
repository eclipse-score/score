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

SWE.2 Software Architectural Design
-----------------------------------

The purpose is to establish an analyzed software architecture,
comprising static and dynamic aspects, consistent with the software
requirements.


Process outcomes
~~~~~~~~~~~~~~~~

1. A software architecture is designed including static and dynamic
   aspects.
2. The software architecture is analyzed against defined criteria.
3. Consistency and bidirectional traceability are established between
   software architecture and software requirements.
4. The software architecture is agreed and communicated to all affected
   parties.


Base practices
~~~~~~~~~~~~~~

.. std_req:: SWE.2.BP1: Specify static aspects of the software architecture
   :id:std_bp__aspice-40__SWE-2-BP1
   :status: valid
   :links:std_bp__aspice-40__iic-04-04

   Specify and document the static aspects of the software architecture
   with respect to the functional and non-functional software requirements,
   including external interfaces and a defined set of software components
   with their interfaces and relationships.

   .. note::

      The hardware-software-interface (HSI) definition puts in context the hardware design and
      therefore is an aspect of system design (SYS.3).


.. std_req:: SWE.2.BP2: Specify dynamic aspects of the software architecture
   :id:std_bp__aspice-40__SWE-2-BP2
   :status: valid
   :links:std_bp__aspice-40__iic-04-04

   Specify and document
   the dynamic aspects of the software architecture with respect to the functional and non-
   functional software requirements, including the behavior of the software components and their
   interaction in different software modes, and concurrency aspects.

   .. note::

      Examples for concurrency aspects are application-relevant interrupt handling, preemptive
      processing, multi-threading.

   .. note::

      Examples for behavioral descriptions are natural language or semi-formal notation (e.g,
      SysML, UML).


.. std_req:: SWE.2.BP3: Analyze software architecture
   :id:std_bp__aspice-40__SWE-2-BP3
   :status: valid
   :links:std_bp__aspice-40__iic-15-51

   Analyze the software architecture regarding
   relevant technical design aspects and to support project management regarding project
   estimates. Document a rationale for the software architectural design decision.

   .. note::

      See MAN.3.BP3 for project feasibility and MAN.3.BP5 for project estimates.

   .. note::

      The analysis may include the suitability of pre-existing software components for the current
      application.

   .. note::

      Examples of methods suitable for analyzing technical aspects are prototypes, simulations,
      qualitative analyses.

   .. note::

      Examples of technical aspects are functionality, timings, and resource consumption (e.g,
      ROM, RAM, external / internal EEPROM or Data Flash or CPU load).

   .. note::

      Design rationales can include arguments such as proven-in-use, reuse of a software
      framework or software product line, a make-or-buy decision, or found in an evolutionary way (e.g,
      set-based design).


.. std_req:: SWE.2.BP4: Ensure consistency and establish bidirectional traceability
   :id:std_bp__aspice-40__SWE-2-BP4
   :status: valid
   :links:std_bp__aspice-40__iic-13-51

   Ensure consistency and establish bidirectional traceability between the software architecture and the
   software requirements.

   .. note::

      There may be non-functional software requirements that the software architectural design
      does not trace to. Examples are development process requirements. Such requirements are still
      subject to verification.

   .. note::

      Bidirectional traceability supports consistency, and facilitates impact analysis of change
      requests, and demonstration of verification coverage. Traceability alone, e.g, the existence of links,
      does not necessarily mean that the information is consistent with each other.


.. std_req:: SWE.2.BP5: Communicate agreed software architecture
   :id:std_bp__aspice-40__SWE-2-BP5
   :status: valid
   :links:std_bp__aspice-40__iic-13-52

   Communicate the agreed software
   architecture to all affected parties.



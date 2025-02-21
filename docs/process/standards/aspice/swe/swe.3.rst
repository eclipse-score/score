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

SWE.3 Software Detailed Design and Unit Construction
----------------------------------------------------

The purpose is to establish a software detailed design, comprising
static and dynamic aspects, consistent with the software architecture,
and to construct software units consistent with the software detailed
design.


Process outcomes
~~~~~~~~~~~~~~~~

1. A detailed design is specified including static and dynamic aspects.
2. Software units as specified in the software detailed design are
   produced.
3. Consistency and bidirectional traceability are established between
   software detailed design and software architecture; and consistency
   and bidirectional traceability are established between source code
   and software detailed design; and consistency and bidirectional
   traceability are established between the software detailed design and
   the software requirements.
4. The source code and the agreed software detailed design are
   communicated to all affected parties.


Base practices
~~~~~~~~~~~~~~

.. std_req:: SWE.3.BP1: Specify the static aspects of the detailed design
   :id:std_bp__aspice-40__SWE-3-BP1
   :status: valid
   :links:std_bp__aspice-40__iic-04-05;std_bp__aspice-40__iic-11-05

   For each software component
   specify the behavior of its software units, their static structure and relationships, their interfaces
   including

   - valid data value ranges for inputs and outputs (from the application domain perspective),
      and
   - physical or measurement units applicable to inputs and outputs (from the application
      domain perspective).

   .. note::

      The boundary of a software unit is independent from the software unit’s representation in the
      source code, code file structure, or model-based implementation, respectively. It is rather driven by
      the semantics of the application domain perspective. Therefore, a software unit may be, at the code
      level, represented by a single subroutine or a set of subroutines.

   .. note::

      Examples of valid data value ranges with applicable physical units from the application
      domain perspective are ‘0..200 [m/s]’, ‘0..3.8 [A]’ or ‘1..100 [N]’. For mapping such application
      domain value ranges to programming language-level data types (such as unsigned Integer with a
      value range of 0..65535) refer to {need}`std_bp_aspice-40__SWE-3-BP2`.

   .. note::

      Examples of a measurement unit are ‘%’ or ‘‰’

   .. note::

      A counter is an example of a parameter, or a return value, to which neither a physical nor a
      surement unit is applicable.

   .. note::

      The hardware-software-interface (HSI) definition puts in context the hardware design and
      refore is an aspect of system design (SYS.3).


.. std_req:: SWE.3.BP2: Specify dynamic aspects of the detailed design
   :id:std_bp__aspice-40__SWE-3-BP2
   :status: valid
   :links:std_bp__aspice-40__iic-04-05;std_bp__aspice-40__iic-11-05

   Specify and document the
   dynamic aspects of the detailed design with respect to the software architecture, including the
   interactions between relevant software units to fulfill the component’s dynamic behavior.

   .. note::

      Examples for behavioral descriptions are natural language or semi-formal notation (e.g,
      SysML, UML).


.. std_req:: SWE.3.BP3: Develop software units
   :id:std_bp__aspice-40__SWE-3-BP3
   :status: valid
   :links:std_bp__aspice-40__iic-11-05

   Develop and document the software units consistent
   with the detailed design, and according to coding principles.

   .. note::

      Examples for coding principles at capability level 1 are not to use implicit type conversions,
      only one entry and one exit point in subroutines, and range checks (design-by-contract, defensive
      programming). Further examples see e.g, ISO 26262-6 clause 8.4.5 together with table 6.


.. std_req:: SWE.3.BP4: Ensure consistency and establish bidirectional traceability
   :id:std_bp__aspice-40__SWE-3-BP4
   :status: valid
   :links:std_bp__aspice-40__iic-13-51

   Ensure
   consistency and establish bidirectional traceability between the software detailed design and the
   software architecture. Ensure consistency and establish bidirectional traceability between the
   developed software units and the software detailed design. Ensure consistency and establish
   traceability between the software detailed design and the software requirements.

   .. note::

      Redundancy should be avoided by establishing a combination of these approaches.

   .. note::

      Examples for tracing a software unit in the detailed design to a software requirement directly
      are communication matrices or basis software aspects such as a list of diagnosis identifiers inherent
      in an Autosar configuration.

   .. note::

      Bidirectional traceability supports consistency, and facilitates impact analysis of change
      requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links,
      does not necessarily mean that the information is consistent with each other.


.. std_req:: SWE.3.BP5: Communicate agreed software detailed design and developed software units
   :id:std_bp__aspice-40__SWE-3-BP5
   :status: valid
   :links:std_bp__aspice-40__iic-13-52

   Communicate the agreed software detailed design and developed software units to all
   affected parties.



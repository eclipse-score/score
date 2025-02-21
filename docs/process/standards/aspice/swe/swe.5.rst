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

SWE.5 Software Component Verification and Integration Verification
------------------------------------------------------------------

The purpose is to verify that software components are consistent with
the software architectural design, and to integrate software elements
and verify that the integrated software elements are consistent with the
software architecture and software detailed design.


Process outcomes
~~~~~~~~~~~~~~~~

1. Verification measures are specified for software integration
   verification of the integrated software elements based on the
   software architecture and detailed design, including the interfaces
   of, and interactions between, the software components.
2. Verification measures for software components are specified to
   provide evidence for compliance of the software components with the
   software components’ behavior and interfaces.
3. Software elements are integrated up to a complete integrated
   software.
4. Verification measures are selected according to the release scope
   considering criteria, including criteria for regression verification.
5. Software components are verified using the selected verification
   measures, and the results of the integration verification are
   recorded.
6. Integrated software elements are verified using the selected
   verification measures, and the results of the integration
   verification are recorded.
7. Consistency and bidirectional traceability are established between
   verification measures and the software architecture and detailed
   design; and consistency and bidirectional traceability are
   established between verification results and verification measures.
8. The results of software component verification and software elements
   integration verification are summarized and communicated to all
   affected parties.


Base practices
~~~~~~~~~~~~~~

.. std_req:: SWE.5.BP1: Specify software integration verification measures
   :id:std_bp__aspice-40__SWE-5-BP1
   :status: valid
   :links:std_bp__aspice-40__iic-08-60

   Specify verification
   measures, based on a defined sequence and preconditions for the integration of software
   elements, against the defined static and dynamic aspects of the software architecture, including
   - techniques for the verification measures;
   - pass/fail criteria for verification measures;
   - entry and exit criteria for verification measures, and
   - the required verification infrastructure and environment setup.

   .. note::

      Examples on which the software integration verification measures may focus on are the
      correct dataflow and dynamic interaction between software components together with their timing
      dependencies, the correct interpretation of data by all software components using an interface, and
      the compliance to resource consumption objectives.

   .. note::

      The software integration verification measure may be supported by using hardware debug
      interfaces or simulation environments (e.g, Software-in-the-Loop-Simulation).


.. std_req:: SWE.5.BP2: Specify verification measures for verifying software component behavior
   :id:std_bp__aspice-40__SWE-5-BP2
   :status: valid
   :links:std_bp__aspice-40__iic-08-60

   Specify verification measures for software component verification against the defined software
   components’ behavior and their interfaces in the software architecture, including
   - techniques for the verification measures,
   - entry and exit criteria for verification measures,
   - pass/fail criteria for verification measures, and
   - the required verification infrastructure and environment setup.

   .. note::

      Verification measures are related to software components but not to the software units since
      software unit verification is addressed in the process `SWE.4 Software Unit Verification <swe4-software-unit-verification>`__.


.. std_req:: SWE.5.BP3: Select verification measures
   :id:std_bp__aspice-40__SWE-5-BP3
   :status: valid
   :links:std_bp__aspice-40__iic-08-58

   Document the selection of integration verification
   measures for each integration step considering selection criteria including criteria for regression
   verification. The documented selection of verification measures shall have sufficient coverage
   according to the release scope.

   .. note::

      Examples for selection criteria can be the need for continuous integration /continuous
      development regression verification (due to e.g, changes to the software architectural or detailed
      design), or the intended use of the delivered product release (e.g, test bench, test track, public road
      etc.).


.. std_req:: SWE.5.BP4: Integrate software elements and perform integration verification
   :id:std_bp__aspice-40__SWE-5-BP4
   :status: valid
   :links:std_bp__aspice-40__iic-06-50;std_bp__aspice-40__iic-01-03;std_bp__aspice-40__iic-01-50

   Integrate the
   software elements until the software is fully integrated according to the specified interfaces and
   interactions between the Software elements, and according to the defined sequence and
   defined preconditions. Perform the selected integration verification measures. Record the
   verification measure data including pass/fail status and corresponding verification measure data.

   .. note::

      Examples for preconditions for starting software integration are qualification of pre-existing
      software components, off-the-shelf software components, open-source-software, or auto-code
      generated software.

   .. note::

      Defined preconditions may allow e.g, big-bang-integration of all software components,
      continuous integration, as well as stepwise integration (e.g, across software units and/or software
      components up to the fully integrated software) with accompanying verification measures.

   .. note::

      See SUP.9 for handling deviations of verification results deviate expected results.


.. std_req:: SWE.5.BP5: Perform software component verification
   :id:std_bp__aspice-40__SWE-5-BP5
   :status: valid
   :links:std_bp__aspice-40__iic-03-50;std_bp__aspice-40__iic-15-52

   Perform the selected verification
   measures for verifying software component behavior. Record the verification results including
   pass/fail status and corresponding verification measure data.

   .. note::

      See SUP.9 for handling deviations of verification results deviate expected results.


.. std_req:: SWE.5.BP6: Ensure consistency and establish bidirectional traceability
   :id:std_bp__aspice-40__SWE-5-BP6
   :status: valid
   :links:std_bp__aspice-40__iic-13-51

   Ensure
   consistency and establish bidirectional traceability between verification measures and the static
   and dynamic aspects of the software architecture and detailed design. Establish bidirectional
   traceability between verification results and verification measures.

   .. note::

      Bidirectional traceability supports consistency, and facilitates impact analysis of change
      requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links,
      does not necessarily mean that the information is consistent with each other.


.. std_req:: SWE.5.BP7: Summarize and communicate results
   :id:std_bp__aspice-40__SWE-5-BP7
   :status: valid
   :links:std_bp__aspice-40__iic-13-52

   Summarize the software component
   verification and the software integration verification results and communicate them to all affected
   parties.

   .. note::

      Providing all necessary information from the test case execution in a summary enables
      other parties to judge the consequences.



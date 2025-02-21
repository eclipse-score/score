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

SWE.4 Software Unit Verification
--------------------------------

The purpose is to verify that software units are consistent with the
software detailed design


Process outcomes
~~~~~~~~~~~~~~~~

1. Verification measures for the software unit verification are
   specified.
2. Software unit verification measures are selected according to the
   release scope, including criteria for regression verification.
3. Software units are verified using the selected verification measures,
   and results are recorded.
4. Consistency and bidirectional traceability are established between
   verification mesaures and software units; and bidirectional
   traceability are established between verification results and
   verification mesaures.
5. Results of the software unit verification are summarized and
   communicated to all affected parties.


Base practices
~~~~~~~~~~~~~~

.. std_req:: SWE.4.BP1: Specify software unit verification measures
   :id:std_bp__aspice-40__SWE-4-BP1
   :status: valid
   :links:std_bp__aspice-40__iic-08-60

   Specify verification measures for
   each software unit defined in the software detailed design, including
   - pass/fail criteria for verification measures,
   - entry and exit criteria for verification measures, and
   - the required verification infrastructure.

   .. note::

      Examples for unit verification measures are static analysis, code reviews, and unit testing.

   .. note::

      Static analysis can be done based on MISRA rulesets and other coding standards.


.. std_req:: SWE.4.BP2: Select software unit verification measures
   :id:std_bp__aspice-40__SWE-4-BP2
   :status: valid
   :links:std_bp__aspice-40__iic-08-58

   Document the selection of
   verification measures considering selection criteria including criteria for regression verification.
   The documented selection of verification measures shall have sufficient coverage according to
   the release scope.

.. std_req:: SWE.4.BP3: Verify software units
   :id:std_bp__aspice-40__SWE-4-BP3
   :status: valid
   :links:std_bp__aspice-40__iic-03-50;std_bp__aspice-40__iic-15-52

   Perform software unit verification using the selected
   verification measures. Record the verification results including pass/fail status and
   corresponding verification measure data.

   .. note::

      See SUP.9 for handling of verification results that deviate from expected results


.. std_req:: SWE.4.BP4: Ensure consistency and establish bidirectional traceability
   :id:std_bp__aspice-40__SWE-4-BP4
   :status: valid
   :links:std_bp__aspice-40__iic-13-51

   Ensure
   consistency and establish bidirectional traceability between verification measures and the
   software units defined in the detailed design. Establish bidirectional traceability between the
   verification results and the verification measures.

   .. note::

      Bidirectional traceability supports consistency, and facilitates impact analysis of change
      requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links,
      does not necessarily mean that the information is consistent with each other.


.. std_req:: SWE.4.BP5: Summarize and communicate results
   :id:std_bp__aspice-40__SWE-4-BP5
   :status: valid
   :links:std_bp__aspice-40__iic-13-52

   Summarize the results of software unit
   verification and communicate them to all affected parties.

   .. note::

      Providing all necessary information from the test case execution in a summary enables other
      parties to judge the consequences.



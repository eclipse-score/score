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

SWE.6 Software Verification
---------------------------

The purpose of the Software Verification process is to ensure that the
integrated software is verified to be consistent with the software
requirements.


Process outcomes
~~~~~~~~~~~~~~~~

1. Verification measures are specified for software verification of the
   software based on the software requirements.
2. Verification measures are selected according to the release scope
   considering criteria, including criteria for regression verification.
3. The integrated software is verified using the selected verification
   measures and the results of software verification are recorded.
4. Consistency and bidirectional traceability are established between
   verification measures and software requirements; and bidirectional
   traceability are established between verification results and
   verification measures.
5. Results of the software verification are summarized and communicated
   to all affected parties.


Base practices
~~~~~~~~~~~~~~

.. std_req:: SWE.6.BP1: Specify verification measures for software verification
   :id:std_bp__aspice-40__SWE-6-BP1
   :status: valid
   :links:std_bp__aspice-40__iic-08-60

   Specify the verification
   measures for software verification suitable to provide evidence for compliance of the integrated
   software with the functional and non-functional information in the software requirements,
   including
   - techniques for the verification measures,
   - pass/fail criteria for verification measures,
   - a definition of entry and exit criteria for the verification measures,
   - necessary sequence of verification measures, and
   - the required verification infrastructure and environment setup.

   .. note::

      The selection of appropriate techniques for verification measures may depend on the
      content of the respective software requirement (e.g, boundary values and equivalence classes for
      data range-oriented requirements, positive/sunny-day-test vs. negative testing such as fault
      injection), or on requirements-based testing vs. “error guessing based on knowledge or experience”.


.. std_req:: SWE.6.BP2: Select verification measures
   :id:std_bp__aspice-40__SWE-6-BP2
   :status: valid
   :links:std_bp__aspice-40__iic-08-58

   Document the selection of verification measures
   considering selection criteria including criteria for regression verification. The documented
   selection of verification measures shall have sufficient coverage according to the release scope.

   .. note::

      Examples for selection criteria can be prioritization of requirements, continuous
      development, the need for regression verification (due to e.g., changes to the software
      requirements), or the intended use of the delivered product release (test bench, test track, public
      road etc.)


.. std_req:: SWE.6.BP3: Verify the integrated software
   :id:std_bp__aspice-40__SWE-6-BP3
   :status: valid
   :links:std_bp__aspice-40__iic-03-50;std_bp__aspice-40__iic-15-52

   Perform the verification of the integrated software
   using the selected verification measures. Record the verification results including pass/fail status
   and corresponding verification measure data.

   .. note::

      See SUP.9 for handling verification results that deviate from expected results.


.. std_req:: SWE.6.BP4: Ensure consistency and establish bidirectional traceability
   :id:std_bp__aspice-40__SWE-6-BP4
   :status: valid
   :links:std_bp__aspice-40__iic-13-51

   Ensure
   consistency and establish bidirectional traceability between verification measures and software
   requirements. Establish bidirectional traceability between verification results and verification
   measures.

   .. note::

      Bidirectional traceability supports consistency, and facilitates impact analysis of change
      requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links,
      does not necessarily mean that the information is consistent with each other.


.. std_req:: SWE.6.BP5: Summarize and communicate results
   :id:std_bp__aspice-40__SWE-6-BP5
   :status: valid
   :links:std_bp__aspice-40__iic-13-52

   Summarize the software verification
   results and communicate them to all affected parties.

   .. note::

      Providing all necessary information from the test case execution in a summary enables other
      parties to judge the consequences.



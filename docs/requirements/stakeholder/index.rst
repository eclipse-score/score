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

.. _stakeholder_requirements:

Stakeholder Requirements
========================


Integration
-----------

.. stkh_req:: Multirepo integration
   :id: STKH_REQ__INT_multi_repo_integration
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Allow independent development of software modules
   :status: valid

   Integration of multiple repositories shall be supported in a unified workflow.


Quality
-------

.. stkh_req:: Document assumptions and design decisions
   :id: STKH_REQ__QLY_document_assumptions_and_design_decisions
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: This is a usability constraint needed for long term maintenance support
   :status: valid

   All assumptions and design decisions made shall be specified as requirements and agreed within the SCORE community.


Requirements Engineering
------------------------

.. stkh_req:: Requirements traceability
   :id: STKH_REQ__RE_requirements_traceability
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: This is a usability constraint needed for long term maintenance support
   :status: valid

   All requirements shall be linked from lower to upper level, whereby the top-level are the stakeholder requirements.

.. stkh_req:: Document requirements as code
   :id: STKH_REQ__RE_requirements_as_code
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: In this project no external tool or service is used. Therefore as-code is the selected option.
   :status: valid

   Requirements shall be documented as code (Docs-as-code).

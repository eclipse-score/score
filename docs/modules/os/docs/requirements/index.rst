..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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



Requirements
############

.. document:: Operating System Requirements
   :id: doc__os_requirements
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_comp

Generally the OS (as an external SW element) is expected by the S-CORE project to fulfill the following requirements,
defined in the SW-platform assumptions (and partly even in the Stakeholder requirements).

The system integrator integrating S-CORE with the OS to provide a safe product has to make sure

- the functional requirements below are matching the OS used - see also :need:`aou_req__platform__safety_matching`
- the non-functional (integration) requirements below are fulfilled by the OS supplier

Integration Requirements
========================

Community Level
---------------

- :need:`aou_req__platform__integration_assistance`
- :need:`aou_req__platform__os_integration_manual`
- :need:`aou_req__platform__bug_interface`

Functional Level
----------------

- :need:`aou_req__platform__bazel_tooling`
- :need:`aou_req__platform__bug_fixing`

Certifiable Level
-----------------

- :need:`aou_req__platform__levels`
- :need:`aou_req__platform__safety_aou`
- :need:`aou_req__platform__safety_functions`
- :need:`aou_req__platform__safety_anomaly`


OS Specific Functional Requirements
===================================

- :need:`aou_req__platform__process_isolation`
- :need:`aou_req__platform__os_safety_functions`

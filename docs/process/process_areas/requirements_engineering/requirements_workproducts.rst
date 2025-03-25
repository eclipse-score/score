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

Workproducts Requirements Engineering
#####################################

.. workproduct:: Stakeholder Requirements
   :id: wp__requirements__stkh
   :status: valid
   :complies: std_wp__iso26262__system_651, std_wp__iso26262__software_651

   Technical requirements from a stakeholder viewpoint and assumptions of use based on the integration as SW platform SEooC in an assumed context.

.. workproduct:: Feature Requirements
   :id: wp__requirements__feat
   :status: valid
   :complies: std_wp__iso26262__software_651

   Feature requirements describe in a more detailed way the functionality which will fulfill a set of stakeholder requirements. A "feature" itself represents a set of requirements. It describes the interaction of the components to form a feature. It shall also be the basis for integration testing on platform level.

.. workproduct:: Component Requirements
   :id: wp__requirements__comp
   :status: valid
   :complies: std_wp__iso26262__software_651

   SW Requirements for components

.. workproduct:: Feature Assumptions of Use
   :id: wp__requirements__feat_aou
   :status: valid
   :complies: std_wp__iso26262__software_651

   SW Safety Requirements for the user of the feature, exportable requirements for the user to integrate in their req mgt system.

.. workproduct:: Component Assumptions of Use
   :id: wp__requirements__comp_aou
   :status: valid
   :complies: std_wp__iso26262__software_651

   SW Safety Requirements for the user of the component, exportable requirements for the user to integrate in their req mgt system.

.. workproduct:: Requirements Inspection
   :id: wp__requirements__inspect
   :status: draft
   :complies: std_wp__iso26262__software_653

   | Depends on requirements management tooling, expect text based requirements maintained in git.
   | - github review with integrated inspection checklist, only valid requirements get merged
   |
   | Compare also `Gitub documentationt <https://docs.github.com/en>`_

.. needextend:: "docs/process/requirements_engineering" in docname
   :+tags: requirements_engineering

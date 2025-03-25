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

Work Products Change Management
###############################

.. workproduct:: Platform Change Management Plan
   :id: wp__chm_plan
   :status: valid
   :tags: change_management
   :complies: std_wp__iso26262__support_851

   Change Management Plan (Part of the Platform Management Plan)

.. workproduct:: Issue tracking system
   :id: wp__issue_track_system
   :status: valid
   :tags: change_management
   :complies: std_wp__iso26262__support_852, std_wp__iso26262__support_853, std_wp__iso26262__support_854, std_req__aspice_40__iic-13-16

   | - Change request
   | - Change request plan
   | - Change report
   | - Identified safety anomaly report
   | - Impact analysis
   |
   | Safety anomaly: Conditions that deviate from expectations and that can lead to harm.
   | The documentation of a change request shall contain the list of changed work products,
     the details of the change and the planned date of deployment of the change.

.. workproduct:: Feature Request
   :id: wp__feat_request
   :status: valid
   :tags: change_management
   :complies: std_wp__iso26262__support_852, std_wp__iso26262__support_853, std_req__aspice_40__iic-13-16

   | - Feature request for a new feature or a feature modification
   |
   | Change Request for a new platform feature or a modification of an existing platform feature,
   | which changes the scope of the feature.

.. workproduct:: Component Request
   :id: wp__cmpt_request
   :status: valid
   :tags: change_management
   :complies: std_wp__iso26262__support_852, std_wp__iso26262__support_853, std_req__aspice_40__iic-13-16

   | - Component request for a new component or a component modification
   |
   | Change Request for a new platform component or a modification of an existing platform component,
   | which changes the scope of the component.
   | Software Modules are also Components (top-level component).

.. needextend:: "docs/process/change_management" in docname
   :+tags: change_management

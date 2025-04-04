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

.. _chm_process_requirements:

Process Requirements
====================

.. _chm_process_change_request_attributes:

Change Request Attributes
-------------------------

.. gd_req:: Change Request attribute: UID
   :id: gd_req__change__attr_uid
   :status: valid
   :tags: chm, attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP1, std_req__iso26262__support_8411, std_req__iso26262__support_8421, std_req__iso26262__support_8432, std_req__iso26262__support_8453

   Each Change Request shall have a unique ID. It shall be in an integer number.

.. gd_req:: Change Request attribute: status
   :id: gd_req__change__attr_status
   :status: valid
   :tags: chm, attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP3, std_req__aspice_40__SUP-10-BP5, std_req__aspice_40__SUP-10-BP6, std_req__iso26262__support_8411, std_req__iso26262__support_8422, std_req__iso26262__support_8432, std_req__iso26262__support_8442

   Each Change Request shall have a status:

      * draft
      * in review
      * accepted
      * rejected

.. gd_req:: Change Request attribute: title
   :id: gd_req__change__attr_title
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP1, std_req__iso26262__support_8411, std_req__iso26262__support_8422

   Reason for the Change Request

.. gd_req:: Change Request attribute: description
   :id: gd_req__change__attr_impact_description
   :status: valid
   :tags: chm, attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP2, std_req__iso26262__support_8411, std_req__iso26262__support_8422, std_req__iso26262__support_8431, std_req__iso26262__support_8432, std_req__iso26262__support_8452, std_req__iso26262__support_8453

   Exact description of the Change Request, including impact analysis on functional safety,
   security, implementation (schedule, risks, resources) verification (measures defined).

.. gd_req:: Change Request attribute: safety
   :id: gd_req__change__attr_impact_safety
   :status: valid
   :tags: chm, attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP2, std_req__iso26262__support_8422

   Each Change Request shall have a automotive safety integrity level (ASIL) identifier:

      * QM
      * ASIL_B
      * ASIL_D

.. gd_req:: Change Request attribute: security
   :id: gd_req__change__attr_impact_security
   :status: valid
   :tags: chm, attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP2, std_req__iso26262__support_8422

   Each Change Request shall have a security relevance identifier:

      * Yes
      * No

.. gd_req:: Change Request attribute: Types
   :id: gd_req__change__attr_types
   :status: valid
   :tags: chm, attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP1

      * Feature
      * Feature Modification
      * Component
      * Component Modification

   Feature/Component means new Feature/Component

.. gd_req:: Change Request attribute: Affected Work Products
   :id: gd_req__change__attr_affected_wp
   :status: valid
   :tags: chm, attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP4, std_req__iso26262__support_8412, std_req__iso26262__support_8422, std_req__iso26262__support_8452, std_req__iso26262__support_8453

   Links to the work products affected by the Change Request

.. gd_req:: Change Request attribute: Milestone
   :id: gd_req__change__attr_milestone
   :status: valid
   :tags: chm, attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP6, std_req__iso26262__support_8413

   Milestone until the Change Request must be implemented (used for prioritization)


.. _chm_process_change_requests_checks:

Change Request Checks
'''''''''''''''''''''

.. gd_req:: Change Requests mandatory attributes provided
   :id: gd_req__change_attr_mandatory
   :status: valid
   :tags: chm, attribute, check
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__iic-13-51

   It shall be checked if all mandatory attributes for each Change Request
   is provided by the user. For all requirements following attributes shall be mandatory:

   .. needtable:: Overview mandatory change request attributes
      :filter: "mandatory" in tags and "attribute" in tags and "chm" in tags
      :style: table
      :columns: title
      :colwidths: 30


.. _chm_process_change_requests_impact_analysis_tool:

Change Request Traceability Impact Analysis Tool
''''''''''''''''''''''''''''''''''''''''''''''''

.. gd_req:: Change Requests Impact Analysis Tool
   :id: gd_req__change_tool_impact_analysis
   :status: valid
   :tags: chm, check, tool
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__iic-13-51

   It shall be reported, which work products and elements are affected by adding a new
   feature or component or by a modification of an existing feature or component.

.. needextend:: "process_areas/change_management" in docname
   :+tags: change_management

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
   :tags: attribute,mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP1, std_req__iso26262__support_16, std_req__iso26262__support_20, std_req__iso26262__support_23, std_req__iso26262__support_28

   Each Change Request shall have a unique ID. It shall be in an integer number.

.. gd_req:: Requirement attribute: status
   :id: gd_req__change__attr_status
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP3, std_req__aspice_40__SUP-10-BP5, std_req__aspice_40__SUP-10-BP6, std_req__iso26262__support_16, std_req__iso26262__support_21, std_req__iso26262__support_23, std_req__iso26262__support_25

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
   :complies: std_req__aspice_40__SUP-10-BP1, std_req__iso26262__support_16, std_req__iso26262__support_21

   Reason for the Change Request

.. gd_req:: Change Request attribute: description
   :id: gd_req__change__attr_impact_description
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP2, std_req__iso26262__support_16, std_req__iso26262__support_21, std_req__iso26262__support_22, std_req__iso26262__support_23, std_req__iso26262__support_27, std_req__iso26262__support_28

   Exact description of the Change Request, including impact analysis on functional safety,
   security, implementation (schedule, risks, resources) verifcation (measures defined).

.. gd_req:: Change Request attribute: safety
   :id: gd_req__change__attr_impact_safety
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP2, std_req__iso26262__support_21

   Each Change Request shall have a automotive safety integrity level (ASIL) identifier:

      * QM
      * ASIL_B
      * ASIL_D

.. gd_req:: Change Request attribute: security
   :id: gd_req__change__attr_impact_security
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP2, std_req__iso26262__support_21

   Each Change Request shall have a security relevance identifier:

      * Yes
      * No

.. gd_req:: Change Request: Types
   :id: gd_req__change__types
   :status: valid
   :tags: structure
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP1

      * Feature
      * Modification

.. gd_req:: Change Request attribute: Affected Work Products
   :id: gd_req__change__attr_affected_wp
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP4, std_req__iso26262__support_17, std_req__iso26262__support_21, std_req__iso26262__support_27, std_req__iso26262__support_28

   Links to the work producs affected by the Change Request

.. gd_req:: Change Request attribute: Milestone
   :id: gd_req__change__attr_milestone
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies: std_req__aspice_40__SUP-10-BP6, std_req__iso26262__support_18

   Milestone unitl the Change Requeste must be implemented (used for prioritization)
.. _chm_process_change requests_checks:


Change Request Checks
'''''''''''''''''''''

.. gd_req:: Change Requests mandatory attributes provided
   :id: gd_req__change_attr_mandatory
   :status: valid
   :tags: attribute, check
   :satisfies: wf__change__cr_an_change_request, wf__change__rv_ap_change_request
   :complies:

   It shall be checked if all mandatory attributes for each Change Request
   is provided by the user. For all requirements following attributes shall be mandatory:

   .. needtable:: Overview mandatory change request attributes
      :filter: "mandatory" in tags and "attribute" in tags and type == "gd_req"
      :style: table
      :columns: title
      :colwidths: 30

.. needextend:: "process_areas/change_management" in docname
   :+tags: change_management

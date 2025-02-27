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
   :satisfies: wf__change__cr_dc_change_request, wf__change__rv_ap_change_request
   :complies:

   Each change request shall have a unique ID. It shall be in a format which is also human
   readable and consists of

      * type of change request
      * keyword describing the content of the change request.

   The naming convention is defined here: :ref:`naming_convention_needs`

.. gd_req:: Requirement attribute: status
   :id: gd_req__change__attr_status
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_dc_change_request, wf__change__rv_ap_change_request
   :complies:

   Each change request shall have a status:

      * draft
      * in review
      * accepted
      * rejected

.. gd_req:: Change Request attribute: title
   :id: gd_req__change__attr_title
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_dc_change_request, wf__change__rv_ap_change_request
   :complies:

   Reason for the change request

.. gd_req:: Change Request attribute: description
   :id: gd_req__change__attr_description
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_dc_change_request, wf__change__rv_ap_change_request
   :complies:

   Exact description of the change request

.. gd_req:: Change Request attribute: safety
   :id: gd_req__change__attr_safety
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_dc_change_request, wf__change__rv_ap_change_request
   :complies:

   Each change request shall have a automotive safety integrity level (ASIL) identifier:

      * QM
      * ASIL_B
      * ASIL_D

.. gd_req:: Change Request attribute: security
   :id: gd_req__change__attr_security
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_dc_change_request, wf__change__rv_ap_change_request
   :complies:

   Each change request shall have a security relevance identifier:

      * Yes
      * No

.. gd_req:: Change Request: Types
   :id: gd_req__change__types
   :status: valid
   :tags: structure
   :satisfies: wf__change__cr_dc_change_request, wf__change__rv_ap_change_request
   :complies:

      * Feature
      * Improvement
      * Bugfix

.. gd_req:: Change Request attribute Affected Work Products
   :id: gd_req__change__attr_rationale
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__change__cr_dc_change_request, wf__change__rv_ap_change_request
   :complies:

   Links to the work producs affected by the change request

.. _chm_process_change requests_checks:

Change Request Checks
'''''''''''''''''''''

.. gd_req:: Change Requests mandatory attributes provided
   :id: gd_req__change_attr_mandatory
   :status: valid
   :tags: attribute, check
   :satisfies: wf__change__cr_dc_change_request, wf__change__rv_ap_change_request
   :complies:

   It shall be checked if all mandatory attributes for each change request
   is provided by the user. For all requirements following attributes shall be mandatory:

   .. needtable:: Overview mandatory change request attributes
      :filter: "mandatory" in tags and "attribute" in tags and type == "gd_req"
      :style: table
      :columns: title
      :colwidths: 30

.. needextend:: "process_areas/change_management" in docname
   :+tags: change_management

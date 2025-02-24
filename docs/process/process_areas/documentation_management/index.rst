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

.. _process_documentation_management:

Documentation Management
========================

Concept
-------

.. doc_concept:: Documentation Management Concept
   :id: doc_concept__documentation_management
   :status: valid

In this section a concept for the documentation management will be discussed. Inputs for this concepts are mainly the requirements of ISO26262 "Part 2: Management of functional safety"

Inputs
^^^^^^

#. Stakeholders for the documentation work products?
#. Who needs which information?
#. Which work products do we have?
#. What tooling do we need?

Stakeholders
^^^^^^^^^^^^

#. :need:`Technical Lead <rl__technical_lead>`

   * planning and status reporting of work products and their documentation

#. :need:`Safety Manager <rl__safety_manager>`

   * wants to know when the safety related documents are ready for a release
   * wants to know who was the author and approver of a document in case of safety issues


Work Products
^^^^^^^^^^^^^

:need:`doc__documentation_mgt_plan` is a document and part of the work product :need:`wp__platform_mgmt`.


Document Management Tooling
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the document attributes to be manually set, sphinx-needs will be used.

For the versioning and version history github is used.

For the automated attributes additional tooling is created (see :doc:`guidance/process_req`)

Getting started
---------------

.. doc_getstrt:: Documentation Management Get Started
   :id: doc_getstrt__documentation_management
   :status: valid

In case you are appointed as a :need:`Technical Lead <rl__technical_lead>` by the :need:`rl__project_lead` in the S-CORE project:

* On platform level, process community already provided a draft documentation management plan,
  see :need:`doc__documentation_mgt_plan`, just set it to "valid"
* On module level, create a documentation management plan using the platform one as a template
* On both levels: make sure only the documents in your scope appear in the documents list within the plan

Workflows
---------

The main work product is the documentation management plan, which is a part of the platform management plan.
Thus the work flow :need:`wf__cr_mt_platform_mngmt_plan` applies.

Guidance
--------

The document management guideline is contained within the document management plan,
to have all relevant information in one space, see :need:`gd_guidl__documentation`

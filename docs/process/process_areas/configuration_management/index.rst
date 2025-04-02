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

.. _process_configuration_management:

Configuration Management
========================

Concept
-------

.. doc_concept:: Configuration Management Concept
   :id: doc_concept__configuration__process
   :status: valid

In this section a concept for the configuration management will be discussed. Inputs for this concepts are mainly the requirements of ISO26262 "Part 8: Supporting Processes"

Inputs
^^^^^^

#. Stakeholders for the configuration work products?
#. Who needs which information?
#. Which work products do we have?
#. What tooling do we need?

Stakeholders
^^^^^^^^^^^^

#. :need:`Technical Lead <rl__technical_lead>`

   * for creating a module or a platform release a baseline of artefacts is needed

#. :need:`Contributor <rl__contributor>` and :need:`Committer <rl__committer>`

   * wants know which artefact version has to be used as input for his work
   * wants to share their created work product with others for example to get those reviewed
   * wants to integrate share their created work product with other work products


Work Products
^^^^^^^^^^^^^

:need:`doc__config_mgt_plan` is a document and part of the work product :need:`wp__platform_mgmt`.


Configuration Management Tooling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Almost all requirements of the standards towards configuration management can be covered by
standard tooling of the Eclipse Foundation (github for versioning) and of the S-CORE project
(sphinx-needs for text based identification of work products).

For the automated storage additional tooling is created (see :doc:`guidance/process_req`)

Getting started
---------------

.. doc_getstrt:: Configuration Management Get Started
   :id: doc_getstrt__configuration__process
   :status: valid

In case you are appointed as a :need:`Technical Lead <rl__technical_lead>` by the :need:`rl__project_lead` in the S-CORE project:

* On platform level, process community already provided a draft configuration management plan,
  see :need:`doc__config_mgt_plan`, just set it to "valid"
* On module level, create a configuration management plan using the platform one as a template.
  If no configuration management plan on module level is created, the platform one is adopted.

As a normal contributor or committer consult the :need:`doc__config_mgt_plan`, but this should not
differ from normal usage of github as a configuration management tool.

Workflows
---------

The main work product is the configuration management plan, which is a part of the platform management plan.
Thus the work flow :need:`wf__cr_mt_platform_mngmt_plan` applies.

Baselines (sets of workproducts and their versions) defining a SW Release on platform or module level
are created as part of this process but are documented in the respective release notes.

Guidance
--------

The configuration management guideline is contained within the configuration management plan,
to have all relevant information in one space, see :need:`gd_guidl__configuration`

Some process requirements to be automated are available:

.. toctree::
   :maxdepth: 1
   :glob:

   guidance/process_req.rst

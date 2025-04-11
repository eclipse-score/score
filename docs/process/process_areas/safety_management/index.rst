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

.. _process_safety_management:

Safety Management
=================

Concept
-------

.. doc_concept:: Safety Management Concept
   :id: doc_concept__safety_management__process
   :status: valid

In this section a concept for the safety management will be discussed. Inputs for this concepts are mainly the requirements of ISO26262 "Part 2: Management of functional safety"

Inputs
^^^^^^

#. Stakeholders for the safety management work products?
#. Who needs which information?
#. Which safety plans do we have?
#. Which other work products of safety management are important?
#. What tooling do we need?

Stakeholders
^^^^^^^^^^^^

#. :need:`Technical Lead <rl__technical_lead>`

   * planning of development for module and for platform projects
   * status reporting of safety activities

#. :need:`Safety Manager <rl__safety_manager>`

   * he is the main responsible for the safety management work products (as in :doc:`workproducts`).
     See also his role definition in :doc:`roles`.

#. :need:`External Auditor <rl__external_auditor>`

   * understand activities planning, processes definition and execution

#. "Distributor" (external role)

   * use the platform in a safe way
   * integrate the platform in his product (distribution) and safety case
   * plan this integration (also in time)
   * qualify the SW platform as part of his product

Safety Plans
^^^^^^^^^^^^

This SW platform project defines two levels of planning: platform and module. There will be one safety plan on platform level and several safety plans on module level (one for each module).
This is how we organize our development teams and repositories. Each of these safety plan "creates" one SEooC.
The :need:`Platform Safety Plan <doc__platform_safety_plan>` exists only once and is part of the :ref:`Platform Management Plan <pmp>` of S-CORE.

Safety Management Work Products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Apart from the safety plans the main work products of safety management are (see also the link to workflows below):

* :need:`Safety Manual <wp__platform_safety_manual>` - the safety manual defines the requirements for safe usage or integration of the SW platform (or its individual modules)
* :need:`Confirmation Reviews <wp__fdr_reports>` - on safety plan, safety package and safety analyses, according to ISO 26262 requirements
* :need:`Safety Package <wp__platform_safety_package>` - the safety package does not contain the safety argumentation. By this the S-CORE project ensures it does not take over liability for the SW platform (or its individual modules). But it enables the distributors to integrate the SW platform (or its individual modules) in their safety package.

Safety Management Tooling
^^^^^^^^^^^^^^^^^^^^^^^^^

For the safety planning and safety manual, sphinx-needs will be used for referencing.

For the activities planning (who, when) we use github issues and monitor these in github projects.

For the reporting (e.g. displaying the status of the work products) additional tooling is created (see :doc:`guidance/process_req`)

Getting started
---------------

.. doc_getstrt:: Safety Management Get Started
   :id: doc_getstrt__safety_management__process
   :status: valid


In case you are appointed as a :need:`Safety Manager <rl__safety_manager>` by the :need:`rl__project_lead` in the S-CORE project:

* Contact the :need:`Technical Lead <rl__technical_lead>` for your SEooC to establish planning and reporting (the TL should already have established a Github project for planning)
* Create your safety plan according to :need:`wf__cr_mt_safety_plan`
* Make familiar with your role description and the other workflows of safety management (see below)
* Make familiar with the development and supporting process descriptions in :ref:`process_description` plus the relevant sections of the :ref:`Platform Management Plan <pmp>`

Workflows
---------

.. toctree::
   :maxdepth: 1
   :glob:

   roles.rst
   workproducts.rst
   workflows.rst

Guidance
--------

.. toctree::
   :maxdepth: 1
   :glob:

   guidance/index.rst

.. needextend:: "process_areas/safety_management" in docname
   :+tags: safety_mgt

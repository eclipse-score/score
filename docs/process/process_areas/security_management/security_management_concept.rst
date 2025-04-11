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

.. _process_security_management:

Concept Description
###################

.. doc_concept:: Concept Description
   :id: doc_concept__security_management_process
   :status: valid
   :tags: security_management

In this section a concept for the Security Management will be discussed. Inputs for this concepts
are mainly the requirements of ISO SAE 21434 Clause 5, 6 and 8.

The term security is used here synonymously for the term cybersecurity as defined in ISO SAE 21434.


Inputs
******

#. Stakeholders for the Security Management work products?
#. Who needs which information?
#. Which security plans do we have?
#. Which other work products of security management are important?
#. What tooling do we need?


Stakeholders for the Security Management
****************************************

#. :need:`Technical Lead <rl__technical_lead>`

   * planning of development for module and for platform projects
   * status reporting of security activities

#. :need:`Security Manager <rl__security_manager>`

   * is the main responsible for the security management work products (as in :doc:`security_management_workproducts`).
     See also his role definition in :doc:`security_management_roles`.

#. :need:`External Auditor <rl__external_auditor>`

   * understand activities planning, processes definition and execution (needs review, if we consider that)

#. "Distributor" (external role)

   * use the platform in a safe and secure way
   * integrate the platform in his product (distribution) and security package
   * plan this integration (also in time)
   * qualify the SW platform as part of his product

Standard Requirements
=====================

Also requirements of standards need to be taken into consideration:

* ISO 26262
* ASPICE
* ISO SAE 21434

Security Management Plans
*************************

This SW platform project defines two levels of planning: platform and module. There will be one security plan on platform level and several security plans on module level (one for each module).
This is how we organize our development teams and repositories. Each of these security plan "creates" one EooC.
The :need:`Platform Security Plan <doc__platform_security_plan>` exists only once and is part of the :ref:`Platform Management Plan <pmp>` of S-CORE.

Security Management Work Products
*********************************

Apart from the security plans the main work products of security management are (see also the link to workflows below):

* :need:`Security Manual <wp__platform_security_manual>` - the security manual defines the requirements for safe and secure usage or integration of the SW platform (or its individual modules)
* :need:`Reviews <wp__fdr_reports_security>` - on security plan, security package and security analyses, according to ISO SAE 21434 requirements
* :need:`Security Package <wp__platform_security_package>` - the security package does not contain the security argumentation. By this the S-CORE project ensures it does not take over liability for the SW platform (or its individual modules). But it enables the distributors to integrate the SW platform (or its individual modules) in their security package.

Security Management Tooling
***************************

For the security planning and security manual, sphinx-needs will be used for referencing.

For the activities planning (who, when) we use github issues and monitor these in github projects.

For the reporting (e.g. displaying the status of the work products) additional tooling is created (see :doc:`guidance/security_management_process_reqs`)

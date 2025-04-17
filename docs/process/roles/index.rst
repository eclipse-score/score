..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

Roles
=====

S-CORE Management Roles
-----------------------

.. role:: Project Lead
   :id: rl__project_lead
   :status: valid

   The Project Leads decide about strategy, addition of modules and election of all other roles.

   Required skills

   * Degree: Master's degree in electrical engineering/computer science/mathematics, or similar degree, or comparable work experience
   * Solid understanding of project management
   * Technical know-how of embedded systems
   * Preferred training: Basic and Management specific safety and security trainings

   Experience

   * 3 years of experience in project or line management

   Responsibility

   * Decisions about strategical topics
   * Filling the Project Lead role according to the `Eclipse Foundation Project Handbook <https://www.eclipse.org/projects/handbook>`_
   * Election of all roles in the S-CORE project, including the :need:`Safety Manager <rl__safety_manager>` on SW platform and module level

   Authority

   * Ultimate decisions on escalated topics
   * Election and replacement of all role's personnel
   * Decide on addition/removal of modules repositories or split-off of projects

.. role:: Quality Manager
   :id: rl__quality_manager
   :status: valid
   :tags: quality_management
   :contains: rl__committer

   The quality managers shall be responsible for the planning and coordination of the quality activities, i.e. the quality management.

.. role:: Security Manager
   :id: rl__security_manager
   :status: draft
   :tags: quality_management
   :contains: rl__committer

   The security managers shall be responsible for the planning and coordination of the security activities.

S-CORE process roles
--------------------

.. role:: Process Community Member
   :id: rl__process_community
   :status: valid
   :tags: process_management
   :contains: rl__committer

   The process community members are responsible for the definition of the process architecture of the project integrated management system and how they processes interact.
   The approval and release of the process is done by the safety, quality and security managers and the technical leads (for the parts which affect them).

S-CORE development roles
------------------------

.. role:: Infrastructure Tooling Community Member
   :id: rl__infrastructure_tooling_community
   :status: valid
   :tags: development
   :contains: rl__committer

   The infrastructure and tooling community members are responsible for the infrastructure and tooling setup for development namely github, bazel, sphinx-needs, but also the rest of the tool chain.

.. role:: Contributor
   :id: rl__contributor
   :status: valid

   (Eclipse) Open Source Role, person(s) who provide(s) possible contribution(s) as pull request(s) to the main line.
   Any contributor which contributes code, tests or documentation to S-CORE.

   .. note::
      Follows the processes defined by the :need:`rl__process_community`

.. role:: Committer
   :id: rl__committer
   :status: valid
   :tags: development

   (Eclipse) Open Source Role, person(s) who accept(s) possible contribution(s) as pull request(s) to the main line and maintains the product.

   .. note::
      Defines and enforces processes.

.. role:: Testing Community Member
   :id: rl__testing_community
   :status: valid
   :tags: verification
   :contains: rl__committer

   The testing community members are responsible for the test case development from component to
   platform level. They shall be included in any requirements reviews. They can also improve
   independence argumentation when involved in the development of unit testing on safety critical
   units. In this way the testing community takes a supportive role for unit testing


S-CORE cross functional teams
-----------------------------

.. role:: Platform Team
   :id: rl__platform_team
   :status: valid
   :tags: cross_functional
   :contains: rl__technical_lead, rl__safety_manager, rl__quality_manager, rl__security_manager, rl__contributor, rl__committer, rl__infrastructure_tooling_community, rl__process_community

   The platform team is responsible for all artifacts within the platform SEooC. Additionally it is also responsible for the overall process including its support by tooling.

.. role:: Module Team
   :id: rl__module_team
   :status: valid
   :tags: cross_functional
   :contains: rl__module_lead, rl__safety_manager, rl__quality_manager, rl__security_manager, rl__contributor, rl__committer

   The module team is responsible for all artifacts within the module SEooCs. Each module has only one responsible team but a team may also be responsible for several (small) modules.

S-CORE Roles list
-----------------

.. needtable::
   :style: table
   :columns: title;id;tags
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["role"]):
                results.append(need)

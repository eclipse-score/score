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

SCORE Management Roles
----------------------

.. role:: Project Lead
   :id: RL_project_lead
   :status: valid
   :security: yes
   :safety: yes
   :tags: project_management

   The Project Leads decide about strategy, addition of modules and election of all other roles.

.. role:: Technical Lead
   :id: RL_technical_lead
   :status: valid
   :security: yes
   :safety: yes
   :tags: project_management
   :contains: RL_committer

   The Technical Leads approve feature requests and perform the project management on SCORE platform level.

.. role:: Quality Manager
   :id: RL_quality_manager
   :status: valid
   :security: no
   :safety: no
   :tags: quality_management
   :contains: RL_committer

   The quality managers shall be responsible for the planning and coordination of the quality activities, i.e. the quality management.

.. role:: Security Manager
   :id: RL_security_manager
   :security: yes
   :status: draft
   :tags: quality_management
   :contains: RL_committer

   The security managers shall be responsible for the planning and coordination of the security activities.

.. role:: Module Project Lead
   :id: RL_module_lead
   :security: yes
   :safety: yes
   :status: valid
   :tags: project_management
   :contains: RL_committer

   The module Project Leads perform the project management on module level. If a module is developed in a sub-project of SCORE they have the eclipse project lead role for this.

SCORE process roles
-------------------

.. role:: Process Community Member
   :id: RL_process_community
   :status: valid
   :security: yes
   :safety: yes
   :tags: process_management
   :contains: RL_committer

   The process community members are responsible for the definition of the process architecture of the project integrated management system and how they processes interact.
   The approval and release of the process is done by the safety, quality and security managers and the technical leads (for the parts which affect them).

SCORE development roles
-----------------------

.. role:: Infrastructure Tooling Community Member
   :id: RL_infrastructure_tooling_community
   :status: valid
   :security: yes
   :safety: yes
   :tags: development
   :contains: RL_committer

   The infrastructure and tooling community members are responsible for the infrastructure and tooling setup for development namely github, bazel, sphinx-needs, but also the rest of the tool chain.

.. role:: Contributor
   :id: RL_contributor
   :status: valid

   (Eclipse) Open Source Role, person(s) who provide(s) possible contribution(s) as pull request(s) to the main line.
   Any contributor which contributes code, tests or documentation to SCORE.

   .. note::
      Follows the processes defined by the :need:`RL_process_community`

.. role:: Committer
   :id: RL_committer
   :status: valid
   :security: yes
   :safety: yes
   :tags: development

   (Eclipse) Open Source Role, person(s) who accept(s) possible contribution(s) as pull request(s) to the main line and maintains the product.

   .. note::
      Defines and enforces processes.

SCORE cross functional teams
----------------------------

.. role:: Platform Team
   :id: RL__platform_team
   :status: valid
   :security: yes
   :safety: yes
   :tags: cross_functional
   :contains: RL_technical_lead, RL_safety_manager, RL_quality_manager, RL_security_manager, RL_contributor, RL_committer, RL_infrastructure_tooling_community, RL_process_community

   The platform team is responsible for all artefacts within the platform SEooC. Additionally it is also responsible for the overall process including its support by tooling.

.. role:: Module Team
   :id: RL__module_team
   :status: valid
   :security: yes
   :safety: yes
   :tags: cross_functional
   :contains: RL_module_lead, RL_safety_manager, RL_quality_manager, RL_security_manager, RL_contributor, RL_committer

   The module team is responsible for all artefacts within the module SEooCs. Each module has only one responsible team but a team may also be responsible for several (small) modules.


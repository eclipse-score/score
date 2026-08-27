..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

Platform Handbook
=================

.. document:: Handbook
   :id: doc__platform_handbook
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__platform_handbook[version==1]
   :hide:

.. raw:: html

   <div style="visibility: hidden;height:0px;">

.. raw:: html

   </div>


.. raw:: html

   <div id="videowrapper">
      <div id="fullScreenDiv">
         <div id="score-title">
           Eclipse S-CORE
               <!--<img id="logo_center_light" class="logo" src="_static/S-CORE_Logo_RGB.svg" width="600px"/>
               <img id="logo_center_drk" class="logo" src="_static/S-CORE_Logo_white.svg" width="600px"/>-->
         </div>
      </div>
   </div>

What it is about
----------------

.. grid:: 1
   :class-container: score-grid score-grid-intro

   .. grid-item-card::

      Eclipse S-CORE was founded in September 2024 by automotive industry members with a shared goal:
      a code-first, open-source software platform for onboard ECUs that the whole industry can build on.

      Rather than each company independently developing and maintaining a software platform — at high cost
      and without direct customer value — S-CORE provides a common foundation with:

      - **A reference implementation** that catches integration issues early and prevents known bugs from reappearing across projects
      - **A Functional-Safety-compliant process** (ISO 26262) applied to all modules, making S-CORE unique among open-source automotive projects
      - **Full transparency**: process, tooling, and CI checks are open source — any stakeholder can verify the results

      **Note:** S-CORE is not a ready-to-integrate series product. It is a generic foundation for commercial distributions.
      Responsibility for ASPICE, ISO 21434 (cybersecurity), and ISO 26262 (functional safety) compliance of the final system always remains with the series project.


Getting Started
---------------

.. grid:: 3
   :gutter: 3
   :class-container: score-grid score-grid-getstarted

   .. grid-item-card::
      :link: introduction/index
      :link-type: doc
      :text-align: center

      :octicon:`book;1.5em`

      Introduction
      ^^^
      Explore the Platform Structure, Technology, Architecture Meta Model.
      Understand the Core Concepts before you start.

   .. grid-item-card::
      :link: contribute/index
      :link-type: doc
      :text-align: center

      :octicon:`code-square;1.5em`

      Contribution Guideline
      ^^^
      Follow a step-by-step guide to build and integrate your first S-CORE
      module — from source code to CI/CD and doc

   .. grid-item-card::
      :link: users_guide/index
      :link-type: doc
      :text-align: center

      :octicon:`rocket;1.5em`

      User`s Guidline
      ^^^
      Check how you can start building Applications on top of S-CORE.

Platform Architecture
---------------------


.. grid:: 1 1 4 4
   :class-container: score-grid score-grid-artifacts

   .. grid-item-card::
      :link: architecture/index
      :link-type: doc
      :text-align: center

      :octicon:`id-badge;1.5em`

      Platform Architecture
      ^^^
      Learn about the S-CORE platform architecture, its building blocks and how they interact with each other.

   .. grid-item-card::
      :link: features/index
      :link-type: doc
      :text-align: center

      :octicon:`package;1.5em`

      Platform Features and Logical Interfaces
      ^^^
      Explore the Features and their Logical Interfaces, which are the heart of the S-CORE software.


   .. grid-item-card::

      :octicon:`checklist;1.5em`

      Platform Requirements
      ^^^
      Understand the main goals of the S-CORE platform by reading the
      :ref:`Stakeholder requirements <stakeholder_requirements>` and
      :ref:`Platform Assumptions <platform_assumptions>`.

   .. grid-item-card::

      :octicon:`graph;1.5em`

      Platform Status
      ^^^
      Inform yourself about the status of the Platform ..... [tbd]


Project Structure and Processes
-------------------------------

.. grid:: 1 1 3 3
   :class-container: score-grid score-grid-processes

   .. grid-item-card::

      :octicon:`organization;1.5em`

      Platform Management
      ^^^^^^^^^^^^^^^^^^^
      Read about our project and organization structure in the
      `Project Management Plan <https://eclipse-score.github.io/score/main/platform_management_plan/project_management.html>`_.
      And learn how we deal with :ref:`Safety Plan Platform<safety_plan_platform>` or care about :ref:`Software Verification Plan <software_verification_plan>`.

   .. grid-item-card::

      :octicon:`workflow;1.5em`

      Process
      ^^^
      Check the `Main Ideas <https://eclipse-score.github.io/process_description/main/introduction/index.html>`_
      and `Concepts <https://eclipse-score.github.io/process_description/main/general_concepts/index.html>`_
      of the Process to understand the reasons behind our software development process.

   .. grid-item-card::

      :octicon:`list-unordered;1.5em`

      Process Areas
      ^^^
      Check the detailed `Documentation of every Process Area <https://eclipse-score.github.io/process_description/main/process_areas/index.html>`_,
      which contains requirements, guidances, workflows and a list of work products for every process.

Reference Integration
---------------------

.. grid:: 1 1 3 3
   :class-container: score-grid score-grid-refintegration

   .. grid-item-card::

      :octicon:`iterations;1.5em`

      Reference Integration Process
      ^^^
      Follow the `Integration Process <https://eclipse-score.github.io/reference_integration/main/integration_process/integration_process.html>`_
      to understand how Platform Modules are integrated together.

   .. grid-item-card::
      :link: https://eclipse-score.github.io/reference_integration/main/s_core_v_1/releases/releases.html
      :link-type: url

      :octicon:`package-dependents;1.5em`

      Reference Releases
      ^^^
      Browse the `release notes <https://eclipse-score.github.io/reference_integration/main/s_core_v_1/releases/releases.html>`_
      and see the current state of the platform.

   .. grid-item-card::

      :octicon:`pivot-column;1.5em`

      Integration Status
      ^^^
      Consult the `cross-repo metrics report <https://eclipse-score.github.io/.github/>`_
      and the `integration status <https://eclipse-score.github.io/reference_integration/main/status_dashboard.html>`_
      for details.


Infrastructure and Tooling
--------------------------

.. grid:: 1 1 3 3
   :class-container: score-grid score-grid-infratooling

   .. grid-item-card::
      :link: https://eclipse-score.github.io/infrastructure/dev/index.html
      :link-type: url

      :octicon:`gear;1.5em`

      Infrastructure Landscape
      ^^^
      Get to know the S-CORE tool stack, testing and CI infrastructure.
      Read the
      `infra & tooling docs <https://eclipse-score.github.io/infrastructure/dev/index.html>`_.

   .. grid-item-card::

      :octicon:`tools;1.5em`

      Toolchains
      ^^^
      S-CORE provides hermetic Bazel toolchains for building its modules.
      Explore the `C++ toolchains <https://github.com/eclipse-score/bazel_cpp_toolchains>`_
      and the `Rust toolchains <https://github.com/eclipse-score/toolchains_rust>`_ used across the platform.

   .. grid-item-card::
      :link: https://eclipse-score.github.io/infrastructure/dev/explanation/index.html
      :link-type: url

      :octicon:`graph;1.5em`

      Infrastructure Status
      ^^^
      Get insights into the current state of the S-CORE tooling and infrastructure.
      Check the status `overview <https://eclipse-score.github.io/infrastructure/dev/explanation/index.html>`_
      to see how the build and CI components are set up and maintained.


.. raw:: html

   <div style="border-top:2px solid #888;margin:2.5rem 0 2rem 0;"></div>

.. grid:: 1 1 3 3
   :class-container: score-sitemap

   .. grid-item::

      **Documentation**

      | :doc:`features/index`
      | :doc:`requirements/index`
      | :doc:`modules/index`
      | :doc:`score_releases/index`

   .. grid-item::

      **Project**

      | :doc:`score_tools/index`
      | :doc:`safety/index`
      | :doc:`design_decisions/index`
      | :doc:`platform_management_plan/index`
      | `Feature Requests <https://github.com/orgs/eclipse-score/projects/4>`_

   .. grid-item::

      **Community**

      | :doc:`contribute/index`
      | `Eclipse Project <https://projects.eclipse.org/projects/automotive.score>`_
      | `GitHub <https://github.com/eclipse-score/score>`_
      | `Mailing List <https://accounts.eclipse.org/mailing-list/score-dev>`_

.. toctree::
   :maxdepth: 1
   :hidden:

   introduction/index
   contribute/index
   architecture/index
   features/index
   users_guide/index
   requirements/index

   score_releases/index
   quality/qms_report

   score_tools/index
   platform_management_plan/index
   safety/index
   design_decisions/index
   modules/index

   Eclipse <https://projects.eclipse.org/projects/automotive.score>



.. raw:: html

   <style>.prev-next-footer { display: none !important; }</style>

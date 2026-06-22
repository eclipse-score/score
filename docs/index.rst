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

S-CORE Platform Documentation
=============================

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

Introduction
------------

Eclipse S-CORE was founded in September 2024 by automotive industry members with a shared goal:
a code-first, open-source software platform for onboard ECUs that the whole industry can build on.

Rather than each company independently developing and maintaining a software platform — at high cost
and without direct customer value — S-CORE provides a common foundation with:

- **A reference implementation** that catches integration issues early and prevents known bugs from reappearing across projects.
- **A Functional-Safety-compliant process** (ISO 26262) applied to all modules, making S-CORE unique among open-source automotive projects.
- **Full transparency**: process, tooling, and CI checks are open source — any stakeholder can verify the results.

**Note:** S-CORE is not a ready-to-integrate series product. It is a generic foundation for commercial distributions.
Responsibility for ASPICE, ISO 21434 (cybersecurity), and ISO 26262 (functional safety) compliance of the final system always remains with the series project.


Get started with S-CORE
-----------------------

.. grid:: 3
   :gutter: 3
   :class-container: score-grid

   .. grid-item-card::
      :link: users_guide/project_basics/index
      :link-type: doc
      :text-align: center

      :octicon:`book;3em`

      Overview
      ^^^
      Explore the S-CORE platform structure, technology stack and software
      architecture. Understand the core concepts before you start building.

   .. grid-item-card::
      :link: users_guide/building_simple_application/index
      :link-type: doc
      :text-align: center

      :octicon:`code-square;3em`

      Contribute own module
      ^^^
      Follow a step-by-step guide to build and integrate your first S-CORE
      module — from source code to CI/CD and doc

   .. grid-item-card::
      :link: users_guide/whats_next/index
      :link-type: doc
      :text-align: center

      :octicon:`rocket;3em`

      What's next?
      ^^^
      Check how you can start being productive immediately

Software artifacts
------------------

.. grid:: 1 1 3 3
   :class-container: score-grid

   .. grid-item-card::

      :octicon:`checklist;3em`

      Requirements
      ^^^
      Analyze :ref:`Stakeholder <stakeholder_requirements>` requirements for
      the work with and implementation inside S-CORE.
      Or get the complete picture on the :ref:`requirements` page.



   .. grid-item-card::

      :octicon:`package;3em`

      Features & Modules
      ^^^
      :ref:`Features <features>` and :ref:`Modules <modules>` are the heart of the S-CORE software.

   .. grid-item-card::

      :octicon:`tag;3em`

      Releases
      ^^^
      Check out our `latest release <https://eclipse-score.github.io/reference_integration/main/>`_
      or explore our `release roadmap <https://eclipse-score.github.io/reference_integration/main/_collections/score_platform/docs/score_releases/index.html>`_.


Project structure and processes
-------------------------------

.. grid:: 1 1 3 3
   :class-container: score-grid

   .. grid-item-card::

      :octicon:`workflow;3em`

      Process
      ^^^
      Understand how we work, by reading our `Process description <https://eclipse-score.github.io/process_description/main/index.html>`_.
      And receive tips & tricks for our used tool stack by reading the
      :ref:`contribute`.

   .. grid-item-card::

      :octicon:`organization;3em`

      Platform Management Plan (PMP)
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      Read about our project and organization structure in the
      :ref:`Project Handbook <pmp>`.
      And learn how we deal with :ref:`Platform Safety Plan <score_platform_safety_plan>` or care about :ref:`Software Verification Plan <software_verification_plan>`.

   .. grid-item-card::
      :link: https://github.com/eclipse-score/reference_integration
      :link-type: url
      :text-align: center

      :octicon:`repo;3em`

      Reference Integration
      ^^^^^^^^^^^^^^^^^^^^^
      Explore the S-CORE reference integration — a continuously built and tested
      assembly of all platform modules, serving as the authoritative integration baseline.

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

   users_guide/index
   features/index
   requirements/index
   modules/index
   contribute/index

   Releases <score_releases/index.rst>
   Tools <score_tools/index.rst>
   PMP <platform_management_plan/index.rst>
   Safety <safety/index>
   Eclipse <https://projects.eclipse.org/projects/automotive.score>
   design_decisions/index

.. toctree::
   :maxdepth: 1
   :hidden:

   introduction/index
   users_guide/index

.. raw:: html

   <style>.prev-next-footer { display: none !important; }</style>

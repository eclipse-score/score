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

.. toctree::
   :hidden:

   project_basics/index.rst
   building_simple_application/index.rst
   whats_next/index.rst

.. document:: Handbook
   :id: doc__platform_handbook
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__platform_handbook
   :hide:

Welcome to S-CORE
=================
Introduction
------------


The Eclipse S-CORE project is evolving rapidly. With the launch of our first release, "Eclipse S-CORE 0.5",
we are providing this tutorial to explain how the project works from a technical perspective.
Because S-CORE follows an iterative, code-centric development model, this description is updated continuously
and may not always reflect the latest state. Contributions from the community are therefore welcome.


Get started with S-CORE
~~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 3
   :gutter: 3
   :class-container: score-grid

   .. grid-item-card:: Overview
      :link: project_basics/index
      :link-type: doc
      :text-align: center

      Explore the S-CORE platform structure, technology stack and software
      architecture. Understand the core concepts before you start building.

   .. grid-item-card:: Contribute own module
      :link: building_simple_application/index
      :link-type: doc
      :text-align: center

      Learn how to contribute your own application or module to the
      Eclipse S-CORE platform following the project process.

   .. grid-item-card:: What's next?
      :link: whats_next/index
      :link-type: doc
      :text-align: center

      Learn how to become an official contributor and how to get productive.

Background of Eclipse S-CORE
------------------------------

Eclipse S-CORE was founded in September 2024 by automotive industry members with a shared goal:
a code-first, open-source software platform for onboard ECUs that the whole industry can build on.

Rather than each company independently developing and maintaining a software platform — at high cost
and without direct customer value — S-CORE provides a common foundation with:

- **A reference implementation** that catches integration issues early and prevents known bugs from reappearing across projects.
- **A Functional-Safety-compliant process** (ISO 26262) applied to all modules, making S-CORE unique among open-source automotive projects.
- **Full transparency**: process, tooling, and CI checks are open source — any stakeholder can verify the results.

**Note:** S-CORE is not a ready-to-integrate series product. It is a generic foundation for commercial distributions.
Responsibility for ASPICE, ISO 21434 (cybersecurity), and ISO 26262 (functional safety) compliance of the final system always remains with the series project.

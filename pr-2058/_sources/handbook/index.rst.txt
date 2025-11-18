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
   own_application/index.rst
   building_simple_application/index.rst

Handbook
========

Introduction
------------


.. image:: _assets/score_image.png
   :alt: Eclipse Score
   :width: 400
   :align: center




Since Eclipse S-CORE project is continuously developing and we are now launching our first release “Eclipse S-CORE 0.5”,
we have decided to provide a tutorial which explains how the Eclipse S-CORE project technically works.
Due to rapid development process in S-CORE, this description is updated continuously and might not be up to date at any given time, so everyone is invited to contribute.

 
Background of Eclipse S-CORE
------------------------------------

Before diving in into the technical details, let´s look in the rear mirror and reflect Eclipse S-CORE´s origin and goals.
Eclipse S-CORE was founded in September 2023, inspired by the open-source idea and achievements in other industries in recent decades.
Alle founding members of S-CORE were companies from the automotive industry. They have shared the same vision,
that a code-based and open-source software platform for onboard electronic control units (ECUs) will have a positive
impact to all parties involved and will bring the automotive industry to the next level.
 
With every new generation the volume and complexity of new functions increase by far, which also impacts the complexity
and the quantity of features provided by the software platform. Developing and maintaining such platforms -separately by every automotive player- is neither
efficient nor has it a positive impact on the product quality. Furthermore, both, the invested effort and capital for software platform development have
no customer value at all. Therefore, the open-source approach seems to be a promising alternative to improve quality, to decrease the overall effort
in the industry and to speed-up the product development.
In the aftermath, an open-source software platform additionally offers a common base for cooperations among active members in future series projects.
 
Eclipse S-CORE is not the first project which addresses the above-mentioned issues.
In past, initiatives like `AUTOSAR <https://www.autosar.org/>`_ also had the idea to standardize the software platform as well as the process, methods, and tools for software platform development.
Yet Eclipse S-CORE goes beyond the standardization, and additionally addresses following goals as well:
 
- **Provide a reference implementation of the software platform**:
  As known from past experiences, a lot of issues appear for the very first time during the integration of the software stack. Other than that, some implementation aspects -e.g., performance- can hardly be specified as a requirement. By providing an open-source reference implementation,
  a high volume of these problems is solved before the development of related series projects has even begun.
  By using the same implementation in every related future series project, already solved issues won´t appear in later stages.

- **Quality assurance** + relevant software development process (usually in focus during the integration phase, especially in ASIL relevant systems):
  Code quality, solid requirements/ architecture, and complete test coverage, are some of the aspects of quality assurance.
  These aspects have to be addressed, in order to use the software platform for future industrialization in series products.
  In order to address them, the Eclipse S-CORE project (1) defines an ASIL conform software development process, and (2) ensures,
  that all S-CORE module implementations follow this process. This is btw. Eclipse S-CORE´s USP among traditional open-source projects,
  which mainly focus on pure coding/ implementation of the software platform.

  The clear goal of S-CORE is to specify only those parts of software development process, which potentially can be validated with automated checks.
 
At the end, it´s important to understand, that **Eclipse S-CORE does not provide a final product** which can be integrated **“out-of-the-box”** into an automotive series project.
Here are some reasons for this:

- Since Eclipse S-CORE is an open-source project, there is **no commercial company which is liable** for any result provided.
- All Eclipse S-CORE´s **work products are generic**, in order to enable their **reuse as basis for multiple commercial distributions** depending on specific project needs.

The strength of the Eclipse S-CORE project is that both, the software development process, and the corresponding tooling which ensures fulfillment of these processes
are open-source (e.g., automated checks and test execution in CI). So, every party involved can check, whether it does what it´s supposed to do.
Therefore, if Eclipse S-CORE is used as basis in series projects, all work products can be reused.
The open-source community is also committed to maintain the work products in future, but 
the **responsibility for** assurance of **quality (ASPICE), security (ISO21434) and safety (ISO26262) of the target system remains within the series project**.

The maintainers of the Eclipse S-CORE project strongly believe, that in near future further automotive companies will understand the benefits,
will join the Eclipse S-CORE project and will use Eclipse S-CORE their in series projects.
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

Module Structure Overview
==========================

.. toctree::
   :maxdepth: 1
   :glob:

As already stated in chapter :ref:`Technology Overview <technology_overview>`,
Eclipse S-CORE project consists of multiple bazel modules, usually located in separate repositories.
Vast majority of Eclipse S-CORE modules are part of `Eclipse S-CORE GitHub organization <https://github.com/eclipse-score>`_,
yet some are placed externally, e.g., reused modules from other eclipse projects.
Here, we will have a closer look at most important bazel modules and repositories in Eclipse S-CORE GitHub organization.


.. image:: ../_assets/module_deps.svg
   :alt: module deps
   :align: center


Eclipse S-CORE Platform
-----------------------
GitHub Link: https://github.com/eclipse-score/score

The Eclipse S-CORE module is the central part of the Eclipse S-CORE project,
where the software architecture is defined. Here you will find the list and explanation of the stakeholder requirements,
AoUs for the platforms for the potential users, features provided by the Eclipse S-CORE platform,
definition of high-level architecture, breakdown of the high-level architecture to the modules as well as the definition
of the functionality (logical interfaces) for every module.


Process Description
--------------------
GitHub Link: https://github.com/eclipse-score/process_description

.. hint::
    We automatically generate for every repository html documentation from rst files.
    You can easily open it as shown at the picture below.

.. image:: ../_assets/generated_doc_in_score_github.png
   :alt: Generated Doc in GitHub
   :width: 500
   :align: center

The process repository describes the Eclipse S-CORE process. It defines both general concepts and ideas
of the Eclipse S-CORE software development process approach and also gives a detailed description of every process area,
as shown in the image below. It´s recommended to be familiar with this description, since it includes a comprehensible
guidance how S-CORE´s work products are specified, requirements, and architecture for instance.

.. image:: ../_assets/process_areas.png
   :alt: Process areas
   :width: 500
   :align: center


Doc-as-Code
-----------
GitHub Link: https://github.com/eclipse-score/docs-as-code

Doc-as-code repository implements the additional tooling around sphinx and sphinx-needs framework including
traceability, linkage of the tests, requirements, and architecture.
Additionally, doc-as-code repository implements all checks on the Eclipse S-CORE metamodel,
which were defined in the process description repository. The current implementation status of tooling requirements
can be checked in `Tool Requirements Overview <https://eclipse-score.github.io/docs-as-code/main/requirements/requirements.html>`_.


Tooling
-------
GitHub Link: https://github.com/eclipse-score/tooling

Tooling repository collects all supporting tools, that are needed in the Eclipse S-CORE project, e.g., format_checker.


Toolchains and bazel platform
----------------------------------
GitHub Link: https://github.com/eclipse-score/toolchains_qnx, https://github.com/eclipse-score/toolchains_gcc, https://github.com/eclipse-score/toolchains_rust

There is a number of repos, which define toolchains (gcc/qnx/rust) including compiler and linker flags,
which are used to compile Eclipse S-CORE software. Furthermore, there is also a repository called “bazel platforms”,
which defines various platforms that are supported by Eclipse S-CORE,
e.g., x86_64-qnx as can be seen in the following `BUILD  <https://github.com/eclipse-score/bazel_platforms/blob/main/BUILD>`_ file.


Bazel Registry
---------------
GitHub Link: https://github.com/eclipse-score/bazel_registry

Bazel registry is one of the most important repositories.
This is the place where official releases of all Eclipse S-CORE bazel modules are
announced in order to enable mutual referencing among modules.


Software Modules
----------------
GitHub Link (e.g. for baselibs): https://github.com/eclipse-score/baselibs

As already mentioned, every software module, a collection of software components,
is also a bazel module located in a separate repository. Software modules usually contain following information:

- component requirements and architecture, detailed design
- implementation
- unit- and component tests
- documentation

Software modules usually depend on other modules in the Eclipse S-CORE GitHub organization, especially on

- https://github.com/eclipse-score module to reference feature requirements and feature architecture in the component requirements and architecture
- https://github.com/eclipse-score/docs-as-code module for sphinx/sphinx-needs framework and tooling around it
- **toolchains** modules for the compiler toolchains.


Reference Integration
----------------------
GitHub Link: https://github.com/eclipse-score/reference_integration

Reference integration repository is one of the most important repositories in the Eclipse S-CORE project,
since this is the location, where all things come together. Here we integrate all Eclipse S-CORE modules
together and ensure, that they match to each other. We do this by integrating all software modules to a
reference image(s), qnx x86 image for instance. On this image we are executing multiple feature integration tests,
which ensure consistency of the dependencies between the software modules and correct implementation
of the feature requirements.


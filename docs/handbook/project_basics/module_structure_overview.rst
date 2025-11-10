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

As it was already stated in the :ref:`Technology Overview <technology_overview>` chapter, Eclipse S-CORE project consists of multiple
bazel modules, normally located in separate repositories. Majority of Eclipse S-CORE modules are part of
`Eclipse S-CORE GitHub organization <https://github.com/eclipse-score>`_ , but some of the modules can be also located
externally, e.g. if we reference an existing module from another eclipse project.


Let us have a look at the most important bazel modules and repositories in Eclipse S-CORE GitHub organization.

.. image:: ../_assets/module_deps.svg
   :alt: module deps
   :align: center

Eclipse S-CORE Platform
-----------------------
GitHub Link: https://github.com/eclipse-score/score

Eclipse S-CORE module is the central part of the Eclipse S-CORE project, where the software architecture is defined. Here you will find the list and explanation of the 
stakeholder requirements, AoUs for the platforms for the potential users, features, that are provided by the Eclipse S-CORE platform,
definition of the high level architecture, break down of the high level architecture to the modules
and the definition of the functionality (logical interfaces) for every module.

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

The process repository describes the Eclipse S-CORE process. It defines both general concepts and ideas of the Eclipse S-CORE software development process approach and
also gives a detailed description of every process area, as shown in the image below. That's definitely worth of checking, as description of process
areas has concrete guidance's e.g. how to specify requirements or architecture.

.. image:: ../_assets/process_areas.png
   :alt: Process areas
   :width: 500
   :align: center


Doc-as-Code
-----------
GitHub Link: https://github.com/eclipse-score/docs-as-code

Doc-as-code repository implements the additional tooling around sphinx and spinx-needs framework including traceability, linkage of the tests, requirements and architecture.
Additionally, doc-as-code repository implements all additional checks on the Eclipse S-CORE metamodel, that were defined in the process_description repository.
The current implementation status of tooling requirements can be checked in
`Tool Requirements Overview <https://eclipse-score.github.io/docs-as-code/main/requirements/requirements.html>`_


Tooling
-------
GitHub Link: https://github.com/eclipse-score/tooling

Tooling repository collects all the supporting tools, that are needed in the Eclipse S-CORE project, e.g. format_checker.


Toolchains and bazel platform
----------------------------------
GitHub Link: https://github.com/eclipse-score/toolchains_qnx, https://github.com/eclipse-score/toolchains_gcc, https://github.com/eclipse-score/toolchains_rust

There are a number of repos, that are defining toolchains (gcc/qnx/rust) including compiper and linker flags, that are used to compile Eclipse S-CORE software.
Additionally, there is also a repository called bazel platforms, that defines various platforms that are supported by Eclipse S-CORE, e.g. x86_64-qnx,
as can be seen in the following `BUILD  <https://github.com/eclipse-score/bazel_platforms/blob/main/BUILD>`_ file.


Bazel Registry
---------------
GitHub Link: https://github.com/eclipse-score/bazel_registry

Bazel registry is one of the most important repositories. This is the place where official releases of all Eclipse S-CORE bazel modules are announced,
so that they can be referenced between each other.

Software Modules
-------
GitHub Link (e.g. for baselibs): https://github.com/eclipse-score/baselibs

As already described, every software module, a collection of software components, is also a bazel module located in a separate repository.
Software module normally contains following information:

- component requirements and architecture, detailed design
- implementation
- unit- and component tests
- documentation

Software module normally depends on other modules in the Eclipse S-CORE GitHub organization, especially on

- https://github.com/eclipse-score module to reference feature requirements and feature architecture in the component requirements and architecture
- https://github.com/eclipse-score/docs-as-code module for sphinx/sphinx-needs framework and tooling around it
- **toolchains** modules for the compiler toolchains.

Reference Integration
----------------------
GitHub Link: https://github.com/eclipse-score/reference_integration

Reference integration repository is one of the most important repositories in the Eclipse S-CORE project, as this is the place,
where all the things come together. Here we integrate all Eclipse S-CORE modules together and ensure, that they match to each other.
We do it by integrating all the software modules to an reference image(s), e.g. qnx x86 image, and executing multiple feature
integration tests, that ensure consistency of the dependencies between the software modules and correct implementation of the
feature requirements. 



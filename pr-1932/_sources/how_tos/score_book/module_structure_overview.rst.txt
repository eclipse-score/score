Module Structure Overview
==========================

As it was already stated in the "Overview of the technologies" part, S-Core project consists of multiple
bazel modules, normally located in separate repositories. Majority of S-Core modules are part of S-Core
GitHub organization (https://github.com/eclipse-score/), but some of the modules can be also located
externally, e.g. if we reference an existing module from another Eclipse project.


Let us have a look at the most important bazel modules and repositories in S-Core GitHub organization.

s-core
-------
GitHub Link: https://github.com/eclipse-score

S-Core module is the central part of the s-core project, where the software architecture is defined. Here you will find the list and explanation of the features,
that are provided by the S-Core platform, definition of the high level architecture, break down of the high level architecture to the modules
and the definition of the functionality (logical interfaces) for every module.

TODO: image here

process_description
---------------------
GitHub Link: https://github.com/eclipse-score

.. hint::
    We automatically generate for every repository html documentation from rst files.
    You can easily open it as shown at the picture (TODO: Link)

The process repository defines the S-Core process. It defines both general concepts and ideas of the S-Core software development process approach and
also gives a detailed description of every process area (TODO: here image with process areas). That's definitely worth of checking, as description of process
areas has concrete guidances e.g. for specyfiying of requirements and architecture.

doc-as-code
-----------
GitHub Link: https://github.com/eclipse-score/docs-as-code

Doc-as-code repository implements the additional tooling around sphinx and spinx-needs framework including traceability, linkage of the tests, requirements and architecture.
Additionally, doc-as-code repository implements all additional checks on the S-Core metamodel, that were defined in the process_description repository. The current status can
be monitored here (Link/Life image https://eclipse-score.github.io/docs-as-code/main/requirements/requirements.html)


tooling
-------
GitHub Link: https://github.com/eclipse-score/tooling

Tooling repository collects all the supporting tools, that are needed in the s-core project, e.g. format_checker.


toolchains and bazel platform
----------------------------------
GitHub Link (for QNX): https://github.com/eclipse-score/toolchains_qnx

There are a number of repos, that are defining toolchains (gcc/qnx/rust) including compiper and linker flags, that are used to compile s-core software.
Additionally, there is also a repository called bazel platforms (Link: https://github.com/eclipse-score/bazel_platforms/blob/main/BUILD), that defines
various platforms that are supported by s-core, e.g. arm64-qnx.

bazel_registry
---------------
GitHub Link: https://github.com/eclipse-score/bazel_registry

Bazel registry is one of the most important repositories. This is the place where official releases of all S-Core bazel modules are announced,
so that they can be referenced between each other.

modules
-------
GitHub Link (for baselibs): https://github.com/eclipse-score/baselibs

As already described, every software module, a collection of software components, is also a bazel module located in a separate repository.
Software module normally contains following information:

- component requirements and architecture, detailed design
- implementation
- unit- and component tests
- documentation

Software module normally depends on other modules in the S-Core GitHub organization, espeicially on

- *s-core* module to reference feature requirements and feature architecture in the component requirements and architecture
- doc-as-code module for sphinx/sphinx-needs framework and tooling around it
- toolchains_* modules for the compiler toolchains.

reference integration
----------------------
GitHub Link: https://github.com/eclipse-score/reference_integration

Reference integration repository is one of the most important repositories in the s-core project, as this is the place,
where all the things come together. Here we integrate all s-core modules together and ensure, that they match to each other.
We do it by integrating all the software modules to an reference image(s), e.g. qnx x86 image, and executing multiple feature
integration tests, that ensure consistency of the dependencies between the software modules and correct implementation of the
feature requirements. 



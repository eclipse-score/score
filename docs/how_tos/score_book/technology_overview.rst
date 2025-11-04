Overview of technologies
===========================

.. _technology_overview:

.. image:: _assets/score_tooling.svg
   :alt: Score tooling
   :align: center

Bazel and repo structure
-------------------------

Before we start with technical details, it is important to understand, which main technologies and tools are used in Eclipse S-CORE project.

We think, we would not lie if we would say, that the whole Eclipse S-CORE project is built up upon `bazel <https://bazel.build/>`_ build system.
Bazel is at the very heart of the Eclipse S-CORE project. Every dependency and almost every automatization that we implement with exception to CI/CD
pipeline is done via bazel.
Validation of requirements, generation of documentation, building source code, execution of unit- or integration tests, for everything
there is a bazel target in Eclipse S-CORE. Not going into very technical details, bazel is a modern build system, that allows hermetical and
reproduciable builds, that are for special importance for building safety systems, and additionally provides the possibility to extend
its functionality for project related use-cases using `bazel macros <https://bazel.build/extending/macros>`_ and
`bazel rules <https://bazel.build/extending/rules>`_. 

Additionally, we use a concept of `bazel modules <https://bazel.build/external/module>`_. In general, Eclipse S-CORE project is built up of multiple repos, every repo implementing its
own functionality. There were quite some discussions on whether we should have a mono repository or should we split our project in
multiple repositores, as you can see here (TODO: link to decision record). At the end, the decision was taken to proceed with multiple repositories.
The main reason for this, is that Eclipse S-CORE project should not only motivate software developers to work together on new solutions inside of Eclipse S-CORE
project but also empower to reuse as much as possible from already existing projects and this is easier to do with an approach, where every functionality
is encapsualted in its own repository. Such an approach has also disadvantages. First, the organizatorical approach of having so many teams working together.
How this is done, is described the `project management plan <https://eclipse-score.github.io/score/main/platform_management_plan/project_management.html>`_.
Second, the technical approach of integrating things together and managing the dependencies between different
modules and components. Our approach for integration is desribed in :ref:`integration process <integration_process>` in more details. But in general, this is where bazel modules play a very important role,
providing how to manage and handle dependencies between multiple modules and providing a mechanism, called `bazel registry <https://bazel.build/versions/6.1.0/build/bzlmod#registries>`_,
for publishing official versions of modules.

At then end, you can see Eclipse S-CORE as an integration project, where some of the modules are developed inside of the Eclipse S-CORE organization and some are integrated from another
projects, where the main responsibility of Eclipse S-CORE as integration project is to ensure, that all modules work seamless together and result in a platform,
that can be used as basis for safety qualifiable products. 

CI/CD pipeline
---------------

There is not much to say about this. As every modern project today, we strongly rely on GitHub infrastructure, e.g. by using `GitHub actions <https://docs.github.com/de/actions>`_
for automatization and implementation of CI/CD check pipeline.

.. image:: _assets/release_verification.png
   :alt: release_verification
   :width: 400
   :align: center

Sphinx/Sphinx-needs and Documentation 
--------------------------------------
For documenting our project, for specifying requirements, assumptions of use, architecture, detailed design, tests 
and further software process related artifacts we completely rely on sphinx and sphinx-needs technology. Additionally we extend sphinx-needs
implementation with additional checks to ensure traciability and compliance to the Eclipse S-CORE metamodel. The Eclipse S-CORE metamodel & traceability concept
are described in the `process description <https://eclipse-score.github.io/process_description/main/general_concepts/index.html>`_
and guidances how to use sphinx/sphinx-needs framework in Eclipse S-CORE can be found in
`docs-as-code how-to documentaion <https://eclipse-score.github.io/docs-as-code/main/how-to/index.html>`_.
(ToDo: is there a better documetation)



Programming languages
------------------------
We heavily use python for any automation.

The target code is mainly implemented in C++. We think, that in the future C++ will be, at least partially, replaced by Rust, therefore
we already try to do the steps in this direction and provide implementation of some of the components in Rust. But as Rust support and acceptance
of the Rust programming language for the series production in the automotive world has not reached the decisive point yet, we mainly
focus on the C/C++ implementation. 


Testing
--------
In general, we differentiate between three testing levels: unit-testing, component testing and feature integration testing.

Unit-test framework strongly depends on the used programming languages, e.g. in case of C++ we rely on gtest/gmock.

Our solution for the compontent testing framework can be found in the `testing tools repo <https://github.com/eclipse-score/testing_tools>`_

For feature integration testing we use a framework called ITF (Integration Testing Framework). It is part of the Eclipse S-CORE project as well,
you can checkt its documentaion in the `README.md file <https://github.com/eclipse-score/itf>`_.

For detailed overview, please check the documetation of our `verification concept <https://eclipse-score.github.io/process_description/main/process_areas/verification/index.html#>`_

(ToDo: double check with Piotr)
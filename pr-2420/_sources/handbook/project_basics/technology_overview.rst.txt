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

Overview of technologies
===========================

.. toctree::
   :maxdepth: 1
   :glob:

.. _technology_overview:

S-CORE Tooling
----------------
Eclipse S-CORE uses a fully open-source toolchain. This ensures a smooth onboarding
experience and enables efficient collaboration across contributors with different backgrounds.
The following sections give an overview of the key technologies, followed by detailed explanations
of each tool and process step.

.. image:: ../_assets/score_tooling.svg
   :alt: Score tooling
   :align: center


Bazel and repo structure
-------------------------
The whole Eclipse S-CORE project is built on the `bazel <https://bazel.build/>`_ build system.
Almost all automated steps – such as requirement validation, documentation generation,
sourcecode compilation, unit execution, and integration tests – are executed through Bazel targets.
The CI/CD pipeline is the only major exception. 

Bazel provides **hermetic** and **reproducible** builds,
which are important for software developed for Functional Safety.
Bazel can be extended using
`bazel macros <https://bazel.build/extending/macros>`_ and
`bazel rules <https://bazel.build/extending/rules>`_, allowing project-specific build logic.

S-CORE also makes strong use of `bazel modules <https://bazel.build/external/module>`_.
The project consists of multiple repositories,
each implementing a specific piece of functionality. The modular approach improves reuse because
independent modules can be integrated into different projects more easily than a single monolithic repository. 

However, modularity introduces organizational and technical challenges: 

- Each module is maintained by a dedicated team, which increases coordination needs.
  Please have a look on the `project management plan <https://eclipse-score.github.io/score/main/platform_management_plan/project_management.html>`_
  for more details regarding S-CORE´s organizational structure. 

Technical integration and dependency management require clear processes.
Eclipse S-CORE´s approach for technical integration is described in the :ref:`integration process <integration_process>`.

- However, a basic support for handling dependencies among bazel modules is provided by the build system.
  For publishing of official modules versions, a mechanism called `bazel registry <https://bazel.build/versions/6.1.0/build/bzlmod#registries>`_
  is used.

In summary, **Eclipse S-CORE acts as an integration project,
combining modules** from other projects with **new modules** specifically developed for Eclipse S-CORE.
The main responsibility is to ensure that all modules work seamlessly together and form
a platform that can serve as the basis for future Functional-Safety- qualifiable products.


CI/CD pipeline
---------------
The CI/CD pipeline follows modern industry practices.
It is based on GitHub infrastructure and uses `GitHub actions <https://docs.github.com/de/actions>`_
for automation and for executing all CI/CD checks.

.. image:: ../_assets/release_verification.png
   :alt: release_verification
   :width: 400
   :align: center


Sphinx/Sphinx-needs and Documentation 
--------------------------------------
Eclipse S-CORE uses **Sphinx** and **sphinx-needs** for documentation, including:

- project documentation
- requirements
- assumptions of use
- architecture descriptions
- detailed designs
- test specifications
- other process-related artefacts

Eclipse S-CORE **extends** sphinx-needs implementation with additional checks **to ensure traceability
and compliance** with the Eclipse S-CORE metamodel.
The Eclipse S-CORE metamodel and -traceability concepts are documented in the
`process description <https://eclipse-score.github.io/process_description/main/general_concepts/index.html>`_.
Guidance on how to use Sphinx and sphinx-needs framework within Eclipse S-CORE is available
in the `docs-as-code how-to documentation <https://eclipse-score.github.io/docs-as-code/main/how-to/index.html>`_.


Programming languages
------------------------
Different programming languages are used in Eclipse S-CORE depending on the purpose:

- **Python**: automation and tooling
- **C++**: primary language for target code
- **Rust**: currently introduced for selected components;
  long-term adoption depends on acceptance in automotive series projects
- **C**: still used where required for compatibility

Although Rust adoption is increasing,
C/C++ remain the main languages due to their current maturity and industry acceptance.


Testing
--------
S-CORE distinguishes between **three test levels: “unit-testing”,
“component testing”** and **“feature integration testing”**. 

1. **Unit testing**
 
   - Depends on used programming languages, e.g., in case of C++ we rely on **“gtest/gmock”**. 

2. **Component testing**
 
   - Framework and documentation are available in the `testing tools repo <https://github.com/eclipse-score/testing_tools>`_. 

3. **Feature integration testing** 

   - Conducted using the framework **“ITF”** (Integration Testing Framework),
     which is part of the Eclipse S-CORE project. 
   - Documentation is available in the `README.md file <https://github.com/eclipse-score/itf>`_.

For more details, refer to our `verification concept <https://eclipse-score.github.io/process_description/main/process_areas/verification/index.html#>`_.

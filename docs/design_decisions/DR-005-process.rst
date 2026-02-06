..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
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

.. _decision_record_feature_as_independent_delivery:

DR-005-process: Feature as Independent Delivery Product
=======================================================

.. dec_rec:: Feature as Independent Delivery Product
   :id: dec_rec__platform__feature_delivery
   :status: proposed
   :Context: TBD
   :Decision: TBD

   Consequences: TBD

Context
-------

With S-CORE, we are jointly developing an open software platform with the goal of reducing complexity,
promoting reuse, gaining speed and enabling scalable innovations.

From today's perspective, the S-CORE platform will not be able to replace the software platforms
currently used in OEM projects in a single step. For this reason,
S-CORE must support the replacement of parts of the currently used software platforms with S-CORE platform parts.

Currently, there are two elements in S-CORE for the decomposition of the platform:
  - Features
  - Components

The platform consists of features. A feature is realized by a number of components.

Furthermore, S-CORE provides for two types of delivery products:
  - Platform Release
  - Software Module Release

These can be used by OEM projects.
Both delivery types are also a Safety Element out of Context (SEooC), making them easier to integrate.

A software module is defined as a component or a set of components.
A software module is contained in a repository.

Features and their artifacts are currently contained in the platform repository.
As a result, they can only be delivered with the platform release.

The goal is to be able to deliver features independently of the platform release.
For this, the Decision Record proposes that the software module also contains the feature artifacts.

The software module that contains the feature artifacts is responsible for fulfilling the feature requirements.
Even though not all S-CORE components required for the feature are located in this SW module (repository).

In section `Alternatives Considered`_, different alternatives are presented.
the current solution is compared with the alternative and evaluated with respect to the following aspects:

  - Independence of Release / Topic Coherence
  - SEooC for Features
  - Reusability across Platforms
  - Maintainability
  - Number of Repositories
  - Traceability

Decision
--------

Feature artifacts will be stored in the SW module repo.

Comparing the alternatives based on the criteria in the decision table
below (see `Justification for the Decision`_) shows that Alternative 2b
(Dedicated Feature Repository with Sub-Features) offers the most advantages.
This alternative enables a clear separation and independence of features,
supports SEooC at the feature level, and promotes reusability across
different platforms. Sub-features should be used very sparingly to avoid
unnecessarily increasing complexity.

Consequences
------------

- Process update
- Moving the feature artifacts to feature repos
- Adaptation of the traceability direction from "satisfies" to "satisfied by" between:
   - Stakeholder Requirement and Feature Requirement
   - Platform Architecture and Feature

Alternatives Considered
-----------------------

Alternative 1: Status Quo - Platform-Centric Feature Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The platform artifacts and the feature artifacts are contained in the S-CORE platform repository.
The component artifacts are contained in the module repository.
This is the current status.

.. uml:: _assets/DR-005-alternative_1_simplified.puml
   :caption: Alternative 1: Status Quo Architecture


Alternative 2: Feature in SW Module Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The platform artifacts are located in the S-CORE platform repository.
The feature artifacts are located in the SW module repository.

Feature artifacts are all artifacts at the feature level, such as feature requirements,
feature architecture, and feature tests.

In addition, this SW module also contains the main components of the feature
that are not to be reused independently of this feature context.
A feature can reuse components from other SW modules, such as BaseLibs.

Component artifacts are all artifacts at the component level, such as component requirements,
component architecture, and component tests.
They also include units with detailed design, source code, and unit tests.

.. uml:: _assets/DR-005-alternative_2_simplified.puml
   :caption: Alternative 2: Dedicated Feature Repository Architecture


Alternative 2b: Feature in SW Module Repository with Sub-Features (System of Systems)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This variant of Alternative 2 extends the dedicated feature repository
approach to support a System of Systems architecture. Features can be
composed of sub-features, each residing in their own repository. This
enables hierarchical composition where complex features can integrate
multiple sub-features, each maintaining its own complete set of artifacts
(requirements, architecture, tests, components, and units).

.. uml:: _assets/DR-005-alternative_2b_simplified.puml
   :caption: Alternative 2b: System of Systems Feature Repository Architecture


Alternative 2c: Dedicated Feature Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternative 2c is similar to Alternative 2,
with the key difference beingthat there is an intermediate feature repository between
the S-CORE platform repository and the SW module repositories (implementation repositories).
The feature artifacts are located in the feature repository.

This is to address the use case where two implementations exist for the same feature
and copies of the feature artifacts should be avoided.

Alternative 2c represents a solution but should be avoided because it increases complexity,
the number of repositories, and thus the maintenance effort.
Furthermore, it increases the risk that the implementations for aspects that should be the same will diverge.

.. uml:: _assets/DR-005-alternative_2c_simplified.puml
   :caption: Alternative 2c: Hierarchical Feature Repository Architecture


Visualization of Artifact Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: _assets/DR-005-artefact_overview.drawio.svg
   :align: center
   :width: 50%

   Artifact Overview - Standard Feature Structure

.. figure:: _assets/DR-005-artefact_overview_sub_feature.drawio.svg
   :align: center
   :width: 100%

   Artifact Overview - Feature with Sub-Features

.. figure:: _assets/DR-005-artefact_overview_tracebility.drawio.svg
   :align: center
   :width: 50%

   Artifact Overview - Traceability Between Artifacts



Justification for the Decision
------------------------------

.. list-table:: Decision Criteria Comparison
   :header-rows: 1
   :widths: 25 18 18 18 21

   * - Decision Criteria
     - Alternative 1: Status Quo
     - Alternative 2: Feature in SW Module Repository
     - Alternative 2b: Feature in SW Module Repository with Sub-Features
     - Alternative 2c: Dedicated Feature Repository
   * - Independence of Release / Topic Coherence (How independently can
       features be released and how well are related artifacts kept
       together?)
     - **(-)**

       Features bound to platform release cycle, split between platform
       and modules
     - **(+)**

       Complete independence, all artifacts self-contained in one place
     - **(+)**

       Full independence with modular sub-features, clear feature
       boundaries
     - **(o)**

       Partial independence, requirements/architecture separated from
       implementation
   * - SEooC for Features (How well can features be delivered as Safety
       Element out of Context?)
     - **(-)**

       Only modules can be SEooC, features are not independent units
     - **(+)**

       Complete SEooC at feature level with all artifacts
     - **(+)**

       Complete SEooC at feature level with all artifacts
     - **(o)**

       Complete SEooC at feature level with all artifacts
   * - Reusability across Platforms (How well can the feature be reused
       in different platforms?)
     - **(-)**

       Platform-specific feature descriptions
     - **(+)**

       Self-contained, portable across platforms
     - **(+)**

       Self-contained, portable across platforms + sub-feature reuse
     - **(o)**

       Self-contained, portable across platforms
   * - Maintainability (How easy is it to maintain and update the
       feature?)
     - **(o)**

       Distributed across platform and module repos
     - **(+)**

       All main artifacts in single location
     - **(o)**

       Multiple repos increase complexity
     - **(-)**

       Multiple repos increase complexity additional for feature
       requirements/architecture
   * - Number of Repositories (How many repositories are required to
       manage?)
     - **(+)**

       Minimal: Platform + Module repos
     - **(+)**

       Minimal: Platform + Feature repo
     - **(o)**

       Multiple per feature (main + sub-features)
     - **(-)**

       Multiple per feature (additional for feature
       requirements/architecture)
   * - Traceability (How well can requirements, architecture, tests, and
       code be traced?)
     - **(+)**

       Only one tracebility direction
     - **(o)**

       Different tracebility directions across repos
     - **(o)**

       Different tracebility directions across repos
     - **(o)**

       Different tracebility directions across repos


Example for Architecture work on platform level
-----------------------------------------------

Architecture work at the platform level means that decisions are made that
are relevant to the entire system. These can include coding guidelines,
safety concepts, structuring the platform or commonly used interfaces.

An example of an overarching concept is the definition of a standardized identifier for an application (APP_ID).
Each feature could define its own format, but this would result in an integrator
having to configure different formats for one application. Therefore, the
definition of APP_IDs should be done at the platform level and adopted by
the features.

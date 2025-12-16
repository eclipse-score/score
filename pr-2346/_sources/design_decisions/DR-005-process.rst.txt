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

**Current Industry Challenge**

At present, it cannot be assumed that OEMs can replace their currently
deployed middleware solutions with SCORE in a single step. Therefore, a
gradual, step-by-step replacement of existing middleware elements with
SCORE elements is necessary.

The current SCORE process only provides for modules (containing one or
more components) to be delivered as SEooC (see `Building Blocks
Metamodel <https://eclipse-score.github.io/process_description/main/general_concepts/score_building_blocks_concept.html#building-blocks-meta-model>`_).
However, it can be expected that the adoption of middleware functions
will occur at the feature level rather than at the component level.

This creates the necessity to provide features as independent SEooC
units. Furthermore, the current repository structure does not allow
features to be released independently from the platform repository.

**Resulting Use Cases**

Based on this industry challenge, two primary use cases emerge for
delivering SCORE software:

1. **Platform Delivery Use Case**: The entire SCORE platform is
   considered as a single, cohesive delivery unit. This use case is
   already covered by the reference integration and supports complete
   platform adoption.

2. **Feature Delivery Use Case**: Individual features are considered as
   independent delivery units. This use case is critical for gradual
   middleware migration but is not adequately supported in the current
   SCORE metamodel.

**Decision Problem**

The challenge is to enable features as independent delivery units that:

- Shall be delivered separately from the platform
- Shall be described consistently and self-contained
- Shall ensure compatibility with the SCORE platform
- Shall support gradual middleware migration at feature level

**Evaluation Approach**

In the following sections, alternatives to the current approach are
described and compared against each other. The evaluation criteria
include:

- Independence of Release / Topic Coherence
- SEooC for Features
- Reusability across Platforms
- Maintainability
- Number of Repositories
- Traceability

Decision
--------
<your text>

Consequences
------------

Comparing the alternatives based on the criteria in the decision table
below (see `Justification for the Decision`_) shows that Alternative 2b
(Dedicated Feature Repository with Sub-Features) offers the most advantages.
This alternative enables a clear separation and independence of features,
supports SEooC at the feature level, and promotes reusability across
different platforms. Sub-features should be used very sparingly to avoid
unnecessarily increasing complexity.

Alternatives Considered
-----------------------

Alternative 1: Status Quo - Platform-Centric Feature Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Feature descriptions reside in the respective SCORE platform repositories.
Module repositories contain the component architectures. This represents
the current state.

.. uml:: _assets/alternative_1_simplified.puml
   :caption: Alternative 1: Status Quo Architecture


Alternative 2: Dedicated Feature Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All feature artifacts are consolidated into a dedicated feature
repository. This repository contains all feature-level artifacts, such as
feature requirements, feature architecture, and feature-level tests.
Furthermore, it includes all component-level artifacts, such as component
requirements, component architecture, component tests, as well as units
with detailed design, source code, and unit tests. It provides the main
functionality or the main safety case for the feature and describes
dependencies to other functions. It is also possible to reference
sub-feature repositories.

.. uml:: _assets/alternative_2_simplified.puml
   :caption: Alternative 2: Dedicated Feature Repository Architecture


Alternative 2b: Dedicated Feature Repository with Sub-Features (System of Systems)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This variant of Alternative 2 extends the dedicated feature repository
approach to support a System of Systems architecture. Features can be
composed of sub-features, each residing in their own repository. This
enables hierarchical composition where complex features can integrate
multiple sub-features, each maintaining its own complete set of artifacts
(requirements, architecture, tests, components, and units).

.. uml:: _assets/alternative_2_sos_simplified.puml
   :caption: Alternative 2b: System of Systems Feature Repository Architecture


Alternative 2c: Hierarchical Feature Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternative 2c corresponds to Alternative 2 with the key difference that
there is an intermediate Feature Repository between the SCORE Repository
and the Implementation Repositories. This Feature Repository contains
feature-level artifacts such as feature requirements, feature architecture,
and feature-level tests. Multiple implementation repositories can then
reference these shared feature artifacts.

.. uml:: _assets/alternative_3_simplified.puml
   :caption: Alternative 2c: Hierarchical Feature Repository Architecture


Visualization of Artifact Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: _assets/artefact_overview.drawio.svg
   :align: center
   :width: 50%

   Artifact Overview - Standard Feature Structure

.. figure:: _assets/artefact_overview_sub_feature.drawio.svg
   :align: center
   :width: 100%

   Artifact Overview - Feature with Sub-Features

.. figure:: _assets/artefact_overview_tracebility.drawio.svg
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
     - Alternative 2: Dedicated Feature Repo
     - Alternative 2b: SoS Feature Repo
     - Alternative 2c: Hierarchical Feature Repo
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

An example of an overarching concept is the definition of APP_IDs. Each
feature could define its own format, but this would result in an integrator
having to configure different formats for one application. Therefore, the
definition of APP_IDs should be done at the platform level and adopted by
the features.

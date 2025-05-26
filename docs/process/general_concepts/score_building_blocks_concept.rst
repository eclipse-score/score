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

.. _general_concepts_building_blocks:

Building blocks concept
-----------------------


Building blocks meta model
++++++++++++++++++++++++++

The following figure gives an overview about the building blocks of the **S-CORE** **Platform**
(blue box, top, 2nd column). The objectives of the platform of the **S-CORE** platform include
enabling of feature integration for different use cases and domains. This includes safety-critical
applications. Thus the intention is, that the platform can be developed as a Safety
Element out of Context (**SEooC**) (green box, top, 1 column). The objectives of the platform are
expressed as concrete **Stakeholder Requirements** (blue box, top, 2nd column), which can be tested
by provided **Platform Tests** (blue box, top, 5nd column) for reference hardware platforms. The
platform consists of **Features** (yellow box, middle, 2nd column).

Further **S-CORE** provides **Software Modules** (red box, middle, 1st column), which can also be
developed as a SEooC. A Software Module is defined as a **Component** (green box, middle, 2nd column)
or a set of components realizing a Feature of the platform. In this sense a Software Module is the
highest level component in our model. A Software Module represents e.g. executable code or a library.

Components are the major building blocks of the platform. Components consists of **Units**
(grey box, bottom, 2nd column), the lowest level in our model. The represent the source code,
which implements the Unit. Units has a **Detailed Design** (grey box, middle, 3nd column), which is
also implemented by the **Source Code** (grey box, bottom, 3nd column). The Detailed Design is
verified by **Unit Tests** (grey box, middle, 5nd column).

Components are defined by **Component Requirements** (green box, middle, 3nd column) and the
**Component Architecture** (green box, middle, 4nd column). A **Component Safety Analysis**
(green box, middle, 6nd column) is required to verify the Component Architecture. Potential faults
may mitigated by updating the Component Requirements or by the **Component Assumptions of Use**
(green box, middle, 8nd column). The latter one must be considered by the user of the Component.
**Component Tests** (green box, middle, 5nd column) verify the Component requirements, and
**Component Integration Tests** (green box, middle, 7nd column) verify the Component Architecture
as well as the Integration of multiple Units to a Component.

As mentioned above a Software Module is defined as a Component or a set of components realizing a
Feature of the platform. Features consists of Components and are defined by **Feature Requirements**
(yellow box, middle, 3nd column) and the **Feature Architecture** (yellow box, middle, 4nd column).
A **Feature Safety Analysis** (yellow box, middle, 6nd column) is required to verify the Feature
Architecture. Potential faults may mitigated by updating the Feature Requirements or by the
**Feature Assumptions of Use** (yellow box, middle, 8nd column). The latter one must be considered
by the user of the Feature. **Feature Integration Tests** (yellow box, middle, 5nd column) verify
the Feature Requirements and the Feature Architecture as well as the Integration of multiple Units
to a Component.

.. figure:: _assets/score_building_blocks_meta_model.drawio.svg
  :width: 100%
  :align: center
  :alt: Building blocks overview for **S-CORE** platform

  Building blocks overview for **S-CORE** platform

.. _building_block_example:

Building blocks example
+++++++++++++++++++++++

The following figure is an example to explain the elements from the meta model. The user of the
**S-CORE** platform wants to use the feature key-value-store. For that the user must integrate
the software module "kvstorage". As this modules dependence on another module, the user must also
integrate the software module "json_al". The module "kvstorage" is built-up by the
components "kvs" and "fs", where the module "json_al" contains only one component "json_al".
The latter example is more or less a corner case.
Components may optionally built-up by other components. Software modules may also be designed
as safety element out of context (SEooC).

.. figure:: _assets/score_building_blocks_example.drawio.svg
  :width: 100%
  :align: center
  :alt: Building blocks example

  Building blocks example

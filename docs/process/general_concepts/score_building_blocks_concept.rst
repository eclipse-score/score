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

The following figure gives an overview about the building blocks of the **S-CORE** platform.
The objectives of the **S-CORE** integration platform are expressed as stakeholder requirements.
These objectives are further detailed and structured in features. Features are described
as a set of feature requirements with a corresponding feature architecture. The feature
requirements satisfies the stakeholder requirements. The technical implementation of a feature
is based on software components, which are built-up by units, the lowest element in our model.
Components are described by component requirements, a component architecture and a detailed
design.
Software modules are used to encapsulate a set of components. Software modules are more or less
container for a component or a set of components realizing a feature.

.. figure:: _assets/score_building_blocks_meta_model.svg
  :width: 100%
  :align: center
  :alt: Building blocks overview for **S-CORE** platform

  Building blocks overview for **S-CORE** platform

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

.. figure:: _assets/score_building_blocks_example.svg
  :width: 100%
  :align: center
  :alt: Building blocks example

  Building blocks example



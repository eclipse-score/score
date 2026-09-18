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

.. _features:

Platform Features and Logical Interfaces
========================================

A **Feature** is the highest-level logical entity, representing a set of interrelated components in respect of the S-CORE software platform.
It is the primary unit of the management of these components and contains the belonging feature requirements and feature architecture for them.

Each Feature is defined by a set of **Logical Interfaces** that describe the interactions between the components of the feature and
the other features of the platform. The Logical Interfaces are defined in terms of **Logical Interface Operations** that describe
the operations provided by the feature to other features and the operations required by the feature from other features.

For further explanation see the `Building blocks concept <https://eclipse-score.github.io/process_description/main/general_concepts/score_building_blocks_concept.html>`_.

The following features are defined:

.. note: toctree will be filled by bazel build system, do not edit manually

.. toctree::
   :maxdepth: 1

Feature List
------------

.. needtable::
   :style: table
   :types: feat
   :columns: id;Security;Safety;status
   :filter:  id not in ["feat__example_feature", "feat__feature_name", "feat__feature_name_example"]

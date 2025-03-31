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

.. _general_concepts_traceability:

Traceability concept
--------------------

Traceability is the key to ensure consistency between work products.
Furthermore, traceability supports impact analysis, dependency analysis, coverage determination
for requirements and verification, and tracking of implementation status.

Therefore **S-CORE** requires at least for safety-relevant work products single-requirement
granularity of traceability.

The following figures gives an overview about the traceability between different work products
on different levels and detail.

High level traceability overview
++++++++++++++++++++++++++++++++

The following figure shows the traceability between the major **S-CORE** work products on each
requirements level. Starting from top, the platform level, going down to feature, component
to the bottom the unit level. The concept is based on the classical V-model approach.

Change request are traced to all affected work products.

.. figure:: _assets/score_traceability_model_wp_overview.drawio.svg
  :width: 100%
  :name: score_wp_traceability
  :align: center
  :alt: High level traceability overview for **S-CORE** work products

  High level traceability overview for **S-CORE** work products

The next figure sets the focus on the feature level and adds the traceability from the Feature
Requirements to the Feature Architecture, Feature Safety Analysis and the Feature Assumption
of use. For convenience also the traceability to upper and lower lever requirements is shown.

.. figure:: _assets/score_traceability_model_feat_overview.drawio.svg
  :width: 100%
  :align: center
  :alt: High level traceability overview for **S-CORE** feature work products

  High level traceability overview for **S-CORE** feature work products

The next figures sets the focus on the component level and adds the traceability from the
Component Requirements to the Component Architecture, Component Safety Analysis
and the Component Assumption of use. Further the traceability to Component Assumptions of use
from external Components is included.


.. figure:: _assets/score_traceability_model_cmp_overview_1.drawio.svg
  :width: 100%
  :align: center
  :alt: High level traceability overview for **S-CORE** component work products

  High level traceability overview for **S-CORE** component work products

Component Architecture may either built-up of other components, then the traceability may in
addition also needed to their architectures.

.. figure:: _assets/score_traceability_model_cmp_overview_2.drawio.svg
  :width: 100%
  :align: center
  :alt: High level traceability overview for **S-CORE** component work products including sub-components

  High level traceability overview for **S-CORE** component work products including sub-components

Or less complex components may not require a Component Architecture, the traceability is not
required as the architecture can be skipped.

.. figure:: _assets/score_traceability_model_cmp_overview_3.drawio.svg
  :width: 100%
  :align: center
  :alt: High level traceability overview for **S-CORE** component work products including sub-components

  High level traceability overview for **S-CORE** component work products including sub-components

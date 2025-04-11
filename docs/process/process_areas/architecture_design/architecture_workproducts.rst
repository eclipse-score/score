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

.. _arch_workproducts:

Architecture Workproducts
=========================

.. workproduct:: Feature Architecture
   :id: wp__feature_arch
   :status: valid
   :complies: std_wp__iso26262__software_751

   Feature Architecture linked to Feature Requirements, i.e. interaction of components

   * Static view (Sphinx Needs) - Feature interfaces (to outside of Feature) and interfaces between own components
   * Dynamic view (UML) - Sequences of component interactions and state diagrams
   * Interface view (Sphinx Needs) - Overview of used and provided interfaces

   Technical concept on platform level.

.. workproduct:: Component Architecture
   :id: wp__component_arch
   :status: valid
   :complies: std_wp__iso26262__software_751, std_wp__isopas8926__4523

   Component Architecture linked to Component Requirements

   * Static view (Sphinx Needs) - Component interfaces (to outside of Component) and interfaces between own (sub) components
   * Dynamic view (UML) - Sequences of components interactions and components states
   * Interface view (Sphinx Needs) - Overview of used and provided interfaces

   Technical concept on component level.

.. workproduct:: Architecture Verification
   :id: wp__sw_arch_verification
   :status: valid
   :complies: std_wp__iso26262__software_754

   Depends on architecture guideline and tooling.
   May include several methods like inspection, modelling ... Which are selected in SW Verification Plan.

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

   Feature Architecture linked to Feature Requirements, i.e. interaction of components

   * Static view (Sphinx Needs) - Feature interfaces (to outside of Feature) and Interfaces between own Components
   * Dynamic view (UML) - Sequences of component interactions and state diagrams
   * Interface view (Sphinx Needs) - Overview of used and provided interfaces

   Technical concept on platform level.

.. workproduct:: Component Architecture
   :id: wp__component_arch
   :status: valid

   Component Architecture linked to Component Requirements

   * Static view (Sphinx Needs) - Component interfaces (to outside of Component) and Interfaces between own Sub-Components
   * Dynamic view (UML) - Sequences of Sub-Components interactions and Components States
   * Interface view (Sphinx Needs) - Overview of used and provided interfaces

   .. note::
      In case no sub-components exist, this can be covered by Detailed Design (in "Implementation" workproduct)

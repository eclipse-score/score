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

Guideline
#########

.. gd_guidl:: Implementation Guideline
   :id: gd_guidl__implementation
   :status: valid

This document describes the general guidances for implementation based on the concept which is defined :need:`[[title]]<doc_concept__imp__concept>`.
In the concept is a example of a Detailed Design included.

Workflow for Implementation
===========================

Detailed description which steps are need for implementation.

#. Consult which programming languages, design/coding guidelines and tools are used for Software
   development within the Software Development Plan :need:`doc__software_development_plan`.
#. Create a Detailed Design by using the template :need:`gd_temp__detailed_design`.
   In this step, the components are broken down into smaller, independent units that can be tested
   separately during the unit testing phase. The detailed design shall be so exact, that test and
   implementation can be run simultaneously.
#. Implement the source code, by using the coding guidelines :need:`doc__cpp_coding_guidelines` for C++,
   or <TBD> for Rust.
#. Create a pull request for your change.
#. Detail Design and Code Inspection is done to review the code of the software and detect errors in it.
#. Check the results of the static and dynamic code analysis (this inlcludes compiler warnings).
#. Fix or justify the errors.
#. Merge the pull request.
#. Create a follow up ticket if not all findings could be fixed.


Traceability
============

The detailed design is created by using the template :need:`gd_temp__detailed_design`. In the template
the static and the dynamic view for unit interactions is described.

.. figure:: _assets/static_view.drawio.svg
   :align: center
   :width: 30%
   :name: static_view_fig

The static diagram statisfies the architecture and implements the requirements of the related component. The static diagram includes Unit1+2.


.. figure:: _assets/dynamic_view.drawio.svg
   :align: center
   :width: 30%
   :name: dynamic_view_fig

The dynamic diagram satisfies the architecture and implements the requirements of the related component.

.. figure:: _assets/dd_traceability.drawio.svg
   :align: center
   :width: 30%
   :name: dd_traceability_fig

The unit description will be generated automatically based on the comments in the source code and from the interface description.

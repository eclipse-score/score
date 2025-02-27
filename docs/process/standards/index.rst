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

Standards
=========

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   iso26262/iso26262
   isopas8926/isopas8926
   aspice_40/index

.. needpie:: Percentage of standard requirements which are linked to at least one item
   :labels: Connected Requirements, Not Connected Requirements
   :legend:
   :colors: green, red
   :filter-func: _tooling.extensions.score_metamodel.checks.standards.my_pie_linked_standard_requirements

.. needpie:: Percentage of standard workproducts which are linked to at least one item
   :labels: Connected Workproducts, Not Connected Workproducts
   :legend:
   :colors: green, red
   :filter-func: _tooling.extensions.score_metamodel.checks.standards.my_pie_linked_standard_workproducts

.. needpie:: Percentage of standard workproducts that are contained in exactly one workflow
   :labels: Not Linked Workproducts, Linked Workproduct To One Workflow, Linked Workproduct To More Then One Workflows
   :legend:
   :colors: red, green, blue
   :filter-func: _tooling.extensions.score_metamodel.checks.standards.my_pie_workproducts_contained_in_exactly_one_workflow


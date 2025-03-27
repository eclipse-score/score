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
   isosae21434/isosae21434

The graphs below presents statistics on:

* percentage of standard requirements linked to guidances
* percentage of standard workproducts linked to S-CORE workproducts

ISO26262
--------

.. needpie:: Linked Requirements ISO26262
   :labels: Linked, Not Linked
   :legend:
   :colors: LightSeaGreen, lightgray
   :filter-func: score_metamodel.checks.standards.my_pie_linked_standard_requirements(iso26262)

.. needpie:: Linked Workproducts ISO26262
   :labels: Linked, Not Linked
   :legend:
   :colors: LightSeaGreen, lightgray
   :filter-func: score_metamodel.checks.standards.my_pie_linked_standard_workproducts(iso26262)


ASPICE 4.0
----------
.. needpie:: Linked Requirements ASPICE 4.0
   :labels: Linked, Not Linked
   :legend:
   :colors: LightSeaGreen, lightgray
   :filter-func: score_metamodel.checks.standards.my_pie_linked_standard_requirements(aspice_40)


ISOPAS8926
----------
.. needpie:: Linked Requirements ISOPAS8926
   :labels: Linked, Not Linked
   :legend:
   :colors: LightSeaGreen, lightgray
   :filter-func: score_metamodel.checks.standards.my_pie_linked_standard_requirements(isopas8926)

.. needpie:: Linked Workproducts ISOPAS8926
   :labels: Linked, Not Linked
   :legend:
   :colors: LightSeaGreen, lightgray
   :filter-func: score_metamodel.checks.standards.my_pie_linked_standard_workproducts(isopas8926)


ISO21434
--------
.. needpie:: Linked Requirements ISO21434
   :labels: Linked, Not Linked
   :legend:
   :colors: LightSeaGreen, lightgray
   :filter-func: score_metamodel.checks.standards.my_pie_linked_standard_requirements(isosae21434)

.. needpie:: Linked Workproducts ISO21434
   :labels: Linked, Not Linked
   :legend:
   :colors: LightSeaGreen, lightgray
   :filter-func: score_metamodel.checks.standards.my_pie_linked_standard_workproducts(isosae21434)

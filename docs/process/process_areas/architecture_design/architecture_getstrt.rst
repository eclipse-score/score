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

.. _arch_getting_startet:

Getting Started
###############

.. doc_getstrt:: Architecture Design Process
   :id: doc_getstrt__arch__process
   :status: valid

This document describes the steps which need to be done to create the high level architecture (HLA) and the component architecture.

Therefore both an architecture :need:`[[title]] <gd_guidl__arch__design>` and a :need:`[[title]]<doc_concept__arch__process>` are available.

General Workflow
****************

.. figure:: _assets/architecture_workflow.svg
   :width: 80%
   :align: center
   :name: architecture_workflow_fig

   Architecture Design Workflow

:numref:`architecture_workflow_fig` shows all steps which are required to create an architectural design. In this getting started only a short overview is given. A more detailed description of all the step is provided in the guideline:

:need:`[[title]] <gd_guidl__arch__design>`

Tooling support
***************

Templates
=========

For creating the architectural design snippets in vs code are available:

* feat_arc_<sta|dyn|int|int_op>_t
* comp_arc_<sta|dyn|int|int_op>_t
* mod_arc_sta

.. _arch_gen_sphinx:

Architecture Generation for Sphinx-Needs
========================================

Overview
--------

The system provides utilities to generate UML diagrams from requirement specifications. It supports various component types including:

* Components
* Component Interfaces
* Logical Interfaces
* Modules
* Features

as well as linkages between them.

Usage
-----

To generate a UML diagram, use the *needarch* directive in your Sphinx-Needs documentation:

.. code-block:: rst

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}

You can add any layout or additional configuration you want before you call the *draw_xyz*.

It's also possible to manually extend the drawing. For an example, check out :ref:`manual_addition_uml`

Available Drawing Classes
-------------------------

.. code-block:: none

   # Draw Feature
   # Generates a UML representation of a feature and its included components/interfaces.

   {{ draw_feature(need(), needs) }}

   # Draw Logical Interface
   # Renders a logical interface and its operations.

   {{ draw_logical_interface(need(), needs) }}

   # Draw Module
   # Renders a module containing multiple components.

   {{ draw_module(need(), needs) }}

   # Draw Component
   # Creates a complete component diagram including internal structure and linkages.

   {{ draw_component(need(), needs) }}

   # Draw Component Interface
   # Generates a component interface diagram with its operations and implementations.

   {{ draw_component_interface(need(), needs)}}

.. note::

   Note: The above syntax is for the *needarch* directive. It is also possible to use the *needuml* directive.
   To achieve this the *need()* call needs to be replaced with the following, as *needuml* does not support *need()*

.. code-block:: none

   # need() => needs.__getitem__('ID OF THE REQUIREMENT YOU ARE IN')

   # For example, drawing the requirement:
   `COMP_ARC_STA__component_manual_1`

    would then look as such
   {{ draw_component( needs.__getitem__('COMP_ARC_STA__component_manual_1'), needs ) }}

Rendered Examples
^^^^^^^^^^^^^^^^^

Here are some excerpts of UML diagrams made from the requirements of that file.

**Module**

.. code-block:: rst

   .. mod_arc_sta:: Module 1
      :id: mod_arc_sta__module_getstrt
      :security: YES
      :safety: ASIL_B
      :status: valid
      :includes: comp_arc_sta__component_getstrt

      .. needarch::
         :scale: 50
         :align: center

         allowmixing
         {{ draw_module( need(), needs ) }}

Which then gives us this rendered image:

.. mod_arc_sta:: Module 1
   :id: mod_arc_sta__module_getstrt
   :security: YES
   :safety: ASIL_B
   :status: valid
   :includes: comp_arc_sta__component_getstrt

   .. needarch::
         :scale: 50
         :align: center

         allowmixing
         {{ draw_module( need(), needs ) }}

**Component**

.. code-block:: rst

   .. comp_arc_sta:: Component 1
      :id: comp_arc_sta__component_getstrt
      :status: valid
      :safety: ASIL_B
      :security: NO
      :uses: comp_arc_int__archdes_component_interface_3
      :implements: comp_arc_int__archdes_component_interface_1
      :fulfils: comp_req__archdes_example_req

      .. needarch::
         :scale: 50
         :align: center

         allowmixing
         {{ draw_component( need(), needs ) }}


.. comp_arc_sta:: Component 1
   :id: comp_arc_sta__component_getstrt
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: comp_arc_int__archdes_component_interface_3
   :implements: comp_arc_int__archdes_component_interface_1
   :fulfils: comp_req__archdes_example_req

   .. needarch::
         :scale: 50
         :align: center

         allowmixing
         {{ draw_component( need(), needs ) }}

.. _manual_addition_uml:

Manual Addition to the UML
^^^^^^^^^^^^^^^^^^^^^^^^^^

We use a similar rst as above, just this time we use *needuml* and add some extra manual UML at the end.
To make *needuml* work we have to replace the *need()* call with a different function call.


.. code-block:: rst

   .. comp_arc_sta:: Component Manual 1
      :id: comp_arc_sta__component_manual_getstrt
      :status: valid
      :safety: ASIL_B
      :security: NO
      :uses: comp_arc_int__archdes_component_interface_3
      :implements: comp_arc_int__archdes_component_interface_1
      :fulfils: comp_req__archdes_example_req

      .. needuml::

         {{ draw_component( needs.__getitem__('comp_arc_sta__component_getstrt'), needs ) }}
         component "Component Manual" as CM {
         }
         CM -> LI1: EXTRA_LINKAGE_MANUALLY_ADDED

.. comp_arc_sta:: Component Manual 1
   :id: comp_arc_sta__component_manual_getstrt_1
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: comp_arc_int__archdes_component_interface_3
   :implements: comp_arc_int__archdes_component_interface_1
   :fulfils: comp_req__archdes_example_req

   .. needuml::

         {{ draw_component( needs.__getitem__('comp_arc_sta__component_getstrt'), needs ) }}
         component "Component Manual" as CM {
         }
         CM -> LI1: EXTRA_LINKAGE_MANUALLY_ADDED


Limitations
-----------

* Grouping functionality needs improvement
* Manual extendability is limited to the same type as the underlying drawing, either class or association diagram types
* Currently only looks for the options *includes, uses, implements*



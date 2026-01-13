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

Docs-As-Code
============

Introduction
------------

This document describes how to write and publish documentation using the S-CORE Docs-As-Code approach.

Diagrams
--------

The S-CORE Docs-As-Code solution supports several ways to create diagrams.
Each has its own strengths and weaknesses.

Draw.io
~~~~~~~

Draw.io can be used to create diagrams in a graphical editor.

The easiest way to use Draw.io is to create a new file in VS Code and use the Draw.io extension.
The new file must be named with the `.drawio.svg` extension.
When you click on the file, the Draw.io editor will open within VS Code:

.. image:: assets/docs-as-code/drawio-editing.png
   :alt: Draw.io Editor in VS Code
   :scale: 20%


Then you can embed the image in .rST files like this:

.. code-block:: rst

   .. image:: assets/docs-as-code/example.drawio.svg
      :alt: Example Diagram

Which will render like this:

.. image:: assets/docs-as-code/example.drawio.svg
   :alt: Example Diagram

PlantUML
~~~~~~~~

PlantUML can be used to create diagrams in a text-based format.
The diagrams are rendered as images in the documentation.

You can use them inline in markdown files like this:

.. code-block:: rst

   .. uml::

      @startuml
      Alice -> Bob: Authentication Request
      Bob --> Alice: Authentication Response
      @enduml

Which will render like this:

.. uml::

   @startuml
   Alice -> Bob: Authentication Request
   Bob --> Alice: Authentication Response
   @enduml

Alternatively you can include them as .puml files like this:

.. code-block:: rst

   .. uml:: assets/docs-as-code/example.puml
      :alt: Example Diagram

Which will render like this:

.. uml:: assets/docs-as-code/example.puml
   :alt: Example Diagram

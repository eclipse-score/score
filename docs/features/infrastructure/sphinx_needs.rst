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

Sphinx Needs
############

.. document:: PlantUML Theming
   :id: doc__plantuml_theming
   :status: valid
   :safety: QM
   :tags: tooling, docs-as-code, sphinx-needs


Description
===========
This section describes why within S-CORE a PlantUML is created and how to apply it for pure PlantUML diagrams as well as for sphinx-needs extensions ``draw_<feature | module | component | Interface>()``.

**Motivation**

* Same `look-and-feel`.
* Emphasize the branding of our project.
* According to S-CORE :ref:`docs-as-code` approach.

**Rational**

What is a theme in context of PlantUML?

* A PlantUML theme is a set of colors, styles, format options, shading applied to do dedicated elements used within the PlantUML diagram syntax.
* The theme will overwrite default ones.
* The diagram creator is not forced or limited to stay with the overrides by SCORE theme, he/she could further adjust every styling element and/or ``skinparam`` according to his/her needs.

.. note::
   The theme is `puml-theme-score.puml <https://raw.githubusercontent.com/kalu-an/score_communication/refs/heads/puml_theme/score/mw/com/design/puml-theme-score.puml>`_ currently located in a fork of communication repository. This might change in the future.

``.. needarch::`` showcase
----------------------------------------
Below it is shown how to use the ``.. needarch::`` directive to draw different views on architecture.
The theme is applied to the diagrams by using the ``:config:`` option with the value ``score_config``.

**Draw a Feature**

.. code-block:: rst

   .. needarch::
      :scale: 50
      :align: center
      :config: score_config

      {{ draw_feature(need(), needs) }}


Real Example: Feature Architecture Communication - :need:`feat_arc_sta__com__communication`

**Draw an Interface**

.. code-block:: rst

   .. needarch::
      :scale: 50
      :align: center
      :config: score_config

      {{ draw_interface(need(), needs) }}

Real Example: Communication User Interface - :need:`logic_arc_int__communication__user`

**Draw an Interface**

.. code-block:: rst

   .. needarch::
      :scale: 50
      :align: center
      :config: score_config

      {{ draw_module(need(), needs) }}

Real Example: Logging Module - :need:`mod_view_sta__logging__logging`

**Draw a Component**

.. code-block:: rst

   .. needarch::
      :scale: 50
      :align: center
      :config: score_config

      {{ draw_component(need(), needs) }}

Real Example: Logging Component - :need:`comp_arc_sta__logging__logging`

``.. needuml::`` showcase
-------------------------
To apply the theme on PlantUML diagrams the ``!include`` directive could be used to include the theme file from the repository.
This could be done for sphinx needs directives and ``.. uml::`` and ``.. needuml::``.

.. code-block:: rst

   .. uml::

      :scale: 50
      :align: center
      :name: doc__tools__plantuml_theming

      @startuml
         !include https://raw.githubusercontent.com/kalu-an/score_communication/refs/heads/puml_theme/score/mw/com/design/puml-theme-score.puml
         Alice -> Bob: Which PlantUML version are you using?
         Bob --> Alice: I am using PlantUML version %version()
      @enduml

will render like this:

.. uml::

    :scale: 50
    :align: center
    :name: doc__tools__plantuml_theming

    @startuml
      !include https://raw.githubusercontent.com/kalu-an/score_communication/refs/heads/puml_theme/score/mw/com/design/puml-theme-score.puml
      Alice -> Bob: Which PlantUML version are you using?
      Bob --> Alice: I am using PlantUML version %version()
    @enduml


Real Examples: Code Analysis C++ - :need:`doc__cpp__code_analysis`

PlantUML - Resources
--------------------

**Preprocessing**

Similar to c language which allows to use `PlantUML preprocessing <https://plantuml.com/preprocessing>`_

* Variables -> ``[=, ?=]``
* Operators -> ``[&&, ||, ()]``
* Conditions -> ``[!if, !else, !elseif, !endif]``
* Control lops -> ``[!while, !endwhile]``
* User functions -> ``[!procedure, !endprocedure], [!function, !endfunction]``
* Includes -> ``[!include]``
* ...


**Builtin functions**

`Builtin functions <https://plantuml.com/preprocessing#291cabbe982ff775>`_ could be used to e.g. insert current date, filenames, paths, env variables.

``%date("YYYY-MM-dd")`` -> will insert current date in format YYYY-MM-dd


Styling and Formatting
----------------------

``Skinparam`` impact on *whole* diagram. Styles or html tags could be used for formatting dedicated *diagram elements*.

**Skinparam**

``skinparam ActorBackgroundColor red`` -> all existing elements of type ``actor`` will be rendered with red background

**Html tags**

* ``<b></b>`` -> bold text between
* ``<font size=20>`` -> font size set to 20

**Styles**

* ``<style> </style>`` -> style definition in between
* Further reading: `<https://plantuml.com/de/style-evolution>`_

Example Skinparam:

.. code-block:: rst

   @startuml
      skinparam SequenceLifeLineBackgroundColor red
      skinparam SequenceLifeLineBorderColor #00FF00
      participant client as C
      participant server as S
      C -> S++ :  <b><font size=20>Hello()</b>
      S --> C-- :
   @enduml

This will render like this:

.. uml::

   :scale: 50
   :align: center

   @startuml
      skinparam SequenceLifeLineBackgroundColor red
      skinparam SequenceLifeLineBorderColor #00FF00
      participant client as C
      participant server as S
      C -> S++ :  <b><font size=20>Hello()</b>
      S --> C-- : Date
   @enduml


Example html tags:

.. code-block:: rst

   @startuml
      skinparam NoteBackgroundColor Transparent
      note over Source
      This is <b>bold</b>
      This is <i>italics</i>
      This is <font:monospaced>monospaced</font>
      This is <s>stroked</s>
      This is <u>underlined</u>
      This is <w>waved</w>
      This is <s:green>stroked</s>
      This is <u:red>underlined</u>
      This is <w:#0000FF>waved</w>
      This is <b>a bold text containing <plain>plain text</plain> inside</b>
      -- other examples --
      This is <color:blue>Blue</color>
      This is <back:orange>Orange background</back>
      This is <size:20>big</size>
      end note
   @enduml


This will render like this:

.. uml::

   :scale: 50
   :align: center

   @startuml
      skinparam NoteBackgroundColor Transparent
      note over Source
      This is <b>bold</b>
      This is <i>italics</i>
      This is <font:monospaced>monospaced</font>
      This is <s>stroked</s>
      This is <u>underlined</u>
      This is <w>waved</w>
      This is <s:green>stroked</s>
      This is <u:red>underlined</u>
      This is <w:#0000FF>waved</w>
      This is <b>a bold text containing <plain>plain text</plain> inside</b>
      -- other examples --
      This is <color:blue>Blue</color>
      This is <back:orange>Orange background</back>
      This is <size:20>big</size>
      end note
   @enduml

Example styles:

.. uml::

   :scale: 50
   :align: center

   @startuml
      hide stereotype
      <style>
         .CLIENT_STYLE {
            Fontsize 20
            Fontname Papyrus
            BackgroundColor LightBlue
         }
         .SERVER_STYLE {
            Fontsize 20
            Fontname Mistral
            BackgroundColor Orange
         }
      </style>
      participant Client as C <<CLIENT_STYLE>>
      participant SERVER as S <<SERVER_STYLE>>
      C -> S++ :  Hello()
      S --> C-- :
   @enduml


This will render like this:

.. code-block:: rst

   :scale: 50
   :align: center

   @startuml
      hide stereotype
      <style>
         .CLIENT_STYLE {
            Fontsize 20
            Fontname Papyrus
            BackgroundColor LightBlue
         }
         .SERVER_STYLE {
            Fontsize 20
            Fontname Mistral
            BackgroundColor Orange
         }
      </style>
      participant Client as C <<CLIENT_STYLE>>
      participant SERVER as S <<SERVER_STYLE>>
      C -> S++ :  Hello()
      S --> C-- :
   @enduml

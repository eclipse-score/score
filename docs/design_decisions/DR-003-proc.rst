..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

DR-002-Proc: Module Folder Structure
====================================

In each DR file, include the following sections:


.. dec_rec:: Module Folder Structure
   :id: dec_rec__platform__module_folder_structure
   :status: accepted
   :version: 1
   :context: Processes
   :decision: Alternative C

Context
-------

The S-CORE project defines as part of the project's processes a `module folder structure <https://eclipse-score.github.io/score/main/contribute/general/folder.html#module-folder-structure>`_.
This defines where the module teams shall put documentation, source code and test files in the module repositories.
Currently disputed are the component artefacts folders below ``/score/<component_name>/`` :

.. parsed-literal::

   <module_name>/                       -> Folder containing all artifacts corresponding to one module.
   │
   └── score/                           -> Folder containing all artifacts corresponding to the components of the module.
       ├── <component_name>/            -> Components of the module.
       │   │                               Folder containing all artifacts corresponding to one component.
       │   ├── docs/                    -> Documentation of the component
       │   ├── src/                     -> Source files of the component consisting of
       │   |   │                           Include and source Files [:need:`wp__sw_implementation`]
       │   |   │                           Unit tests [:need:`wp__verification_sw_unit_test`]
       │   |   └── <lower_level_comp>/  -> lower level component following <component_name> folder structure
       │   └── tests/                   -> Component-level tests (e.g., integration tests)
       │                                   [:need:`wp__verification_comp_int_test`]
       └── tests/                       -> Module-level tests (e.g., feature integration tests, system tests)
                                           [:need:`wp__verification_feat_int_test`]

Alternatives Considered
-----------------------

Alternative A
^^^^^^^^^^^^^
The modules will have the same folder structure below ``/score/<component_name>/`` but the ``src/`` folder
will be removed.

Advantages
""""""""""
*  **Advantage 1:** The user of the S-CORE modules has the same "look-and-feel" when exploring the S-CORE modules.
*  **Advantage 2:** Structure from module_template can be used without adaptions.
*  **Advantage 3:** Tooling (config) may be more easy to share between modules.
*  **Advantage 4:** Removing ``src/`` is less effort as less teams use it than do not use it.
*  **Advantage 5:** Include paths do not need to have the ``src/`` in it.
*  **Advantage 6:** Storing the component documents near the source code is consensus and the structure reflects this.

Disadvantages
"""""""""""""
*  **Disadvantage 1:** From folder naming it is not clear any more where the "sourde code" shall be stored.
*  **Disadvantage 2:** Teams are not free any more to find optimal solutions in their substructure.

Alternative B
^^^^^^^^^^^^^
Every module team can decide on their own how to organize their substructure.

Advantages
""""""""""
*  **Advantage 1:** No alignment effort. Folder structures can be left as those are.
*  **Advantage 2:** Optimizing possible in every module.

Disadvantages
"""""""""""""
*  **Disadvantage 1:** Not having the Alternative A advantages 1-3

Alternative C
^^^^^^^^^^^^^
Opt-Out solution: have the folder structure as defined centrally but be able to rearrange the
source code folders if there are better reasons as given for Alternative A.
Document this by a Decision Record in the module repository.
Test folders as described centrally are a recommendation only.

Advantages
""""""""""
*  **Advantage 1:** Do not rule out optimal solutions.
*  **Advantage 2:** Having a ``docs/`` folder below the ``component_name`` already supports a similar look and feel.
*  **Advantage 3:** Mostly also keeps the advantages from Alternative A

Disadvantages
"""""""""""""
*  **Disadvantage 1:** No central alignment of test folders.

Decision
--------
**Alternative C** is selected.

Justification for the Decision
------------------------------

Alternative C is a good compromise between A and B.
There are no strong feelings about the removal of the ``src/`` folder in the teams who need to do this.

The arrangement of test folders and files (including their names) differs strongly between all the analyzed
modules. The effort to align this seems (currently) higher than the gain.

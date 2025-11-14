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

.. document:: Naming Conventions
   :id: doc__naming_conventions
   :status: valid
   :safety: ASIL_B
   :realizes: wp__sw_development_plan

Naming Conventions
==================

.. _naming_convention_files:

Naming Conventions of Files
---------------------------

The overall naming convention is to use snake case for all files and folders (all files are named lowercase and spaces are replaced by underscores).

For drawio pictures use the extension .drawio.svg - this enables the tooling to recognize a picture as modifiable by drawio.

.. _naming_convention_needs:

Naming Convention for UIDs
--------------------------

The naming convention for the UIDs of **all** elements shall be defined as follows:

* It should not exceed 30 characters
* It shall show a meaningful name
* It shall only consist of lowercase, digits and underscores

For the naming of the UIDs also following convention shall be applied:

* It shall consist of 3 parts separated by double underscore
   * | prefix
     | (defined in the Metamodel)
   * | structural element
     | (e.g. abbreviation for the feature / subfeature)
   * | keyword (s)
     | (keyword(s) referring the the description, separated by underscore)

As examples:

* feat_req__ipc__e2e_protection
* comp_req__persistency__storage

Only for **process UIDs** the structural element is optional:

* gd_temp__review
* gd_req__req__structure

.. _branch_naming:

Naming convention for git branches
----------------------------------

In order to keep an overview which branch belongs to whom the branch
name also should be descriptive. The following rules shall apply:

#. The branch name shall start with your github username. This will make
   it easier for everybody to identify the owner of the branch.
#. Branch names must be lower case.
#. Concatenation is done by underscores _.

An example could look like this:

Mustermann, GitHub Name: maximuster

.. code::

   maximuster_my_awesome_branch_name

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

.. _modules:

Modules
=======

A **Module** is a major architectural building block which is defined as a component or a set of components realizing a :ref:`feature <features>` of the platform.
It is the physically compiled and packaged unit that results from the build process and is made available for delivery. For further explanation see the `Building blocks concept <https://eclipse-score.github.io/process_description/main/general_concepts/score_building_blocks_concept.html>`_.

.. image:: _assets/module_architecture.drawio.svg
   :alt: Module Architecture


.. note::
   For now, we store the modules documentation in the modules tree, because multi-repo docs are not yet supported.
   Once this support becomes available it will be moved to the right repo.

.. toctree::
   :maxdepth: 1
   :glob:

   ./*/index

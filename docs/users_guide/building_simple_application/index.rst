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

.. _contribute_own_module:

Contribute own module
=====================

This guide walks you through contributing a new platform module to Eclipse S-CORE end-to-end.
As a running example you will build a small demo application called
`scrample <https://github.com/eclipse-score/scrample/tree/v0.1.2-simple-app>`_, which shows how
to compose existing S-CORE platform modules into new functionality.

By the end of this section you will have:

- Created a properly structured S-CORE module from scratch.
- Generated documentation from source and integrated it into the platform docs.
- Built the module with Bazel and verified it compiles cleanly.
- Wired up CI/CD workflows so every change is automatically validated.
- Plugged the module into the reference integration so it becomes part of the platform.

.. toctree::
   :maxdepth: 1

   first_score_module.rst
   doc_generation.rst
   building_source_code.rst
   cicd_workflows.rst
   reference_integration.rst

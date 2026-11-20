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

This guide walks you through contributing a new module to Eclipse S-CORE.
Every new module repository is created from the
`Eclipse S-CORE module template <https://github.com/eclipse-score/module_template>`_, so the guide follows the template
step by step and explains what it already provides and how to adapt it to your module.

As a running example it uses the component ``component_example`` of the template
(`score/component_example <https://github.com/eclipse-score/module_template/tree/main/score/component_example>`_):
a small C++ library which returns a greeting, e.g. ``Hello, World!``. The code is deliberately simple, so that you
can focus on what makes an S-CORE module: the structure of the repository, the build with Bazel, the tests on the
different test levels, the documentation of requirements and architecture and the traceability between them.

You don't need your own repository to follow the guide. Clone the template and try every step there:

.. code-block:: bash

   git clone https://github.com/eclipse-score/module_template.git
   cd module_template

Open the folder in the S-CORE devcontainer (see :ref:`setting_up_dev_env`), then all required tools are available.

By the end of this section you will:

- know how to request a module repository and what the template contains,
- build the module and run its unit, component integration and feature integration tests,
- document requirements and architecture and trace them to code and tests in the generated documentation,
- know the CI/CD workflows that check every pull request.

.. toctree::
   :maxdepth: 1

   first_score_module.rst
   building_source_code.rst
   doc_generation.rst
   cicd_workflows.rst

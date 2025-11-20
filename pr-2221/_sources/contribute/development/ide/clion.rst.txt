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

CLion
#####

For CLion some of the configuration can be provided via the *.clwb* directory. But with this approach not all plugins can be configured.

Starlark
========

For Bazel support the Plugin `Bazel <https://plugins.jetbrains.com/plugin/9554-bazel-for-clion>`_ needs to be installed from the marketplace.

No further configuration is required here.

Python
======

For CLion a python interpreter needs to be configured first:

`File | Settings | Build, Execution, Deployment | Python Interpreter <jetbrains://JetBrainsClient/settings?name=Build%2C+Execution%2C+Deployment--Python+Interpreter>`_

Select your system python and as location select the score venv (located in <scorerepo>/.venv_docs)

Sphinx
======

Code Formatting
---------------
A definition of the tab size of .rst files is included in project settings.

Error Highlighting
------------------
To provide error handling within the Sphinx Docs build the Plugin `LSP4IJ <https://plugins.jetbrains.com/plugin/23257-lsp4ij>`_ is required. The plugin can be configured using predefined configuration files:

* Download Configuration file from `Github <https://github.com/eclipse-score/score/tree/main/docs/contribute/development/ide/_assets/lsp4ij/esbonio>`_
* Navigate to `File | Settings | Languages & Frameworks | Language Servers <jetbrains://JetBrainsClient/settings?name=Languages+%26+Frameworks--Language+Servers>`_
* Select add language server | Import from Custom Template | select folder which contains downloaded config

Then error highlighting in the source files should be available, maybe a restart is required.

Live Preview
------------
For the preview of the documentation the live preview can be used:

.. code-block:: shell

   bazel build //docs:live_preview
   bazel-bin/docs/live_preview

If the live preview is build and run via the executable with these two separate commands the bazel instance is not blocked in the repository.

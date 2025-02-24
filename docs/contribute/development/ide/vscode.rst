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

VS Code
#######

For VS Code any preexisting configuration is provided via the workspace configuration in the directory <workspace_root/.vscode>. It includes

* some formatting rules
* configuration for recommended plugins

Starlark
========

For Starlark currently no solution is integrated in VScode.

C++
===


Python
======

For Python currently the full feature set of the official `Python <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_  Extension (MIT License) is provided included features e.g. autocomplete, syntax checking, ...

Also the configuration for displaying and executing pytest in the IDE is provided.

As a linter the `ruff extension <https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff>`_  (MIT License) is set up.

Debugging
---------

For debugging the `Python Debugger <https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy>`_ (MIT License) and *debugpy* can be used for remote debugging.

Debugging the docs build
''''''''''''''''''''''''
For debugging the docs environment all necessary configuration is already provided. It can be activated for the incremental build via the following command:

.. code-block:: shell

   bazel run //docs:incremental -- --debug

Manual debugging
''''''''''''''''
For all other tools the debugging needs to be setup manually. Therefore following steps need to be executed:

#. Add following code to the project (e.g. the __init__.py)

   .. code-block:: python

      debugpy.listen(('0.0.0.0', <<port>>))
      print('Waiting for client to connect')
      debugpy.wait_for_client()

#. Create a launch configuration (can also be done automatically in VScode) similar to this

   .. code-block:: json

      {
      // Use IntelliSense to learn about possible attributes.
      // Hover to view descriptions of existing attributes.
      // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
      "version": "0.2.0",
      "configurations": [
         {
               "name": "Python Debugger: Remote Attach Bazel",
               "type": "debugpy",
               "request": "attach",
               "connect": {
                  "host": "<<localhost or name of remote workstation>>",
                  "port": "<<portnumber>>",
               },
         }
         ]
      }

#. Execute the bazel command to run the target
#. Wait till "Waiting for client to connect" appears in the output
#. Execute launch configuration
#. Enjoy debugging

Sphinx
======

For Sphinx development currently following features are supported:

* Syntax checking
* live-preview within IDE
* autocompletion

Therefore a configuration for following plugins is available:

   * `lextudio.restructuredtext <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_ : rst syntax highlighting (MIT License)
   * `swyddfa.esbonio <https://marketplace.visualstudio.com/items?itemName=swyddfa.esbonio>`_ (only release version): linting and live preview (MIT License)
   * `usernamehw.errorlens <https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens>`_: highlights errors and warnings in IDE (MIT License)

The live-preview can then be activated inside a .rst file by pressing Ctrl + Shift + V or clicking on the tiny symbol on the top right corner which looks like a book with a magnifier.

If the sphinx configuration is altered the language server has to be restartet: Ctrl + Shift + P and select "Esbonio: Restart Language Server"

If there is any issue with the preview or syntax highlighting the error log can be visualized via the output and select "Esbonio"

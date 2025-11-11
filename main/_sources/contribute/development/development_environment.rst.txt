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

.. document:: Development Environment
   :id: doc__develop_environment
   :status: valid
   :safety: ASIL_B
   :realizes: wp__sw_development_plan

.. _setting_up_dev_env:

Setting Up the Development Environment
######################################

*The development environment may vary depending on the repository you want to contribute to. This
document describes the setup for the `score` repository. Others should be similar.*

Devcontainer Setup
==================

The recommended way to set up the development environment is by using the provided devcontainer.
The devcontainer includes all necessary tools and dependencies pre-configured for development, as
not everything can be installed via Bazel.

To use the devcontainer:

1. Ensure you have Docker installed and running on your system.
2. Open the project in a `devcontainer capable editor of your choice <https://containers.dev/supporting>`_.
3. e.g. for VSCode (see IDE section below for more details):

   * Install the "Remote - Containers" extension in VS Code if not already installed.
   * Open the project in VS Code.
   * When prompted, select "Reopen in Container" to build and start the devcontainer.
     Alternatively, you can open the Command Palette (Ctrl+Shift+P) and select "Remote-Containers:
     Reopen in Container".

This approach simplifies the setup process and ensures a consistent development environment.

**No** manual setup needs to be done when using the devcontainer.

Manual Setup
============

If you prefer to set up the development environment manually, follow the steps below:

General Setup
-------------

* Install the required dependencies for your operating system. This includes:

  * Bazelisk
  * Python 3.x
  * Graphviz/Dot (for generating diagrams)

  Check `Dockerfile <https://github.com/eclipse-score/devcontainer/tree/main/src/s-core-devcontainer/.devcontainer>`_ for
  an accurate list and exemplary instructions.
* Clone the score repository to your hard drive.

Additional assistance for working with Bazel is provided by the following tools:

Buildifier
----------

Buildifier is a tool which can format *.bzl* files. Additional info and installation instructions are provided
`on github <https://github.com/bazelbuild/buildtools/blob/main/buildifier/README.md>`_

In short:

* download binary
* renamed binary to buildifier
* place it somewhere in the system path e.g.

  * ~/.local/bin (no root required)
  * /usr/local/bin

Autocompletion in the Shell
---------------------------

How to activate autocompletion in *bash* and *zsh* is described `here <https://bazel.build/install/completion>`_

Basically following steps need to be performed:

#. Navigate to project workspace folder
#. Determine bazel version

   .. code-block:: shell

      bazel --version

#. Build and install the bash completion:

   * Change to any temporary directory and execute

   .. code-block:: shell

      git clone https://github.com/bazelbuild/bazel.git
      cd bazel
      git checkout <VERSION_OF_BAZEL>
      USE_BAZEL_VERSION=<VERSION_OF_BAZEL> bazel build //scripts:bash_completion
      sudo cp bazel-bin/scripts/bazel-complete.bash /etc/bash_completion.d/
      cd ..
      rm -rf bazel

Graphviz/Dot Installation
-------------------------

Graphviz/Dot is mandatory for local development (outside the `devcontainer`).
To install it on a Linux system using apt, execute the following command:

.. code-block:: shell

   sudo apt update && sudo apt install graphviz

This ensures that all necessary dependencies for generating diagrams are available during development.

IDE Support
===========
Currently as a goal for this project the IDE shall provide support for most of the languages which are used in this project. For this Project *VS Code* is selected as the primary IDE. This means that only *VS code* will be checked in case of breaking changes!

Other IDE integrations are provided on a community best effort basis.

Python Environment
------------------
The tooling environment, which includes all essential python packages for *docs* can be built in a *virtual python environment* which is located in <workspace_root/.venv_dovs>. It needs be build first:

.. code-block:: shell

   bazel run //docs:ide_support

Later the different IDEs shall be configured to use the tools which were installed into this virtual environment.

IDE Guides
----------

.. toctree::
   :maxdepth: 1

   ide/vscode
   ide/clion

WSL2 Settings
=============
If you encounter memory issues on WSL2, the following minimal settings in your .wslconfig file are recommended:

.. code-block:: shell

   [wsl2]
   swap=8GB
   memory=16GB

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

Setting Up the Development Environment
######################################

General Setup
=============

The basic steps for setup the development environment and building the source file are described in the `readme.md <https://github.com/eclipse-score/score/blob/main/README.md>`_ of the score repository.


This includes:

* on your linux operating system `Bazelisk <https://github.com/bazelbuild/bazelisk>`_ is available
* the score repository is cloned to your hard drive

Additional assistance for working with Bazel is provided by following tools:

.. _buildifier:

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

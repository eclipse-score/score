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

Documentation generation
==========================

.. toctree::
   :maxdepth: 1
   :glob:

Introduction
---------------

As already explained in chapter :ref:`Overview of technologies <technology_overview>`, we use sphinx and sphinx-needs toolchain
to generate documentation out of rst files, where elements of Eclipse S-CORE metamodel are modelled as sphinx-needs elements.

Integration of the sphinx and sphinx-needs toolchain into bazel and Eclipse S-CORE specific extensions are
implemented in https://github.com/eclipse-score/docs-as-code/tree/main/docs module.
Following `documentation <https://eclipse-score.github.io/docs-as-code/main/how-to/index.html>`_ provides an exhaustive description,
how the documentation in Eclipse S-CORE can be created and built. Here, we will focus on a simple example.

First, we need to define a target in bazel, in order to generate html documentation from rst files.
Such target is already provided in the main top level `BUILD <https://github.com/eclipse-score/scrample/blob/main/BUILD>`_
file of the repository:

.. code-block:: python
    :linenos:

    docs(
        source_dir = "docs",
    )


The bazel rule docs needs source_dir as an input parameter. This directory will be given to the *sphinx/sphinx-needs* toolchain,
which will use this directory as source directory and will generate the html documentation based on the files located in the
source directory. Sphinx toolchain will not rely here on any bazel dependencies,
but will use its own mechanism to decide which files should be included for documentation generation.
This is well described in `toctree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`_
chapter of its documentation.

In general, two files are especially important for sphinx doc generation:

- `docs/conf.py <https://github.com/eclipse-score/scrample/blob/main/docs/conf.py>`_ provides configuration for the *sphinx-toolchain*.
  
  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    project = "Module Template Project"
    project_url = "https://eclipse-score.github.io/module_template/"
    project_prefix = "SCRAMPLE_"
    author = "Eclipse S-CORE"
    version = "0.1"

    # -- General configuration ---------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


    extensions = [
        "sphinx_design",
        "sphinx_needs",
        "sphinxcontrib.plantuml",
        "score_plantuml",
        "score_metamodel",
        "score_draw_uml_funcs",
        "score_source_code_linker",
        "score_layout",
    ]

  As you can see, we use here special score configuration and score project extensions.
  The line number 3 is important, since here you have to set the prefix for your module.
  In our case it is *“SCRAMPLE_”*. This prefix will be used, when other external modules are referencing sphinx-needs elements of your module.

- `index.rst <https://github.com/eclipse-score/scrample/blob/main/docs/index.rst>`_ ist the main entry point,
  that includes all other rst files, that should be used for documentation generation  

We can try now to build the documentation using the following command:

.. code-block:: python
  :emphasize-lines: 1

  % bazel build //:docs

Don´t be surprised, if the very first time running the bazel command takes a while to execute.
The first time you call bazel, everything needs to be downloaded locally to its cache folder  (also all toolchain tarballs).
This takes a while, but don’t worry, your next executions will be much faster.
The command we’ve called will check the consistency of your documentation for errors,
but will not generate any html files. To do so, run following command:

.. code-block:: python
  :emphasize-lines: 1, 38

  % bazel run //:docs
  Running Sphinx v8.2.3
  loading translations [en]... done
  DEBUG: Found 0 need references in 0.00 seconds
  calculate directory_hash = e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 within 0.00019431114196777344 seconds.
  loading pickled environment... The configuration has changed (7 options: 'html_permalinks_icon', 'html_static_path', 'needs_layouts', 'needs_types', 'plantuml', ...)
  done
  building [mo]: targets for 0 po files that are out of date
  writing output... 
  building [html]: build_info mismatch, copying .buildinfo to .buildinfo.bak
  building [html]: targets for 1 source files that are out of date
  updating environment: [config changed ('skip_rescanning_via_source_code_linker')] 1 added, 0 changed, 0 removed
  reading sources... [100%] index
  Copying static files for sphinx-data-viewer support
  Copying static files for sphinx-needs datatables support
  Copying static style files for sphinx-needs
  looking for now-outdated files... none found
  pickling environment... done
  checking consistency... done
  preparing documents... done
  copying assets... 
  copying static files... 
  Writing evaluated template result to /home/_dev/scrample/_build/_static/basic.css
  Writing evaluated template result to /home/_dev/scrample/_build/_static/language_data.js
  Writing evaluated template result to /home/_dev/scrample/_build/_static/documentation_options.js
  copying static files: done
  copying extra files... 
  copying extra files: done
  copying assets: done

  generating indices... genindex done
  writing additional pages... search done
  dumping search index in English (code: en)... done
  dumping object inventory... done
  Needs successfully exported
  build succeeded.

  The HTML pages are in ../../../../../../../../../../../_dev/scrample/_build.

Now we have the generated html files, that we can copy somewhere and open in a web browser.

Normally, when you’re working on the documentation, you need a handy way to see the current status of
your work in the web browser. One option for this, is to use the *live preview* feature.
The bazel target for this is automatically imported when you import *doc bazel rule* into your BUILD file (this should work “out-of-the-box”).


.. code-block:: python
  
  load("@score_docs_as_code//:docs.bzl", "docs")

So now run following command:

.. code-block:: python
  :emphasize-lines: 1, 9

  % bazel run //:live_preview

  ...

  Needs successfully exported
  build succeeded.

  The HTML pages are in ../../../../../../../../../../../_dev/playground_2/scrample/_build.
  [sphinx-autobuild] Serving on http://127.0.0.1:8000
  [sphinx-autobuild] Waiting to detect changes...
 
As you can see, a local server is started on following port and address: http://127.0.0.1:8000 .
Open it in your web browser and you should be able to see the current version of the documentation.

.. image:: ../_assets/initial_module_rst_content.png
   :width: 400
   :alt: Architecture overview
   :align: center

The live preview feature stays active, rebuilds and reacts on every change in your documentation.
This makes the work with the documentation quite convenient.
You can stop it by killing the bazel process in the terminal (Ctrl+C).

Now it´s time to replace the dummy context of the index.rst with some meaningful text,
as shown in the following `commit <https://github.com/eclipse-score/scrample/commit/5179175823ecda51775e459ad73d7230cd4c880a>`_.

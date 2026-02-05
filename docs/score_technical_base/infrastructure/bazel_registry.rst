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

.. _bazel_registry:

Bazel registry
##############

Documentation
**************

Description
===========

S-CORE, as a multi repository projects requires a setup of it's own
registry, that will help managing the dependencies between various
parts.

The registry is located at:
https://github.com/eclipse-score/bazel_registry

In order to use it the following lines need to be added to the .bazelrc
file of a module:

.. code::

   common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
   common --registry=https://bcr.bazel.build

S-CORE registry is set as first registry with the fallback to Bazel's
central registry for other open source modules.

Minimal module entry
====================

The following directory layout reflects a minimal module entry:

.. code::

   ├── bazel_registry.json
   ├── modules
   │   └── score_example
   │       ├── 0.1
   │       │   ├── MODULE.bazel
   │       │   └── source.json
   │       └── metadata.json
   └── README.md

The *score_example* directory contains the metadata.json file which holds basic information about the module:

.. code::

   {
       "homepage": "https://github.com/eclipse-score/example",
       "repository": [
           "github:eclipse-score/example"
       ],
       "versions": [
           "0.1"
       ],
       "yanked_versions": {}
   }

Each version of the module is stored as a separate directory. Version directory requires a *source.json* and *MODULE.bazel* files.
The *source.json* file tell bazel where to get the sources from.

.. code::

   {
       "integrity": "sha256-hGJ4VQ+0q/HcxbvOrY/C2UT4SjMnNLVgQAD4k5aAToI=",
       "strip_prefix": "example-872caac46177cc3699899ef91348a643881b0981",
       "url": "https://github.com/eclipse-score/example/archive/872caac46177cc3699899ef91348a643881b0981.zip"
   }


The *MODULE.bazel* file should be the same as delpoyed in the referenced sources.

Module version should comply to the established `Bazel version format <https://bazel.build/external/module#version_format>`_
and use the `compatibility_level <https://bazel.build/external/module#compatibility_level>`_ to specify breaking changes.


References
==========

-  Bazel external dependency management:
   https://bazel.build/external/overview#bzlmod
-  Bazel central registry browser: https://registry.bazel.build/
-  Bzlmod usage examples:
   https://github.com/bazelbuild/examples/tree/main/bzlmod\

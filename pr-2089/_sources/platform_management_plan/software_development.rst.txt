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
.. _sw_development:

Software Development
--------------------

.. document:: Software Development Plan
   :id: doc__software_development_plan
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_development_plan
   :tags: platform_management

Purpose
+++++++

The main purpose of the software development plan is to define several software development related conditions:

* selection of design and programming language
* design guideline
* coding guideline (e.g. MISRA, can also include style guide or naming convention)
* SW configuration guideline
* development tools

Objectives and Scope
++++++++++++++++++++

Objective is to define the main SW development policies as defined in the "Purpose" in an ISO 26262 and ASPICE compliant manner.
Scope is the complete SW platform and the development parts of the process.

Approach
++++++++

Design and programming language
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For specifying **Detailed Design** (like for the Architecture) a mixture of UML diagrams and natural language is used.
Additionally for the Detailed Design linking to code, Doxygen style comments are used.
This is described in :need:`doc_concept__imp_concept` and guided by :need:`gd_temp__detailed_design`

As required in :need:`stkh_req__dev_experience__prog_languages`, S-CORE allows the use of two programming languages:

**C++ with the language set of C++17** - in case additional elements from C++20 are needed this will be considered by
:need:`rl__safety_manager`, :need:`rl__security_manager` and :need:`rl__quality_manager`
and based on their analysis decided by the technical lead circle (:need:`rl__technical_lead`).

**Rust - in "Edition" <tbd>** - selection of language edition has still to be done in the S-CORE project.
For the Rust code of ASIL rated units the "safe subset" shall be used (which is checked by the compiler by configuration of #![forbid(unsafe_code)] in lib.rs)

C language is allowed in incubation phase, as long it is compilable be the selected compiler, but not for a S-CORE release.

Design guideline
^^^^^^^^^^^^^^^^

The design guideline is defined in :need:`doc_concept__imp_concept` and :need:`gd_guidl__implementation`.

API guideline
^^^^^^^^^^^^^

To provide the user with a consistent approach on the use of APIs, there is a guideline documented in :need:`doc__api_guidelines`,
this defines for example the error handling concept or rules to improve user experience.

Coding guideline
^^^^^^^^^^^^^^^^

**C++** - see :need:`doc__cpp_coding_guidelines`

**Rust** - state of the art open source Rust guidelines are currently developed by `Safety Critical Rust Consortium <https://github.com/rustfoundation/safety-critical-rust-consortium/>`_
(which will be adopted by the S-CORE project). A summary of the current state of information regarding Rust in safety critical applications can be found in :need:`doc__rust_coding_guidelines`.

SW configuration guideline
^^^^^^^^^^^^^^^^^^^^^^^^^^

<tbd>

SW development tools
^^^^^^^^^^^^^^^^^^^^

This list will evolve into the complete "Tool List" for the S-CORE project used for
tool evaluation and qualification. In the moment the :need:`doc__verification_plan`
contains additional tools used in verification.

Additional tools for static and dynamic analysis (in addition to compilers and Clang-Tidy) are currently evaluated: `#244 <https://github.com/eclipse-score/score/issues/244>`_

.. rubric:: GitHub

is used for hosting, versioning and contribution of the software. Within
pull requests it's possible to contribute. For contribution a separate process description is
<Link to contribute> available. In the discussion section the information regarding meeting
minutes and Working Sections were stored. Within issues can bugfixes, improvements, blank issues
set up. It's also possible to report there Security vulnerabilities. GitHub Actions is used
as a support for continuous integration.

.. rubric:: Sphinx

is used for software documentation to generate html-sides from reStructuredText.

.. rubric:: Sphinx-Needs

is used for docs-as-code based documentation that is created
and managed by the sphinx documentation generator. With "needs" objects, created in rst-files,
requirements, static architecture views and other Sw development documentation is generated. Sphinx-Needs is 100% compliant to
Sphinx and reStructuredText.

.. rubric:: PlantUML

this UML drawing tool is used for dynamic and static diagrams for unit interaction. Also for dynamic architecture views.

.. rubric:: Draw.io

this drawing tool is used to create flowcharts and diagrams for all uses where PlantUML is not suited
e.g. in process or concept descriptions

.. rubric:: Host Compiler C++

GCC is used as host C++ compiler with its associated linker. It's used as a development (compilation and linking) and verification tool
as it generates compiler warnings and builds unit tests and binaries for SW integration testing.

.. rubric:: Target Compiler C++

QCC the qualify-able compiler/linker from Blackberry offered together with its Posix conform Operating System QNX is planned to be used for target compilation.

.. rubric:: Clang-tidy

is used in conjunction with the Clang compiler to perform static analysis.

.. rubric:: Host Compiler Rust

There is currently no selection of a Rust compiler for S-CORE. Pick your own favorite.

.. rubric:: Target Compiler Rust

The qualified `Ferrocene <https://github.com/ferrocene>`__ compiler is planned to be used.

.. rubric:: Bazel

The main build environment of the project is based on `Bazel <https://bazel.build>`__. It it used to build software
components, documentation, and automated tests.

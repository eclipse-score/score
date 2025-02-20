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

Getting Started
###############

.. doc_getstrt:: Getting Started on Requirements
   :id: doc_getstrt__req__process
   :status: valid
   :tags: requirements_engineering

This document describes the steps which need to be done to create requirements, derive child requirements and finally to perform the formal requirement inspection.

Therefore both a :need:`[[title]] <gd_guidl__req__engineering>` and a :need:`[[title]] <doc_concept__req__process>` are available.

The subsequent steps of linking requirements to code and test cases are described in different guidelines:

Linking Requirements

* to code: <TBD Implementation Guideline>
* to tests: <TBD Verification Guideline>

General Workflow
****************

.. figure:: _assets/requirements_workflow.svg
   :align: center
   :width: 80%
   :name: requirements_workflow_fig

   Requirements Workflow

The details of what needs to be done in each steps are described in the :ref:`workflow_requirements`

Tooling Support
***************

Linking Requirements to Source Code
===================================

For linking requirements to source code a tool is available:

<TBD link implementation guideline>

Linking Requirements to Tests
=============================

For linking Requirements to tests metatags shall be used <TBD link Verification Guidline>


Developer Experience
====================

Additionally tooling is provided to assist the :need:`[[title]] <rl__contributor>` to define the requirements in spinx needs. The current feature set is described as IDE requirements:

.. needtable:: Implemented IDE Requirements
   :tags: sphinx, ide
   :style: table
   :columns: title;id
   :filter: "ide" in tags and type == "tool_req"
   :colwidths: 70,30

A *HowTo* which describes the setup of Sphinx Needs in VScode is available here: <TBD>

For all RST files also a linter is configured, it will be automatically run in the CI upon check-in.
Locally it can be run via

.. code-block:: shell

   bazel test //:format.check


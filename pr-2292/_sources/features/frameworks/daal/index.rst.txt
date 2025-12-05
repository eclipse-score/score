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


Deterministic App Abstraction Layer
--------------------------------------
.. document:: Deterministic App Abstraction Layer
   :id: doc__daal
   :status: valid
   :safety: QM
   :security: NO
   :tags: contribution_request, feature_request
   :realizes: wp__feat_request

.. toctree::
   :maxdepth: 2
   :caption: Contents

   requirements/index.rst

Feature flag
------------

To activate this feature, use the following feature flag:

``experimental_daal``

Abstract
--------

Provides an application abstraction layer and APIs for testing.
Implements common code and several safety requirements.


Motivation
----------
Currently there is no abstraction layer to make component tests independent from application frameworks like 'Fixed Execution Order Framework'.
With the abstraction layer you can test against different execution frameworks and in different environments (linux & qnx).

Rationale
---------

The lifecycle states are designed like in usual execution frameworks to emulate the same behavior also in testing.
Also error handling and health monitoring is part of the framework for emulation of all aspects.
Different communication frameworks can be plugged in to use in testing.
The idea is also to use the framework as a testing area for our future Autosar process.


Backwards Compatibility
-----------------------

It can have impact in the Feo Framework because we need only one Lifecycle interface.


Open Issues
-----------

[Any points that are still being decided/discussed.]

   .. note::
       While a CR is in draft, ideas can come up which warrant further discussion.
       Those ideas should be recorded so people know that they are being thought about but do not have a concrete resolution.
       This helps make sure all issues required for the CR to be ready for consideration are complete and reduces people duplicating prior discussion.



Footnotes
---------

[A collection of footnotes cited in the CR, and a place to list non-inline hyperlink targets.]

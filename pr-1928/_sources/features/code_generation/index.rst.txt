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

.. _code_generation_feature:

Code Generation
###############

.. document:: Code-Generation
   :id: doc__code_generation
   :status: draft
   :safety: ASIL_B
   :security: NO
   :tags: feature_request
   :realizes: wp__feat_request

.. toctree::
   :maxdepth: 1
   :glob:
   :titlesonly:
   :hidden:

   */index


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_code_generation``


Abstract
========


Motivation
==========

To accomplish multi-generational portability of systems and
applications across suppliers, there is a need to enable
decoupling of human-written functional code from vendor-specific
system deployment architectures, application development frameworks,
communication mechanism libraries and operating system interface
specifics.

Rationale
=========

Separation of concern
_____________________

Traditionally, automotive project/system-specific implementations tend
to be very heavily interwoven with technology supplier API
peculiarities and vendor framework-expected application code
structures. This is okay for one-off projects, but not for reusable
code across different technology stacks and vehicle generations. To
address this issue, a key design philosophy is to impose a very
specific code structure requirement for all functional code that is to
be run in the middleware space. For example, one want to have the freedom to
swap communication mechanisms as new improved technologies
emerge. This means the architecture needs to be
simultaneously agnostic and accomodating of different communication
frameworks and protocols. This is accomplished by enforcing a standard
API for the function/application developer to access input data,
runtime parameters, internal state variables, hardware interface
contexts and to populate output data structures.

A standard well defined API is the condition to code generation.


Code generation approach
________________________


The isolation of functional code from system-level and
deployment-level context allows for code reuse, rapid system
reconfiguration, prototyping, simulation and advanced fuzz testing
without in-code changes and refactoring when the application lifecycle
standard API is combined with a code generator. The code generator is
responsible for generating the middleware boiler code that gets compiled and
deployed. There is no need for the developer to know how this is done.

This allows eliminating large amounts of
"boilerplate" code that would otherwise clutter human-written
codebases and slow down refactoring. This opens the door to affordable
code base translation.


The only limiting factor in freedom-of-redeployment is if the
functional code's dependency libraries (if any) require
specific hardware or drivers. Abstracting away vendor-specific
accelerator hardware/driver interfaces is beyond the current scope.



Specification
=============

Software Compute Unit
_____________________

Let's define a software unit an entity that implements a specific
input-output algorithmic function as part of a larger graph
algorithm. This would be a ROS node or an ARA Application.

We want to support both functional programming style or Object
Oriented programming style.  In object-oriented programming languages,
such as C++, a software unit would be implemented as a trivially
default-constructible class with public methods and no defined
constructors, that inherits from the C++ base class. Conversely in
Rust, it would be a struct that implements the equivalent public
functions with no constructor.

We want to support error handling and not enforce throwing exception.
Each of the standard interface functions must return an ErrorCode.

We want to advanced code re-usability. We therefore define the concept
for an archetype which is the skeleton of a software unit. An instance
is a unique implementation of an archetype, with a specific
configuration defined as a parameter set. For example, if you would
have 5 cameras in the car, you would define a single archetype, but
instanciate it 5 times, with a different set of parameters for each
camera.

We want to support different steps in the operation mode.
The standard set of API we came up looks like this:

**onInit(Parameters p, InternalState is)** is responsible for
initializing any Internal State or Hidden State variables and data
structures, including any hardware contexts. onInit() is only called
once during the lifecycle of a software unit. You can think of this as
roughly equivalent to the contents of a class constructor. This
function determines the starting point of the lifecycle of a software
unit instance.

**onUpdate(Time t, Parameters p, Inputs in, InternalState is, Output
out)** is responsible for the core repeated logic to be
executed. onUpdate() is called by the execution triggering logic that
may be internal or external depending on the execution environment.

**onReset(Parameters p, InternalState is)** is responsible for
handling situations where the internal state needs to
be reset, to either recover from a trivial error state or because
something in the execution environment has changed. Any trivial
mechanisms for recovery from transient error states can be handled as
part of the onReset function. onReset() can be called any number of
times during the lifecycle of a compute unit instance.

**onShutdown(Parameters p, InternalState is)** is responsible for
handling any cleanup tasks of hardware states and deallocation of
heap-allocated data structures before a compute unit will be deallocated
from memory and any execution terminated. You can think of this as
roughly equivalent to the contents of a class destructor.



Interface
_________


Software Compute units communicate via abstracted input and output
interfaces, with the Software Compute instance itself not knowing
anything about where the data come from or where it should go.

The Inputs data structure contains a collection of input queues for
each inputs modeled for the Software Compute Archetype.

The Outputs data structure is similar to the Inputs data structure
with the difference that the contents are mutable, i.e. writable by
the Software Compute Archetype.


Internal State
______________

A Software Compute unit only concern
is with its own internal needs relevant to the implementation of
an algorithm or other logic block.

For storing variables between execution cycles that have no relevance
for the reproducibility of computation results of a stateful
algorithm, a special Hidden State data structure can be defined.


Parameter
_________

The Parameters data structure contains any runtime Parameters required
by the Software Compute instance. A default parameter data structure
is defined for the archetype. It can be re-configured for each
instance of the Compute instance.

Error Handling
______________

There shall be a error management framework defining error type,
category of errors, mechanism for the propagation of error. In Rust or
modern C++, monadic behavior would be recommended.  The recovery logic
should be modelable in the Modeling Language.



Static analysis of the system
_____________________________

The system would be modeled using a specific description language.
The description language consists of three primary concepts:

**Interface Lists** these are collections of data types of the data to
 be exchanged. They are modeled similarly to common IDLs;

**Software Compyte Unit Archetype Lists** these are collections of
 metadata descriptions of human-written Software Compyte Unit
 implementations. One can think of them as similar to application
 manifests in Adaptive Autosar or the Android Framework.

**Software Compyte Unit Instance Lists** these are used to describe
 the deployment of (instantiate) Software Compyte Unit Archetypes in
 an operating system context, including both standard and user-defined
 configuration parameters.

The above are parsed as files into an intermediate representation that
represents the entire modeled system.  The intermediate representation
open the doors to a static system analysis (resources analysis and
checks, resource allocation, static schedling).

Subchapter
__________

.. example for image embedding
.. .. image:: _assets/sample_image.svg
..    :alt: Name

.. example for image embedding
.. .. image:: _assets/architetcure_diagram_for_code_generation.svg
..    :alt: Architecture Diagram


uml example:

.. uml::

   @startuml

   class ExampleClass {
      +fun(input): bool
   }

   @enduml


Requirements
____________

The related requirements can be found in :doc:`requirements/index`.


Backwards Compatibility
=======================


Security Impact
===============


Safety Impact
=============

Strict repeatible design pattern, extensive code re-usablility, is easy to certify.
Requires tool qualification for the code generator for ASIL relevant components.

License Impact
==============


How to Teach This
=================


Rejected Ideas
==============


Open Issues
===========


Footnotes
=========

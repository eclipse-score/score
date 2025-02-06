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

Inter-process Communication
===========================

.. document:: Inter-process Communication
   :id: DOC__IPC
   :status: valid
   :safety: ASIL_B
   :tags: contribution_request, feature_request


.. toctree::
   :hidden:

   requirements/index.rst


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_ipc``

Abstract
========

This contribution describes a framework to exchange information between processes.
This framework includes:

- an abstraction layer to enable different communication mechanisms
- a communication mechanism that enables zero-copy communication

The abstraction layer is designed in a way to ensure full testability for an end-user, while enabling runtime selection
of the underlying communication mechanism.
It provides the user with a high-level API to focus on the content of information – and not on low-level synchronization
primitives.
The proposed communication mechanism (called LoLa) is optimized for micro-kernel operating systems (like e.g. QNX). By
utilizing shared memory, it enables low latency communication also for mixed-criticality systems (e.g. processes of
different safety integrity level). The possibility for mixed-criticality systems is especially enabled by certain
implementation choices and safety mechanisms that will continue to ensure freedom from interference between separate
processes.

.. _Motivation:

Motivation
==========

S-CORE is targeting high-performance automotive systems with safety impact.
In general, these systems consist of multiple processes that are executed on an operating system.
To fulfill the system needs, these processes need to exchange information in most of the cases.

The communication framework is not a one-fits-all.
For example, it does not replace a standardized platform API that an application links against.

Key aspects of S-CORE and therefore also the IPC communication framework are:

1. High cohesion and loose coupling
2. Mixed-criticality safety systems
3. Performance

In the following we will explain and argue each of these three different aspects. Further secondary aspects will follow
in the section :ref:`Specification` where we also formalize all aspects.

High cohesion and loose coupling
--------------------------------

Complex systems require high cohesion and loose coupling to remain maintainable.
The benefit of loose coupling is to limit the effect of changes throughout the system.
Key to achieve this is stability of interfaces.

Since the communication of a module is also part of its interface, we must consider its stability.
How stable an interface is, largely depends on the implementation reachable through it.
This means, the communication framework can not provide stability on its own.
It can only provide the necessary tools for developers to consider the stability when changing the interface or
implementation.

.. _mot_mixed_criticality:

Mixed-Criticality safety systems
--------------------------------

In complex safety-critical systems, applications often have different criticality.
Communication happens not only on the same criticality level but also between different criticality levels.

For example, a service with low-criticality may provide data to a highly critical application.
Or the reverse could be the case, where a less critical application depends on data produced by a highly critical one.
More complex scenarios are also possible, where the same data is consumed by multiple recipients with different
criticality.

Hence, it is crucial that applications can not only safely communicate on the same criticality level.
They must be able to also safely communicate between different criticality levels.

Support for mixed criticality is a core feature of a communication framework. Hence, it greatly impacts architectural
decisions and influences many other aspects. One of them being performance, which is the third primary aspect of a
communication framework.

Performance
-----------

In the recent years high-performance automotive systems rely more and more on communication of huge amounts of data.
This communication must be performant, to enable decomposition of the system.
With ever increasing complexity of the tasks automotive systems must tackle, this trend will continue in the future.
Hence, architectural decisions for the communication framework must ensure scalable performance.

In general, good scalable performance can be decomposed into two aspects:

1. High throughput
2. Low latency

To achieve both, only zero-copy approaches are feasible.
Further, reliable low-latency communication is only possible with appropriate scheduling.
Meaning, if a consumer is not scheduled when he receives an event, the latency of the communication is out of the hand
of the communication framework.
Thus, the communication framework must be capable to interact with the scheduler to influence the scheduling behavior.

For mixed-criticality safety systems this means, that the original non-duplicated data must be provided to consumers
with different criticality levels.

The previous three key aspects and further aspects are formalized in the section :ref:`Specification`.

Rationale
=========

.. _Specification:

Specification
=============

To provide a clear picture of the base requirements to an IPC communication framework, we formalize the primary and
secondary aspects in this section. For aspects that are mentioned for the first time, we also provide a rationale.
For the previously presented primary aspects, please refer to the section :ref:`Motivation` for the rationale.

Before we can discuss the primary aspects, we must define what basic communication patterns the framework supports.
S-CORE defines in its stakeholder requirements different architectures that must be supported by the communication
framework.
This leads to the three requirements:

9. :need:`FEAT_REQ__ipc__time_based_arch`
10. :need:`FEAT_REQ__ipc__data_driven_arch`
11. :need:`FEAT_REQ__ipc__request_driven_arch`

Based on this, the basic communication elements consist of:

- :need:`FEAT_REQ__ipc__event_type`
- :need:`FEAT_REQ__ipc__method`
- :need:`FEAT_REQ__ipc__signal`

Since often communication regarding a specific feature consists of many of these elements, we allow grouping of them
through communication interfaces (:need:`FEAT_REQ__ipc__interfaces`).

To allow more flexible scheduling of the system and as a prerequisite of :need:`FEAT_REQ__ipc__time_based_arch`,
the communication framework must support caching: :need:`FEAT_REQ__ipc__producer_consumer`

Further, we promote stateless communication :need:`FEAT_REQ__ipc__stateless_communication` to simplify the communication
logic both in the framework as well as the user code.

With the basic syntax for communication covered, we now discuss the key aspects a communication framework must fulfill.

We coin the term "Service instance" to refer to an entity that offers functionality through a communication interface
(:need:`FEAT_REQ__ipc__service_instance`).

In general, we put no restrains in how service instances are grouped in the architecture
(:need:`FEAT_REQ__ipc__service_granularity`).

High cohesion and loose coupling
--------------------------------

As discussed in the motivation, versioning of communication interfaces is key for a communication framework to promote
high cohesion and loose coupling.

Version compatibility can be separated into syntactic compatibility and semantic compatibility.
Communication partners are only capable to communicate properly with each other, if they are compatible in both domains.
Thus, a versioning concept must consider both syntax and semantics.
Therefore, it does not suffice to only version communication interfaces.
Similarly, only versioning the behavior of the functionality behind an interface is not enough.

Instead, we define a single version scheme over both syntax and semantics of a service instance.
Meaning, whenever the service instance has a syntactic or semantic change, the version must be bumped.

This leads to the conclusion that the version is associated to the service instance (:need:`FEAT_REQ__ipc__versioning`).

It is impossible to define a global versioning scheme over all protocols, with their significantly differing
capabilities in that regard. Thus, version compatibility ranges must be supplied per protocol
(:need:`FEAT_REQ__ipc__versioning`).

Additional to versioning, loose coupling also requires that the communication partners are unaware of where their
counterpart resides (:need:`FEAT_REQ__ipc__service_location_transparency`).
This implies, that communication partners are discovered dynamically at runtime
(:need:`FEAT_REQ__ipc__service_discovery`).
Discovery of communication partners must consider their compatibility based on the versioning concept.

To retain loose coupling, the public API of the communication framework shall treat discovery implicitly without
unneeded user involvement (:need:`FEAT_REQ__ipc__service_discovery`).
Further, service discovery is based on a naming scheme where each service instance is associated to one or more names
(:need:`FEAT_REQ__ipc__service_instance_names`).

.. _spec_mixed_criticality:

Mixed-Criticality safety systems
--------------------------------

As discussed in the motivation the communication framework shall support mixed-criticality safety systems
:need:`FEAT_REQ__ipc__safe_communication`.

In the light of mixed-criticality safety systems and based on the failure modes for communication in the ISO26262,
the communication framework gains four additional requirements:

1. :need:`FEAT_REQ__ipc__data_corruption`
2. :need:`FEAT_REQ__ipc__data_reordering`
3. :need:`FEAT_REQ__ipc__data_repetition`
4. :need:`FEAT_REQ__ipc__data_loss`

The communication framework does not take timing related failure modes into account, since the overall stack must
consider such failure modes on a more generic level.

Performance
-----------

Based on the discussion in the motivation, the specific use cases can be condensed to the overall requirement to support
zero-copy IPC (:need:`FEAT_REQ__ipc__zero_copy`).

For now, there is no requirement to support zero-copy communication for other protocols.
While this may be of interest in the future, it remains for now out of scope.

User friendly API for information exchange
------------------------------------------

Programming languages have their own feature set and idioms.
It is crucial for any library that it seamlessly integrates into both.
This means, wherever possible and meaningful, infrastructure of the programming language and accompanying standard
libraries shall be reused.
Further, a developer used to the programming language shall have no problems understanding the API.
It should feel natural to use.
This includes error handling, which shall follow one of the error handling concepts of the programming language.

1. :need:`FEAT_REQ__ipc__lang_idioms`
2. :need:`FEAT_REQ__ipc__lang_infra`

Since S-CORE supports multiple programming languages (see :need:`STKH_REQ__260`), this leads to multiple APIs that might
diverge significantly from each other, but provide the same feature set to the user.
To support something like this, without reimplementing the full communication stack in both languages, an abstraction
layer within the communication framework is unavoidable.

:need:`FEAT_REQ__ipc__multi_lang`

Full testability for the user facing API
----------------------------------------

Our users will be required to proof certain coverage metrics, like line coverage or MC/DC coverage.
For them to reach full coverage, they need to be easily able to mock or fake parts of the communication systems in their
unit tests.
Most of the current solutions (e.g. ara::com) keep this outside their requirements.
This forces the users to introduce an additional abstraction layer over the communication framework to inject test
doubles.
This is additional work for the user, and abstraction layers come with a certain cost in runtime and maintenance.
Our goal is to provide an API that requires no additional abstraction layer over the communication framework.

:need:`FEAT_REQ__ipc__testability_mock_api`

In some test scenarios users must fake communication.
Instead of mocking the fine-granular behavior of the framework, users shall be able to simulate communication simply by
providing an implementation of the communication partner in the test environment. For IPC this does not require big
architectural decisions. In the light of a robust API that also supports communication between multiple hosts,
this can be achieved through multi-binding support.

:need:`FEAT_REQ__ipc__testability_fake_binding`

.. _multi_binding_support:

Multi-binding support
---------------------

In the beginning, S-CORE will only provide inter-process communication.
But this will not suffice for later.
A communication framework for high-performance automotive systems with safety impact will require support for
communication to other VMs or hosts.

Following the idea of service location transparency, we introduce multi-binding support.
A binding is responsible of translating requests from the user to the respective protocol used for communication.
It may do so by directly performing the communication into the chosen protocol without intermediate protocols inbetween.
But it can also use a gateway approach where it forwards the communication using a different protocol (e.g. IPC) to a
gateway which then performs the translation between protocols.

:need:`FEAT_REQ__ipc__multi_binding_support`

To enable service location transparency, the public API is designed to be binding-agnostic.
If the binding is exchanged, the public API remains syntactically and semantically unchanged.

:need:`FEAT_REQ__ipc__binding_agnostic_api`

The framework forwards requests from the public API to the appropriate binding of the service instance.
Bindings are specified in the deployment configuration.

:need:`FEAT_REQ__ipc__multi_binding_depl`

Some possible bindings are:

- IPC  (see :need:`STKH_REQ__2`)
- SOME/IP (see :need:`STKH_REQ__160`)
- DDS (see :need:`STKH_REQ__160`)
- fake binding (for testing)

Dynamic deployment at runtime
-----------------------------

In the light of safety, security and startup requirements, `Service discovery` without some deployment information is
not ideal.
For this reason, most implementations prefer a limited `Service discovery` and supply partial deployment information
in advance.
We too provide partial deployment information through configuration files read at runtime.
This information is enriched through a runtime `Service discovery`.

:need:`FEAT_REQ__ipc__depl_config_runtime`

Tracing
-------

Based on :need:`STKH_REQ__242` the communication framework must support tracing of communication events.
In a framework with multiple bindings, this requires a zero-copy binding-agnostic tracing solution in the abstraction
layer.

:need:`FEAT_REQ__ipc__tracing`

Backwards Compatibility
=======================

As there is currently no previous solution for communication in S-CORE, no backwards compatibility is required.

Security Impact
===============

Security of communication is important for the security of the overall system.
To efficiently handle security with the least amount of overhead, each binding must determine the best security approach
for its circumstances.

Depending on the binding, the security approach may achieve different
`security goals <https://en.wikipedia.org/wiki/Information_security#Security_Goals>`_.

To provide users a generic concept of security configuration on the level of interfaces, the chosen solution of every
binding must map at least to an Access Control List (ACL) concept, but may have additional deployment configuration
options.

The ACL of each service instance is defined in the deployment configuration of producer and consumer.

- :need:`FEAT_REQ__ipc__acl_placement`
- :need:`FEAT_REQ__ipc__acl_per_service_instance`

Entries in the ACL of:

- the producer list the allowed consumers (:need:`FEAT_REQ__ipc__acl_for_producer`)
- the consumer list the allowed producers (:need:`FEAT_REQ__ipc__acl_for_consumer`)

IPC Security Goals
------------------

The security approach of the IPC binding achieves the security goals:

- confidentiality (:need:`FEAT_REQ__ipc__confidentiality`)
- integrity (:need:`FEAT_REQ__ipc__integrity`)
- availability (per criticality-level) (:need:`FEAT_REQ__ipc__acl_placement`)

Safety Impact
=============

The safety impact was already exhaustively covered in :ref:`mot_mixed_criticality` and :ref:`spec_mixed_criticality`.

Overall, the communication framework supports use cases up to ASIL-B (:need:`FEAT_REQ__ipc__asil`).
Future extension to ASIL-D use cases is feasible but not in scope for now.

License Impact
==============

[How could the copyright impacted by the license of the new contribution?]


How to Teach This
=================


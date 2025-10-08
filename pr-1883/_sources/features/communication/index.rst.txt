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

.. _com_feature:

Communication
#############

.. document:: Communication
   :id: doc__com
   :status: valid
   :tags: feature_request

.. toctree::
   :maxdepth: 1
   :glob:
   :titlesonly:
   :hidden:

   docs/**/index
   ipc/index
   some_ip_gateway/index
   abi_compatible_data_types/index

Feature flag
============

To activate this feature, use the following feature flag:

``experimental_com``

.. _com_abstract:

Abstract
========

The Communication Module contains:

- an abstraction layer to enable different communication mechanisms (aka Frontend)
- different bindings which provide the communication functionality (e.g. IPC or Some/IP)

The abstraction layer is designed in a way to ensure full testability for an end-user, while enabling runtime selection
of the underlying communication mechanism with the help of different bindings (e.g. IPC, Some/IP ...).

It provides the user with a high-level API to focus on the content of information – and not on low-level specifics of the used binding. The concept is displayed in Figure :numref:`lola_layers`

.. figure:: _assets/lola_layers.drawio.svg
   :align: center
   :name: lola_layers

   Layered architecture with binding-agnostic mw::com and bindings beneath

.. _com_rationale:

Rationale
=========

S-CORE is targeting high-performance automotive systems with safety impact. In general, these systems consist of multiple processes that are executed on an operating system which also exchange information with other CPUs or ECUs in the system.

Key aspects of S-CORE and therefore also the Communication framework are:

#. :ref:`High cohesion and loose coupling <com_high_cohesion_loose_coupling>`
#. :ref:`Mixed-criticality safety systems <com_mixed_criticality>`
#. :ref:`Performance <com_performance>`
#. :ref:`API Management <com_api_management>`

But also secondary aspect for the Communication framework should not be neglected:

#. :ref:`User friendly API for information exchange <com_user_friendly_api>`
#. :ref:`Full testability for the user facing API <com_testability_user_facing_api>`
#. :ref:`Multi-Binding Support <com_multi_binding_support>`
#. :ref:`Tracing <com_tracing>`

To provide a clearer picture we define which basic communication patterns the framework shall support. S-CORE defines in its stakeholder requirements different architectures that must be supported by the communication framework. This leads to the three requirements:

- :need:`Time Based Architecture <feat_req__com__time_based_arch>`
- :need:`Data Driven Architecture <feat_req__com__data_driven_arch>`
- :need:`Request Driven Architecture <feat_req__com__request_driven_arch>`

Based on this, the basic communication elements consist of:

- :need:`Events <feat_req__com__event_type>`
- :need:`Methods <feat_req__com__method>`
- :need:`Signals <feat_req__com__signal>`

Since often communication regarding a specific feature consists of many of these elements, we allow grouping of them
through :need:`communication interfaces <feat_req__com__interfaces>`.

To allow more flexible scheduling of the system and as a prerequisite of :need:`Time based Architecture <feat_req__com__time_based_arch>`, the communication framework must support :need:`caching <feat_req__com__producer_consumer>`

Further, we promote :need:`stateless communication<feat_req__com__stateless_communication>` to simplify the communication logic both in the framework as well as the user code.

We coin the term :need:`Service instance <feat_req__com__service_instance>` to refer to an entity that offers functionality through a communication interface.

In general, we put no restrains in how :need:`service instances are grouped in the architecture<feat_req__com__service_instance_granularity>`.
In the following we will explain and argue each one of these different aspects from a top level communication point of view.

.. _com_specification:

Specification
=============

.. _com_high_cohesion_loose_coupling:

High cohesion and loose coupling
--------------------------------

Complex systems require high cohesion and loose coupling to remain maintainable. The benefit of loose coupling is to limit the effect of changes throughout the system. Key to achieve this is stability of interfaces.

Since the communication of a module is also part of its interface, we must consider its stability. How stable an interface is, largely depends on the implementation reachable through it. This means, the communication framework can not provide stability on its own. It can only provide the necessary tools for developers to consider the stability when changing the interface or implementation.

.. _com_mixed_criticality:

Mixed-Criticality safety systems
--------------------------------

In complex safety-critical systems, applications often have different criticality. However communication is also required between applications on different criticality levels.

For example, a service with low-criticality may provide data to a highly critical application. Or the reverse could be the case, where a less critical application depends on data produced by a highly critical one. More complex scenarios are also possible, where the same data is consumed by multiple recipients with different criticality.

Hence, it is crucial that applications can also safely communicate between different criticality levels. This assumption adds four additional requirements which are based on the failure modes for communication in the ISO26262:

#. :need:`Data Corruption <feat_req__com__data_corruption>`
#. :need:`Data Reordering <feat_req__com__data_reordering>`
#. :need:`Data Repetition <feat_req__com__data_repetition>`
#. :need:`Data Loss <feat_req__com__data_loss>`

The communication framework does not take timing related failure modes into account, since the overall stack must
consider such failure modes on a more generic level.

Support for mixed criticality is a core feature of a communication framework. Hence, it greatly impacts architectural
decisions and influences many other aspects. One of them being performance, which is the third primary aspect of a
communication framework.

.. _com_performance:

Performance
-----------

In the recent years high-performance automotive systems rely more and more on communication of huge amounts of data. This communication must be performant, to enable decomposition of the system. With ever increasing complexity of the tasks automotive systems must tackle, this trend will continue in the future. Hence, architectural decisions for the communication framework must ensure scalable performance.

In general, good scalable performance can be decomposed into two aspects:

1. High throughput
2. Low latency

Further, reliable low-latency communication is only possible with appropriate scheduling. Meaning, if a consumer is not scheduled when he receives an event, the latency of the communication is out of the hand of the communication framework. Thus, the communication framework must be capable to interact with the scheduler to influence the scheduling behavior.

To also achieve a high throughput the focus of the development shall focus on :need:`zero-copy <feat_req__com__zero_copy>` solutions.

.. _com_api_management:

API Management
--------------

Version compatibility can be separated into *syntactic* compatibility and *semantic* compatibility. Communication partners are only capable to communicate properly with each other, if they are compatible in both domains. Thus, a versioning concept must consider both syntax and semantics. Therefore, it does not suffice to only version communication interfaces. Similarly, only versioning the behavior of the functionality behind an interface is not enough.

Instead, we define a single version scheme over both syntax and semantics of a service instance. Meaning, whenever the service instance has a syntactic or semantic change, the version must be bumped. This leads to the conclusion that the version is associated to the service instance.

It is impossible to define a global versioning scheme over all protocols, with their significantly differing
capabilities in that regard. Thus, :need:`version compatibility <feat_req__com__versioning>` ranges must be supplied per protocol.

Additional to versioning, loose coupling also requires that the communication partners are unaware of where their
:need:`counterpart resides <feat_req__com__service_location_transparency>`. This implies, that communication partners are :need:`discovered dynamically <feat_req__com__service_discovery>` at runtime .

Discovery of communication partners must consider their compatibility based on the versioning concept.

To retain loose coupling, the public API of the communication framework shall treat discovery implicitly without
unneeded user involvement (:need:`feat_req__com__service_discovery`). Further, service discovery is based on a naming scheme where each service instance is associated to one or more names (:need:`feat_req__com__service_instance_names`).

.. _com_user_friendly_api:

User friendly API for information exchange
------------------------------------------

Programming languages have their own feature set and idioms. It is crucial for any library that it seamlessly integrates into both. This means, wherever possible and meaningful, infrastructure of the programming language and accompanying standard libraries shall be reused. Further, a developer used to the programming language shall have no problems understanding the API. It should feel natural to use. This includes error handling, which shall follow one of the error handling concepts of the programming language.

#. :need:`Language Idioms <feat_req__com__lang_idioms>`
#. :need:`Language infrastructure <feat_req__com__lang_infra>`

Since S-CORE supports multiple :need:`programming languages <stkh_req__dev_experience__prog_languages>`, this leads to multiple APIs that might diverge significantly from each other, but provide the same feature set to the user.
To support something like this, without reimplementing the full communication stack in both languages, an abstraction
layer within the communication framework is unavoidable.

:need:`feat_req__com__multi_lang`

.. _com_testability_user_facing_api:

Full testability for the user facing API
----------------------------------------

Our users will be required to proof certain coverage metrics, like line coverage or MC/DC coverage. For them to reach full coverage, they need to be easily able to mock or fake parts of the communication systems in their unit tests.

Most of the current solutions (e.g. ara::com) keep this outside their requirements. This forces the users to introduce an additional abstraction layer over the communication framework to inject test doubles.

This is additional work for the user, and abstraction layers come with a certain cost in runtime and maintenance. Our goal is to provide an API that requires no additional abstraction layer over the communication framework.

:need:`feat_req__com__testability_mock_api`

In some test scenarios users must fake communication:

Instead of mocking the fine-granular behavior of the framework, users shall be able to simulate communication simply by
providing an implementation of the communication partner in the test environment. For communication this does not require big architectural decisions. In the light of a robust API that also supports communication between multiple hosts, this can be achieved through multi-binding support.

:need:`feat_req__com__testability_fake_binding`

.. _com_multi_binding_support:

Multi-binding support
---------------------

Following the idea of service location transparency, we introduce multi-binding support.
A binding is responsible of translating requests from the user to the respective protocol used for communication.
It may do so by directly performing the communication into the chosen protocol without intermediate protocols inbetween.
But it can also use a gateway approach where it forwards the communication using a different protocol (e.g. IPC) to a
gateway which then performs the translation between protocols.

:need:`feat_req__com__multi_binding_support`

To enable service location transparency, the public API is designed to be binding-agnostic.
If the binding is exchanged, the public API remains syntactically and semantically unchanged.

:need:`feat_req__com__binding_agnostic_api`

The framework forwards requests from the public API to the appropriate binding of the service instance.
Bindings are specified in the deployment configuration.

:need:`feat_req__com__multi_binding_depl`

Some possible bindings are:

- :need:`IPC <stkh_req__communication__inter_process>`
- :need:`SOME/IP <stkh_req__communication__supported_net>`
- :need:`DDS <stkh_req__communication__supported_net>`
- :ref:`fake binding<mock_binding>` (for testing)

In the beginning, S-CORE will only provide inter-process communication.
But this will not suffice for later.
A communication framework for high-performance automotive systems with safety impact will require support for
communication to other VMs or hosts.

.. _mock_binding:

Mock Binding
^^^^^^^^^^^^

To support users in their testing efforts, the communication framework must provide support for mocking and faking.
Since the public API of mw::com is highly templated, most testing frameworks would reach their limits.
So instead of making the public API directly mockable, we use the binding concept to provide a mock binding.
The mock binding utilizes the GMock framework.

.. _dynamic_deployment_runtime:

Dynamic deployment at runtime
-----------------------------

In the context of safety, security and startup requirements, `Service discovery` without some deployment information is
not ideal.
For this reason, most implementations prefer a limited `Service discovery` and supply partial deployment information
in advance.
We too provide partial deployment information through configuration files read at runtime.
This information is enriched through a runtime `Service discovery`.

:need:`feat_req__com__depl_config_runtime`

.. _com_tracing:

Tracing
-------

The communication framework must support :need:`tracing of communication events <stkh_req__dev_experience__tracing_of_comm>`. In a framework with multiple bindings, this requires a zero-copy binding-agnostic tracing solution in the abstraction layer.

:need:`feat_req__com__tracing`


Architecture
------------

The architecure of communication is displayed :ref:`here<com_architecture>`

Requirements
------------

The requirements for communication are listed :ref:`here<com_requirements>`

.. _com_security_impact:

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

- :need:`ACL Placement <feat_req__com__acl_placement>`
- :need:`ACL per Service Instance <feat_req__com__acl_per_service_instance>`

Entries in the ACL of:

- the producer list the :need:`allowed consumers <feat_req__com__acl_for_producer>`
- the consumer list the :need:`allowed producers <feat_req__com__acl_for_consumer>`

.. _com_safety_impact:

Safety Impact
=============

The safety impact was already exhaustively covered in :ref:`com_mixed_criticality`.

Overall, the communication framework supports use cases up to :need:`ASIL-B <feat_req__com__asil>`. Future extension to ASIL-D use cases is feasible but not in scope for now.

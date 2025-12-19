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

.. _com_architecture:

Architecture
============

Overview
--------

An brief overview of communication is described :ref:`here <com_abstract>`.

Description
-----------

A description of the communication module is located :ref:`here <com_rationale>`

.. _com_static_architecture:

Static Architecture
-------------------

As discussed in :ref:`com_rationale`, the overall architecture of the communication framework must be layered. This is required, to separate the frontend from the underlying communication mechanisms (also called bindings).

This ensures a stable public API, independent of the underlying binding(s). At the same time, the communication framework can support many different communication protocols in a flexible manner.

.. feat_arc_sta:: Feature Architecture Communication
   :id: feat_arc_sta__com__communication
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces
   :includes: logic_arc_int__communication__user

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}
      mod_view_sta__tracing__tracing -[hidden]-> mod_view_sta__baselibs__baselibs

In the following sections we will look on the different architectural elements of the communication framework in more
detail.

Frontend
^^^^^^^^

The frontend is responsible of providing a stable public API to the user. In general, the communication framework (`mw::com`) follows the client-server, pub-sub and producer-consumer patterns.

Following these patterns, the user interacts with different APIs depending on whether he is producer/server or
consumer/client.

A producer creates a `Skeleton` to communicate with consumers. Each consumer creates a `Proxy` to connect to a producer. Consumers can find available producers through a service discovery mechanism. This mechanism is tightly bound to the `Proxy`, to only discover producers offering a compatible implementation of a `Skeleton`.

.. uml::
    :scale: 50
    :align: center
    :name: doc__communication__proxy_skeleton
    :caption: Communication through mw::com

    package "Consumer" <<Rectangle>> {
        package "Frontend" <<Frame>> #D5E8D4 {
        object "Proxy" as proxy_t
        }
        package "Binding" <<Frame>> #DAE8FC {
        object "Proxy" as proxy_b
        }
    }

    package "Producer" <<Rectangle>>  {
        package "Frontend" <<Frame>> #D5E8D4 {
        object "Skeleton" as skeleton_t
        }
        package "Binding" <<Frame>> #DAE8FC {
        object "Skeleton" as skeleton_b
        }
    }

    skeleton_t -d-> skeleton_b
    proxy_t -d-> proxy_b
    proxy_b -l(0- skeleton_b

In addition to these elements, a runtime singleton is used for background tasks to reduce resource consumption. This runtime is invisible to the user. This runtime is responsible for service discovery (explained in :ref:`ipc_service_discovery`), notification reception and other infrastructure tasks.

Compatibility of *Skeleton* and *Proxy* is currently defined by them sharing the same communication interface. Additionally, versioning will be taken into account in the future (see :ref:`ipc_roadmap`).

The communication interface for now consists of events. Support for methods and signals will be added in the future
(see :ref:`ipc_roadmap`).

Since S-CORE supports strongly typed programming languages, the API of *Skeleton* and *Proxy* is also strongly typed. Instead of a code generator, we utilize features like templates in C++ and macros in Rust to "generate" the necessary code at compile time.

But there are some "niche" use cases, where the need to "regenerate" and recompile the *Proxy* can be detrimental.
This is the case when:

- signatures are trivial and changes/differences between them are minimal
- the communicated data/payload gets handled very generically (loosely typed) anyhow
- the communicated data/payload has to get deep-inspected based on additional/separate type-information anyhow

For these cases *mw::com* provides a *GenericProxy* that allows introspection of communication interfaces at runtime.

While the frontend is based on a communication model, it is independent from any communication protocol. Therefore, it always forwards user requests to the binding(s) underneath. Which bindings to use is defined in a configuration file.

A multi-binding approach is chosen, where API calls are mapped to a set of selected bindings.

Interface Description
^^^^^^^^^^^^^^^^^^^^^

The public API for the frontend is defined as:

.. logic_arc_int:: Communication User Interface
   :id: logic_arc_int__communication__user
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

Bindings
^^^^^^^^

The need for bindings was discussed in :ref:`com_multi_binding_support`.
Bindings reside beneath the frontend layer and accept the forwarded requests

Currently, the available bindings are:

- :ref:`IPC (LoLa) <communication_ipc>`
- :ref:`mock binding <mock_binding>`

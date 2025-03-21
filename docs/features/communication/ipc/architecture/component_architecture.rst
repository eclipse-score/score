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

Component Architecture
######################

Technical Concept Description
*****************************

As discussed in :ref:`ipc_feature`, the overall architecture of the communication framework must be layered.
This is required, to separate the frontend from the underlying communication mechanisms (also called bindings).

This ensures a stable public API, independent of the underlying binding(s).
At the same time, the communication framework can support many different communication protocols in a flexible manner.

.. image:: _assets/lola_layers.drawio.svg
   :alt: Layered architecture with binding-agnostic mw::com and bindings beneath

In the following sections we will look on the different architectural elements of the communication framework in more
detail.

Frontend
========

The frontend is responsible of providing a stable public API to the user.
In general, the communication framework (`mw::com`) follows the client-server, pub-sub and producer-consumer patterns.

Following these patterns, the user interacts with different APIs depending on whether he is producer/server or
consumer/client.

A producer creates a `Skeleton` to provide events to consumers.
Each consumer creates a `Proxy` to connect to a producer.
Consumers can find available producers through a service discovery mechanism.
This mechanism is tightly bound to the `Proxy`, to only discover producers offering a compatible implementation of a
`Skeleton`.

.. document:: Communication through mw::com
   :id: doc__communication__proxy_skeleton
   :safety: ASIL_B
   :status: valid

   .. needarch::
      :scale: 50
      :align: center

      allowmixing


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

Additional to these elements, a runtime singleton is used for background tasks to reduce resource consumption.
This runtime is invisible to the user.
This runtime is responsible for service discovery (explained in :ref:`service_discovery`), notification reception and
other infrastructure tasks.

Compatibility of `Skeleton` and `Proxy` is currently defined by them sharing the same communication interface.
Additionally, versioning will be taken into account in the future (see :ref:`roadmap`).

The communication interface for now consists of events. Support for methods and signals will be added in the future
(see :ref:`roadmap`).

Since S-CORE supports strongly typed programming languages, the API of `Skeleton` and `Proxy` is also strongly typed.
Instead of a code generator, we utilize features like templates in C++ and macros in Rust to "generate" the necessary
code at compile time.

But there are some "niche" use cases, where the need to "regenerate" and recompile the `Proxy` can be detrimental.
This is the case when:

- signatures are trivial and changes/differences between them are minimal
- the communicated data/payload gets handled very generically (loosely typed) anyhow
- the communicated data/payload has to get deep-inspected based on additional/separate type-information anyhow

For these cases mw::com provides a `GenericProxy` that allows introspection of communication interfaces at runtime.

While the frontend is based on a communication model, it is independent from any communication protocol.
Therefore, it always forwards user requests to the binding(s) underneath.
Which bindings to use is defined in a configuration file.

A multi-binding approach is chosen, where API calls are mapped to a set of selected bindings.
Currently, the available bindings are:

- IPC (LoLa)
- mock binding

Bindings
========

The need for bindings was discussed in :ref:`multi_binding_support`.
Bindings reside beneath the frontend layer and accept the forwarded requests.

IPC Binding
-----------

The basic idea of the ipc binding concept is to use two main operating system facilities:

1. Shared Memory: Shall be used for the heavy lifting of data exchange
2. Message Passing: Shall be used as notification mechanism

We decided for this side channel since implementing a notification system via shared memory would include the usage of
condition variables.
These condition variables would require a mutex.
This could lead to the situation that a malicious process could lock the mutex forever and thus destroy any event
notification.
In general we can say that any kind of notification shall be exchanged via message passing facilities.
The section :ref:`message_passing_facilities` below will go into more detail.

The usage of shared memory has some implications.
First, any synchronization regarding thread-safety / process-safety needs to be performed by the user.
Second, the memory that is shared between the processes is directly mapped into their virtual address space.
This implies that it is easy for a misbehaving process to destroy or manipulate any data within this memory segment.
In order to cope with the latter, we split up the shared memory into three segments.

- First, a segment where only the to-be-exchanged data is provided.
  This segment shall be read-only to consumers and writeable by the producer.
  This will ensure that nobody besides the producer process can manipulate the provided data.
- The second and third segment shall contain necessary control information for the data segment.
  Necessary control information can include atomics that are used to synchronize the access to the data segments.
  Since this kind of access requires write access, we split the shared memory segments for control data by ASIL Level.
  This way it can be ensured that no low-level ASIL process interferes with higher level ones.
  More information on shared memory handling can be found in :ref:`shared_memory_handling`.

.. image:: _assets/lola_mixed_crit_1_n.drawio.svg
   :alt: Mixed criticality setup for zero-copy IPC

One of the main ideas in this concept is the split of control data from sample (user) data.
In order to ensure a mapping, the shared memory segments are divided into slots.
By convention, we then define that the slot indexes correlate.
Meaning, slot 0 in the control data is used to synchronize slot 0 in the sample data.
More information on these slot and the underlying algorithm can be found in :ref:`synchronization_algorithm`.

.. image:: _assets/lola_slots.drawio.svg
   :alt: Relation of control data and sample data

.. _message_passing_facilities:

Message Passing Facilities
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Message Passing facilities, will not be used to synchronize the access to the shared memory segments.
This is done over the control segments.
We utilize message passing for notifications only.
These notifications include:

- event notification
- partial restart

This is done, since there is no need to implement an additional notification handling via shared memory, which would
only be possible by using mutexes and condition variables.
The utilization of mutexes would make the implementation of a wait-free algorithms more difficult.

Instead, we use an OS feature for notification:

- QNX Message Passing (under QNX)
- Unix Domain Sockets (under Linux)

As illustrated in the graphic below a process should provide one message passing port to receive data for each supported
ASIL-Level.
In order to ensure that messages received from QM processes will not influence ASIL messages, each message passing port
shall use a custom thread to wait for new messages.
Further, it must be possible to register callbacks for mentioned messages.
These callbacks shall then be invoked in the context of the socket specific thread.
This way we can ensure that messages are received in a serialized manner.

.. image:: _assets/lola_message_passing.drawio.svg
   :alt: Message Passing in LoLa

.. _shared_memory_handling:

Shared Memory Handling
^^^^^^^^^^^^^^^^^^^^^^

POSIX based operating systems generally support two kinds of shared memory:

- file-backed
- anonymous

Former is represented by a file within the file-system, while the latter is not visible directly to other processes.
We decide for former, in order to utilize the filesystem for a simpler service discovery.
In order to avoid fault propagation over restarts of the system, any shared memory communication shall not be
persistent.
Processes will identify shared memory segments over their name.
The name will be commonly known by producers and consumers and deduced by additional parameters like for example service
id and instance id.
When it comes to the granularity of the data stored in the shared memory segments, multiple options can be considered.
We could have one triplet of shared memory segments per process or one triplet of shared memory segments per event
within a service instance.
Former would make the ASIL-Split of segments quite hard, while the latter would explode the number of necessary segments
within the system.
As trade-of we decided to have one triplet of shared memory segments per service instance.

It is possible to map shared memory segments to a fixed virtual address.
This is highly discouraged by POSIX and leads to undefined behaviour.
Thus, shared memory segments will be mapped to different virtual addresses.
In consequence no raw pointer can be stored within shared memory, since it will be invalid within another process.
Only offset pointer (fancy pointer, relative pointer) shall be stored within shared memory segments.

The usage of shared memory does not involve the operating system, after shared memory segments are setup.
Thus, the operating system can no longer ensure freedom from interference between processes that have access to these
shared memory regions.
In order to restrict access we use ACL support of the operating system.

In addition to the restricted permissions, we have to ensure that a corrupted shared memory region cannot influence
other process-local memory regions.
This can be ensured by performing Active Bounds Checking.
So the only way how data corruption could propagate throughout a shared memory region is if a pointer within a shared
memory region points out of it.
Thus, a write operation to such a pointer could forward memory corruption.
The basic idea to overcome such a scenario is, that we check that any pointer stays within the bounds of the shared
memory region.
Since anyhow only offset pointers can be stored in a shared memory region, this active bounds check can be performed
whenever a offset pointer is dereferenced.

The last possible impact can be on timing.
If another process for example wrongly locks a mutex within the shared memory region and another process would then wait
for this lock, we would end up in a deadlock.
While timing is explicitly not a safety requirement (see :ref:`spec_mixed_criticality`), we still want to strive for
wait-free algorithms to avoid such situations.
Further, avoiding mutexes in our algorithms increases performance since it reduces kernel calls.

.. _synchronization_algorithm:

Synchronization Algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^

A slot shall contain all necessary meta-information in order to synchronize data access.
This information most certainly needs to include a timestamp to indicate the order of produced data within the slots.
Additionally, a use count is needed, indicating if a slot is currently in use by one process.
The concrete data is implementation defined and must be covered by the detailed design.

The main idea of the algorithm is that a producer shall always be able to store one new data sample.
If he cannot find a respective slot, this indicates a contract violation, which indicates that a QM process misbehaved.
In such a case, a producer should exclude any QM consumer from the communication.

This whole idea builds up on the split of shared memory segments by ASIL levels.
This way we can ensure that an QM process will not degrade the ASIL Level for a communication path.
In another case, where we already have a QM producer, it is possible for an ASIL B consumer to consume the QM data.
In this scenario, there is no separate control data for ASIL B, and they instead interact on the control data
for ASIL QM.
This is because, the data is QM and it is impossible for the middleware to apply additional checks to
enhance the quality of data.
This can only be done on application layer level.
Hence, separating QM and ASIL consumers holds no benefit.

.. _service_discovery:

Service Discovery
^^^^^^^^^^^^^^^^^

The communication framework must be capable to discover available service offers at runtime.
The offered services are differentiated by:

- service id (a unique identifier per different service interface)
- instance id (a unique identifier per different producer offering the same service interface)
- criticality level
- version (not yet supported, see :ref:`roadmap`)

To reduce resource consumption we decide against using an approach with a service registry daemon.
Instead we choose to use operating system facilities to achieve a performant service discovery.

The key technology behind the service discovery is the inotify subsystem of POSIX compliant operating systems.
It allows resource efficient and performant tracking of changes in the filesystem.

Keeping track of available service instances is left to the operating system.
Producers notify the OS about new service offers by creating a flag file.
Consumers either crawl the filesystem for existing offers or attach an inotify watch to wait for upcoming offers.
Whenever a new file is created, the OS automatically checks for impacted inotify watches and notifies each watch with
an appropriate event.

Also complex search requests where a consumer wants to know about all service instances with the same service interface,
can be solved efficiently with the inotify subsystem.

Service discovery is currently fully explicit.
Implicit service discovery for consumers is on our :ref:`roadmap`.
The goal is to handle service discovery transparently wherever possible.

Partial Restart Capability
^^^^^^^^^^^^^^^^^^^^^^^^^^

Partial restart capability means, that one of several communication partners may crash at any point in time and will
still be able to start up again and rejoin the communication, without affecting the other communication partners.

Challenge to overcome
"""""""""""""""""""""

There is a shared state held in shared memory (the control data), which is maintained by all communication partners
(provider and consumers).
Consumers annotate within this shared state, which data (events/fields) they are currently
consuming (and therefore blocking underlying slots from re-use by the producer).
The provider annotates within this shared state, which slots are currently blocked for data updates that can't be
accessed by consumers.

When a communication partner crashes, it may leave slots blocked within the shared state.
When it restarts later, it has to reclaim/re-use or free exactly the same slots, it claimed in a previous run.
Not doing so, would lead to resource exhaustion, since the slots would remain blocked indefinitely for either the
producer or consumers.
This requires, that a restarting communication partner knows exactly, which changes it had done to the shared state
previously in order to roll them back again.

Recovery mechanism
""""""""""""""""""

The mechanism to enable the cleanup/recovery of shared state by a restarting communication partner is based
on transaction logs:

Each consumer and the producer owns a corresponding transaction log, which resides in shared memory.
They annotate what change to the shared state they are going to do.
Creating a transaction log entry means:

1. Writing a transaction begin marker, which completely describes, which change the upcoming activity will do.
2. Executing the activity in question.
3. Writing a transaction end marker, which annotates, whether the activity in (2) was done or not.

During the restart of a communication partner, he checks for existing transaction logs in shared memory, which it
created in an earlier run, so that it can roll them back.

Two scenarios are possible:

- All transaction log entries are complete (transaction end marker is written).
  The communication partner can roll all transactions back and rejoin communication.
- A transaction log entry is incomplete (transaction end marker is missing).
  The communication partner is incapable of rolling back his actions fully.
  Rejoining the communication would impact other communication partners.
  The communication partner is barred from rejoining the communication.

We reduce the likelihood of the second scenario, by using transactions only when unavoidable and by keeping them short.

Mock Binding
------------

To support users in their testing efforts, the communication framework must provide support for mocking and faking.
Since the public API of mw::com is highly templated, most testing frameworks would reach their limits.
So instead of making the public API directly mockable, we use the binding concept to provide a mock binding.
The mock binding utilizes the GMock framework.

Interfaces
**********


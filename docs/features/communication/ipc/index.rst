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
   #
   # Authors
   # @hartmannnico,


Communication Framework
#######################

The Communication Framework handles the safe, secure and performant exchange of information between software and/or hardware components of the Score stack.

Communication covers information exchange between endpoints residing in

* the same or different process, running on
* the same or different operating systems, deployed on
* the same or different compute devices, built into
* the same or different devices.

In current communication designs (SomeIP, Protobuf, Zenoh) communication on networks is at the centerpoint of considerations. We believe this to be the wrong approach for software defined machines. Network based communication circles around protocols based on a wire based communication paradigm, requiring serialization and segmentation of data.

Instead, we promote a memory centered core paradigm and put Inter-Process Communication (IPC) into our conceptional focus. This allows for true zero copy design, does not segment or serialize data and fosters significantly higher performance in algorithms. As a bonus, it provides easy gateway mechanisms into serial communication like Ethernet and CAN.

The communication framework is independent of the domain of the application it is used in.

General Architecture
--------------------

The communication framework defines two central groups of elements:

* Information Elements
* Infrastructure Elements

While the former carry the information exchanged the latter provide the means through which the information is exchanged.

Information Elements
````````````````````

There are three fundamental concepts of information exchange defined. One communication element represents each concept:

* **Topics**: A topic is the information carrier for **data**. A unique Id identifies a topic while a *data type* defines it's memory layout. The topic carries zero or multiple *values*. A value represents a single instances of the data type. See `Topics`_, `Names`_, `Data Types`_.
* **Remote Procedures**: A remote procedure is the information carrier for **execution** progress. A Id handle identifies the remote procedure together with an ordered set of named *parameters*. Each parameter defined by a data type. A caller of a remote procedure can cause it's activation by invoking the remote procedure with passed *arguments*. An argument is a single value instance for a parameter. See `Remote Procedures`_, `Names`_, `Data Types`_.
* **Events**: An event is the information carrier for runtime **synchronization**. A unique Id identifies the event. It signals the change of state. There is no data conveyed with the event. See `Events`_, `Names`_.

While the Id uniquely identifies an information element within the communication framework, it can also have a *name* as alias to conveniently identify the element. While the Id may not be publicly known, the *name* allows for public lookup.


Infrastructure Elements
```````````````````````

Infrastructure elements provide the means through which the information exchange executes.
We define three fundamental building elements:

* **Endpoints**: Endpoints are both the source and the target of every information exchange in teh communication framework. An endpoint providing information is consequently called a *provider*. With the same logic a *consumer* is an endpoint consuming information. Endpoints have an *Id* that uniquely identifies the endpoint within a node.
* **Nodes**: A node is an entity in the communication system that hosts several endpoints. It is the central element of the communication fabric by connecting endpoints and routing data. Nodes have an *Id* that uniquely identifies the node within a fabric. A node itself is also an endpoint.
* **Links**: A link is the fundamental abstraction of a connection between any two nodes. A link conveys information between nodes.

The combination of NodeId and EndpointId we also refer to as *address*. As nodes are also endpoints, they implicitly have an address.

Nodes and endpoints may also be identified by a *name* that resolves into references to these elements. See `Names`_, `References`_.

Connecting nodes though links creates a mesh of nodes that can mutually exchange information utilizing the above concepts. The boundary of the mesh is at the sole discretion of the deployment and may span from a single application into a connected cloud environment.

The entirety of connected nodes within a mesh we call *fabric*.

.. admonition:: Design Note

   From a perspective of safety, a node also encapsulates a single safety domain. Links provide the means for separating safety domains and thus allow for mixed criticality applications.


Names
-----

A name is an UTF-8 tag of an element. The underlying Unicode standard is `release 16.0.0 <https://www.unicode.org/versions/Unicode16.0.0>`_.

All codepoints are valid in a name with the exception of the following codepoints:

* the *control* codepoints ``&#0000`` to ``&#001F``
* the *dot* separator, codepoint ``FULL STOP``: ``.`` ``&#002E``
* the *path separator*, codepoint ``SOLIDUS``: ``/`` ``&#002F``
* the *wildcard* marker, codepoint ``ASTERISK``: ``*`` ``&#002A``
* the *any* marker, codepoint ``QUESTION MARK``: ``?`` ``&#003F``

Forbidden as first character in a name is

* the *reference* marker codepoint ``AMPERSAND``: ``&`` ``&#0026``. It's use is discouraged in names in general.

Further discouraged is the use of the *whitespace* codepoint ``SPACE``: `` `` ``&#0020``.

Element names prefixed with an underscore ``LOW LINE``: ``_`` ``&#005F`` are regarded to have *private* visibility within the scope they are defined in. While references to private elements are possible, name resolution ony works from within the namespace they are defined in.

.. admonition:: Design Note

   A name is not a property of an element itself.
   Instead, a name acts as an *alias* to obtain an element *reference*.
   See `References`_.


Namespaces
----------

A namespace is a named scope in which the definition of the elements topic, remote procedures, event and recursively namespace is valid.

General rules of names apply to namespace names.

Namespaces can be nested.
The path separator between the names is the unicode codepoint ``SOLIDUS``: ``/`` ``&#002F``.

::

   This/is/a/nested/namespace


The namespace name ``/`` is reserved and refers to the global namespace.
*Global* here means visible with respect to a certain realm that is not further defined. A realm can be a vehicle with it's attached cloud environment or just an application context. It is up to deployment to define the scope of the global namespace.

The namespace name ``super`` is reserved and refers to the parent namespace of the namespace where ``super`` is used. The use of ``super`` in the global namespace is an error.

The namespace name ``package`` is reserved for future use. It must appear as first name in a path.


Scoping Rules
`````````````

Namespaces isolate a naming scope from another. Within a namespace element names must be unique.

Elements in one namespace are by default not visible to elements in other namespaces.

::

   namespace A
      topic T: Int8     // This is T in A

   namespace B
      topic T: Float64  // This is T in B

The topics ``A/T`` and ``B/T`` are different.

Namespaces can be nested, i.e. within a namespace another namespace can exist.

::

   namespace A
      topic T: Int8     // This resides in namespace A

      namespace Aa
         topic T: Int8  // This T resides in namespace A/Aa


A namespace can *use* elements of another namespace thus making it visible under a given or implied local name.

::

   namespace A
      topic Important: Int8

      namespace Aa
         topic Nested: Int8

   namespace B
      use A/Important   // makes topic "Important" visible in B
      use A/Aa          // makes namespace "Aa" visible in B

      algorithm
         access Important
         access Aa/Nested

A ``use`` clause may end with the wildcard ``ASTERISK``: ``*`` ``&#002A``. This indicates the mapping of all elements of the given namespace into the current scope.

::

   namespace A
      topic One: Int8
      topic Two: Int8

   namespace B
      use A/*     // makes One and Two visible in B

      algorithm
         access One  // valid, One is visible in B
         access Two  // valid, Two is visible in B


Within a namespace elements from another namespace are visible without an explicit use when a resolving path is given.

::

   namespace A
      topic Important: Int8

   namespace B
      algorithm
         access A/Important


Handles
-------

A handle is a numeric value that uniquely refers to an individual element in the communication system.

The numeric value can safely be transported through the communication system and shall be resolvable into a reference of the original element.

Data Types
----------

Data types describe the inner structure of data entities known as values.
A specific data type will always have the identical memory layout, independent from compiler, operating system and controller architecture.


Primitive Types
```````````````

Primitive data types consist of a single element with no further inherent structure.
The following primitive data types and their Rust and C++ representation are defined:

========= ========== ========= ========================== ====== ============================
Data Type Class      Rust      C++                        Size   Description
========= ========== ========= ========================== ====== ============================
Bool      Boolean    ``bool``  ``bool``                   1      A boolean value, true or false
Int8      Integer    ``i8``    ``int8_t``                 1      An 8 bit signed integer
UInt8     Integer    ``u8``    ``uint8_t``                1      An 8 bit unsigned integer
UInt128   Integer    ``u128``  ``uint128_t``              16     An 128 bit unsigned integer
Float16   Floating   ``f16``   ``float16_t``              2      An IEEE 756 32 bit floating point
Float32   Floating   ``f32``   ``float``, ``float32_t``   4      An IEEE 756 32 bit floating point
Float64   Floating   ``f64``   ``double``, ``float64_t``  8      An IEEE 756 64 bit floating point
BFloat16  Floating   ``bf16``  ``bfloat16_t``             2      A Google brain float 16 floating point
TFloat32  Floating   ``tf32``  ``tfloat32_t``             4      An NVIDIA tensor float 32 floating point
Char      String     ``char``  ``char32_t``               4      A unicode codepoint (32 bit)
String    String     ``str``   -                          n/a    A UTF-8 encoded text
Handle    Reference  -         -                          8      A 64 bit unsigned integer handle
========= ========== ========= ========================== ====== ============================

The type ``Byte`` may be used as alias for ``UInt8``.
The type ``Handle`` may be used as alias for ``UInt64``.

Tuples
``````

Tuples are ordered collections of arbitrary data types. A tuple shall be expressed by parentheses:
``(Int8, Float32)``.

The empty Tuple `()` is called the *unit* type, identifying the type with no data. The unit type can carry the one and only one value `()`.

There is no explicit Data Type for neither `Empty`, `Void` or `None`.


Structs
```````

A struct is an ordered collection of named arbitrary data types called fields:

::

   struct MyStruct {
      field1: Int8,
      field2: Float32
   }

Arrays
``````

Arrays are ordered collections of data elements of the same type with a fixed length. A single element is addressed by an *index*:

::

   Char[32]


Tensors
```````

A Tensor is a multi-dimensional array of numerical values that generalizes scalars, vectors, and matrices to higher dimensions, commonly used in mathematics, physics, and machine learning.

The number of dimensions is called the *rank* or *order* of the Tensor.
The vector of dimensions with the Tensor's rank is called the *shape* of the Tensor.

::

   Tensor<Float16, [5, 5, 128]>

The 5x5 kernel of a CNN layer with 128 features.

List
````

A List is an ordered collection of data elements of the same type with a variable length. A single element is addressed by an *index*:

::

   List<Char>

HashMap
```````

A HashMap is an unordered collection of data element of the same type with variable length. A single element is addressed by a *key* of a specific data type.

::

   HashMap<UInt32, String>


Pointers
````````

There are no data types defined for pointers to data types.

References
``````````

The communication framework allows for three potential classes of references:

* References to data types

   There are no data types defined for references to data types.

* References to information elements

   * Topic References, data type ``TopicRef``
   * Remote Procedure References, data type ``FnRef``
   * Event References, data type ``EventRef``

* References to infrastructure elements

   Currently we do not define references to infrastructure elements.
   However, for conceptual symmetry reasons and application value they
   might come up in future versions.

The `AMPERSAND`: `&` `&#0026` as first character in a path is defined as the marker for references to information elements.

In names and paths the reference marker to an information element of a path.

::

   &/Body/Doors/Windows/LeftFront/Position

References the topic of the top left windows's position.

A Reference shall have a corresponding unique handle. The communication framework shall be able to dispatch handles of references like any other value of a data type. The underlying value type for handles should be ``UInt64`` and must have lockfree atomic read and write operations available.

The application should not have access to handles directly, but only to the references themselves. We call the conversion of a handle into a reference “resolution of the handle”.

The operations granted through a reference to an information item shall be identical to the operations of the information item itself.


.. admonition:: Implementation Note

   Internally, the communication framework may actually only pass TopicRef's to the application. From a semantic view it makes no difference to hold a TopicRef or a Topic directly.

.. admonition:: Implementation Note

   A ``TopicRef`` is *not* the same as ``&Topic`` as it may require additional validity checks.


Topics
------

A topic is an information carrier for data elements. Data elements have a data type and zero to multiple values, following the format and layout defined by the type.

Publisher & Subscriber
``````````````````````

A topic follows the publisher/subscriber pattern. This means

- A topic exists on it's own. The framework's data communication system owns the topic.
- A topic can have zero or one publishers. The publisher updates ('publishes') new data into the topic.
- A topic can have zero or multiple subscribers. A subscriber consumes the data published into the topic.

Queue
`````

A topic stores it's values in a queue with a given depth. The queue has a policy that defines the behavior of new data published. There are four policies when the queue is full:

- Ignore: New data is ignored.
- Overwrite oldest: New data overwrites the oldest element. This makes the topic a ring buffer.
- Replace latest: New data replaces the latest element. This makes the latest update always available.
- Error: Writing new data to the topic raises an error at the subscriber (and potentially in the topic)

Namespace and Name
``````````````````

A topic can have a name that exists within a namespace. The name is not an attribute of the topic itself. Instead, it is an alias to the topic's reference that allows access to the data of the topic.

Lifetime
````````

Once created, the topic belongs to the communication framework which determines it's lifetime.

A topic must live while it is in use, i.e. it has a publisher and/or subscribers.


Remote Procedures
-----------------

A remote procedure is an invokable information element that receives a set of values ('arguments') following a given signature ('parameters') individual to each invocation.

The invocation happens asyncronously. I.e. the invocation of a remote procedure returns immediately to the invoker.

Synchronous behavior is achievable by two intertwined remote procedures. See Result.

**Discussion**: An alternative to intertwined RPCs is the use of a Future mechanism. The advantage of the RPC reference based approach is the symmetry in invocation and result transmission. One implementation achieves both.

Result
``````

A remote procedure may produce a result that is returned to the caller. The result also has a data type and consists of a single value.

.. note::

   Instead of passing back the result from the procedure the caller may pass a result-return reference that is a remote procedure itself. This way the framework may have a straight-forward way of implementing a Future mechanism that completes upon reception of the response call.

Name & Namespace
````````````````

A remote procedure may have a name that exists in a namespace. The name is not a property of the remote procedure, but acts as an alias to a unique RPC reference associated with the remote procedure.

Publishing & Discovery
``````````````````````

Attaching a name to a remote procedure means to publish the remote procedure.
The communication framework owns both the name and the namespace.

Thus, publishing a remote procedure under a name also provides the means to discover it.

Interfaces & Services
`````````````````````

There is no specific structure defined as an 'Interface' or 'Service'. Instead, an interface as collection of remote procedures can be seen as a collection of remote procedures within a specific namespace that represents the interface.

Lifetime
````````

Once created, the remote procedure belongs to the communication framework which determines it's lifetime.

It must exist as long as references to it exist.

Events
------

An event is an information element that communicates the change of a state. An event has no value.
The main purpose of an event is to support runtime orchestration.

.. note:: An Event is not the same as a topic with no data. Topic mechanisms are designed to convey values. Events convey occurrences of state changes.

Publisher & Subscriber
``````````````````````

An event follows the publisher/subscriber pattern. This means

- An event exists on it's own. The framework's data communication system owns the event.
- An event can have zero or one publishers. The publisher updates ('publishes') new occurrences of associated state changes into the event. This is called 'triggering the event'.
- An event can have zero or multiple subscribers, also called 'listeners'. A subscriber consumes the state change notifications.

Immediate Events & Queued Events
````````````````````````````````

An event is designed to convey an immediate notification of the associated state change. However for cases where a subscriber cannot react immediately an event occurrence may be latched in a queue for deferred processing. This is called an 'Event Queue'. The framework may opt to offer event queues on top of immediate event propagation.

Namespace and Name
``````````````````

An event can have a name that exists within a namespace. The name is not an attribute of the event itself. Instead, it is an alias to the event's reference that allows triggering and listening to the event.

Lifetime
````````

Once created, the event belongs to the communication framework which determines it's lifetime.

An event must live while it is in use, i.e. it has a publisher and/or subscribers.


Zero Copy
---------

Zero-Copy data exchange is defined as concurrent access to data by a sender and a receiver without alternation of the memory location or layout of the data in the process of the exchange.

This includes:

- No serialization of data
- No deserialization of data
- No moving of data in memory

Data Properties
```````````````

To meet zero-copy requirements data require to be:

- Coherent - All data belonging to a data item must occupy adjacent memory locations.
- Relocatable - The correct interpretation of a data item is independent from it's address in memory.
- Atomic -  Access to the data item is an atomic operation. To achieve this the data requires one of two access modes:

  - Lockfree Access - No thread lock is required to read or write the data. This is the preferred property of zero-copy data.
  - Mutually Exclusive Access - A thread lock (mutex) is required to access the data.

Buffers
```````

In general zero-copy requires that data locations and layout are owned by the communication framework. Obviously these locations must be placed in shared memory to allow access from both producer and consumer side, should these lie in different processes or operating systems or even compute devices.

A data storage memory location is called a 'buffer'. The communication framework executes buffer allocation and deallocation. It shall provide references to these buffers that can be shared between the communication partners.

From a data producer side as well as from a data consumer side this means that the data is accessed directly through a buffer reference to the data.

DMA
```

As large amount of data are often produced or consumed by hardware the communication framework shall be able to provide raw access to buffers for direct memory access (DMA) capabilities of the underlying platforms.

Safety
------

We base this document on the ISO 26262-1:2018 released in December 2018.

Exchange of information through information elements always involves an information producer and one or many information consumers. As these can be part of different functions or partitions in the context of the application purpose. As such these partitions are likely to differ in their safety requirements and are thus domains of different safety levels.

The communication framework shall support safety integrity level ASIL-B. The communication framework shall also provide means for information exchange in mixed-criticallity applications where sender and receiver reside in domains of different safety classification.


Security
--------

We base this document on the ISO/SAE 21434 released in August 2021.

Communication and data exchange at the boundaries within the communication framework is subject of security considerations.

The communication framework shall support the following principal security capabilities:

- Authenticaion: Unambigous identification of the communication elements, especially producers and consumers of data.
- Authorization: A set of rules granting or denying access to communication operations based on the Authentication of participants in the communication framework.
- Protection: Means to protect the integrity of data received by consumers.
- Encryption: Means to protect the content of data in transit.

The definition of requirements for appropriate cryptographic hashing and encryption algorithms is not part of this document.

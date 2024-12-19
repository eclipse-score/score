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

Communiction covers information exchange between endpoints residing in
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

* **Topics**: A topic is the information carrier for **data**. A unique Id identifies a topic while a *data type* defines it's memory layout. The topic carries zero or multiple *values*. A value represents a single instances of the data type. See _`Topics`, _`Names`, _`Data Types`.
* **Remote Procedures**: A remote procedure is the information carrier for **execution** progress. A Id handle identifies the remote procedure together with an ordered set of named *parameters*. Each parameter defined by a data type. A caller of a remote procedure can cause it's activation by invoking the remote procedure with passed *arguments*. An argument is a single value instance for a parameter. See _`Remote Procedures`, _`Names`, _`Data Types`.
* **Events**: An event is the information carrier for runtime **synchronization**. A unique Id identifies the event. It signals the change of state. There is no data conveyed with the event. See _`Events`, _`Names`.

While the Id uniquely identifies an information element within the communication framework, it can also have a *name* as alias to conveniently identify the element. While the Id may not be publicly known, the *name* allows for public lookup.


Infrastructure Elements
```````````````````````

Infrastructure elements provide the means through which the information exchange executes.
We define three fundamental building elements:

* **Endpoints**: Endpoints are both the source and the target of every information exchange in teh communication framework. An endpoint providing information is consequently called a *provider*. With the same logic a *consumer* is an endpoint consuming information. Endpoints have an *Id* that uniquely identifies the endpoint within a node.
* **Nodes**: A node is an entity in the communication system that hosts several endpoints. It is the central element of the communication fabric by connecting endpoints and routing data. Nodes have an *Id* that uniquely identifies the node within a fabric. A node itself is also an endpoint.
* **Links**: A link is the fundamental abstraction of a connection between any two nodes. A link conveys information between nodes.

The combination of NodeId and EndpointId we also refer to as *address*. As nodes are also endpoints, they implicitly have an address.

Nodes and endpoints may also be identified by a *name* that resolves into references to these elements. See _`Names`, _`References`.

Connecting nodes though links creates a mesh of nodes that can mutually exchange information utilizing the above concepts. The boundary of the mesh is at the sole discretion of the deployment and may span from a single application into a connected cloud environment.

The entirety of connected nodes within a mesh we call *fabric*.

**Design Note**

From a perspective of safety, a node also encapsulates a single safety domain. Links provide the means for separating safety domains and thus allow for mixed criticality applications. 


Names
-----

A name is an UTF-8 tag of an element. The underlying Unicode standard is release 16.0.0 https://www.unicode.org/versions/Unicode16.0.0/. 

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

**Design Note**

A name is not a property of an element itself. 
Instead, a name acts as an *alias* to obtain an element *reference*. 
See _`References`.


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

A specific element in the communication system 

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

There are no data types defined for pointers to other data.

References
``````````

| Generic references are not allowed as data types. Instead, there are distinct reference types defined:

* Topic References
* Remote Procedure References
* Event References

The reference marker to an element shall be `AMPERSAND`: `&` `&#0026`.

Values of reference



Topic Reference
```````````````

A topic reference is a data type that provides a resolvable reference to a Topic.

::

   TopicRef

The underlying implementation shall not use more than 64 bits for the representation of TopicRef.

All properties of the referenced topics shall be retrievable through the TopicRef.

Data access to the content of the Topic shall be possible through the TopicRef.


RP Reference
`````````````

An RP Reference is a data type that provides a resolvable reference to a Remote Procedure.

::

   RPRef

The underlying implementation shall not use more than 64 bits for the representation of RPRef.

All properties of the referenced Remote Procedure shall be retrievable through the RPRef.

Invocation of the referenced Remote Procedure shall be possible through the RPRef.


Namespaces
----------


Topics
------

* Name
* Data Type
* Queue Depth
* Initialization
* Publisher
* Subscriber


Remote Procedures
-----------------

* Name
* Signature, Parameter Pack
* Publishing
* Discovery
* Invocation
* Sync/Async

Events
------

* Name
* Publisher
* Subscriber
* Chains / Buffering


Zero Copy
---------

* Definition
* Shared Memory
* Memory Management
* DMA


Safety
------

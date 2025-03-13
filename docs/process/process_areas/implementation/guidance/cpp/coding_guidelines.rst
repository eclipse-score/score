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

Writing C++ Code
################

.. gd_guidl:: Coding Guidelines CPP
   :id: gd_guidl__cpp_coding_guidelines
   :status: valid
   :complies: std_req__iso26262__software_1, std_req__iso26262__software_2, std_req__iso26262__software_3

Coding Guidelines
=================
Most programming languages are not specifically designed to be used within safety critical systems. If they are still applied in this context, *coding guidelines* are required. In those guidelines e.g. a safe subset of the language is defined which can be used safely and is not known to be error-prone. Another approach could be that those guidelines require a SW which includes only low complexity code. This means by using those guidelines the risk for systematic error, when using this language, can be minimized.

MISRA C++:2023
--------------
*MISRA* introduces coding rules for C++ which aim at providing a language subset which guarantees a high code quality. As *MISRA* is mostly accepted as an industry standard, SCORE will adhere to those rules.

*MISRA C++:2023* guidelines were released on November 2023. They are designed to be used with *C++17* and replace the *AUTOSAR guidelines for C++14* and the *MISRA C++:2008 guidelines*.

However if the *MISRA C++:2023* guidelines were used in combination with other C++ versions like *C++14* or *C++11*, it would mean that additional or different guidelines would need to be applied. For example, from *MISRA C++:2008* and/or *AUTOSAR guidelines for C++14* some rules have been dropped because they address issues which are no longer relevant for *C++17*. The same would apply if the *MISRA C++:2023* guidelines were used with a newer C++ standard like *C++20* or *C++23*.

Code Format
===========
Appropriate code formatting provides a source code which is easier to read and better to understand as it follows a well defined, known standard. That is why usually code formatters are applied. For this project *Clang-Format* will be used.

Code Style
==========
A *code style* describes which patterns, elements, conventions or best practices should be used during implementation.

Examples are:

* naming convention
* function calls
* initialization of variables.

For this project an code style is not yet decided.

C++ Version
===========

**C++17** is selected as the C++ standard for this project. This means that basically, all C++17 Features can be used according to the *MISRA C++:2023* guidelines.

Only if absolutely necessary also features of *C++:20* which are mentioned in the Chapter :ref:`cpp20` **might** be used. The reason for this is, that the current discussions on the new *MISRA* standard are going in a direction that those features should be ok to use.

**However to do so, a discussion and detailed evaluation needs to take place together with the process community beforehand for every such feature.**

This is because the new standard is not finalized yet and therefore a rule might come up which prohibits exactly the use case or places restrictions to it.

Language features
=================

Every new version of C++ brings new features with it. Some of them can have a positive impact due to making the code safer by reducing the chances to have undesired behavior.

In this section, some of these features will be explained, however it is not intended to be a complete list and it is up to the developer to judge if certain features make sense or not in each particular use case.

The features are divided by C++ version where it became available. This structure can help you to judge which C++ version to use.

.. _cpp17:

C++17
-----

* `[[nodiscard]] <https://en.cppreference.com/w/cpp/language/attributes/nodiscard>`_
* `type traits <https://en.cppreference.com/w/cpp/header/type_traits>`_
* `transformation traits <https://en.cppreference.com/w/cpp/named_req/TransformationTrait>`_

.. _cpp20:

C++20
-----
* `Concepts <https://en.cppreference.com/w/cpp/language/constraints>`_
* `Spaceship operator <https://en.cppreference.com/w/cpp/language/default_comparisons>`_
* `consteval <https://en.cppreference.com/w/cpp/language/consteval>`_
* `constinit <https://en.cppreference.com/w/cpp/language/constinit>`_
* `Formatting Library <https://en.cppreference.com/w/cpp/utility/format>`_
* `Synchronization Primitives <https://isocpp.org/blog/2024/10/synchronization-primitives-in-cpp20-shivam-kunwar>`_
   * `Latches <https://en.cppreference.com/w/cpp/thread/latch>`_
   * `Barriers <https://en.cppreference.com/w/cpp/thread/barrier>`_
* `source_location <https://en.cppreference.com/w/cpp/utility/source_location>`_
* `Spans <https://en.cppreference.com/w/cpp/container/span>`_
* `jthread <https://en.cppreference.com/w/cpp/thread/jthread>`_
* `stop_token <https://en.cppreference.com/w/cpp/thread/stop_token>`_

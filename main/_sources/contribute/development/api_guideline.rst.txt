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

Designing API
#############

.. document:: API Guidelines
   :id: doc__api_guidelines
   :status: draft
   :safety: QM
   :security: NO
   :realizes: wp__training_path

What makes a good API? A start is to create an API that feels natural to a user.
There are multiple layers to "natural".

One part is finding a natural abstraction of the usecase that this API should fulfill.
Since this is a general guidance on designing APIs, it is out of its scope to answer how that abstraction looks for your individual usecase.
But, this guidance can help you on some other aspects of "natural".

In the following, we go through some aspects of an API you should consider.
This is not a complete list. Designing a good API is no easy task.
See this more as a starting point and feel free to add further aspects you think are worth the read.

Naming conventions
------------------

Patterns and Idioms of the Programming Language
-----------------------------------------------

When a software developer interacts with an API, he does so using a programming language.
With this language come specific patterns and idioms, how good code should look like.
To make an API feel "natural" to a user, it must follow these patterns and idioms prescribed by the programming language.
Otherwise, it will feel foreign and requires a user to constantly doublecheck in the manual how the API behaves.

An example from the C++ world is the named requirement `Container <https://en.cppreference.com/w/cpp/named_req/Container.html>`_.
If an API is developed against this named requirement, it seamlessly fits into the expectations a C++ developer has for code.

So, when designing an API, do not only consider the problem you are trying to solve, but also how a user would want to interact with your solution.
Approaches like test-driven development can support you in taking the perspective of a user.
Given that the interaction differs for multiple programming languages, that the same API is likely not a good fit for more than one programming language.

Programming Language Infrastructure
-----------------------------------

Each programming language comes with a set of infrastructure. Be it features of the compiler, standard libraries or other helpers.
To make an API feel natural to the user means that you use this infrastructure wherever possible.

This has several reasons:

* The infrastructure is used most likely in the surrounding code already
* The infrastructure supports you in getting the patterns and idioms right
* By using existing infrastructure you reduce code duplication and maintenance effort

Should it be impossible to use the existing infrastructure, try to stay as close as possible to it with your replacement.

Error handling
--------------

Avoid encoding errors in the returned value (e.g.: do not use -1 for a function that returns an integer).
Instead, follow the language-specific coding guidelines or the language specific features if no guidelines exist.

Further, handle errors internally if feasible but bubble an error up if a user should know about it.

Consider aborts as a final resort, since they will reduce the availability of the S-CORE platform.
Even if an error does not allow you to continue operation, providing this error to the user is still better than an abort.
The user may decide to abort himself, or he may continue in a degraded fashion without your library.

Testability
-----------

Consider that users may have to test their code that interfaces with your API.
This means, an API always needs to consider the additional usecase of testing.

A common solution is to apply the dependency injection pattern to the API.

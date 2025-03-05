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

Verification Templates
======================

gTest
-----

gTest is the preferred and accepted test framework to write test cases for C/C++ code in the project.

Each test case requires a link to one or more requirement/design element.
A more detailed description of how to link code to requirements is available here: :need:`gd_req__link_tests_cpp`

Writing test cases using gTest shall follow the recommendations from the official gTest documentation.
For very basic start follow http://google.github.io/googletest/primer.html
For advanced information follow http://google.github.io/googletest/advanced.html

Rust
----

The rust community uses the terms unit test and integration test. Where unit test basically represents what the project
considers as unit tests the term "integration test" in rust can be treated for component and feature testing.
Details on the definition an the test organization in rust can be found here:
https://doc.rust-lang.org/book/ch11-03-test-organization.html

Each test case requires a link to one or more requirement/design element.
A more detailed description of how to link code to requirements is available here: :need:`gd_req__link_tests_rust`

Writing test cases in rust shall follow the recommendations from the official rust documentation.
https://doc.rust-lang.org/book/ch11-01-writing-tests.html


Python
------

Writing test cases in python should be done using pytest.
Note that python unittest does not support metatags and therefore should not be considered as test framework.

Each test case requires a link to one or more requirement/design element.
A more detailed description of how to link code to requirements is available here: :need:`gd_req__link_tests_python`

Writing test cases in python shall follow the recommendations from the official python and community documentation.
https://docs.python-guide.org/writing/tests/


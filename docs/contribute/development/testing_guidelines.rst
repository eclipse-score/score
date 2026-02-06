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

Testing Guidelines
##################

.. document:: Testing Guidelines
   :id: doc__testing_guidelines
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_development_plan

These guidelines are based on discussions within the score com team. They're not set in stone and can be changed in the future.
Feel free to submit a PR if you disagree with something or want to add something.
These rules can also be deviated from depending on the specific case. It's impossible to come up with guidelines that are suitable
in every single situation so use these as a starting point and if following the guidelines would make the tests less readable,
less functional, more complex etc then you can deviate. However, if you want to deviate, only do so because there's a good reason.

Test Naming
===========

``TEST(TestSuiteName, TestName)``

We don't propose any strict guidelines for ``TestSuiteName`` or ``TestName`` except that the names:

- should be descriptive
- should use PascalCase style.
- a ``TestSuiteName`` that does not use a fixture should have the suffix ``Test``.
- a ``TestSuiteName`` that does use a fixture should have the suffix ``Fixture``.

It should be clear from the name of a test what exactly it's testing. Conceptually following
"Given, when, then" in your naming may help to come up with a good name.

E.g. ``TEST(RuntimeWithInvalidTracingRuntimeTest, WhenCallingTraceThenAnErrorIsReturned)``
``TEST(SkeletonFieldPrepareOfferTest, WhenCallingPrepareOfferBeforeCallingUpdateThenAnErrorIsReturned)``

You can also use the ``TestSuiteName`` to group together tests that are testing the same functions / behaviours.
Note: if using descriptive ``TestSuiteName``\s, then you can reduce repetition in the ``TestName``.

E.g.

- ``TEST(SkeletonEventTest, WhenCallingSendThenSendWillBeCalledOnTheSkeletonEventBinding)`` can be shortened to ``TEST(SkeletonEventSendTest, SendWillBeCalledOnTheSkeletonEventBinding)``
- ``TEST(ProxyEventFixture, CallingGetNewSamplesCallsReceiverForEachSample)`` can be shortened to ``TEST(ProxyEventGetNewSamplesFixture, CallsReceiverForEachSample)``

The only strict guideline is that any tests which contain ``EXPECT_DEATH`` should always have ``DeathTest`` at the end of ``TestSuiteName``.
(See `Death Tests and Threads <https://github.com/google/googletest/blob/main/docs/advanced.md#death-tests-and-threads>`_).
More information about death tests in the :ref:`death-tests` section.

Test Content
============

Given, When, (Expecting / Then)
-------------------------------

You can read about the "Given, when, then" test structure (this gives a good and simple summary:
`GivenWhenThen <https://martinfowler.com/bliki/GivenWhenThen.html>`_). We add in an additional
section "Expecting", which can be optionally added to add expectations on mocked function calls.

Given
^^^^^

The "Given" section of the test should contain the setup code required to get the environment into a state
that is ready to run the actual code to be tested in the "When" section.
Unless this code is very minimal (e.g. one or two lines), this should be added to a test fixture.

This section also includes any default behaviour required on mocks. (``ON_CALL``\s)

Expecting
^^^^^^^^^

This is where you check that a certain mock call was called as a result of the behaviour in the "When" section,
when the mock call itself is what you're testing for (See :ref:`expect-call-vs-on-call` for further explanation).
This should be an ``EXPECT_CALL``.

Sometimes you might have an "Expecting" section and a "Then" section. This can happen when the return value
tested in the "Then" section is completely related to the expectation in the "Expecting" section.
E.g. if the function under test returns the value returned by the mock function, or it forwards
an error from the mock function etc. If they're not clearly related, then they should not both be asserted
in the same test. E.g. if the mock function is simply a side effect and doesn't affect the return value of
the function under test. This would become evident because there would then be multiple tests with different
expected behaviour specified on the mock function with the exact same return value from the function under test.

If there are multiple mocked functions whose behaviour is specified in a test, then we only add multiple
``EXPECT_CALL``\s if all the functions are dependent on something else set in the "Given" section, rather
than simply being dependent on each other. E.g. if some state is true, then 2 mock functions will be
called: in this case, you can have 2 ``EXPECT_CALL``\s in a single test. However, if one function is
dependent on the other function, then it's better to have one mock expectation specified in the "Given"
section and the other in the "Expecting" section. E.g. "Given FunctionA returns x, Expecting that FunctionB returns y".

When
^^^^

This is the behaviour that you want to test.

Then
^^^^

This is where you check that the behaviour you're testing performed as expected. E.g. checking the return
value of the function called in the "When" section, checking some side effect etc.

Examples
^^^^^^^^

.. code-block:: cpp

   // Given, When, Then
   TEST(MyFooTest, CallingFooReturnsSuccess)
   {
       // Given some setup code (the test setup should add any required default actions)
       MySetup()

       // When calling foo
       const auto foo_result = foo();

       // Then we get a valid result
       EXPECT_TRUE(foo_result.has_value());
   }

   // Given, Expecting, When
   TEST(MyFooTest, CallingFooCallsXOnY)
   {
       // Given some setup code
       MySetup()

       // Expecting that x is called on y
       EXPECT_CALL(y, x());

       // When calling foo
       amp_ignore = foo();
   }

   // Given, Expecting, When, Then
   TEST(MyFooTest, CallingFooReturnsErrorWhenBindingReturnsError)
   {
       // Given some setup code
       MySetup();

       // Expecting that when x is called on y it returns an error
       EXPECT_CALL(y, x()).WillOnce(Return(MakeUnexpected(SomeError{}));

       // When calling foo
       const auto foo_result = foo();

       // Then we get an error
       EXPECT_FALSE(foo_result.has_value());
   }

What Should a Test Contain
--------------------------

A unit test should only test one functionality. In general, each test should be testing a single functionality. This may be that:

* calling a function given some setup will call some other mock function with some specified arguments
* calling a function given some setup will return a particular value
* calling a function given some setup will terminate (More about death tests in the :ref:`death-tests` section)
* a function will return a specific value given what some mock function did / returned.

Each test should have a single *semantic* assertion or expectation. If our function calls a mock function which returns
some value and the return value of the function under test is highly dependent on what the mock function did / returned
then we may assert both the behaviour of the mock function and the return value of the function under test in a single test.
E.g. if the function under test simply returns the result of the mock function, if the function under test returns an error
when the mock function returns an error etc. However, if the return value of our function under test does **not** depend
directly on a mock function being called (i.e. the mock function is simply a side effect), then they should be tested in
different tests.

If we want to test that a function returns an error code, then it makes sense to have:

.. code-block:: cpp

   ASSERT_FALSE(some_result.has_value());
   EXPECT_EQ(some_result.error(), SomeErrorCode);

If a function returns a struct, then ideally we would want to use the comparison operator of the struct to check that
the returned struct is the same as an expected struct. If it doesn't make sense to add a comparison operator for some
reason and the elements of the struct are related, then we may have multiple expectations. E.g.

.. code-block:: cpp

   EXPECT_EQ(my_dummy_struct.service_id, expected_service_id);
   EXPECT_EQ(my_dummy_struct.instance_id, expected_instance_id);

Another option in this case would be to define a custom matcher within the test file.
See `Defining Matchers <https://google.github.io/googletest/reference/matchers.html#defining-matchers>`_ for details.

However, if for example our test function returns a configuration object which contains a lot of unrelated data, then we
may split the test up into multiple tests which each test one part of the returned configuration object.

.. note::

   Sometimes a test will rely on behaviour that was already tested in a previous test. In general, this behaviour should
   not be retested. However, sometimes additional asserts may be useful to avoid undefined behaviour in a test. It's up
   to the common sense of the author of the test and the reviewer to decide when additional asserts are needed.

   E.g. if a test checks that a certain function returns a valid pointer in certain situations, other tests that make
   this same assumption but are not directly testing this behaviour may add an additional assert to check that the pointer
   is not a nullptr to avoid undefined behaviour. (Note: in these other tests, the assert should not be in the ``Then``
   section, but can rather be placed immediately after the function call that returns the pointer so that it's not
   confused with the functionality being tested in that particular test)

.. _expect-call-vs-on-call:

EXPECT_CALL vs ON_CALL
----------------------

Please read: `Setting Expectations <https://google.github.io/googletest/gmock_cook_book.html#setting-expectations>`_.

Generally, ``ON_CALL`` should be used to set default actions whenever a function on a particular mock is called.
This may be default actions that should occur in every test unless specified otherwise (e.g. every time we call
``Runtime::getInstance()``, then a ``RuntimeMock`` should be returned). Such expectations should usually be added
to the test fixture as they will be relevant to multiple tests.

If we want to inject some behaviour into a mock function which directly impacts the return value of the function
under test, we should use ``EXPECT_CALL`` e.g. if we want to test that ``SkeletonEvent::Send()`` returns an error
if ``Runtime::getInstance()`` returns a nullptr, then we can add
``EXPECT_CALL(runtime_mock_, getInstance()).WillOnce(Return(nullptr))`` to our test.

We use ``EXPECT_CALL`` when we want to test that a specific function is called on a mock object as the result of
the behaviour that we're testing in the "When" section. E.g. if we want to make sure that ``SkeletonEvent::Send()``
does not dispatch to the binding given that ``Runtime::getInstance()`` returns a nullptr, then we can have:

.. code-block:: cpp

   TEST_F(SkeletonEventFixture, CallingSendWillNotDispatchToBindingIfGettingRuntimeReturnsNullptr)
   {
       // Given that a valid Runtime cannot be returned
       ON_CALL(runtime_mock_, getInstance()).WillByDefault(Return(nullptr));

       // Expecting that Send will NOT be called on the skeleton event binding
       EXPECT_CALL(skeleton_event_binding_mock_, Send()).Times(0);

       // When calling Send
       amp::ignore = skeleton_event_.Send();
   }

Test Constants
--------------

Often we require some constants in our tests e.g. which we must pass to the function that we're testing. If the
specific value of this constant is relevant to the test, then it should be within the test itself. Otherwise,
it should be a global constant or if it's relevant to the test fixture, it should go there.

E.g.

.. code-block:: cpp

   TEST_F(ProxyEventSubscribeFixture, CallingSubscribeWillChangeSubscriptionStateToSubscribed)
   {
       // Given a constructed ProxyEvent and an offered service

       // When calling Subscribe
       amp::ignore = proxy_event_.Subscribe(kSomeValidMaxSampleCountThatIDontCareAbout); // Constant is global or in the fixture

       // Then the subscription state changes to subscribed
       EXPECT_EQ(proxy_event_.GetSubscriptionState(), SubscriptionState::Subscribed);
   }

   TEST_F(ProxyEventSubscribeFixture, CallingSubscribeWithTooManySamplesWillNotChangeSubscriptionState)
   {
       // Given a constructed ProxyEvent and an offered service

       // When calling Subscribe with more max_samples than was configured
       const auto max_samples_count = configured_max_sample_count_ + 1; // Constant is relevant to test so it should be here
       amp::ignore = proxy_event_.Subscribe(max_samples_count);

       // Then the subscription state is unchanged
       EXPECT_EQ(proxy_event_.GetSubscriptionState(), SubscriptionState::NotSubscribed);
   }

.. note::

   If an object is created as a global constant, then it must be ensured that the object does not use globals in its
   implementation. There is no guarantee that the global in the implementation of the object will be initialised before
   the test global constant which can lead to accessing uninitialised memory.
   (See `Static Initialization Order Fiasco <https://en.cppreference.com/w/cpp/language/siof.html>`_ for details)

Test Fixtures
=============

We don't propose any strict guidelines for Test Fixtures. Although we suggest:

* For consistency all test fixtures should be placed immediately before the first test that uses it. This includes aliases for fixtures.
* Try to keep fixtures small. If they grow too large, then either try to extract some functionality into separate functions or classes and use composition.
  Large fixtures may also hint at poor architectural design of the unit under test.
* Avoid inheriting from other fixtures.

If a test fixture contains some code that must be checked (e.g. the setup code contains an ``EXPECT`` / ``ASSERT``),
then you can also create an empty test which tests that the test setup works as expected. E.g. Assuming the
``ProxyEventSubscribeFixture`` will create a ``ProxyEvent`` and ASSERT that the ProxyEvent was successfully created,
then we can create an empty test:

.. code-block:: cpp

   TEST_F(ProxyEventSubscribeFixture, CanConstructAProxyEvent)
   {
       // When constructing a ProxyEvent
       // Then the ProxyEvent can be successfully created without an error
   }

Test Fixture Builder Pattern
----------------------------

One approach to fixture design is to employ a builder pattern. This allows the test setup code to be done in a concise
and easily readable way, while also making the test setup configurable in each individual test. The idea is to add
functions to the test fixture which return a reference to the fixture itself so that they can be chained together.

You can see an example of the usage in
`service_discovery_client_test_fixtures.h <https://github.com/eclipse-score/communication/blob/main/score/mw/com/impl/bindings/lola/service_discovery/test/service_discovery_client_test_fixtures.h>`_.
The ``ServiceDiscoveryClientFixture`` contains general setup code which is relevant to all tests in its ``SetUp()``
function. It then provides functions such as ``GivenAServiceDiscoveryClient()``, ``WithAnOfferedService(InstanceIdentifier)``,
``WithAnActiveStartFindService()``. This allows us to minimise the boilerplate code in each test while still allowing
the tests to be readable, easy to understand and easily configurable without copying and pasting boilerplate code.
These functions can also take arguments to allow additional configuration from within the tests themselves.

In general, the unit under test should be created in a function prefixed with ``Given`` (e.g. ``GivenAServiceDiscoveryClient``)
rather than in the ``SetUp()``. This makes the test more explicit and also allows tests to not call it or to create the
unit under test directly within the test e.g. when testing the destructor of the unit under test, it may have to be created
in the test itself if we need to set an expectation that interacts with a variable defined in the test. Otherwise, the
variable may be destroyed at the end of the test before the unit under test is destroyed in the fixture.

A snippet of the fixture and an example test to illustrate the point:

.. code-block:: cpp

   class ServiceDiscoveryClientFixture : public ::testing::Test
   {
     public:

       void SetUp() override
       {
           ASSERT_TRUE(inotify_instance_->IsValid());

           ON_CALL(inotify_instance_mock_, IsValid()).WillByDefault([this]() {
               return inotify_instance_->IsValid();
           });
           ...
       }

       ServiceDiscoveryClientFixture& GivenAServiceDiscoveryClient()
       {
           auto inotify_instance_facade = std::make_unique<os::InotifyInstanceFacade>(inotify_instance_mock_);
           auto unistd = std::make_unique<os::internal::UnistdImpl>();
           service_discovery_client_ = std::make_unique<ServiceDiscoveryClient>(
               long_running_threads_container_, std::move(inotify_instance_facade), std::move(unistd), filesystem_);
           return *this;
       }

       ServiceDiscoveryClientFixture& WithAnOfferedService(const InstanceIdentifier& instance_identifier)
       {
           EXPECT_TRUE(service_discovery_client_->OfferService(instance_identifier).has_value());
           return *this;
       }

       ServiceDiscoveryClientFixture& WithAnActiveStartFindService(
           const InstanceIdentifier& instance_identifier,
           const FindServiceHandle find_service_handle,
           FindServiceHandler<HandleType> find_service_handler = [](auto, auto) noexcept {})
       {
           EXPECT_TRUE(service_discovery_client_->StartFindService(
               find_service_handle, std::move(find_service_handler), EnrichedInstanceIdentifier{instance_identifier}));
           return *this;
       }
       ...
   }

   TEST_F(ServiceDiscoveryClientStartFindServiceFixture,
          CallingStartFindServiceOnOfferedServiceTwiceWithTheSameIdentifierCallsBothHandlers)
   {
       ...
       MockFunction<void(ServiceHandleContainer<HandleType>, FindServiceHandle)> find_service_handler_1{};

       // Given a ServiceDiscoveryClient with an offered service and a currently active StartFindService
       GivenAServiceDiscoveryClient()
           .WithAnOfferedService(kSomeInstanceIdentifier)
           .WithAnActiveStartFindService(
               kSomeInstanceIdentifier, kHandle, CreateWrappedMockFindServiceHandler(find_service_handler_1));
       ...
   }

We are still exploring the usage of this pattern so we don't propose any further guidelines for naming or usage at this
point. But feel free to try it out and add to the guidelines.

Miscellaneous
=============

Test File Length
----------------

A test file may contain all tests for a single unit (e.g. a class) as long as there aren't "too many" tests in that file.
It's difficult to give an exact number of files or tests which are "too many". Therefore, it's up to the developer to
decide whether test readability / maintainability will be improved by splitting up a single test file into multiple.

If a developer decides that there are too many tests in one file, then the split should not be arbitrary but rather be
based on features of the unit under test. It should be easy to find tests and also easy for developers (including other
developers who didn't write the initial tests) to know where to put new tests.

**Example:** A large test file was split into (see the
`service_discovery/client <https://github.com/eclipse-score/communication/tree/main/score/mw/com/impl/bindings/lola/service_discovery/client>`_
folder):

* ``service_discovery_client_find_service_test.cpp``
* ``service_discovery_client_offer_service_test.cpp``
* ``service_discovery_client_sequence_test.cpp``
* ``service_discovery_client_start_find_service_test.cpp``
* ``service_discovery_client_stop_find_service_test.cpp``
* ``service_discovery_client_stop_offer_service_test.cpp``
* ``service_discovery_client_worker_thread_test.cpp``

Each test file tests one specific feature of ``ServiceDiscoveryClient``. I.e. ``service_discovery_client_find_service_test.cpp``
is testing the ``FindService`` function. ``service_discovery_client_worker_thread_test.cpp`` is testing the behaviour of the
worker thread which runs throughout the lifetime of ``ServiceDiscoveryClient``. ``service_discovery_client_sequence_test.cpp``
tests more complex sequences of calling different ``ServiceDiscoveryClient`` functions (e.g. calling ``OfferService`` then
``StopOfferService`` then ``StartFindService`` etc.).

Testing Interfaces Which Take unique_ptr
----------------------------------------

Some interfaces require that the caller must provide a mockable object to the unit under test by transferring ownership,
e.g. via a ``unique_ptr``. In general, we can simply set our expectations on the mock object and then inject it. The
expectations will be evaluated by gtest on destruction of the mock object. However, if this is not possible then another
option is to use a mock facade, which is explained below.

Mock Facade
^^^^^^^^^^^

A mock facade is a class which inherits from the interface of the mockable object so can be passed to the unit under test
as a ``unique_ptr``. The facade stores a reference to the actual mocked object which is owned by the test and forwards all
calls to the mocked object. This allows the ownership of the mock to be managed by the test while the ownership of the
facade is managed by the unit under test (which can destroy the facade at any time while not affecting the mocked object).
An example of a facade class can be found in
`inotify_instance_facade.h <https://github.com/eclipse-score/baselibs/blob/main/score/os/utils/inotify/inotify_instance_facade.h>`_.

Specify Expectations on Mock Before Handing Over
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GTest does not require mocks to stay alive until a test finishes. In fact, it evaluates mocks on destruction (i.e. to check
whether all expectations were met). Therefore, you can simply specify all expectations on a mock before passing it to the
unit under test as a ``unique_ptr``.

Bazel Targets
-------------

Generally, we should have one bazel test target per production code test target. We should avoid having a single test target
per directory. This leads to longer build times when wanting to run a single test, complicates the dependency tree and also
requires us to mark multiple tests as flaky, long running etc. even if only one test in the suite is the culprit.

We should try to use the following macros in the following order (i.e. if the first cannot be used, then try the next one):
``cc_gtest_unit_test`` -> ``cc_unit_test`` -> ``cc_test``.

We should also have one ``cc_unit_test_suites_for_host_and_qnx`` per directory which accumulates all of the test targets in
the directory and the test suites from child directories.

.. _death-tests:

Death Tests
-----------

Tests containing ``EXPECT_DEATH`` should always have ``DeathTest`` at the end of the ``TestSuiteName``.
See `Death Tests and Threads <https://github.com/google/googletest/blob/main/docs/advanced.md#death-tests-and-threads>`_
for more information.

Examples of Good Tests
======================

*(This section is a placeholder for future examples.)*

Future Work
===========

This document is a work in progress. Feel free to add to existing sections, add new sections or add points here for
discussion / addition in the future.

* Add better guidelines for naming tests and fixtures
* Add better guidelines for test fixture design (including builder pattern)
* Add examples of good tests
* Add guidelines for death tests
* Add guidelines for typed tests and parameterised tests (figure out if we can name each sub-test)
* Do we always want given, when, then comments? What if the test is simple and it's completely clear in the code what's
  being done? What if we use the builder pattern and have a setup solely consisting of ``GivenSomeObject()``. Do we need
  a comment above saying ``// Given some object``?
* Add examples to Expecting section

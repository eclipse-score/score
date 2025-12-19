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

.. _feature_flags:

Feature Flags
=============

Background
----------

Feature flags
^^^^^^^^^^^^^

Feature flags, also known as feature toggles, are a technique used in software
development to enable or disable features dynamically. The main goal is to
allow teams to manage and release new features more effectively, enabling A/B
testing and quickly roll back if issues arise. This guidance aims
to define how we intend to make use of these features for configuration and
variant management of S-CORE.

There are two categories of flags, build flags and runtime feature toggles:

- **Build Flags**: These are build/compile time switches used to include or
  exclude certain pieces of code from the build process. When a build flag is
  set, the corresponding code is compiled into the final application/consumer.
  These flags can be used for specific environments, such as build vs. debug.
  Build flags typically require a new full deployment to change the state of the
  feature.

- **Runtime Feature toggles**: These toggles control features at runtime,
  meaning they can be changed with partial deployments or ultimately while the
  application is running. They are generally more flexible, allowing for easier
  experimentation. Runtime toggles are typically implemented through
  configuration settings in the application or by querying an external service
  for configuration.

This guidance will focus on the former.

Also, do not confuse feature flags with platforms. Feature flags are independent from
the platform. A platform is for example QNX on an ARM architecture.

Example for a feature flag
^^^^^^^^^^^^^^^^^^^^^^^^^^

Feature flags are defined in BUILD Files:

.. code-block:: bazel
    :caption: some_module/BUILD

    load("@bazel_skylib//rules:common_settings.bzl", "bool_flag")

    bool_flag(
        name = "some_feature",
        build_setting_default = True,
    )

    config_setting(
        name = "config_some_feature",
        flag_values = {
            ":some_feature": "True",
        },
    )

Feature flags can be specified via the command line to quickly enable or
disable features for builds and tests.

.. code-block:: bash

    bazel build \
    --platforms=//platform:some_platform \ # TODO: To be defined with overall integration
    --//some_module:some_feature=True \
    --extra_toolchains=//toolchains:some_compiler //some_module:some_target


Defining convenient combinations of feature flags
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To simplify the user interface, configurations can be defined that specify
values for a set of feature flags.

.. code-block:: bash
    :caption: .bazelrc

    build:no_rear_doors --//rear_doors:left_door=False --//rear_doors:right_door=False

.. code-block:: bash

    bazel build \
    --platforms=//platform:some_platform \ # TODO: To be defined with overall integration
    --config=no_rear_doors \
    --extra_toolchains=//toolchains:some_compiler //some_module:some_target

Note that these are mere user conveniences and combinatorial scenarios will not
be allowed in CI testing.



Design Guidance of feature flags in S-CORE
------------------------------------------

Goals
^^^^^

1. Ease of use for developers:

   1. One general goal should be to avoid the necessity of memorization of N
      feature flags in order to produce working software. Therefore, the first
      assumption is that the default configuration **must** match the most
      productive/stable version of the software.
   2. Testing configurations shall be entirely managed within the build
      system, i.e. there should be no reason for a developer to know extra steps
      or touch CI configuration in order to configure their feature flags and
      respective build/test configuration.

2. Avoiding duplicated build/test steps: We should avoid wastefulness when
   running our builds / tests. If we are running two sets of tests, with a feature
   enabled/disabled, an application/component or test that is not affected by the
   configuration switch should not need to be built/executed again. This poses
   some interesting challenges that will be detailed later in this document.

3. Avoid validation complexity: Feature-flagged systems will inherently make
   our integration processes more complex, especially regarding testing, since now
   multiple code paths for the same product must be tested. This can be aggravated
   with combinatorial configurations which can quickly explode the number of test
   cases. Different levels of abstraction are also affected by different
   restrictions, for unit testing it might be trivial to test all features but at
   integration level it might be impossible to test all feature sets due to the
   inherent complexity and resource limitations.

   1. To avoid combinations, features **should** be independent of each other.
      If there is a combination of settings that represent a feature, it might
      make sense to bring them all together in a single flag.

   2. To start off, we test two configurations:

      - Configuration of the Core Software Stack
      - Configuration for increased coverage of features

      This restricts feature flags to at most two tested values.
      It is recommended to not use more values for a feature flag.
      On request, further configurations may be added after impact evaluation.

   3. Features flags should be treated as inventory with a carrying cost.
      In order to keep the number of feature flags manageable, it is recommended to
      time-scope flags and teams must be proactive in its management. One
      possible approach is to create an "expiration date" or "cleanup" task when
      adding new flags. The responsible group for governance shall supervise this
      practice but responsibility for maintenance must remain with the area.

Feature flags structure
-----------------------

S-CORE has four categories of feature flags.

Generic requirements for feature flags:

- Any feature flag shall be defined with a reasonable default value.
- Features that are experimental must be clearly marked as such by prepending `experimental_`
  (e.g. `experimental_<flag_name>`).
- Above every feature flag in the BUILD file a comment must link to the relevant documentation.

Below, we list the four categories of feature flags and provide additional information and constraints for each.

Enabling a feature
^^^^^^^^^^^^^^^^^^

For each feature there is exactly one flag that enables it.
It is mentioned in the feature description at the top of the feature documentation found in :ref:`features`.

The name of the flag is defined as `<feature_name>`, where `<feature_name>` corresponds to the name of
the feature in `snake_case`.

The feature flag must be of type `bool_flag`.

Feature flags of this category reside in `eclipse-score/score:flags`_.

Selection of the implementation for an enabled feature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A feature may be provided by multiple modules. The selection of the module which is used for a feature happens through
a feature flag.

The name of the flag is defined as `<feature_name>_implementation`, where `<feature_name>` corresponds to the name of
the feature in `snake_case`.

The feature flag is a string.
In Starlark it is represented by a `string_list_flag` which is configured to only allow a single value.
Each value must be encoded in `snake_case`.

Feature flags of this category reside in `eclipse-score/score:flags`_.

Configuration of a feature
^^^^^^^^^^^^^^^^^^^^^^^^^^

To modify behavior of a feature, the documentation in the feature tree may point out several feature flags. Such flags
are of this category.

The name of the flag is defined as `<feature_name>_<configuration>` where:

- `<feature_name>` corresponds to the name of the feature in `snake_case`
- `<configuration>` corresponds to the name of the configuration in `snake_case`

Feature flags of this category reside in `eclipse-score/score:flags`_.

Implementation specific configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Modules may have configuration options that are implementation specific. Such options are not mentioned in the feature
tree but inside the documentation of the module itself.

The name of the flag is defined as `<feature_name>_<module_name>_<configuration>` where:

- `<feature_name>` corresponds to the name of the feature in `snake_case`
- `<module_name>` corresponds to the name of the module in `snake_case`
- `<configuration>` corresponds to the name of the configuration in `snake_case`

Feature flags of this category reside in a top-level directory called `flags` of the module.

Propagation of feature flags
----------------------------

To take effect beyond Bazel, the values of features needs to be propagated to
different programming languages.

Definition of Public APIs
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bazel
    :caption: some_module/BUILD

    alias(
        name = "public_lib",
        actual = select({
            ":config_some_feature": [":lib"],
            "//conditions:default": [],
        }),
    )

    cc_library(
        name = "lib",
        # ...
    )

Please refrain from trying to use the approach below.
It will not work, since `select()` cannot be combined with `visibility`.

.. code-block:: bazel
    :caption: some_module/BUILD

    cc_library(
        name = "public_lib",
        visibility = select({
          ":config_some_feature": ["//visibility:__public__"],
          "//conditions:default": [],
        }),
    )

C++
^^^

.. note::
    The preferred way is to be discussed in the score-cpp-community.

Possible options are:

- select for tag local_defines in Bazel rule & preprocessor
- templated config file with constexpr flags
- select() for tag srcs in Bazel rule to choose specific source files


Python
^^^^^^

We recommend to propagate features via command line arguments. e.g.

.. code-block:: bazel
    :caption: some_module/BUILD

    py_binary(
      name = "foo.py",
      srcs = ["test.cpp"],
      deps = [":lib"],
      args = select({
        ":config_some_feature": ["--some_feature"],
        "//conditions:default": [],
      }),
    )

Config Files
^^^^^^^^^^^^

Feature flags can be used in config files via bazel template expansion.
E.g.:

.. code-block::
    :caption: some_module/config.json.tmpl

    {
        "some_key": @SOME_FEATURE@
    }

.. code-block:: bazel
    :caption: some_module/BUILD

    expand_template(
        name = "config",
        out = "config.json",
        substitutions = select({
            ":config_some_feature": {
                "@SOME_FEATURE@": "value_for_some_feature"
            },
            "//conditions:default": {
                "@SOME_FEATURE@": "some_default"
            },
        }),
        template = "config.json.tmpl",
    )

Testing
-------

With the support of Path Mapping, we are able to fully take advantage of a
machine's resources and correctly support an arbitrary set of configurations.
We can setup Bazel targets / test_suites which set their configuration as code
and run them all in parallel. Developers are able to run all tests with one
command while avoiding duplication.

Since Bazel will not support shared actions, the deduplication mechanism in
this case will be the use of a cache. There are still a couple of minor
drawbacks with cache deduplication:

- There is a slight inefficiency in a first execution if two equal actions
  under different configurations start at the same time without any cache
  entry.
- Using a disk_cache as a deduplication mechanism implies developers should be
  aware of this and regularly use caches in their day-to-day business, which is
  generally recommended anyways.

Note that Path Mapping must be individually supported by every rule.

Unit tests
^^^^^^^^^^

A unit test shall never test more than one single feature.

.. note::
    The preferred way is to be discussed in the score-cpp-community.

The selection which tests shall be executed depending on a feature flag shall
be done via preprocessor macros in the test.cpp.

The activation/deactivation of features is propagated via `local_defines`.

.. code-block:: cpp
    :caption: some_module/test.cpp

    #if defined(SOME_FEATURE)
        EXPECT_CALL(...)
    #else
        EXPECT_CALL(...)

.. code-block:: bazel
    :caption: some_module/BUILD

    cc_test(
        name = "test",
        srcs = ["test.cpp"],
        deps = [":lib"],
        local_defines = select({
            ":config_some_feature": ["SOME_FEATURE"],
        "//conditions:default": [],
        }),
    )

    cc_library(
        name = "lib",
        local_defines = select({
            ":config_some_feature": ["SOME_FEATURE"],
            "//conditions:default": [],
        }),
        # ...
    )

Test with the default feature value:

.. code-block:: bash

    bazel test :test

Test with the feature value explicitly enabled

.. code-block:: bash

    bazel test :test --//some_module:some_feature=True

Feature flag discovery
----------------------

Available feature flags can be found with bazel cqueries.

.. code-block:: bash

    bazel cquery \
      "filter('.*',
          kind('.*_flag', deps('//TODO Main target to be defined with overall integration'))
      )" --output label_kind | sort

Example output:

.. code-block:: bash

    //some_module:some_feature
    //some_other_module:some_feature

Information for Bazel Power Users
---------------------------------

In the following sections we provide some additional background.
This is quite technical and not required by standard users.

Custom rules must be compatible with Path Mapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As aforementioned, configuration of a build/test is typically set by the user
via command-line. **Transitions** break this pattern in order to support
multi-configuration builds/tests in one go. This is accomplished by creating an
entry point for the build that automatically configures its graph, ignoring the
configuration set by the user.

Let's imagine a scenario where we have a test depending on an application that
depends on a library, represented by `Test -> Application -> Library`. Let's
also assume that our flag/configuration affects the `Application` but not the
`Library`. If one runs both versions of the test, with the feature
enabled/disabled, one would assume the `Library` is reused and only the
`Application` and `Test` would have to be re-built.

This deduplication is accomplished via the cache (but not on the build system itself!).
Several efforts have been done over the years which finally converge in
`Path Mapping <https://github.com/bazelbuild/bazel/discussions/22658>`_.
It was confirmed using a Java example, which is the language with most advanced
support, this is behaving as desired.

Path mapping for C++ is `supported <https://github.com/bazelbuild/bazel/pull/22876>`_
since Bazel version 7.3.0. Any internal custom rules in S-CORE must also support this.
A starting point for requirements based on the rules can be found
`here <https://github.com/bazelbuild/bazel/discussions/22658>`_.
Please be advised, that this may be incomplete. Please refer to Bazel documentation.

Transitions have a slight user experience issue.
Since they are applied via entry point which recursively configures it's
tree, users must be aware that building any dependency referenced by the
transition will lose the configuration set by the transition itself (instead,
the configuration will be taken from the user's command).

..
  _Links used in the document:

.. _eclipse-score/score:flags: <https://github.com/eclipse-score/score/tree/main/flags>

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
variant management of SCORE.

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

    build:feature_flag_values_non_default --//some_module:some_feature=False --//yet_another_module:some_other_feature=False

.. code-block:: bash

    bazel build \
    --platforms=//platform:some_platform \ # TODO: To be defined with overall integration
    --config=feature_flag_values_non_default \
    --extra_toolchains=//toolchains:some_compiler //some_module:some_target

Note that these are mere user conveniences and combinatorial scenarios will not
be allowed in CI testing.

Bazel configuration items
^^^^^^^^^^^^^^^^^^^^^^^^^

Bazel has two fundamental building blocks for specifying configuration:

- **Build settings**: A build setting is a single piece of configuration
  information. Configuration information can be modeled as key/value map, where
  one build setting could assume multiple values. Build settings generally
  affect the target application build graph (via select()). Build settings must
  have default values and can be overwritten using **build flags**.
- **Platforms**: A platform is a concrete definition within dimensions that can
  vary across target environments. Platforms in Bazel are defined by
  specifying the concrete values (constraint_value) within a varying dimension
  (constraint_setting), similar to the key/value map. For example, the
  fundamental dimensions for processor systems are typically defined by the CPU
  architecture (ISA on a high-level, but could be specialized to a
  micro architecture) and the Operating System. Platforms in Bazel are designed
  for configuration of host/build tools, e.g. select the appropriate compiler
  when building for x86 vs. ARM.

Since this guidance is meant to address feature configuration, we will only
focus on **Build settings**

For further details on the implementation of build settings, check out the
`Bazel documentation <https://bazel.build/extending/config#user-defined-build-settings>`_.

When a user is building/testing, the configuration is set via a combination of
information passed from the user, via command line, and the default values
configured in the build settings. Bazel also provides convenient indirections
that abstract a collection of flags, namely
`--config <https://bazel.build/docs/user-manual#config>`_.

Bazel transitions
^^^^^^^^^^^^^^^^^

As aforementioned, configuration of a build/test is typically set by the user
via command-line. **Transitions** break this pattern in order to support
multi-configuration builds/tests in one go. This is accomplished by creating an
entry point for the build that automatically configures its graph, ignoring the
configuration set by the user.

Transitions have drawbacks though:

Let's imagine a scenario where we have a test depending on an application that
depends on a library, represented by `Test -> Application -> Library`. Let's
also assume that our flag/configuration affects the `Application` but not the
`Library`. If one runs both versions of the test, with the feature
enabled/disabled, one would assume the `Library` is reused and only the
`Application` and `Test` would have to be re-built.

Unfortunately, this is not the case, with transitions the entire build tree
would be duplicated. This happens because Bazel has a core assumption for
correctness: Isolation between different actions/configurations, i.e. no shared
actions. A more detailed explanation can be found
`here <https://github.com/bazelbuild/bazel/issues/14236#issuecomment-1332896717>`_.

The Bazel maintainers and community have mitigated this issue, by accomplishing
this de-duplication via the cache (but not on the build system itself!).
Several efforts have been done over the years which finally converging in
`Path Mapping <https://github.com/bazelbuild/bazel/discussions/22658>`_.
It was confirmed using a Java example, which is the language with most advanced
support, this is behaving as desired.

Path mapping for C++ is `supported <https://github.com/bazelbuild/bazel/pull/22876>`_
since Bazel version 7.3.0. Any internal custom rules in SCORE must also support this.

Besides the functional issues, transitions also have a slight user experience
issue. Since they are applied via entry point which recursively configures it's
tree, users must be aware that building any dependency referenced by the
transition will lose the configuration set by the transition itself (instead,
the configuration will be taken from the user's command).

Design
------

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

SCORE has four categories of feature flags.

Generic requirements for feature flags:

- Any feature flag shall be defined with a reasonable default value.
- Features that are experimental must be clearly marked as such by prepending `experimental_`
  (e.g. `experimental_<flag_name>`).
- Above every feature flag in the BUILD file a comment must link to the relevant documentation.

Below, we list the four categories of feature flags and provide additional information and constraints for each.

Enabling a feature
^^^^^^^^^^^^^^^^^^

This feature flag is unique per feature in the feature tree and mentioned in the feature description at the top of the
document.

The name of the flag is defined as `<feature_name>`, where `<feature_name>` corresponds to the name of
the feature in `snake_case`.

The feature flag must be of type `bool_flag`.

Feature flags of this category reside in
`eclipse-score/score:flags`_.

Selection of the implementation for an enabled feature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A feature may be provided by multiple modules. The selection of the module which is used for a feature happens through
a feature flag.

The name of the flag is defined as `<feature_name>_implementation`, where `<feature_name>` corresponds to the name of
the feature in `snake_case`.

The feature flag must be of type `string_list_flag` and shall only allow single values.

Feature flags of this category reside in
`eclipse-score/score:flags`_.

Configuration of a feature
^^^^^^^^^^^^^^^^^^^^^^^^^^

To modify behavior of a feature, the documentation in the feature tree may point out several feature flags. Such flags
are of this category.

The name of the flag is defined as `<feature_name>_<configuration>` where:

- `<feature_name>` corresponds to the name of the feature in `snake_case`
- `<configuration>` corresponds to the name of the configuration in `snake_case`

Feature flags of this category reside in
`eclipse-score/score:flags`_.

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

The selection which tests shall be executed depending on a feature values shall
be done via preprocessor macros in the test.cpp

The activation/deactivation of features is propagated via `local_defines`.

.. code-block:: cpp
    :caption: some_module/test.cpp

    #if defined(SOME_FEATURE)
        EXPECT_CALL(...)
    #else
        EXPECT_CALL(...)

.. code-block:: bazel
    :caption: some_module/BUILD

    cc_library(
        name = "lib",
        local_defines = select({
            ":config_some_feature": ["SOME_FEATURE"],
            "//conditions:default": [],
        }),
        # ...
    )

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
        ":config_some_feature": ["SOME_FEATURE"],
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

The selection which tests shall be executed depending on a feature values shall
be done via preprocessor macros in the test.cpp

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

Example output

.. code-block:: bash

    //some_module:some_feature

..
  _Links used in the document:

.. _eclipse-score/score:flags: <https://github.com/eclipse-score/reference_integration/tree/main/flags>

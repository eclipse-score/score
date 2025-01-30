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
load("@bazel_skylib//rules:common_settings.bzl", "BuildSettingInfo", "bool_flag")

OutputPathInfo = provider(fields = ["path"])

FEATURE_TAG_MAPPING = {
    "feature1": ["some-ip", "tag2"],
    "second-feature": ["test-feat", "tag6"],
}

def _get_all_tags():
    """Returns a list of all unique tags from the feature mapping."""
    all_tags = []
    for tags in FEATURE_TAG_MAPPING.values():
        for tag in tags:
            if tag not in all_tags:
                all_tags.append(tag)
    return all_tags

def _feature_flag_translator_impl(ctx):
    output = ctx.actions.declare_file("feature_flags.txt")

    # Start with all possible tags
    remaining_tags = _get_all_tags()

    # Remove tags for each enabled feature
    for flag, _ in ctx.attr.flags.items():
        if flag[BuildSettingInfo].value:
            flag_name = flag.label.name
            if flag_name in FEATURE_TAG_MAPPING:
                # Remove the tags associated with this feature
                for tag in FEATURE_TAG_MAPPING[flag_name]:
                    if tag in remaining_tags:
                        remaining_tags.remove(tag)

    # Sort tags for consistent output
    remaining_tags = sorted(remaining_tags)
    content = ",".join(remaining_tags)
    print("Feature flags content: %s" % content)
    ctx.actions.write(output = output, content = content)

    # Return both DefaultInfo and RunfilesInfo
    return [
        DefaultInfo(
            files = depset([output]),
            runfiles = ctx.runfiles(files = [output]),
        ),
    ]

feature_flag_translator = rule(
    implementation = _feature_flag_translator_impl,
    attrs = {
        "flags": attr.label_keyed_string_dict(
            mandatory = True,
            providers = [BuildSettingInfo],
        ),
    },
)

def define_feature_flags(name):
    bool_flag(
        name = "feature1",
        build_setting_default = False,
    )
    bool_flag(
        name = "second-feature",
        build_setting_default = False,
    )

    feature_flag_translator(
        name = name,
        flags = {":feature1": "True", ":second-feature": "True"},
    )

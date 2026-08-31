# *******************************************************************************
# Copyright (c) 2026 Contributors to the Eclipse Foundation
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

load("@score_docs_as_code//:docs.bzl", "docs_bundle")
load("@score_tooling//bazel/rules/rules_score:rules_score.bzl", "feature_requirements")

package(default_visibility = ["//visibility:public"])

# Exposes the raw RST source so other repos (e.g. baselibs) can reference it,
# e.g. for docs assembly or ad-hoc tooling that doesn't need TrlcProviderInfo.
filegroup(
    name = "feat_req_baselibs_rst",
    srcs = ["index.rst"],
)

# This directory has its own BUILD file (needed for feature_requirements
# below), so the root docs()'s glob no longer descends into it. Re-expose
# these RST sources as a docs_bundle, mounted back into place from //BUILD,
# so the //docs/features/baselibs/index.rst toctree keeps resolving.
docs_bundle(
    name = "docs",
    source_dir = ".",
)

# TRLC-level stand-in for the stakeholder requirements (stkh_req, which have
# no TRLC representation of their own) that feat_req_baselibs derives_from.
# Defined in //docs/requirements/stakeholder (same package as its RST source,
# required by the rst_to_trlc rule's declare_file/sibling constraint), package
# "StakeholderRequirements" (see there for details).

# Converts the feature requirement directives to TRLC and provides
# TrlcProviderInfo + FeatureRequirementsInfo, consumable by
# component_requirements()/dependable_element() targets in downstream repos
# (e.g. baselibs). derived_from references resolve against
# asr_req_stakeholder (ref_package must match its package name above:
# "StakeholderRequirements").
#
# This is the single feature-requirements target for all of baselibs (no
# more narrower per-feature split like the former feat_req_bitmanipulation):
# downstream dependable_element()/component_requirements() targets that only
# care about one feature (e.g. baselibs' bitmanipulation) pull in all 14
# baselibs feature requirements as their "Feature Requirements" lobster pool.
# Accepted trade-off: their traceability report's Feature Requirements
# coverage will be well below 100% (only their own feature is ever
# referenced by a Component Requirement; the other 13 are unrelated), but
# that's a reporting-precision concern only - maturity=development treats it
# as a warning, not a build/test failure.
feature_requirements(
    name = "feat_req_baselibs",
    srcs = ["index.rst"],
    deps = ["//docs/requirements/stakeholder:asr_req_stakeholder"],
    ref_package = "StakeholderRequirements",
)

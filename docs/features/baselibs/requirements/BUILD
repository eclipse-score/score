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
# srcs lists both index.rst and bitmanipulation.rst: the latter's content is
# `.. include::`-d back into index.rst (so the rendered docs/toctree are
# unaffected), but rst_to_trlc.py parses raw RST text and doesn't resolve
# Sphinx includes, so the bitmanipulation feat_req has to be listed
# explicitly here as well to still be picked up by this target (in addition
# to feat_req_bitmanipulation below, which converts it in isolation for
# consumers that only want that one feature requirement).
feature_requirements(
    name = "feat_req_baselibs",
    srcs = [
        "index.rst",
        "bitmanipulation.rst",
    ],
    deps = ["//docs/requirements/stakeholder:asr_req_stakeholder"],
    ref_package = "StakeholderRequirements",
)

# Bitmanipulation's feat_req in isolation (same source file as above, just
# converted on its own), so downstream consumers (baselibs'
# dependable_element_bitmanipulation) can depend on only the one feature
# requirement relevant to them instead of pulling in all 14 baselibs feature
# requirements via feat_req_baselibs. Package defaults to "Bitmanipulation"
# (derived from the "bitmanipulation.rst" stem), distinct from
# feat_req_baselibs's "Index"/"Bitmanipulation" package pair above - no
# collision since each .rst source gets its own auto-derived package name.
feature_requirements(
    name = "feat_req_bitmanipulation",
    srcs = ["bitmanipulation.rst"],
    deps = ["//docs/requirements/stakeholder:asr_req_stakeholder"],
    ref_package = "StakeholderRequirements",
)

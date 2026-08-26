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
load("@score_tooling//bazel/rules/rules_score:rules_score.bzl", "assumed_system_requirements")

package(default_visibility = ["//visibility:public"])

# This directory has its own BUILD file (needed for assumed_system_requirements
# below), so the root docs()'s glob no longer descends into it. Re-expose
# these RST sources as a docs_bundle, mounted back into place from //BUILD, so
# the surrounding requirements toctree keeps resolving.
docs_bundle(
    name = "docs",
    source_dir = ".",
)

# TRLC-level stand-in for the stakeholder requirements: stkh_req has no TRLC
# representation of its own, so rst_to_trlc.py's stkh_req -> AssumedSystemReq
# mapping converts every stkh_req directive in index.rst into an
# AssumedSystemReq record. This pulls in all stkh_req entries (not just the
# ones downstream feature_requirements()/component_requirements() targets
# derive_from), same "extra content" tradeoff already accepted elsewhere for
# feat_req_baselibs (see Notes.md in baselibs). package is set explicitly
# since the default (derived from the "index.rst" stem: "Index") would
# collide with other same-named sources.
assumed_system_requirements(
    name = "asr_req_stakeholder",
    srcs = ["index.rst"],
    package = "StakeholderRequirements",
)

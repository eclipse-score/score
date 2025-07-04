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

load("@trlc//:trlc.bzl", "trlc_requirements", "trlc_requirements_test", "trlc_specification")

trlc_requirements(
    name = "feat_req_communication",
    srcs = [
        "feat_req_communication.trlc",
        "//docs/requirements/stakeholder:stkh_reqs",
    ],
    spec = [
        "@score_platform//docs:requirements_metamodel",
        "@score_platform//docs:score_types",
    ],
    visibility = ["//visibility:public"],
)

trlc_requirements_test(
    name = "feat_req_communication_test",
    reqs = [
        ":feat_req_communication",
    ],
    visibility = ["//visibility:public"],
)

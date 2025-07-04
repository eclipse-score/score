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

load("@lobster//:lobster.bzl", "lobster_trlc", "lobster_test")

lobster_trlc(
    name = "system-requirements",
    config = "lobster-trlc-sys.conf",
    requirements = [
        "//docs/requirements/stakeholder:stkh_reqs",
    ],
)

lobster_trlc(
    name = "feature-requirements",
    config = "lobster-trlc-sw.conf",
    requirements = [
        "//docs/features/communication/docs/requirements:feat_req_communication",
    ],
)

lobster_test(
    name = "traceability",
    config = "lobster.conf",
    inputs = [
        ":feature-requirements",
        ":system-requirements",
    ],
)

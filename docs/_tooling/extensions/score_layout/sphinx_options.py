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
from typing import Literal, TypedDict

LayoutDict = dict[str, list[str]]


class SingleLayout(TypedDict):
    grid: Literal["complex", "content"]
    layout: dict[str, list[str]]


needs_layouts: dict[str, SingleLayout] = {
    "score": {
        "grid": "complex",
        "layout": {
            "head_left": [
                '<<meta("title")>>',
            ],
            "head": [
                '<<meta("status",prefix="status: ")>>',
                '<<meta("security",prefix="security: ")>>',
                '<<meta("safety",prefix="safety: ")>>',
            ],
            "head_right": [
                '<<collapse_button("meta",'
                'collapsed="icon:arrow-down-circle",'
                'visible="icon:arrow-right-circle",'
                "initial=False)>>",
            ],
            "meta_left": [
                '<<meta_all(no_links=True, exclude=["layout","style"])>>',
                "<<meta_links_all()>>",
            ],
            "meta_right": [],
            "footer_left": ["<<meta_id()>>"],
            "footer": ['<<meta("type_name")>>'],
            "footer_right": [],
        },
    },
    "focus": {
        # Just show content without title
        "grid": "content",
        "layout": {},
    },
}

needs_global_options = {"layout": "score"}

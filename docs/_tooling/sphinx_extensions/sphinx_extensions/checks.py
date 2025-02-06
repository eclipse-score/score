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
from sphinx.application import Sphinx
from sphinx_needs.api.configuration import add_warning

from docs._tooling.sphinx_extensions.sphinx_extensions.requirements.checks.id import (
    check_id_title_part,
)


def add_warnings(app: Sphinx):
    add_warning(app, "G_Req_Id_Title", check_id_title_part)

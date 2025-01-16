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
from sphinx_needs.api.configuration import add_warning
from sphinx.application import Sphinx
from docs._tooling.sphinx_extensions.sphinx_extensions.requirements.checks.id import (
    check_id_title_part,
)
from docs._tooling.sphinx_extensions.sphinx_extensions.requirements.checks.traceability import (
    check_g_reqid_traceability,
    check_linkage_parent,
    check_linkage_safety,
    check_linkage_status,
    get_all_needs,
)

from docs._tooling.sphinx_extensions.sphinx_extensions.check_options import (
    check_options,
)


def add_warnings(app: Sphinx):
    add_warning(app, "G_Req_Traceability_Get_All_Needs", get_all_needs)
    add_warning(
        app, "G_Req_Traceability_Check_Linkage_Parent_Check", check_linkage_parent
    )
    add_warning(
        app, "G_Req_Traceability_Check_Linkage_Safety_Check", check_linkage_safety
    )
    add_warning(
        app, "G_Req_Traceability_Check_Linkage_Status_Check", check_linkage_status
    )
    add_warning(app, "G_Options", check_options)
    add_warning(app, "G_Req_Traceability", check_g_reqid_traceability)
    add_warning(app, "G_Req_Id_Title", check_id_title_part)

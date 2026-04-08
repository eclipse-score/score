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

# Configuration file for the Sphinx documentation builder.

import os
import sys

# Make local extensions importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "extensions"))

project = "S-CORE"
project_url = "https://eclipse-score.github.io/score"
version = "0.1"

# Base URL of the fault models guideline page in the process_description build.
# fault_id values in FMEA XML files (e.g. "MF_01_01") are linked as
# {fmea_fault_model_base_url}#fmea_fault_model__mf_01_01
fmea_fault_model_base_url = (
    "https://eclipse-score.github.io/process_description/"
    "process_areas/safety_analysis/guidance/fault_models_guideline.html"
)

extensions = [
    # TODO: remove plantuml here once
    # https://github.com/useblocks/sphinx-needs/pull/1508 is merged and docs-as-code
    # is updated with new sphinx-needs version
    "sphinxcontrib.plantuml",
    "score_sphinx_bundle",
    "fmea_xml_table",
]

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

needs_types = [
    {
        "directive": "workproduct",  # = work_product
        "title": "Workproduct",  # = Work Product
        "prefix": "WP__",
        "color": "#DDDD00",
        "style": "artifact",
        "req_opt": [
            ("id", "^WP_.*$"),
            ("status", "^(draft|valid|invalid|volatile)$"),
            ("tags", "^.*$"),
            ("relevant", "^.*$"),
            ("compliance-wp", "^.*$"),
        ],
    },
    {
        "directive": "workflow",
        "title": "Workflow",
        "prefix": "WF__",
        "color": "#FFFF00",
        "style": "process",
        "req_opt": [
            ("id", "^WF_.*$"),
            ("approver", "^.*$"),
            ("supporter", "^.*$"),
            ("input", "^.*$"),
            ("output", "^.*$"),
            ("guidance", "^.*$"),
            ("executes", "^.*$"),
            ("compliance-wf", "^.*$"),
        ],
    },
    {
        "directive": "guidance",
        "title": "Guidance",
        "prefix": "GD__",
        "color": "#DCB239",
        "style": "file",
        "req_opt": [
            ("id", "^GD_.*$"),
        ],
    },
    {
        "directive": "gd_req",
        "title": "Process Requirement",
        "prefix": "GD_REQ__",
        "color": "#DCB239",
        "style": "file",
        "req_opt": [
            ("id", "^GD_REQ__[0-9a-z_]*$"),
        ],
    },
    {
        "directive": "gd_temp",
        "title": "Process Template",
        "prefix": "GD_TEMP__",
        "color": "#DCB239",
        "style": "file",
        "req_opt": [
            ("id", "^GD_TEMP__[0-9a-z_]*$"),
        ],
    },
    {
        "directive": "gd_chklst",
        "title": "Process Checklist",
        "prefix": "GD_CHKLST__",
        "color": "#DCB239",
        "style": "file",
        "req_opt": [
            ("id", "^GD_CHKLST__[0-9a-z_]*$"),
        ],
    },
    {
        "directive": "gd_guidl",
        "title": "Process Guideline",
        "prefix": "GD_GUIDL__",
        "color": "#DCB239",
        "style": "file",
        "req_opt": [
            ("id", "^GD_GUIDL__[0-9a-z_]*$"),
        ],
    },
    {
        "directive": "gd_concept",
        "title": "Process Concept Definition",
        "prefix": "GD_CONCEPT__",
        "color": "#DCB239",
        "style": "file",
        "req_opt": [
            ("id", "^GD_CONCEPT__[0-9a-z_]*$"),
        ],
    },
    {
        "directive": "gd_howto",
        "title": "Process Howto Description",
        "prefix": "GD_HOWTO__",
        "color": "#DCB239",
        "style": "file",
        "req_opt": [
            ("id", "^GD_HOWTO__[0-9a-z_]*$"),
        ],
    },
    {
        "directive": "role",  # = Einzelne Leute der Codeowner Gruppe
        "title": "Role",
        "prefix": "RL_",
        "color": "#DCB239",
        "style": "actor",
        "req_opt": [
            ("id", "^RL_.*$"),
        ],
    },
    {
        "directive": "team",  # = Codeowners
        "title": "Team",
        "prefix": "TE_",
        "color": "#DCB239",
        "style": "node",
        "req_opt": [
            ("id", "^TE_.*$"),
        ],
    },
    {
        "directive": "phase",
        "title": "Phase",
        "prefix": "PH__",
        "color": "#DCB239",
        "style": "queue",
        "req_opt": [
            ("id", "^PH_.*$"),
        ],
    },
    {
        "directive": "milestone",
        "title": "Milestone",
        "prefix": "MS__",
        "color": "#DCB239",
        "style": "circle",
        "req_opt": [
            ("id", "^MS_.*$"),
        ],
    },
    {
        "directive": "process",
        "title": "Process",
        "prefix": "PR__",
        "color": "#DCB239",
        "style": "frame",
        "req_opt": [
            ("id", "^PR_.*$"),
        ],
    },
    {
        "directive": "document",
        "title": "Document",
        "prefix": "DOC__",
        "color": "#DCB239",
        "style": "file",
        "req_opt": [
            ("id", "^DOC__.*$"),
            ("status", "^(draft|valid|invalid|volatile)$"),
            ("safety", "^.*$"),
            ("compliance-gd", "^GD_.*$"),
        ],
    },
    {
        "directive": "req",  # = std_req
        "title": "Requirement",
        "prefix": "R_",
        "color": "#BFD8D2",
        "style": "node",
        "req_opt": [
            ("id", "^R_.*$"),
            ("status", "^(draft|valid|invalid)$"),  # TODO Why draft as well?
        ],
    },
    {
        "directive": "stkh_req",
        "title": "Stakeholder requirements",
        "prefix": "STKH_REQ__",
        "color": "#BFD8D2",
        "style": "node",
        "req_opt": [
            ("id", "^STKH_REQ__.*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("rationale", "^.*$"),
        ],
    },
    {
        "directive": "feat_req",
        "title": "Feature Requirements",
        "prefix": "FEAT_REQ__",
        "color": "#BFD8D2",
        "style": "node",
        "req_opt": [
            ("id", "^FEAT_REQ__.*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^STKH_REQ__.*$"),
        ],
    },
    {
        "directive": "comp_req",
        "title": "Component Requirements",
        "prefix": "COMP_REQ__",
        "color": "#BFD8D2",
        "style": "node",
        "req_opt": [
            ("id", "^COMP_REQ__.*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^FEAT_REQ__.*$"),
        ],
    },
    {
        "directive": "tool_req",
        "title": "Tool Requirements",
        "prefix": "TOOL_REQ__",
        "color": "#BFD8D2",
        "style": "node",
        "req_opt": [
            ("id", "^TOOL_REQ__.*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^GD_.*$"),
        ],
    },
    {
        "directive": "aou",
        "title": "Assumption of Use",
        "prefix": "AOU__",
        "color": "#BFD8D2",
        "style": "node",
        "req_opt": [
            ("id", "^AOU__.*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
        ],
    },
    {
        "directive": "feat_arc_sta",
        "title": "Feature Architecture Static View",
        "prefix": "FEAT_ARC_STA__",
        "color": "#FEDCD2",
        "style": "card",
        "req_opt": [
            ("id", "^FEAT_ARC_STA__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^FEAT_REQ__.*$"),
        ],
    },
    {
        "directive": "feat_arc_dyn",
        "title": "Feature Architecture Dynamic View",
        "prefix": "FEAT_ARC_DYN__",
        "color": "#FEDCD2",
        "style": "card",
        "req_opt": [
            ("id", "^FEAT_ARC_DYN__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^FEAT_REQ__.*$"),
        ],
    },
    {
        "directive": "feat_arc_int",
        "title": "Feature Architecture Interfaces",
        "prefix": "FEAT_ARC_INT__",
        "color": "#FEDCD2",
        "style": "card",
        "req_opt": [
            ("id", "^FEAT_ARC_INT__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^FEAT_REQ__.*$"),
            # ("includes","^FEAT_ARC_INT_OP__.*$"),
            # ("satisfies","^FEAT_REQ__.*$"),
        ],
    },
    {
        "directive": "feat_arc_int_op",
        "title": "Feature Architecture Interface Operation",
        "prefix": "FEAT_ARC_INT_OP__",
        "color": "#FEDCD2",
        "style": "card",
        "req_opt": [
            ("id", "^FEAT_ARC_INT_OP__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
        ],
    },
    {
        "directive": "mod_arc_sta",
        "title": "Module Architecture Static View",
        "prefix": "MOD_ARC_STA__",
        "color": "#FEDCD2",
        "style": "card",
        "req_opt": [
            ("id", "^MOD_ARC_STA__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            # ("includes", "^COMP_ARC_STA__.*$"),
        ],
    },
    {
        "directive": "comp_arc_sta",
        "title": "Component Architecture Static View",
        "prefix": "COMP_ARC_STA__",
        "color": "#FEDCD2",
        "style": "card",
        "req_opt": [
            ("id", "^COMP_ARC_STA__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^COMP_REQ__.*$"),
            # ("uses", "^COMP_ARC_INT__.*$"),
            # ("implements", "^COMP_ARC_INT__.*$"),
            # ("includes", "^SUB_COMP_ARC_STA__.*$"),
            # ("satisfies","^COMP_REQ__.*$"),
        ],
    },
    {
        "directive": "comp_arc_dyn",
        "title": "Component Architecture Dynamic View",
        "prefix": "COMP_ARC_DYN__",
        "color": "#FEDCD2",
        "style": "card",
        "req_opt": [
            ("id", "^COMP_ARC_DYN__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^COMP_REQ__.*$"),
        ],
    },
    {
        "directive": "comp_arc_int",
        "title": "Component Architecture Interfaces",
        "prefix": "COMP_ARC_INT__",
        "color": "#FEDCD2",
        "style": "card",
        "req_opt": [
            ("id", "^COMP_ARC_INT__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^COMP_REQ__.*$"),
            # ("includes","^COMP_ARC_INT_OP__.*$"),
        ],
    },
    {
        "directive": "comp_arc_int_op",
        "title": "Component Architecture Interface Operation",
        "prefix": "COMP_ARC_INT_OP__",
        "color": "#FEDCD2",
        "style": "card",
        "req_opt": [
            ("id", "^COMP_ARC_INT__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^COMP_REQ__.*$"),
            # ("implements","^FEAT_ARC_INT_OP_.*$"),
        ],
    },
    {
        "directive": "review_header",
        "req_opt": [
            ("id", ".*"),
        ],
    },
]


# Extra link types, which shall be available and allow need types to be linked to each other.
# We use a dedicated linked type for each type of a conncetion, for instance from
# a specification to a requirement. This makes filtering and visualization of such connections
# much easier, as we can sure the target need of a link has always a specific type.
# Docs: https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-extra-links
needs_extra_links = [
    {  # team -> role
        "option": "contains",
        "incoming": "is part of",
        "outgoing": "consists of",
    },
    {  # workflow -> role
        "option": "responsible",
        "incoming": "is reponsible for",
        "outgoing": "responsible",
    },
    {  # workflow -> role
        "option": "approver",
        "incoming": "is approver for",
        "outgoing": "approving",
    },
    {  # workflow -> role
        "option": "supporter",
        "incoming": "is supporter for",
        "outgoing": "supporting",
    },
    {  # process -> role
        "option": "owner",
        "incoming": "is process owner for",
        "outgoing": "process owner",
    },
    {  # process -> workflow
        "option": "includes",
        "incoming": "is included in",
        "outgoing": "includes workflow",
    },
    {  # workflow -> workproduct
        "option": "output",
        "incoming": "is output from",
        "outgoing": "has output",
    },
    {  # workflow -> workproduct
        "option": "input",
        "incoming": "is input from",
        "outgoing": "has input",
    },
    {  # workflow -> guidance
        "option": "guidance",
        "incoming": "is guiding",
        "outgoing": "has guidance",
    },
    {  # workflow -> phase
        "option": "executes",
        "incoming": "relevant workflows",
        "outgoing": "is relevant for phase",
    },
    {  # milestone -> phase
        "option": "phase-relevant",
        "incoming": "is relevant for milestone",
        "outgoing": "relevant phases",
    },
    {  # workproduct  -> milestone
        "option": "relevant",
        "incoming": "relevant workproducts",
        "outgoing": "is relevant for milestone",
    },
    {  # workproduct -> req
        "option": "compliance-wp",
        "incoming": "complies to",
        "outgoing": "is complying with",
    },
    {  # workflow -> req
        "option": "compliance-wf",
        "incoming": "complies to",
        "outgoing": "is complying with",
    },
    # in future we want to migrate to
    {  # guidance -> req compliance
        "option": "compliance-gd",
        "incoming": "complies to",
        "outgoing": "is complying with",
    },
    {
        "option": "satisfies",
        "incoming": "is satisfied by",
        "outgoing": "satisfies",
        "style_start": "-up",
        "style_end": "->",
    },
    {"option": "implements", "incoming": "implements by", "outgoing": "implements"},
]

# Define extra options for needs object
needs_extra_options = [
    "security",
    "safety",
    "level",
    "rationale",
    "mitigated_by",
    "reqtype",
    "source_code_link",
    "codelink",
    "testlink",
    "reqcovered",
    "testcovered",
    "author",
    "reviewers",
    "hash",
    "approvers",
]

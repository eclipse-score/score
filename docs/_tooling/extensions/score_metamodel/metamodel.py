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
    ##############################################################
    #  Process Metamodel
    ##############################################################
    {
        "directive": "workproduct",
        "title": "Workproduct",
        "prefix": "WP__",
        "req_opt": [
            ("id", "^WP__[0-9a-z_]*$"),
            ("status", "^(valid|draft)$"),
            ("complies", "^(ISO26262_WP|ISO21434_WP|ASPICE-40_IIC)[0-9a-z_]*$"),
        ],
    },
    {
        "directive": "workflow",
        "title": "Workflow",
        "prefix": "WF__",
        "req_opt": [
            ("id", "^WF__[0-9a-z_]*$"),
            ("status", "^(valid|draft)$"),
            ("input", "^WP__[0-9a-z_]*$"),
            ("output", "^WP__[0-9a-z_]*$"),
            ("contains", "^GD_(REQ|TEMP|CHKLST|GUIDL|METH)__[0-9a-z_]*$"),
            ("has", "^DOC_(GETSTRT|CONCEPT)__.*$"),
            ("approved_by", "^RL__.*$"),
            ("responsible", "^RL__.*$"),
        ],
        "opt_opt": [
            ("supported_by", "^RL__.*$"),
        ],
    },
    {
        "directive": "gd_req",
        "title": "Process Requirements",
        "prefix": "GD_REQ__",
        "req_opt": [
            ("id", "^GD_REQ__[0-9a-z_]*$"),
            ("status", "^(valid|draft)$"),
            ("complies", "^(ISO26262_REQ|ISO21434_REQ|ASPICE-40_(G|B)P)[0-9a-z_]*$"),
        ],
    },
    {
        "directive": "gd_temp",
        "title": "Process Template",
        "prefix": "GD_TEMP__",
        "req_opt": [
            ("id", "^GD_TEMP__[0-9a-z_]*$"),
            ("status", "^(valid|draft)$"),
            ("complies", "^(ISO26262_REQ|ISO21434_REQ|ASPICE-40_(G|B)P)[0-9a-z_]*$"),
        ],
    },
    {
        "directive": "gd_chklst",
        "title": "Process Checklist",
        "prefix": "GD_CHKLST__",
        "req_opt": [
            ("id", "^GD_CHKLST__[0-9a-z_]*$"),
            ("status", "^(valid|draft)$"),
            ("complies", "^(ISO26262_REQ|ISO21434_REQ|ASPICE-40_(G|B)P)[0-9a-z_]*$"),
        ],
    },
    {
        "directive": "gd_guidl",
        "title": "Process Guideline",
        "prefix": "GD_GUIDL__",
        "req_opt": [
            ("id", "^GD_GUIDL__[0-9a-z_]*$"),
            ("status", "^(valid|draft)$"),
            ("complies", "^(ISO26262_REQ|ISO21434_REQ|ASPICE-40_(G|B)P)[0-9a-z_]*$"),
        ],
    },
    {
        "directive": "gd_method",
        "title": "Process Method",
        "prefix": "GD_METH__",
        "req_opt": [
            ("id", "^GD_METH__[0-9a-z_]*$"),
            ("status", "^(valid|draft)$"),
            ("complies", "^(ISO26262_REQ|ISO21434_REQ|ASPICE-40_(G|B)P)[0-9a-z_]*$"),
        ],
    },
    {
        "directive": "doc_concept",
        "title": "Process Concept Definition",
        "prefix": "DOC_CONCEPT__",
        "req_opt": [
            ("id", "^DOC_CONCEPT__[0-9a-z_]*$"),
            ("status", "^(valid|draft)$"),
        ],
    },
    {
        "directive": "doc_getstrt",
        "title": "Process Getting Startet",
        "prefix": "DOC_GETSTRT__",
        "req_opt": [
            ("id", "^DOC_GETSTRT__[0-9a-z_]*$"),
            ("status", "^(valid|draft)$"),
        ],
    },
    {
        "directive": "role",
        "title": "Role",
        "prefix": "RL__",
        "req_opt": [
            ("id", "^RL__[0-9a-z_]*$"),
        ],
        "opt_opt": [
            ("contains", "^RL__.*$"),
        ],
    },
    {
        "directive": "std_req",
        "title": "Standard Requirement",
        "prefix": "STD_REQ__",
        "req_opt": [
            ("id", "^STD_REQ__[0-9a-z_]*$"),
            ("status", "^(valid)$"),
        ],
    },
    ##############################################################
    #  Score Metamodel
    ##############################################################
    # General
    {
        "directive": "document",
        "title": "Generic Document",
        "prefix": "DOC__",
        "req_opt": [
            ("id", "^DOC__[0-9a-z_]*$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("rationale", "^.+$"),
        ],
    },
    # Requirements
    {
        "directive": "stkh_req",
        "title": "Stakeholder Requirement",
        "prefix": "STKH_REQ__",
        "req_opt": [
            ("id", "^STKH_REQ__[0-9a-z_]*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("rationale", "^.+$"),
        ],
        "opt_opt": [
            ("codelink", "^.*$"),
            ("testlink", "^.*$"),
            ("reqcovered", "^(YES|NO)$"),
            ("testcovered", "^(YES|NO)$"),
            ("hash", "^.*$"),
        ],
    },
    {
        "directive": "feat_req",
        "title": "Feature Requirement",
        "style": "node",
        "req_opt": [
            ("id", "^FEAT_REQ__[0-9a-z_]*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^STKH_REQ__.*$"),
        ],
        "opt_opt": [
            ("codelink", "^.*$"),
            ("testlink", "^.*$"),
            ("reqcovered", "^(YES|NO)$"),
            ("testcovered", "^(YES|NO)$"),
            ("hash", "^.*$"),
        ],
    },
    {
        "directive": "comp_req",
        "title": "Component Requirement",
        "prefix": "COMP_REQ__",
        "req_opt": [
            ("id", "^COMP_REQ__[0-9a-z_]*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^FEAT_REQ__.*$"),
        ],
        "opt_opt": [
            ("codelink", "^.*$"),
            ("testlink", "^.*$"),
            ("reqcovered", "^(YES|NO)$"),
            ("testcovered", "^(YES|NO)$"),
            ("hash", "^.*$"),
        ],
    },
    {
        "directive": "tool_req",
        "title": "Tool Requirement",
        "prefix": "TOOL_REQ__",
        "req_opt": [
            ("id", "^TOOL_REQ__[0-9a-z_]*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^GD_.*$"),
        ],
        "opt_opt": [
            ("codelink", "^.*$"),
            ("testlink", "^.*$"),
            ("reqcovered", "^(YES|NO)$"),
            ("testcovered", "^(YES|NO)$"),
            ("hash", "^.*$"),
        ],
    },
    {
        "directive": "aou_req",
        "title": "Assumption of Use",
        "prefix": "AOU_REQ__",
        "req_opt": [
            ("id", "^AOU_REQ__[0-9a-z_]*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
        ],
        "opt_opt": [
            ("codelink", "^.*$"),
            ("testlink", "^.*$"),
            ("reqcovered", "^(YES|NO)$"),
            ("testcovered", "^(YES|NO)$"),
            ("hash", "^.*$"),
        ],
    },
    # Architecture
    {
        "directive": "feat_arc_sta",
        "title": "Feature Architecture Static View",
        "prefix": "FEAT_ARC_STA__",
        "color": "#FEDCD2",
        "style": "card",
        "req_opt": [
            ("id", "^FEAT_ARC_STA__[0-9a-z_]*$"),
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
            ("id", "^FEAT_ARC_DYN__[0-9a-z_]*$"),
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
            ("id", "^FEAT_ARC_INT__[0-9a-z_]*$"),
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
            ("id", "^FEAT_ARC_INT_OP__[0-9a-z_]*$"),
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
            ("id", "^MOD_ARC_STA__[0-9a-z_]*$"),
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
            ("id", "^COMP_ARC_STA__[0-9a-z_]*$"),
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
            ("id", "^COMP_ARC_DYN__[0-9a-z_]*$"),
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
            ("id", "^COMP_ARC_INT__[0-9a-z_]*$"),
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
            ("id", "^COMP_ARC_INT__[0-9a-z_]*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^COMP_REQ__.*$"),
            # ("implements","^FEAT_ARC_INT_OP_.*$"),
        ],
    },
]


# Extra link types, which shall be available and allow need types to be linked to each other.
# We use a dedicated linked type for each type of a conncetion, for instance from
# a specification to a requirement. This makes filtering and visualization of such connections
# much easier, as we can sure the target need of a link has always a specific type.
# Docs: https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-extra-links
needs_extra_links = [
    ##############################################################
    #  Process Metamodel
    ##############################################################
    # Workflow
    {
        "option": "contains",
        "incoming": "contains",
        "outgoing": "is contained by",
    },
    {
        "option": "has",
        "incoming": "has",
        "outgoing": "relates to",
    },
    {
        "option": "input",
        "incoming": "needs input",
        "outgoing": "is input to",
    },
    {
        "option": "output",
        "incoming": "outputs",
        "outgoing": "is output from",
    },
    # Roles
    {
        "option": "responsible",
        "incoming": "is responsible for",
        "outgoing": "responsible",
    },
    {
        "option": "approved_by",
        "incoming": "approved by",
        "outgoing": "approves",
    },
    {
        "option": "supported_by",
        "incoming": "supported by",
        "outgoing": "supports",
    },
    # Workproduct
    {
        "option": "complies",
        "incoming": "complies",
        "outgoing": "complies to",
    },
    ##############################################################
    #  Score Metamodel
    ##############################################################
    # Requirements
    {
        "option": "satisfies",
        "incoming": "is satisfied by",
        "outgoing": "satisfies",
    },
    # Architecture
    {
        "option": "implements",
        "incoming": "implements by",
        "outgoing": "implements",
    },
]

# Define extra options for needs object
needs_extra_options = [
    "security",
    "safety",
    "rationale",
    "reqtype",
    "codelink",
    "testlink",
    "reqcovered",
    "testcovered",
    "hash",
    "author",
    "reviewers",
    "approvers",
]

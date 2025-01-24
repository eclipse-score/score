from pprint import pprint
from sphinx.application import Sphinx
from sphinx_needs.data import SphinxNeedsData, NeedsInfoType
from sphinx_needs.config import NeedsSphinxConfig
from sphinx.environment import BuildEnvironment
from sphinx.util import logging
from copy import deepcopy
import os
import json

logger = logging.getLogger(__name__)


def read_filter_tags(app: Sphinx):
    """
    Helper function to read in the 'filter_tags' provided by `feature_flag.bzl`.

    Args:
        app: The current running Sphinx-Build application

    Returns:
       - List of tags e.g. ['some-ip','another-tag']
       OR
       - Empty list if there is an exception when reading the file.

    Errors:
        If 'filter_tags_file_path' can't be found in the config
    """
    # asserting our worldview
    assert hasattr(
        app.config, "filter_tags_file_path"
    ), "Config missing filter_tags_file_path, this is mandatory."
    print(f"Attempting to read filter tags from: {app.config.filter_tags_file_path}")
    try:
        with open(app.config.filter_tags_file_path, "r") as f:
            content = f.read().strip()
            filter_tags = [tag.strip() for tag in content.split(",")] if content else []
            print(f"Successfully read filter tags: {filter_tags}")
            return filter_tags
    except Exception as e:
        print(f"Could not read filter tags. Error: {e}")
        return []


def hide_needs(app: Sphinx, env: BuildEnvironment):
    """
    Function that hides needs (requirements) if *all* of their tags are in the specified tags to hide.
    Also deletes any references to hidden requirements, e.g. in 'satisfies' option.

    Args:
        app: The current running Sphinx-Build application, this will be supplied automatically
        env: The current running BuildEnvironment, this will be supplied automatically
    """
    filter_tags = read_filter_tags(app)
    Need_Data = SphinxNeedsData(env)
    needs = Need_Data.get_needs_mutable()
    extra_links = [x["option"] for x in NeedsSphinxConfig(env.config).extra_links]
    rm_needs_docs = set()
    rm_needs = []
    for need_id, need in needs.items():
        if need["tags"] and all(tag in filter_tags for tag in need["tags"]):
            rm_needs.append(need_id)
            need["hide"] = True

    # Remove references
    for need_id in needs:
        for opt in extra_links:
            needs[need_id][opt] = [x for x in needs[need_id][opt] if x not in rm_needs]
            needs[need_id][opt + "_back"] = [
                x for x in needs[need_id][opt + "_back"] if x not in rm_needs
            ]


def setup(app):
    app.add_config_value("filter_tags", [], "env", [list])
    app.add_config_value(
        "filter_tags_file_path", None, "env"
    )  # Change default from "" to None

    # Add validation
    app.connect("env-updated", hide_needs)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

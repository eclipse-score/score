from pprint import pprint
from sphinx_needs.data import SphinxNeedsData, NeedsInfoType
from sphinx_needs.config import NeedsSphinxConfig
from sphinx.util import logging
from copy import deepcopy
import os
import json

logger = logging.getLogger(__name__)

def read_filter_tags(app):
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

def set_hide(app, env):
    filter_tags = read_filter_tags(app)
    Need_Data = SphinxNeedsData(env)
    needs = Need_Data.get_needs_mutable()
    extra_links = [x['option'] for x in NeedsSphinxConfig(env.config).extra_links]
    rm_needs_docs = set()
    rm_needs = []
    for need_id, need in needs.items():
        if need['tags'] and all(tag in filter_tags for tag in need['tags']):
            rm_needs.append(need_id)
            need["hide"] = True

    # Remove references 
    for need_id in needs:
        for opt in extra_links:
            needs[need_id][opt] = [x for x in needs[need_id][opt] if x not in rm_needs]
            needs[need_id][opt + "_back"] = [x for x in needs[need_id][opt + "_back"] if x not in rm_needs]


def setup(app):
    app.add_config_value('filter_tags', [], 'env', [list])
    app.add_config_value('filter_tags_file_path', None, 'env')  # Change default from "" to None
    
    # Add validation
    def validate_config(app, config):
        if not config.filter_tags_file_path:
            logger.warning("No filter_tags_file_path configured")
        elif not os.path.exists(config.filter_tags_file_path):
            logger.error(f"Filter tags file not found at: {config.filter_tags_file_path}")
    
    app.connect('config-inited', validate_config)
    app.connect("env-updated", set_hide)
    
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

    
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }



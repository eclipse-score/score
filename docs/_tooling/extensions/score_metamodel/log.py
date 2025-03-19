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
import os

from sphinx_needs.data import NeedsInfoType
from sphinx_needs.logging import SphinxLoggerAdapter


class CheckLogger:
    def __init__(self, log: SphinxLoggerAdapter, prefix: str):
        self._log = log
        self._count = 0
        self._prefix = prefix

    @staticmethod
    def _location(need: NeedsInfoType, prefix: str):
        def get(key):
            return need.get(key, None)

        if get("docname") and get("doctype") and get("lineno"):
            # Note: passing the location as a string allows us to use
            # readable relative paths, passing as a tuple results
            # in absolute paths to ~/.cache/.../bazel-out/..
            if "RUNFILES_DIR" in os.environ or "RUNFILES_MANIFEST_FILE" in os.environ:
                matching_file = f"{need['docname']}{need['doctype']}"
            else:
                matching_file = f"{prefix}/{need['docname']}{need['doctype']}"

            return f"{matching_file}:{need['lineno']}"
        return None

    def warning_for_option(self, need: NeedsInfoType, option: str, msg: str):
        self.warning(
            f"{need['id']}.{option} ({need.get(option, None)}): " + msg,
            location=CheckLogger._location(need, self._prefix),
        )

    def warning_for_need(self, need: NeedsInfoType, msg: str):
        self.warning(
            f"{need['id']}: " + msg, location=CheckLogger._location(need, self._prefix)
        )

    def warning(self, msg: str, location=None):
        self._log.warning(msg, type="score_metamodel", location=location)
        self._count += 1

    @property
    def has_warnings(self):
        return self._count > 0

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
from typing import Any

from docutils.nodes import Node
from sphinx_needs.data import NeedsInfoType
from sphinx_needs.logging import SphinxLoggerAdapter


class CheckLogger:
    def __init__(self, log: SphinxLoggerAdapter, prefix: str):
        self._log = log
        self._info_count = 0
        self._warning_count = 0
        self._prefix = prefix

    @staticmethod
    def _location(need: NeedsInfoType, prefix: str):
        def get(key: str) -> Any:
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

    def warning_for_option(
        self, need: NeedsInfoType, option: str, msg: str, new_check: bool = False
    ):
        full_msg = f"{need['id']}.{option} ({need.get(option, None)}): {msg}"
        location = CheckLogger._location(need, self._prefix)
        self._log_message(full_msg, location, new_check)

    def warning_for_need(self, need: NeedsInfoType, msg: str, new_check: bool = False):
        full_msg = f"{need['id']}: {msg}"
        location = CheckLogger._location(need, self._prefix)
        self._log_message(full_msg, location, new_check)

    def _log_message(
        self,
        msg: str,
        location: None | str | tuple[str | None, int | None] | Node = None,
        is_info: bool = False,
    ):
        if is_info:
            msg += (
                "\nPlease fix this warning related to the new check "
                "before the release of the next version of Score."
            )
            self.info(msg, location)
        else:
            self.warning(msg, location)

    def info(
        self,
        msg: str,
        location: None | str | tuple[str | None, int | None] | Node = None,
    ):
        self._log.info(msg, type="score_metamodel", location=location)
        self._info_count += 1

    def warning(
        self,
        msg: str,
        location: None | str | tuple[str | None, int | None] | Node = None,
    ):
        self._log.warning(msg, type="score_metamodel", location=location)
        self._warning_count += 1

    @property
    def has_warnings(self):
        return self._warning_count > 0

    @property
    def has_infos(self):
        return self._info_count > 0

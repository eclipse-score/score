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
"""The tool for checking if artifacts have proper copyright."""

import argparse
import os
import logging
import sys
import tempfile
import mmap
import json
from datetime import datetime
from pathlib import Path

LOGGER = logging.getLogger()

COLORS = {
    "BLUE": "\033[34m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "RED": "\033[31m",
    "DARK_RED": "\033[35;1m",
    "ENDC": "\033[0m",
}

LOGGER_COLORS = {
    "DEBUG": COLORS["BLUE"],
    "INFO": COLORS["GREEN"],
    "WARNING": COLORS["YELLOW"],
    "ERROR": COLORS["RED"],
    "CRITICAL": COLORS["DARK_RED"],
}


class ColoredFormatter(logging.Formatter):
    """
    A custom logging formatter to add color to log level names based on the logging level.

    The `ColoredFormatter` class extends `logging.Formatter` and overrides the `format`
    method to add color codes to the log level name (e.g., `INFO`, `WARNING`, `ERROR`)
    based on a predefined color mapping in `LOGGER_COLORS`. This color coding helps in
    visually distinguishing log messages by severity.

    Attributes:
        LOGGER_COLORS (dict): A dictionary mapping log level names (e.g., "INFO", "ERROR")
                              to their respective color codes.
        COLORS (dict): A dictionary of terminal color codes, including an "ENDC" key to reset
                       colors after the level name.

    Methods:
        format(record): Adds color to the `levelname` attribute of the log record and then
                        formats the record as per the superclass `Formatter`.
    """

    def format(self, record):
        log_color = LOGGER_COLORS.get(record.levelname, "")
        record.levelname = f"{log_color}{record.levelname}:{COLORS['ENDC']}"
        return super().format(record)


class ParamFileAction(argparse.Action):  # pylint: disable=too-few-public-methods
    """
    A custom argparse action to support exclusive parameter files for command-line arguments.

    The `ParamFileAction` class allows users to specify a parameter file (prefixed with '@')
    containing file paths or other inputs, which will override any additional inputs provided
    in the command line. If a parameter file is found, its contents are used exclusively,
    and all other inputs are ignored. If no parameter file is provided, standard inputs are used.

    Attributes:
        parser (argparse.ArgumentParser): The argument parser instance.
        namespace (argparse.Namespace): The namespace where arguments are stored.
        values (list): The list of argument values passed from the command line.
        option_string (str, optional): The option string that triggered this action, if any.

    Methods:
        __call__(parser, namespace, values, option_string=None): Processes the arguments.
            - If any value starts with '@', it reads the parameter file and sets `file_paths`
              in `namespace`.
            - If no parameter file is detected, it directly assigns `values` to `namespace`.
    """

    def __call__(self, parser, namespace, values, option_string=None):
        paramfile = next((v[1:] for v in values if v.startswith("@")), None)
        if paramfile:
            with open(paramfile, "r", encoding="utf-8") as handle:
                file_paths = [line.strip() for line in handle if line.strip()]
            setattr(namespace, self.dest, file_paths)
        else:
            setattr(namespace, self.dest, values)


def get_years_from_config(config_path):
    """
    Reads the years from a JSON configuration file.

    Args:
        config_path (Path): Path to the configuration JSON file.

    Returns:
        list: List of years from the configuration file.
    """
    with config_path.open("r") as file:
        config = json.load(file)
    return config.get("years", [])


def load_templates(path):
    """
    Loads the copyright templates from a configuration file.

    Args:
        path (str): Path to the template file.

    Returns:
        dict: A dictionary where each key is a file extension (e.g., ".cpp")
              and the value is the template string from the config.
    """
    templates = {}
    current_extensions = []

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        templates_for_extensions = ""

        for line in lines:
            stripped_line = line.strip()

            if stripped_line.startswith("[") and stripped_line.endswith("]"):
                if current_extensions:
                    for ext in current_extensions:
                        templates[ext] = templates_for_extensions
                    templates_for_extensions = ""
                    current_extensions = []

                extensions = stripped_line[1:-1].split(",")
                current_extensions = [ext.strip() for ext in extensions]
                LOGGER.debug(current_extensions)
            elif current_extensions:
                templates_for_extensions += line

            if line.strip() == "":
                for ext in current_extensions:
                    templates[ext] = templates_for_extensions
                templates_for_extensions = ""
                current_extensions = []

        if current_extensions:
            for ext in current_extensions:
                templates[ext] = templates_for_extensions

    LOGGER.debug(templates)
    return templates


def configure_logging(log_file_path=None, verbose=False):
    """
    Configures logging to write messages to the specified log file.

    Args:
        log_file_path (str, optional): Path to the log file.
        verbose (bool, optional): If True, sets log level to DEBUG. Otherwise, sets it to INFO.
    """
    log_level = logging.DEBUG if verbose else logging.INFO
    LOGGER.setLevel(log_level)
    LOGGER.handlers.clear()

    if log_file_path is not None:
        handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter("%(levelname)s: %(message)s")
    else:
        handler = logging.StreamHandler()
        formatter = ColoredFormatter("%(levelname)s %(message)s")

    handler.setLevel(log_level)
    handler.setFormatter(formatter)
    LOGGER.addHandler(handler)


def load_text_from_file(path, header_length, encoding, offset):
    """
    Reads the first portion of a file, up to `header_length` characters
    plus an additional offset if provided.

    Args:
        path (Path): A `pathlib.Path` object pointing to the file.
        header_length (int): Number of characters to read for the header.
        encoding (str): Encoding type to use when reading the file.
        offset (int): Additional number of characters to read beyond
                      `header_length`, typically used to account for extra
                      lines (such as a shebang) before the header.

    Returns:
        str: The portion of the file read, which should contain the header if present,
             including any extra characters specified by `offset`.
    """
    total_length = header_length + offset
    LOGGER.debug(
        "Reading first %d characters from file: %s [%s]", total_length, path, encoding
    )
    with open(path, "r", encoding=encoding) as handle:
        return handle.read(total_length)


def load_text_from_file_with_mmap(path, header_length, encoding, offset):
    """
    Maps the file and reads only the first `header_length` bytes plus
    an additional offset if provided.

    Args:
        path (Path): A `pathlib.Path` object pointing to the file.
        header_length (int): Length of the header text to check.
        encoding (str): String for setting decoding type.
        offset (int): Additional number of characters to read beyond
                      `header_length`, typically used to account for extra
                      lines (such as a shebang) before the header.

    Returns:
        str: The portion of the file read, which should contain the header if present.
    """

    file_size = os.path.getsize(path)
    total_length = header_length + offset
    length = min(total_length, file_size)

    if not length:
        LOGGER.warning(
            "File %s is empty [length: %d]. Return empty string.", path, length
        )
        return ""

    LOGGER.debug("Memory mapping first %d bytes from file: %s", header_length, path)
    with open(path, "r", encoding=encoding) as handle:
        with mmap.mmap(handle.fileno(), length=length, access=mmap.ACCESS_READ) as fmap:
            return fmap[:header_length].decode(encoding)


def has_copyright(path, copyright_text, use_mmap, encoding, offset, config):
    """
    Checks if the specified copyright text is present in the beginning of a file.

    Args:
        path (Path): A `pathlib.Path` object pointing to the file to check.
        copyright_text (str): The copyright text to search for at the beginning
                              of the file.
        use_mmap (bool): If True, uses memory-mapped file reading for efficient
                         large file handling.
        encoding (str): Encoding type to use when reading the file.
        offset (int): Additional number of characters to read beyond the length
                      of `copyright_text`, used to account for extra content
                      (such as a shebang) before the copyright text.
        config (Path): Path to the config JSON file where configuration
                variables are stored (e.g. years for copyright headers).

    Returns:
        bool: True if the file contains the copyright text, False if it is missing.

    Raises:
        IOError: If there is an error opening or reading the file.
    """

    load_text = load_text_from_file
    if use_mmap:
        load_text = load_text_from_file_with_mmap

    for year in get_years_from_config(config):
        formated_cr = copyright_text.format(year=year)
        if formated_cr in load_text(path, len(formated_cr), encoding, offset):
            LOGGER.debug("File %s has copyright.", path)
            return True

    LOGGER.debug("File %s doesn't have copyright.", path)
    return False


def get_files_from_dir(directory, exts=None):
    """
    Finds files in the specified directories. Filters by extensions if provided.

    Args:
        dirs (list of str): List of directories to search for files.
        exts (list of str, optional): List of extensions to filter files.
                                      If None, all files are returned.

    Returns:
        list of str: List of file paths found in the directories.
    """
    collected_files = []
    LOGGER.debug("Getting files from directory: %s", directory)
    for path in directory.rglob("*"):
        if path.is_file() and path.stat().st_size != 0:
            if exts is None or path.suffix[1:] in exts:
                collected_files.append(path)
    return collected_files


def collect_inputs(inputs, exts=None):
    """
    Collects files from a list of input paths, optionally filtering by file extensions.

    Args:
        inputs (list): A list of paths to files or directories.
                       If a directory is provided, all files within it are added to the output.
        exts (list, optional): A list of file extensions to filter by (e.g., ['.py', '.txt']).
                               Only files with these extensions will be included if specified.

    Returns:
        list: A list of file paths collected from the input paths, filtered by the given extensions.
              If an input is neither a file nor a directory, it is skipped with a warning.

    Logs:
        Logs messages at the DEBUG level, detailing processing of directories and files,
        and warns if an invalid input path is encountered.
    """
    all_files = []
    LOGGER.debug("Extensions: %s", exts)
    for i in inputs:
        item = Path(i)
        if item.is_dir():
            LOGGER.debug("Processing directory: %s", item)
            all_files.extend(get_files_from_dir(item, exts))
        elif item.is_file() and (exts is None or item.suffix[1:] in exts):
            LOGGER.debug("Processing file: %s", item)
            all_files.append(item)
        else:
            LOGGER.warning("Skipped (input is not a valid file or directory): %s", item)
    return all_files


def create_temp_file(path, encoding):
    """
    Creates a temporary file with the provided content.

    Args:
        path (str): The path of file to write the content to the temporary file.
        encoding (str, optional): Encoding type to use when writing the file.

    Returns:
        str: The path to the temporary file created.
    """
    with tempfile.NamedTemporaryFile(mode="w", encoding=encoding, delete=False) as temp:
        with open(path, "r", encoding=encoding) as handle:
            for chunk in iter(lambda: handle.read(4096), ""):
                temp.write(chunk)
    return temp.name


def fix_copyright(path, copyright_text, encoding, offset):
    """
    Inserts a copyright header into the specified file, ensuring that existing
    content is preserved according to the provided offset.

    Args:
        path (str): The path to the file that needs the copyright header.
        copyright_text (str): The copyright text to be added.
        encoding (str): The character encoding used to read and write the file.
        offset (int): The number of bytes to preserve at the top of the file.
                      If 0, the first line is overwritten unless it's empty.
                      For non-zero offsets, ensures the correct number of bytes
                      are preserved.
    """

    temporary_file = create_temp_file(path, encoding)

    with open(temporary_file, "r", encoding=encoding) as temp:
        # Read the first bytes of first line to check if it is equal to the offset
        first_line = temp.readline()
        byte_array = len(first_line.encode(encoding))

        if offset > 0 and offset != byte_array:
            LOGGER.error("Invalid offset value: %d, expected: %d", offset, byte_array)
            return

        with open(path, "w", encoding=encoding) as handle:
            if offset > 0:
                handle.write(first_line + "\n")
            handle.write(copyright_text.format(year=datetime.now().year))
            # Reset the file pointer to the beginning of the temporary file
            temp.seek(0)
            for chunk in iter(lambda: temp.read(4096), ""):
                handle.write(chunk)
    LOGGER.info("Fixed missing header in: %s", path)


def process_files(
    files, templates, fix, config, use_mmap=False, encoding="utf-8", offset=0
):  # pylint: disable=too-many-arguments
    """
    Processes a list of files to check for the presence of copyright text.

    Args:
        files (list): A list of file paths to check.
        templates (dict): A dictionary where keys are file extensions
                          (e.g., '.py', '.txt') and values are strings or patterns
                          representing the required copyright text.
        config (Path): Path to the config JSON file where configuration
                       variables are stored (e.g. years for copyright headers).
        use_mmap (bool): Flag for using mmap function for reading files
                         (instead of standard option).
        encoding (str): Encoding type to use when reading the file.
        offset (int): Additional number of characters to read beyond the length
                      of `copyright_text`, used to account for extra content
                      (such as a shebang) before the copyright text.

    Returns:
        int: The number of files that do not contain the required copyright text.
    """
    results = {"no_copyright": 0, "fixed": 0}
    for item in files:
        name = Path(item).name
        key = name if name == "BUILD" else Path(item).suffix[1:]
        if key not in templates.keys():
            logging.debug(
                "Skipped (no configuration for selected file extension): %s", item
            )
            continue
        if not has_copyright(item, templates[key], use_mmap, encoding, offset, config):
            if fix:
                fix_copyright(item, templates[key], encoding, offset)
                results["no_copyright"] += 1
                results["fixed"] += 1
            else:
                LOGGER.error(
                    "Missing copyright header in: %s, use --fix to introduce it", item
                )
                results["no_copyright"] += 1
    return results


def parse_arguments(argv):
    """
    Parses command-line arguments.

    Args:
        argv (list of str): List of command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments containing files, directories,
                            copyright_file, extensions and log_file.
    """
    parser = argparse.ArgumentParser(
        description="A script to check for copyright in files with specific extensions."
    )

    parser.add_argument(
        "-t",
        "--template-file",
        type=Path,
        required=True,
        help="Path to the template file",
    )

    parser.add_argument(
        "-c",
        "--config-file",
        type=Path,
        required=True,
        help="Path to the config file",
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable debug logging level"
    )

    parser.add_argument(
        "-l",
        "--log-file",
        type=Path,
        default=None,
        help="Redirect logs from STDOUT to this file",
    )

    parser.add_argument(
        "-e",
        "--extensions",
        type=str,
        nargs="+",
        default=None,
        help="List of extensions to filter when searching for files, e.g., '.h .cpp'",
    )

    parser.add_argument(
        "--use_memory_map",
        action="store_true",
        help="Use memory map for reading conent of files \
              (should be used reading gigabyte ranged files).",
    )

    parser.add_argument(
        "-f",
        "--fix",
        action="store_true",
        help="Fix missing copyright headers by inserting them",
    )

    parser.add_argument(
        "--encoding", default="utf-8", help="File encoding (default: utf-8)."
    )

    parser.add_argument(
        "--offset",
        dest="offset",
        type=int,
        default=0,
        help="Additional length offset to account for characters like a shebang (default is 0)",
    )

    parser.add_argument(
        "inputs",
        nargs="+",
        action=ParamFileAction,
        help="Directories and/or files to parse.",
    )

    return parser.parse_args(argv)


def main(argv=None):
    """
    Entry point for processing files to check for the presence of required copyright text.

    This function parses command-line arguments, configures logging, loads copyright templates,
    collects input files based on provided criteria, and checks each file for the required
    copyright text.

    Args:
        argv (list, optional): List of command-line arguments.
                               If `None`, defaults to `sys.argv[1:]`.

    Returns:
        int: Error code if an IOError occurs during loading templates or collecting input files;
        otherwise, returns 0 as success.
    """
    args = parse_arguments(argv if argv is not None else sys.argv[1:])
    configure_logging(args.log_file, args.verbose)

    try:
        templates = load_templates(args.template_file)
    except IOError as err:
        LOGGER.error("Failed to load copyright text: %s", err)
        return err.errno

    try:
        files = collect_inputs(args.inputs, args.extensions)
    except IOError as err:
        LOGGER.error("Failed to prcess file %s with error", err.filename)
        return err.errno

    LOGGER.debug("Running check on files: %s", files)

    results = process_files(
        files,
        templates,
        args.fix,
        args.config_file,
        args.use_memory_map,
        args.encoding,
        args.offset,
    )
    total_no = results["no_copyright"]
    total_fixes = results["fixed"]

    LOGGER.info("=" * 64)
    LOGGER.info("Process completed.")
    LOGGER.info(
        "Total files without copyright: %s%d%s",
        COLORS["RED"] if total_no > 0 else COLORS["GREEN"],
        total_no,
        COLORS["ENDC"],
    )
    if args.fix:
        total_not_fixed = total_no - total_fixes
        LOGGER.info(
            "Total files that were fixed: %s%d%s",
            COLORS["GREEN"],
            total_fixes,
            COLORS["ENDC"],
        )
        LOGGER.info(
            "Total files that were NOT fixed: %s%d%s",
            COLORS["RED"] if total_not_fixed > 0 else COLORS["GREEN"],
            total_not_fixed,
            COLORS["ENDC"],
        )
    LOGGER.info("=" * 64)

    return 0 if total_no == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

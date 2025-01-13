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
"""The tool for converting requirements.txt into dash checker format"""

import re
import sys
import argparse
import logging
from pathlib import Path
from typing import Optional

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


def configure_logging(log_file_path: Path = None, verbose: bool = False) -> None:
    """
    Configures the logging settings for the application.

    Args:
        log_file_path (Path, optional): The file path where logs should be written.
            If not provided, logs are written to the console. Defaults to `None`.
        verbose (bool, optional): A flag that determines the logging level.
            If `True`, sets the logging level to DEBUG; if `False`, sets it to INFO.
            Defaults to `False`.

    Returns:
        None: This function does not return any value, it only configures logging.

    Notes:
        - If `log_file_path` is provided, the log messages will be saved to the specified file.
        - If `verbose` is `True`, detailed logs (DEBUG level) will be captured; otherwise,
          less detailed logs (INFO level) will be captured.
        - The default logging format is `%(asctime)s - %(name)s - %(levelname)s - %(message)s`.
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


def format_line(
    line: str, regex: str = r"([a-zA-Z0-9_-]+)==([a-zA-Z0-9.\-_]+)"
) -> Optional[str]:
    """
    Formats a line of text by matching a specified regex pattern and extracting components.

    Args:
        line (str): The input string to be processed.
        regex (str, optional): A regular expression pattern to match the input line.

    Returns:
        Optional[str]: A formatted string based on the regex match if the pattern is found,
        or None if no match is found.

    Notes:
        - The function uses the provided regex to capture two components from the input line:
          the package name and its version.
        - The formatted string follows the pattern "pypi/pypi/-/{package}/{version}".
        - If the regex does not match, None is returned.
    """

    ret = None
    match = re.match(f"{regex}", line)

    if match:
        package, version = match.groups()
        ret = f"pypi/pypi/-/{package}/{version}"

    return ret


def convert_to_dash_format(input_file: Path, output_file: Path) -> int:
    """
    Converts the content of an input to a "dash format" and writes output file.

    The exact transformation applied to the content is assumed to replace specific patterns or
    structures with a dash-separated format, although the details depend on the implementation.

    Args:
        input_file (Path): Path to the input file containing the original content.
        output_file (Path): Path to the output file where the converted content will be written.

    Returns:
        int: Error thrown by system over exceptions.
    """
    encoding = "utf-8"
    with open(input_file, "r", encoding=encoding) as infile:
        with open(output_file, "w", encoding=encoding) as outfile:
            for line in infile:
                formatted_line = format_line(line.strip())
                if formatted_line:
                    outfile.write(formatted_line + "\n")


def parse_arguments(argv: list[str]) -> argparse.Namespace:
    """
    Parses command-line arguments passed to the script.

    Args:
        argv (list[str]): A list of command-line arguments, typically `sys.argv[1:]`.

    Returns:
        argparse.Namespace: An object containing the parsed arguments as attributes.

    Notes:
        - This function expects an `argparse.ArgumentParser` to be configured with
          the required arguments. If `argv` is not provided, it defaults to an empty list.
        - Use the `argparse.Namespace` object to access parsed arguments by their names.
    """

    parser = argparse.ArgumentParser(
        description="The tool for converting requirements.txt into dash \
                     checker format."
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable debug logging level",
    )

    parser.add_argument(
        "-l",
        "--log-file",
        type=Path,
        default=None,
        help="Redirect logs from STDOUT to this file",
    )

    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        required=True,
        help="Path to the requirement.txt file",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        required=True,
        help="Path to the formatted_list.txt file",
    )

    return parser.parse_args(argv)


def main(argv: list[str] = None) -> int:
    """
    The main entry point of the script.

    Args:
        argv (list[str], optional): A list of command-line arguments. If not provided,
            defaults to `None`, in which case `sys.argv[1:]` is typically used.

    Returns:
        int: An exit code where `0` indicates successful execution, and any non-zero
        value indicates an error.

    Notes:
        - This function is often called in the `if __name__ == "__main__":` block.
        - The function typically orchestrates parsing arguments, performing the core
          logic of the script, and handling exceptions.
        - Ensure the function catches and logs errors appropriately before returning
          a non-zero exit code.
    """
    args = parse_arguments(argv if argv is not None else sys.argv[1:])
    configure_logging(args.log_file, args.verbose)
    convert_to_dash_format(args.input, args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

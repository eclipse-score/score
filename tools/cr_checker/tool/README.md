# CopyRight Checker

`cr_checker.py` is a tool designed to check if files contain a specified copyright header. It provides configurable logging, color-coded console output, and can handle large file sets efficiently. The script supports reading configuration files for custom copyright templates and can utilize memory-mapped file reading for better performance with large files. Tool itself can also appened copyright header at the beggining of file if flag `--fix` is used.

## Features

- Checks files for specified copyright headers based on file extensions.
- Configurable logging, including color-coded output for easy visibility of log levels.
- Supports parameter files for flexible input handling.
- Can use memory mapping for large file handling.
- Customizable file encoding and offset adjustments for header text positioning.
- Can append copyright headers.
- Can remove provided number of characters from begining of the file.

## Requirements

- Python 3.6+
- `argparse`, `logging`, `os`, `sys`, `mmap`, `tempfile`, and `pathlib` (standard library modules)

## Installation

To use `cr_checker.py`, simply clone this repository.

## Usage

The script can be run from the command line with various options to customize its behavior:

```bash
python cr_checker.py -t <template_file> [options] <inputs>
```

### Arguments

- **-t**, **--template-file**: (Required) Path to the template file that defines the copyright text for each file extension.
- **-v**, **--verbose**: Enable debug-level logging.
- **-l**, **--log-file**: Path to a log file where logs will be saved. If not provided, logs will print to the console.
- **-e**, **--extensions**: List of file extensions to filter, e.g., -e .py .cpp.
- **--use_memory_map**: Use memory-mapped file reading for large files.
- **--encoding**: File encoding (default is utf-8).
- **--offset**: Additional offset for the header length to account for lines like a shebang.
- **--fix**: Setting script into fix mode where copyright header will be added to the files if it's missing from same.
- **--remove-offset**: Number of characters to remove before appending proper copyright header (works only with `--fix` option).
- **inputs**: (Required) Directories or files to parse, or a parameter file prefixed with @ that lists files or directories.

> NOTE: Option `--remove-offset` can have severe consequences if the offset is miscalculated. Use with **extreme caution**.

### Examples

```sh
python cr_checker.py -t templates.ini -e py cpp -v -l logs.txt my_random_file.cpp my_random_file.py

python cr_checker.py -t templates.ini -e py cpp --offset 24 --use_memory_map @files_to_check.txt

python cr_checker.py -t templates.ini -e py cpp --fix --offset 24 --use_memory_map @files_to_check.txt

```

### Template File Format

The template file should be in INI format, with each section representing a file extension and a template key specifying the copyright text.

Example templates.ini:

```ini
[py,sh]
template = # Copyright (c) 2024 Score Project

[cpp,c,hpp, h]
template = // Copyright (c) 2024 Score Project
```

## Exit Codes

- 0: All files contain the required copyright text.
- 1: Some files are missing the required copyright text.
- Other: Error encountered during file processing.

### Logging and Color-Coded Output

By default, logs are printed to the console in color-coded format to indicate log levels. You can redirect logs to a file using the -l option.

#### Log Colors

- DEBUG: Blue
- INFO: Green
- WARNING: Yellow
- ERROR: Red

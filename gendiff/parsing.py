"""The module for checking files format and reading them."""

import json

import yaml


def parse_files(file_path1, file_path2):
    """Check formats of files and read them.

    Args:
        file_path1: Path to the first file.
        file_path2: Path to the second file.

    Returns:
        Parsed files.

    Raises:
        ValueError: if format of file(s) is unsupported or
            trying to parse two files with unmatching formats.
    """
    if file_path1.endswith('json') and file_path2.endswith('json'):
        with open(file_path1) as first_file:
            first_file = json.load(first_file)
        with open(file_path2) as second_file:
            second_file = json.load(second_file)
        return (first_file, second_file)
    elif file_path1.endswith('yaml') or file_path1.endswith('yml'):
        if file_path2.endswith('yaml') or file_path2.endswith('yml'):
            with open(file_path1) as first_file:
                first_file = yaml.safe_load(first_file)
            with open(file_path2) as second_file:
                second_file = yaml.safe_load(second_file)
            return (first_file, second_file)
    raise ValueError('Unsupported format or combination of formats')

"""The module for checking file extension and reading it."""

import json
import os

import yaml

YAML_EXTENSIONS = ('.yaml', '.yml')


def parse_file(file_path):
    """Check extension of file and read it.

    Args:
        file_path: Path to the file.

    Returns:
        Parsed file.

    Raises:
        ValueError: if extension of file is unsupported.
    """
    file_extension = os.path.splitext(file_path)[-1].lower()
    if file_extension == '.json':
        with open(file_path) as parsed_json_file:
            return json.load(parsed_json_file)
    elif file_extension in YAML_EXTENSIONS:
        with open(file_path) as parsed_yaml_file:
            return yaml.safe_load(parsed_yaml_file)
    raise ValueError('Unsupported extension of file')

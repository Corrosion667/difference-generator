"""The engine to run diff generator."""

import json

from gendiff.formatters.plain import plained
from gendiff.formatters.stylish import stylished
from gendiff.parsing import parse_files

formatter_map = {
    'stylish': stylished,
    'plain': plained,
    'json': json.dumps,
}


def converted(python_value):
    """Convert Python's bools and None to required format.

    Args:
        python_value: input value to be examined and converted if necessary.

    Returns:
        Value or converted value if it is True, False or None.
    """
    if python_value is True:
        return 'true'
    elif python_value is False:
        return 'false'
    elif python_value is None:
        return 'null'
    return python_value


def generate_diff(file_path1, file_path2, formatter='stylish'):
    """Get differences between two files.

    Args:
        file_path1: Path to the first file.
        file_path2: Path to the second file.
        formatter: Chosen style of diff CLI view.

    Returns:
        Differences between two files.
    """
    (first_dict, second_dict) = parse_files(file_path1, file_path2)

    def walk(first_dict, second_dict):
        keys = sorted(first_dict.keys() | second_dict.keys())

        def inner(key):
            if key in (first_dict.keys() - second_dict.keys()):
                return (key, converted(first_dict.get(key)), None)
            elif key in (second_dict.keys() - first_dict.keys()):
                return (key, None, converted(second_dict.get(key)))
            elif isinstance(first_dict.get(key), dict):
                if isinstance(second_dict.get(key), dict):
                    new_first_dict = first_dict.get(key)
                    new_second_dict = second_dict.get(key)
                    return (key, walk(new_first_dict, new_second_dict))
            return (
                key,
                converted(first_dict.get(key)),
                converted(second_dict.get(key)),
            )
        return tuple(map(inner, keys))
    return formatter_map[formatter](walk(first_dict, second_dict))

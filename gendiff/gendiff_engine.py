"""The engine to run diff generator."""

NESTED = 'nested'
ADDED = 'added'
KEPT = 'kept'
UPDATED = 'updated'
REMOVED = 'removed'

from gendiff.formatters.json import jsoned
from gendiff.formatters.plain import plained
from gendiff.formatters.stylish import stylished
from gendiff.parsing import parse_file

formatter_map = {
    'stylish': stylished,
    'plain': plained,
    'json': jsoned,
}


def generate_diff(file_path1, file_path2, formatter='stylish'):
    """Get differences between two files.

    Args:
        file_path1: Path to the first file.
        file_path2: Path to the second file.
        formatter: Chosen style of diff CLI view.

    Returns:
        Differences between two files.
    """
    first_dict = parse_file(file_path1)
    second_dict = parse_file(file_path2)

    def walk(first_dict, second_dict):
        keys = (first_dict.keys() | second_dict.keys())

        def inner(key):
            first_value = first_dict.get(key)
            second_value = second_dict.get(key)
            if key in (first_dict.keys() - second_dict.keys()):
                return (key, REMOVED, first_value)
            elif key in (second_dict.keys() - first_dict.keys()):
                return (key, ADDED, second_value)
            elif isinstance(first_value, dict):
                if isinstance(second_value, dict):
                    return (key, NESTED, walk(first_value, second_value))
            elif first_value == second_value:
                return (key, KEPT, first_value)
            return (
                key,
                UPDATED,
                (first_value, second_value),
            )
        return list(map(inner, keys))
    return formatter_map[formatter](walk(first_dict, second_dict))

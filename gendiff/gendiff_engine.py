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
    first_dict = parse_file(file_path1)
    second_dict = parse_file(file_path2)

    def walk(first_dict, second_dict):
        keys = (first_dict.keys() | second_dict.keys())

        def inner(key):
            first_value = first_dict.get(key)
            second_value = second_dict.get(key)
            if key in (first_dict.keys() - second_dict.keys()):
                return (key, REMOVED, converted(first_value))
            elif key in (second_dict.keys() - first_dict.keys()):
                return (key, ADDED, converted(second_value))
            elif isinstance(first_value, dict):
                if isinstance(second_value, dict):
                    return (key, NESTED, walk(first_value, second_value))
            elif first_value == second_value:
                return (key, KEPT, converted(first_value))
            return (
                key,
                UPDATED,
                (converted(first_value), converted(second_value)),
            )
        return list(map(inner, keys))
    return formatter_map[formatter](walk(first_dict, second_dict))

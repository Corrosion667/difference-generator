"""The engine to run diff generator."""
import json


def generate_diff(file_path1, file_path2):
    """Get differences between two files.

    Args:
        file_path1: Path to the first file.
        file_path2: Path to the second file.

    Returns:
        Differences between two files
    """
    with open(file_path1) as first_file:
        first_file = json.load(first_file)
    with open(file_path2) as second_file:
        second_file = json.load(second_file)
    difference = ['{']
    keys = sorted(first_file.keys() | second_file.keys())
    for key in keys:
        if first_file.get(key) == second_file.get(key):
            difference.append('   {0}: {1}'.format(key, first_file.get(key)))
        else:
            difference.append(' - {0}: {1}'.format(key, first_file.get(key)))
            difference.append(' + {0}: {1}'.format(key, second_file.get(key)))
    difference.append('}')
    difference = [_ for _ in difference if 'None' not in _]
    return '\n'.join(difference)

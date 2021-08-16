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
    first_file = json.load(open(file_path1))
    second_file = json.load(open(file_path2))
    difference = ['{']
    keys = sorted(
        [_ for _ in list(first_file.keys()) and list(second_file.keys())],
    )
    for key in keys:
        if first_file.get(key) == second_file.get(key):
            difference.append('   {0}: {1}'.format(key, first_file.get(key)))
        else:
            difference.append(' - {0}: {1}'.format(key, first_file.get(key)))
            difference.append(' + {0}: {1}'.format(key, second_file.get(key)))
    difference.append('}')
    difference = [_ for _ in difference if 'None' not in _]
    return '\n'.join(difference)

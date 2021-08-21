"""The engine to run diff generator."""

from gendiff.parsing import parse_files


def converted(python_value):
    """Convert Python's bools and None to required format.

    Args:
        python_value: input value to be examined and converted if necessary.

    Returns:
        Value or converted value if it is True, False or None
    """
    if python_value is True:
        return 'true'
    elif python_value is False:
        return 'false'
    elif python_value is None:
        return 'null'
    return python_value


def generate_diff(file_path1, file_path2):
    """Get differences between two files.

    Args:
        file_path1: Path to the first file.
        file_path2: Path to the second file.

    Returns:
        Differences between two files
    """
    (first_file, second_file) = parse_files(file_path1, file_path2)
    print(first_file)
    print(second_file)
    difference = ['{']
    keys = sorted(first_file.keys() | second_file.keys())
    for key in keys:
        if key in (first_file.keys() - second_file.keys()):
            difference.append(
                ' - {0}: {1}'.format(key, converted(first_file.get(key))),
            )
        elif key in (second_file.keys() - first_file.keys()):
            difference.append(
                ' + {0}: {1}'.format(key, converted(second_file.get(key))),
            )
        else:
            if first_file.get(key) == second_file.get(key):
                difference.append('   {0}: {1}'.format(
                    key, converted(first_file.get(key)),
                ),
                )
            else:
                difference.append(
                    ' - {0}: {1}'.format(key, converted(first_file.get(key))),
                )
                difference.append(
                    ' + {0}: {1}'.format(key, converted(second_file.get(key))),
                )
    difference.append('}')
    return '\n'.join(difference)

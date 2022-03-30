"""The module contains common utilities for formatters."""

from gendiff.diff import NESTED


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


def sort(diff):
    """Sort keys in diff.

    Args:
        diff: generated difference between two files.

    Returns:
        Sorted diff.
    """
    diff.sort()
    for node in diff:
        key, status, value = node
        if status == NESTED:
            sort(value)
    return diff

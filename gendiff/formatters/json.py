"""Classic json: list of lists with [key, value_file1, value_file2]."""

import json

from gendiff.gendiff_engine import NESTED


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


def jsoned(diff):
    """Convert diff to a CLI notion.

    Args:
        diff: generated difference between two files.

    Returns:
        Difference in classic json format.
    """
    return json.dumps(sort(diff))

"""Classic json: list of lists with [key, status, value(s)]."""

import json

from gendiff.formatters.format_utilities import sort


def jsoned(diff):
    """Convert diff to a CLI notion.

    Args:
        diff: generated difference between two files.

    Returns:
        Difference in classic json format.
    """
    return json.dumps(sort(diff))

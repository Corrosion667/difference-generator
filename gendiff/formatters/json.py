"""Classic json: list of lists with [key, value_file1, value_file2]."""
import json


def jsoned(diff):
    """Convert diff to a CLI notion.

    Args:
        diff: generated difference between two files.

    Returns:
        Difference in classic json format.
    """
    return json.dumps(diff)

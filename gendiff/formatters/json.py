"""Classic json: list of lists with [key, value_file1, value_file2]."""
import json

def sort(diff):
    diff.sort()
    for each in diff:
        if isinstance(each[1], list):
            sort(each[1])
        elif isinstance(each[2], list):
            sort(each[2])
    return diff


def jsoned(diff):
    """Convert diff to a CLI notion.

    Args:
        diff: generated difference between two files.

    Returns:
        Difference in classic json format.
    """
    
    return json.dumps(sort(diff))

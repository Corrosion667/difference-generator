"""Module to create special data structure - diff."""

NESTED = 'nested'
ADDED = 'added'
KEPT = 'kept'
UPDATED = 'updated'
REMOVED = 'removed'


def create_diff(first_dict, second_dict):  # noqa: WPS212, WPS231, C901
    """Get differences between two dicts in special data structure (diff).

    Args:
        first_dict: the first dictionary.
        second_dict: the second dictionary.

    Returns:
        Created diff.
    """
    keys = (first_dict.keys() | second_dict.keys())
    unique_keys1 = (first_dict.keys() - second_dict.keys())
    unique_keys2 = (second_dict.keys() - first_dict.keys())

    def walk(key):  # noqa: WPS430, WPS231
        first_value = first_dict.get(key)
        second_value = second_dict.get(key)
        if key in unique_keys1:
            return (key, REMOVED, first_value)
        elif key in unique_keys2:
            return (key, ADDED, second_value)
        elif isinstance(first_value, dict):
            if isinstance(second_value, dict):
                return (key, NESTED, create_diff(first_value, second_value))
        elif first_value == second_value:
            return (key, KEPT, first_value)
        return (key, UPDATED, (first_value, second_value))
    return list(map(walk, keys))

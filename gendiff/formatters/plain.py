"""Thesis-like format with satements about adding, updating and removal."""

bools = ['true', 'false', 'null']


def formatted(element):
    """Check type of an elemant and format it for CLI.

    Args:
        element: the element of a diff to be checked.

    Returns:
        Formatted element if needed.
    """
    if isinstance(element, dict):
        return '[complex value]'
    elif isinstance(element, int):
        return element
    elif element in bools:
        return element
    return "\'{0}\'".format(element)


def plained(diff):
    """Convert diff to a CLI notion.

    Args:
        diff: generated difference between two files.

    Returns:
        Difference formated into string with necessary syntax.
    """
    difference = ''
    for each in diff:
        if each[1] == each[2]:
            continue
        elif each[2] is None:
            difference = difference + \
                "Property \'{0}\' was removed\n".format(each[0])
        elif each[1] is None:
            difference = difference + \
                "Property \'{0}\' was added with value: {1}\n".format(
                    each[0], formatted(each[2]),
                )
        else:
            difference = difference + \
                "Property \'{0}\' was updated. From {1} to {2}\n".format(
                    each[0], formatted(each[1]), formatted(each[2]),
                )
    return difference

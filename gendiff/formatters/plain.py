"""Thesis-like format with satements about adding, updating and removal."""

bools = ['true', 'false', 'null']
REMOVED = "Property \'{0}{1}\' was removed\n"
ADDED = "Property \'{0}{1}\' was added with value: {2}\n"
UPDATED = "Property \'{0}{1}\' was updated. From {2} to {3}\n"


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

    def walk(sequence, difference, level):
        for each in sequence:
            if isinstance(each[1], tuple):
                level = level + '{0}.'.format(each[0])
                check_len = len('{0}.'.format(each[0]))
                difference += '{0}'.format(walk(each[1], '', level))
                level = level[:-check_len]
            elif isinstance(each[2], tuple):
                level = level + '{0}.'.format(each[0])
                check_len = len('{0}.'.format(each[0]))
                difference += '{0}'.format(walk(each[2], '', level))
                level = level[:-check_len]
            elif each[1] == each[2]:
                continue
            elif each[2] is None:
                difference += REMOVED.format(level, each[0])
            elif each[1] is None:
                difference += ADDED.format(level, each[0], formatted(each[2]))
            else:
                difference += UPDATED.format(
                    level, each[0], formatted(each[1]), formatted(each[2]),
                )
        return difference
    return walk(diff, '', '')[:-1]

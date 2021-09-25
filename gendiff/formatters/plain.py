"""Thesis-like format with satements about adding, updating and removal."""

from gendiff.formatters.format_utilities import converted, sort
from gendiff.gendiff_engine import ADDED, KEPT, NESTED, REMOVED

bools = [True, False, None]
REMOVAL = "Property \'{0}{1}\' was removed\n"
ADDING = "Property \'{0}{1}\' was added with value: {2}\n"
UPDATE = "Property \'{0}{1}\' was updated. From {2} to {3}\n"


def formatted(element):
    """Check type of an elemant and format it for CLI.

    Args:
        element: the element of a diff to be checked.

    Returns:
        Formatted element if needed.
    """
    if isinstance(element, dict):
        return '[complex value]'
    elif element in bools:
        return converted(element)
    elif isinstance(element, int):
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
        for node in sequence:
            key, status, value = node
            if status == NESTED:
                level = '{0}{1}.'.format(level, key)
                check_len = len('{0}.'.format(key))
                difference.append('{0}'.format(walk(value, [], level)))
                level = level[:-check_len]
            elif status == REMOVED:
                difference.append(REMOVAL.format(level, key))
            elif status == ADDED:
                difference.append(ADDING.format(level, key, formatted(value)))
            elif status == KEPT:
                continue
            else:
                old, new = value
                if old == new:
                    continue
                difference.append(UPDATE.format(
                    level, key, formatted(old), formatted(new),
                ))
        return ''.join(difference)
    return walk(sort(diff), [], '')[:-1]

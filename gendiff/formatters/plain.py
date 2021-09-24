"""Thesis-like format with satements about adding, updating and removal."""

from gendiff.gendiff_engine import ADDED, NESTED, REMOVED, KEPT

bools = ['true', 'false', 'null']
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
        sequence.sort()
        for node in sequence:
            key, status, value = node
            if status == NESTED:
                level = level + '{0}.'.format(key)
                check_len = len('{0}.'.format(key))
                difference += '{0}'.format(walk(value, '', level))
                level = level[:-check_len]
            elif status == REMOVED:
                difference += REMOVAL.format(level, key)
            elif status == ADDED:
                difference += ADDING.format(level, key, formatted(value))
            elif status == KEPT:
                continue
            else:
                old, new = value
                if old == new:
                    continue
                difference += UPDATE.format(
                    level, key, formatted(old), formatted(new),
                )
        return difference
    return walk(diff, '', '')[:-1]

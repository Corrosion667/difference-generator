"""Json-like format with - for deleted elements and + for added."""

from gendiff.diff import ADDED, KEPT, NESTED, REMOVED
from gendiff.formatters.format_utilities import converted, sort

LEVEL_TAB = '    '
DICT_TEMPLATE = '{0}{1}: {2}\n'
RECURSION_TEMPLATE = '{0}    {1}: '
KEEPING = '{0}    {1}: {2}\n'
REMOVAL = '{0}  - {1}: {2}\n'
ADDING = '{0}  + {1}: {2}\n'


def format_dict(element, level):
    """Check wheteher an element of a diff is dict and format it.

    Args:
        element: the element of a diff to be checked.
        level: current level of nesting.

    Returns:
        Formatted dict as a string.
    """

    def walk(element, difference, level):
        for key in sorted(element.keys()):
            if isinstance(element[key], dict):
                difference.append(
                    DICT_TEMPLATE.format(
                        (LEVEL_TAB * (level + 1)),
                        key,
                        walk(element[key], ['{\n'], (level + 1)),
                    ),
                )
            else:
                difference.append(DICT_TEMPLATE.format(
                    (LEVEL_TAB * (level + 1)), key, element[key],
                ))
        difference.append('{0}}}'.format((LEVEL_TAB * level)))
        return ''.join(difference)
    if isinstance(element, dict):
        return walk(element, ['{\n'], (level + 1))
    return converted(element)


def stylished(diff):
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
                difference.append(RECURSION_TEMPLATE.format(
                    (LEVEL_TAB * level), key,
                ))
                difference.append('{0}\n'.format(
                    walk(value, ['{\n'], level + 1),
                ))
            elif status == KEPT:
                difference.append(KEEPING.format(
                    (LEVEL_TAB * level), key, format_dict(value, level),
                ))
            elif status is REMOVED:
                difference.append(REMOVAL.format(
                    (LEVEL_TAB * level), key, format_dict(value, level),
                ))
            elif status is ADDED:
                difference.append(ADDING.format(
                    (LEVEL_TAB * level), key, format_dict(value, level),
                ))
            else:
                old, new = value
                difference.append(REMOVAL.format(
                    (LEVEL_TAB * level), key, format_dict(old, level),
                ))
                difference.append(ADDING.format(
                    (LEVEL_TAB * level), key, format_dict(new, level),
                ))
        difference.append('{0}}}'.format((LEVEL_TAB * level)))
        return ''.join(difference)
    return walk(sort(diff), ['{\n'], 0)

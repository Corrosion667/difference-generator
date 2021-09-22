"""Json-like format with - for deleted elements and + for added."""

LEVEL_TAB = '    '
DICT_TEMPLATE = '{0}{1}: {2}\n'
RECURSION_TEMPLATE = '{0}    {1}: '
KEPT = '{0}    {1}: {2}\n'
REMOVED = '{0}  - {1}: {2}\n'
ADDED = '{0}  + {1}: {2}\n'


def format_dict(element, level):
    """Check wheteher an element of a diff is dict and format it.

    Args:
        element: the element of a diff to be checked.
        level: current level of nesting.

    Returns:
        Formatted dict as a string.
    """
    level += 1

    def walk(element, difference, level):
        for key in sorted(element.keys()):
            if isinstance(element[key], dict):
                level += 1
                difference += DICT_TEMPLATE.format(
                    (LEVEL_TAB * level), key, walk(element[key], '{\n', level),
                )
                level -= 1
            else:
                level += 1
                difference += DICT_TEMPLATE.format(
                    (LEVEL_TAB * level), key, element[key],
                )
                level -= 1
        return difference + '{0}}}'.format((LEVEL_TAB * level))
    if isinstance(element, dict):
        return walk(element, '{\n', level)
    return element


def stylished(diff):
    """Convert diff to a CLI notion.

    Args:
        diff: generated difference between two files.

    Returns:
        Difference formated into string with necessary syntax.
    """
    def walk(sequence, difference, level):
        sequence = sorted(sequence)
        for each in sequence:
            if isinstance(each[1], tuple):
                difference += RECURSION_TEMPLATE.format(
                    (LEVEL_TAB * level), each[0],
                )
                level += 1
                difference += '{0}\n'.format(
                    walk(each[1], '{\n', level),
                )
                level -= 1
            elif isinstance(each[2], tuple):
                difference += RECURSION_TEMPLATE.format(
                    (LEVEL_TAB * level), each[0],
                )
                level += 1
                difference += '{0}\n'.format(
                    walk(each[2], '{\n', level),
                )
                level -= 1
            elif each[1] == each[2]:
                difference += KEPT.format(
                    (LEVEL_TAB * level), each[0], format_dict(each[1], level),
                )
            elif each[2] is None:
                difference += REMOVED.format(
                    (LEVEL_TAB * level), each[0], format_dict(each[1], level),
                )
            elif each[1] is None:
                difference += ADDED.format(
                    (LEVEL_TAB * level), each[0], format_dict(each[2], level),
                )
            else:
                difference += REMOVED.format(
                    (LEVEL_TAB * level), each[0], format_dict(each[1], level),
                )
                difference += ADDED.format(
                    (LEVEL_TAB * level), each[0], format_dict(each[2], level),
                )
        return difference + '{0}}}'.format((LEVEL_TAB * level))
    return walk(diff, '{\n', 0)

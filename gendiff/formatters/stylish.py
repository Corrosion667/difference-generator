"""Json-like formatter with - for deleted elements and + for added."""

LEVEL_INDENT = '    '


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
                difference = difference + \
                    '{0}{1}: {2}\n'.format(
                        (LEVEL_INDENT * level),
                        key, walk(element[key], '{\n', level),
                    )
                level -= 1
            else:
                level += 1
                difference = difference + \
                    '{0}{1}: {2}\n'.format(
                        (LEVEL_INDENT * level), key, element[key],
                    )
                level -= 1
        return difference + '{0}}}'.format((LEVEL_INDENT * level))
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
        for each in sequence:
            if isinstance(each[1], tuple):
                difference = difference + \
                    '{0}    {1}: '.format((LEVEL_INDENT * level), each[0])
                level += 1
                difference = difference + \
                    '{0}\n'.format(walk(each[1], '{\n', level))
                level -= 1
            elif isinstance(each[2], tuple):
                difference = difference + \
                    '{0}    {1}: '.format((LEVEL_INDENT * level), each[0])
                level += 1
                difference = difference + \
                    '{0}\n'.format(walk(each[2], '{\n', level))
                level -= 1
            elif each[1] == each[2]:
                difference = difference + \
                    '{0}    {1}: {2}\n'.format(
                        (LEVEL_INDENT * level),
                        each[0], format_dict(each[1], level),
                    )
            elif each[2] is None:
                difference = difference + \
                    '{0}  - {1}: {2}\n'.format(
                        (LEVEL_INDENT * level),
                        each[0], format_dict(each[1], level),
                    )
            elif each[1] is None:
                difference = difference + \
                    '{0}  + {1}: {2}\n'.format(
                        (LEVEL_INDENT * level),
                        each[0], format_dict(each[2], level),
                    )
            else:
                difference = difference + \
                    '{0}  - {1}: {2}\n'.format(
                        (LEVEL_INDENT * level),
                        each[0], format_dict(each[1], level),
                    )
                difference = difference + \
                    '{0}  + {1}: {2}\n'.format(
                        (LEVEL_INDENT * level),
                        each[0], format_dict(each[2], level),
                    )
        return difference + '{0}}}'.format((LEVEL_INDENT * level))
    return walk(diff, '{\n', 0)

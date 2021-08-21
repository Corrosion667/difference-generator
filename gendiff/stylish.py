"""The module with CLI formatters for diffs."""


def stylished(diff):
    """Convert diff to a CLI notion.

    Args:
        diff: generated difference between two files.

    Returns:
        Difference formated into string with necessary syntax.
    """
    difference = '{\n'
    for each in diff:
        if each[2] == 'both':
            difference = difference + '   {0}: {1}\n'.format(each[0], each[1])
        elif each[2] == 'first':
            difference = difference + ' - {0}: {1}\n'.format(each[0], each[1])
        else:
            difference = difference + ' + {0}: {1}\n'.format(each[0], each[1])
    return '{0}}}'.format(difference)

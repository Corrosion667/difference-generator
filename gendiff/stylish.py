"""The module with CLI formatters for diffs."""


def stylished(diff):
    """Convert diff to a CLI notion.

    Args:
        diff: generated difference between two files.

    Returns:
        Difference formated into string with necessary syntax.
    """
    def walk(sequence):
        difference = '{\n'
        for each in sequence:
            if isinstance(each[1], list):
                return difference + '   {0}: {1}\n'.format(each[0], walk(each[1]))
            elif isinstance(each[2], list):
                return difference + '   {0}: {1}\n'.format(each[0], walk(each[2]))
            elif each[1] == each[2]:
                difference = difference + '   {0}: {1}\n'.format(each[0], each[1])
            elif each[2] is None:
                difference = difference + ' - {0}: {1}\n'.format(each[0], each[1])
            elif each[1] is None:
                difference = difference + ' + {0}: {1}\n'.format(each[0], each[2])
            else:
                difference = difference + ' - {0}: {1}\n'.format(each[0], each[1])
                difference = difference + ' + {0}: {1}\n'.format(each[0], each[2])
        return '{0}}}'.format(difference)
    return walk(diff)
    




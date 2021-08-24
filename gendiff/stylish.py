"""The module with CLI formatters for diffs."""


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
                    '{0}    {1}: '.format(('    '*level), each[0])
                level += 1
                difference = difference + \
                    '{0}\n'.format(walk(each[1], '{\n', level))
                level -= 1
            elif isinstance(each[2], tuple):
                difference = difference + \
                    '{0}    {1}: '.format(('    '*level), each[0])
                level += 1
                difference = difference + \
                    '{0}\n'.format(walk(each[2], '{\n', level))
                level -= 1
            elif each[1] == each[2]:
                difference = difference + \
                    '{0}    {1}: {2}\n'.format(('    '*level), each[0], each[1])
            elif each[2] is None:
                difference = difference + \
                    '{0}  - {1}: {2}\n'.format(('    '*level), each[0], each[1])
            elif each[1] is None:
                difference = difference + \
                    '{0}  + {1}: {2}\n'.format(('    '*level), each[0], each[2])
            else:
                difference = difference + \
                    '{0}  - {1}: {2}\n'.format(('    '*level), each[0], each[1])
                difference = difference + \
                    '{0}  + {1}: {2}\n'.format(('    '*level), each[0], each[2])
        difference = difference + '{0}}}'.format(('    '*level))
        return (difference)
    return walk(diff, '{\n', 0)

"""The engine to run diff generator."""

from gendiff.diff import create_diff
from gendiff.formatters.json import jsoned
from gendiff.formatters.plain import plained
from gendiff.formatters.stylish import stylished
from gendiff.parsing import parse_file

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'

formatter_map = {
    STYLISH: stylished,
    PLAIN: plained,
    JSON: jsoned,
}


def generate_diff(file_path1, file_path2, formatter=STYLISH):
    """Get differences between two files.

    Args:
        file_path1: Path to the first file.
        file_path2: Path to the second file.
        formatter: Chosen style of diff CLI view.

    Returns:
        Differences between two files.
    """
    first_dict = parse_file(file_path1)
    second_dict = parse_file(file_path2)
    return formatter_map[formatter](create_diff(first_dict, second_dict))

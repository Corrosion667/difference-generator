"""This is a module to test gendiff program."""

from gendiff.gendiff_engine import generate_diff
from tests.fixtures.estimated_json_result import estimated_difference_json


def test_generate_diff_json():
    """Basic test for json defference generator."""
    assert generate_diff(
        'tests/fixtures/first_test_file.json',
        'tests/fixtures/second_test_file.json',
    ) == estimated_difference_json

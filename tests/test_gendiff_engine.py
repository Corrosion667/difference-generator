"""This is a module to test gendiff program."""

from gendiff.gendiff_engine import generate_diff
from tests.fixtures.estimated_json_result import estimated_difference_json
from tests.fixtures.estimated_yaml_result import estimated_difference_yaml


def test_generate_diff_json():
    """Basic test for json difference generator."""
    assert generate_diff(
        'tests/fixtures/first_test_file.json',
        'tests/fixtures/second_test_file.json',
    ) == estimated_difference_json


def test_generate_diff_yml():
    """Basic test for yaml difference generator."""
    assert generate_diff(
        'tests/fixtures/first_test_file.yml',
        'tests/fixtures/second_test_file.yaml',
    ) == estimated_difference_yaml

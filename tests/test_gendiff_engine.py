"""This is a module to test gendiff program."""

from tests.fixtures.estimated_results import estimated_diff_json, estimated_diff_yaml
from gendiff.gendiff_engine import generate_diff


def test_generate_diff_json():
    """Basic test for json difference generator."""
    assert generate_diff(
        'tests/fixtures/first_test_file.json',
        'tests/fixtures/second_test_file.json',
    ) == estimated_diff_json


def test_generate_diff_yml():
    """Basic test for yaml difference generator."""
    assert generate_diff(
        'tests/fixtures/first_test_file.yml',
        'tests/fixtures/second_test_file.yaml',
    ) == estimated_diff_yaml

"""This is a module to test gendiff program."""
import pytest
from gendiff.gendiff_engine import generate_diff
from tests.fixtures.estimated_results import (
    estimated_difference_json,
    estimated_difference_yaml,
)


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


def test_generate_diff_wrong_formats():
    """Do not allow to parse unmatching formats."""
    with pytest.raises(ValueError):
        generate_diff(
            'tests/fixtures/first_test_file.yml',
            'tests/fixtures/second_test_file.json',
        )

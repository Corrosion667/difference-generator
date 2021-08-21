"""This is a module to test gendiff program."""
import pytest
from gendiff.gendiff_engine import generate_diff
from gendiff.stylish import stylished
from tests.fixtures.estimated_results import (
    estimated_diff_flat_json,
    estimated_diff_flat_yaml,
)


def test_generate_diff_flat_json():
    """Basic test for flat json difference generator."""
    assert stylished(generate_diff(
        'tests/fixtures/flat_test_file1.json',
        'tests/fixtures/flat_test_file2.json',
    )) == estimated_diff_flat_json


def test_generate_diff_flat_yml():
    """Basic test for flat yaml difference generator."""
    assert stylished(generate_diff(
        'tests/fixtures/flat_test_file1.yml',
        'tests/fixtures/flat_test_file2.yaml',
    )) == estimated_diff_flat_yaml


def test_generate_diff_wrong_formats():
    """Do not allow to parse unmatching formats."""
    with pytest.raises(ValueError):
        generate_diff(
            'tests/fixtures/flat_test_file1.yml',
            'tests/fixtures/flat_test_file2.json',
        )

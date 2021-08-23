"""This is a module to test gendiff program."""
import pytest
from gendiff.gendiff_engine import generate_diff
from gendiff.stylish import stylished

with open('tests/fixtures/estimated_results/estimated_flat.txt') as result_file:
    estimated_result_flat = result_file.read()


def test_generate_diff_flat_json():
    """Basic test for flat json difference generator."""
    assert stylished(generate_diff(
        'tests/fixtures/test_files/flat_test_file1.json',
        'tests/fixtures/test_files/flat_test_file2.json',
    )) == estimated_result_flat


def test_generate_diff_flat_yml():
    """Basic test for flat yaml difference generator."""
    assert stylished(generate_diff(
        'tests/fixtures/test_files/flat_test_file1.yml',
        'tests/fixtures/test_files/flat_test_file2.yaml',
    )) == estimated_result_flat


def test_generate_diff_wrong_formats():
    """Do not allow to parse unmatching formats."""
    with pytest.raises(ValueError):
        generate_diff(
            'tests/fixtures/test_files/flat_test_file1.yml',
            'tests/fixtures/test_files/flat_test_file2.json',
        )

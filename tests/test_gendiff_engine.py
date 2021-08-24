"""This is a module to test gendiff program."""
import pytest
from gendiff.gendiff_engine import generate_diff
from gendiff.stylish import stylished


def test_generate_diff_flat_json(get_flat_result):
    """Basic test for flat json difference generator.

    Args:
        get_flat_result: Estimated result for flat diff.
    """
    assert stylished(generate_diff(
        'tests/fixtures/test_files/flat_test_file1.json',
        'tests/fixtures/test_files/flat_test_file2.json',
    )) == get_flat_result


def test_generate_diff_nested_json(get_nested_result):
    """Basic test for nested json difference generator.

    Args:
        get_nested_result: Estimated result for nested diff.
    """
    assert stylished(generate_diff(
        'tests/fixtures/test_files/nested_test_file1.json',
        'tests/fixtures/test_files/nested_test_file2.json',
    )) == get_nested_result


def test_generate_diff_flat_yml(get_flat_result):
    """Basic test for flat yaml difference generator.

    Args:
        get_flat_result: Estimated result for flat diff.
    """
    assert stylished(generate_diff(
        'tests/fixtures/test_files/flat_test_file1.yml',
        'tests/fixtures/test_files/flat_test_file2.yaml',
    )) == get_flat_result


def test_generate_diff_nested_yml(get_nested_result):
    """Basic test for nested yaml difference generator.

    Args:
        get_nested_result: Estimated result for nested diff.
    """
    assert stylished(generate_diff(
        'tests/fixtures/test_files/nested_test_file1.yml',
        'tests/fixtures/test_files/nested_test_file2.yaml',
    )) == get_nested_result


def test_generate_diff_wrong_formats():
    """Do not allow to parse unmatching formats."""
    with pytest.raises(ValueError):
        generate_diff(
            'tests/fixtures/test_files/flat_test_file1.yml',
            'tests/fixtures/test_files/flat_test_file2.json',
        )

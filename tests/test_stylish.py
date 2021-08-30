"""This is a module to test gendiff program with stylish formatter."""
from gendiff.gendiff_engine import generate_diff


def test_generate_diff_flat_json_stylish(get_flat_result_stylish):
    """Basic test for flat json difference generator with stylish formatter.

    Args:
        get_flat_result_stylish: Estimated result of flat diff(stylish format).
    """
    assert generate_diff(
        'tests/fixtures/test_files/flat_test_file1.json',
        'tests/fixtures/test_files/flat_test_file2.json',
    ) == get_flat_result_stylish


def test_generate_diff_nested_json_stylish(get_nested_result_stylish):
    """Basic test for nested json difference generator with stylish formatter.

    Args:
        get_nested_result_stylish: Est. result of nested diff (stylish format).
    """
    assert generate_diff(
        'tests/fixtures/test_files/nested_test_file1.json',
        'tests/fixtures/test_files/nested_test_file2.json',
    ) == get_nested_result_stylish


def test_generate_diff_flat_yml_sylish(get_flat_result_stylish):
    """Basic test for flat yaml difference generator with stylish formatter.

    Args:
        get_flat_result_stylish: Estimated result of flat diff(stylish format).
    """
    assert generate_diff(
        'tests/fixtures/test_files/flat_test_file1.yml',
        'tests/fixtures/test_files/flat_test_file2.yaml',
    ) == get_flat_result_stylish


def test_generate_diff_nested_yml_stylish(get_nested_result_stylish):
    """Basic test for nested yaml difference generator with stylish formatter.

    Args:
        get_nested_result_stylish: Est. result of nested diff (stylish format).
    """
    assert generate_diff(
        'tests/fixtures/test_files/nested_test_file1.yml',
        'tests/fixtures/test_files/nested_test_file2.yaml',
    ) == get_nested_result_stylish

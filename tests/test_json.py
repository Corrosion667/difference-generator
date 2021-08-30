"""This is a module to test gendiff program with json formatter."""
from gendiff.gendiff_engine import generate_diff


def test_generate_diff_flat_json_json(get_flat_result_json):
    """Basic test for flat json difference generator with json formatter.

    Args:
        get_flat_result_json: Estimated result of flat diff(json format).
    """
    assert generate_diff(
        'tests/fixtures/test_files/flat_test_file1.json',
        'tests/fixtures/test_files/flat_test_file2.json',
        'json',
    ) == get_flat_result_json


def test_generate_diff_nested_json_json(get_nested_result_json):
    """Basic test for nested json difference generator with json formatter.

    Args:
        get_nested_result_json: Est. result of nested diff (json format).
    """
    assert generate_diff(
        'tests/fixtures/test_files/nested_test_file1.json',
        'tests/fixtures/test_files/nested_test_file2.json',
        'json',
    ) == get_nested_result_json


def test_generate_diff_flat_yml_json(get_flat_result_json):
    """Basic test for flat yaml difference generator with json formatter.

    Args:
        get_flat_result_json: Estimated result of flat diff(json format).
    """
    assert generate_diff(
        'tests/fixtures/test_files/flat_test_file1.yml',
        'tests/fixtures/test_files/flat_test_file2.yaml',
        'json',
    ) == get_flat_result_json


def test_generate_diff_nested_yml_json(get_nested_result_json):
    """Basic test for nested yaml difference generator with json formatter.

    Args:
        get_nested_result_json: Est. result of nested diff (json format).
    """
    assert generate_diff(
        'tests/fixtures/test_files/nested_test_file1.yml',
        'tests/fixtures/test_files/nested_test_file2.yaml',
        'json',
    ) == get_nested_result_json

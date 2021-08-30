"""This is a module to test gendiff program with plain formatter."""
from gendiff.gendiff_engine import generate_diff


def test_generate_diff_flat_json_plain(get_flat_result_plain):
    """Basic test for flat json difference generator with plain formatter.

    Args:
        get_flat_result_plain: Estimated result of flat diff(plain format).
    """
    assert generate_diff(
        'tests/fixtures/test_files/flat_test_file1.json',
        'tests/fixtures/test_files/flat_test_file2.json',
        'plain',
    ) == get_flat_result_plain


def test_generate_diff_nested_json_plain(get_nested_result_plain):
    """Basic test for nested json difference generator with plain formatter.

    Args:
        get_nested_result_plain: Est. result of nested diff (plain format).
    """
    assert generate_diff(
        'tests/fixtures/test_files/nested_test_file1.json',
        'tests/fixtures/test_files/nested_test_file2.json',
        'plain',
    ) == get_nested_result_plain


def test_generate_diff_flat_yml_plain(get_flat_result_plain):
    """Basic test for flat yaml difference generator with plain formatter.

    Args:
        get_flat_result_plain: Estimated result of flat diff(plain format).
    """
    assert generate_diff(
        'tests/fixtures/test_files/flat_test_file1.yml',
        'tests/fixtures/test_files/flat_test_file2.yaml',
        'plain',
    ) == get_flat_result_plain


def test_generate_diff_nested_yml_plain(get_nested_result_plain):
    """Basic test for nested yaml difference generator with plain formatter.

    Args:
        get_nested_result_plain: Est. result of nested diff (plain format).
    """
    assert generate_diff(
        'tests/fixtures/test_files/nested_test_file1.yml',
        'tests/fixtures/test_files/nested_test_file2.yaml',
        'plain',
    ) == get_nested_result_plain

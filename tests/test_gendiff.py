"""This is a module to test gendiff program using pytest parametrize."""

import pytest
from gendiff.gendiff_engine import JSON, PLAIN, STYLISH, generate_diff


def get_result(path):
    """Get result to test difference generator.

    Args:
        path: path to result file to be read.

    Returns:
        Estimated result for testing.
    """
    with open(path) as result_file:
        estimated_result = result_file.read()
    return estimated_result


@pytest.mark.parametrize('path1, path2, formatter, path_to_result', [
    ('tests/fixtures/test_files/flat_test_file1.json',
     'tests/fixtures/test_files/flat_test_file2.json',
     STYLISH,
     'tests/fixtures/results/flat_stylish.txt',
     ),
    ('tests/fixtures/test_files/flat_test_file1.yml',
     'tests/fixtures/test_files/flat_test_file2.yaml',
     STYLISH,
     'tests/fixtures/results/flat_stylish.txt',
     ),
    ('tests/fixtures/test_files/nested_test_file1.json',
     'tests/fixtures/test_files/nested_test_file2.json',
     STYLISH,
     'tests/fixtures/results/nested_stylish.txt',
     ),
    ('tests/fixtures/test_files/nested_test_file1.yml',
     'tests/fixtures/test_files/nested_test_file2.yaml',
     STYLISH,
     'tests/fixtures/results/nested_stylish.txt',
     ),
    ('tests/fixtures/test_files/flat_test_file1.json',
     'tests/fixtures/test_files/flat_test_file2.json',
     PLAIN,
     'tests/fixtures/results/flat_plain.txt',
     ),
    ('tests/fixtures/test_files/flat_test_file1.yml',
     'tests/fixtures/test_files/flat_test_file2.yaml',
     PLAIN,
     'tests/fixtures/results/flat_plain.txt',
     ),
    ('tests/fixtures/test_files/nested_test_file1.json',
     'tests/fixtures/test_files/nested_test_file2.json',
     PLAIN,
     'tests/fixtures/results/nested_plain.txt',
     ),
    ('tests/fixtures/test_files/nested_test_file1.yml',
     'tests/fixtures/test_files/nested_test_file2.yaml',
     PLAIN,
     'tests/fixtures/results/nested_plain.txt',
     ),
    ('tests/fixtures/test_files/flat_test_file1.json',
     'tests/fixtures/test_files/flat_test_file2.json',
     JSON,
     'tests/fixtures/results/flat_json.txt',
     ),
    ('tests/fixtures/test_files/flat_test_file1.yml',
     'tests/fixtures/test_files/flat_test_file2.yaml',
     JSON,
     'tests/fixtures/results/flat_json.txt',
     ),
    ('tests/fixtures/test_files/nested_test_file1.json',
     'tests/fixtures/test_files/nested_test_file2.json',
     JSON,
     'tests/fixtures/results/nested_json.txt',
     ),
    ('tests/fixtures/test_files/nested_test_file1.yml',
     'tests/fixtures/test_files/nested_test_file2.yaml',
     JSON,
     'tests/fixtures/results/nested_json.txt',
     ),
])
def test_generate_diff(path1, path2, formatter, path_to_result):
    """Test for difference generator.

    Args:
        path1: path to first file.
        path2: path to second file.
        formatter: chosen formatter to test.
        path_to_result: path fo file with estimated result.
    """
    assert generate_diff(
        path1,
        path2,
        formatter,
    ) == get_result(path_to_result)

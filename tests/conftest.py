"""This is a module with fixtures for testing."""
import pytest


@pytest.fixture
def get_flat_result_stylish():
    """Get fixture of estimated diff for testing flat files with stylish formatter.

    Returns:
        Estimated result for flat diff with stylish formatter.
    """
    with open('tests/fixtures/results/flat_stylish.txt') as result_file:
        estimated_result_flat_stylish = result_file.read()
    return estimated_result_flat_stylish


@pytest.fixture
def get_nested_result_stylish():
    """Get fixture of estimated dif for testing nested files with stylish formatter.

    Returns:
        Estimated result for nested diff with stylish formatter.
    """
    with open('tests/fixtures/results/nested_stylish.txt') as result_file:
        estimated_result_nested_stylish = result_file.read()
    return estimated_result_nested_stylish

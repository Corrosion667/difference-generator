"""This is a module with fixtures for testing."""
import json

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


@pytest.fixture
def get_flat_result_plain():
    """Get fixture of estimated diff for testing flat files with plain formatter.

    Returns:
        Estimated result for flat diff with plain formatter.
    """
    with open('tests/fixtures/results/flat_plain.txt') as result_file:
        estimated_result_flat_plain = result_file.read()
    return estimated_result_flat_plain


@pytest.fixture
def get_nested_result_plain():
    """Get fixture of estimated diff for testing nested files with plain formatter.

    Returns:
        Estimated result for nested diff with plain formatter.
    """
    with open('tests/fixtures/results/nested_plain.txt') as result_file:
        estimated_result_nested_plain = result_file.read()
    return estimated_result_nested_plain


@pytest.fixture
def get_flat_result_json():
    """Get fixture of estimated diff for testing flat files with json formatter.

    Returns:
        Estimated result for flat diff with json formatter.
    """
    with open('tests/fixtures/results/flat_json.json') as result_file:
        estimated_result_flat_json = json.load(result_file)
    return estimated_result_flat_json


@pytest.fixture
def get_nested_result_json():
    """Get fixture of estimated diff for testing nested files with json formatter.

    Returns:
        Estimated result for nested diff with json formatter.
    """
    with open('tests/fixtures/results/nested_json.json') as result_file:
        estimated_result_nested_json = json.load(result_file)
    return estimated_result_nested_json

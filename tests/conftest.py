"""This is a module with fixtures for testing."""
import pytest


@pytest.fixture
def get_flat_result():
    """Get a fixture of estimated result for testing flat files.

    Returns:
        Estimated result for flat diff.
    """
    with open('tests/fixtures/estimated_results/flat.txt') as result_file:
        estimated_result_flat = result_file.read()
    return estimated_result_flat

"""This is a module to test gendiff program for erroe raising."""
import pytest
from gendiff.gendiff_engine import generate_diff


def test_generate_diff_wrong_formats():
    """Do not allow to parse unmatching formats."""
    with pytest.raises(ValueError):
        generate_diff(
            'tests/fixtures/test_files/flat_test_file1.yml',
            'tests/fixtures/test_files/flat_test_file2.json',
        )

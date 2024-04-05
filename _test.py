# test_comparator.py
import pytest
from MKR import compare_files
import filecmp
import os


@pytest.fixture(scope="module")
def create_test_files():
    with open('test_file1.txt', 'w') as f:
        f.write('Line1\nLine2\nLine3\n')
    with open('test_file2.txt', 'w') as f:
        f.write('Line2\nLine3\nLine4\n')
    yield
    os.remove('test_file1.txt')
    os.remove('test_file2.txt')
    os.remove('same.txt')
    os.remove('diff.txt')


def test_compare_files(create_test_files):
    compare_files('test_file1.txt', 'test_file2.txt')

    assert filecmp.cmp('same.txt', os.path.join('expected_outputs', 'expected_same.txt'))
    assert filecmp.cmp('diff.txt', os.path.join('expected_outputs', 'expected_diff.txt'))

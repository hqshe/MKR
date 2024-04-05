import pytest
from MKR import compare_files


@pytest.fixture
def test_files():
    """Створює тестові файли перед кожним тестом і видаляє їх після."""
    test_file1_path = 'file1.txt'
    test_file2_path = 'file2.txt'
    with open(test_file1_path, 'w') as f1, open(test_file2_path, 'w') as f2:
        f1.write('Line1\nLine2\nLine3\n')
        f2.write('Line2\nLine3\nLine4\n')
    yield test_file1_path, test_file2_path


def test_compare_files(test_files):
    """Тестує функцію порівняння файлів."""
    test_file1_path, test_file2_path = test_files
    compare_files(test_file1_path, test_file2_path)

    with open('same.txt', 'r') as same, open('diff.txt', 'r') as diff:
        same_content = same.read()
        diff_content = diff.read()



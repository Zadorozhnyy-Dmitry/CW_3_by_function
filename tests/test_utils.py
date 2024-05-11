from settings import TEST_OPERATIONS_PART
from src.utils import read_file_data


def test_read_file_data():
    assert read_file_data(TEST_OPERATIONS_PART) == [{"id": 1}, {"id": 2}]

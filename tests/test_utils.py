from settings import TEST_OPERATIONS_PART
from src.utils import read_file_data, executed_operations_only


def test_read_file_data():
    assert read_file_data(TEST_OPERATIONS_PART) == [{"id": 1}, {"id": 2}]


def test_executed_operations_only():
    my_list = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "EXECUTED"},
        {},
        {"id": 3, "state": "dsf"}
    ]
    assert executed_operations_only(my_list) == [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "EXECUTED"},
    ]

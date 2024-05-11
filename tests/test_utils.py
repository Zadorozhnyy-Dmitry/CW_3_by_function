from settings import TEST_OPERATIONS_PART
from src.utils import read_file_data, executed_operations_only, translate_date_format


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


def test_translate_date_format():
    assert translate_date_format("2019-08-26T10:50:58.294041") == '26.08.2019'
    assert translate_date_format("2018-06-30T02:08:58.425572") == '30.06.2018'

from settings import TEST_OPERATIONS_PART
from src.utils import read_file_data, executed_operations_only, translate_date_format, sort_operations_by_date, \
    disguise_number, output_data


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


def test_sort_operations_by_date():
    test_list = [
        {'date': '2018-09-12T21:27:25.241689'},
        {'date': '2019-07-03T18:35:29.512364'},
        {'date': '2018-03-23T10:45:06.972075'},
        {'date': '2018-06-30T02:08:58.425572'},
        {'date': '2019-08-26T10:50:58.294041'},
    ]
    expected_list = [
        {'date': '2019-08-26T10:50:58.294041'},
        {'date': '2019-07-03T18:35:29.512364'},
        {'date': '2018-09-12T21:27:25.241689'},
        {'date': '2018-06-30T02:08:58.425572'},
        {'date': '2018-03-23T10:45:06.972075'},
    ]
    assert sort_operations_by_date(test_list) == expected_list


def test_disguise_number():
    assert disguise_number("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"
    assert disguise_number("Счет 14211924144426031657") == "Счет **1657"
    assert disguise_number("Maestro 3928549031574026") == "Maestro 3928 54** **** 4026"
    assert disguise_number('') == ''


def test_output_data():
    test_dict1 = {
        "id": 596171168,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {
            "amount": "79931.03",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 72082042523231456215"
    }
    expected_output1 = '''\n11.07.2018 Открытие вклада\n -> Счет **6215\n79931.03 руб.\n'''
    test_dict2 = {
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {
            "amount": "40701.91",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72731966109147704472"
    }
    expected_output2 = """\n04.04.2018 Перевод организации\nVisa Gold 5999 41** **** 6353 -> Счет **4472\n40701.91 USD\n"""
    assert output_data(test_dict1) == expected_output1
    assert output_data(test_dict2) == expected_output2

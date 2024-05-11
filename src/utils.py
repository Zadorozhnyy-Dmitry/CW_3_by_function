import datetime
from json import loads
from pathlib import Path


def read_file_data(path: Path) -> list[dict]:
    """
    Читает файл operations.json и выводит список со словарями
    :param path: путь к файлу operations.json
    :return: список со словарями
    """
    with open(path, 'r', encoding='utf-8') as file:
        return loads(file.read())


def executed_operations_only(list_operations: list[dict]) -> list[dict]:
    """
    Функция определяет новый список со словарями,
    в котором указаны только удачные операции
    :param list_operations: список со словарями из файла operations.json
    :return: список с удачными операциями
    """
    return [
        op for op in list_operations if op.get('state') == "EXECUTED"
    ]


def translate_date_format(date: str) -> str:
    """
    Преобразование времени из ISO формата в необходимый
    :param date: строка в ISO формате
    :return: строка
    """
    iso_date = datetime.datetime.fromisoformat(date)
    return iso_date.strftime('%d.%m.%Y')


def sort_operations_by_date(list_operations: list[dict]) -> list[dict]:
    """
    Функция сортирует список операций по дате начиная с последней
    :param list_operations: список словарей с операциями
    :return: отсортированный список словарей с операциями
    """
    return sorted(list_operations, key=lambda date: date['date'], reverse=True)


def disguise_number(number: str) -> str:
    """
    Функция скрытия номеров счета или карты
    :param number: строка с номером
    :return: скрытая строка
    """
    if number[:4] == 'Счет':
        return f'Счет **{number[-4:]}'
    elif number == '':
        return ''
    else:
        return f'{number[:-12]} {number[-12:-10]}** **** {number[-4:]}'

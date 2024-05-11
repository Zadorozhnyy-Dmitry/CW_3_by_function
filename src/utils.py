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

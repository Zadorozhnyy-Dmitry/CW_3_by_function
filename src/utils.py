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

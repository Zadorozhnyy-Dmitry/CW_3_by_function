from settings import OPERATIONS_DATA_PATH, NUMBER_OPERATIONS
from src.utils import read_file_data, executed_operations_only, sort_operations_by_date, translate_date_format, \
    output_data


def main():
    """
    Виджет, который показывает несколько последних успешных банковских операций клиента
    :return: None
    """
    # создаю список словарей с операциями
    list_operations: list[dict] = read_file_data(OPERATIONS_DATA_PATH)
    # создаю список словарей с успешными операциями
    executed_operations: list[dict] = executed_operations_only(list_operations)
    # создаю список сс словарями отсортированный по дате
    sort_list_operations = sort_operations_by_date(executed_operations)
    # вывожу последние операции
    for op in sort_list_operations[:NUMBER_OPERATIONS]:
        print(output_data(op), end='')


if __name__ == '__main__':
    main()

import json


def read_json(file_path):
    """
    Читает файл json и возвращает его содержимое
    :return: Данные в виде списка словарей
    """
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)

    return data


def sort_data(data):
    """
    сортирует данные по статусу операции
    :param data: исходные даннеы для сортировки
    :return: Отсортированные данные
    """
    pass


def bluring_cnumber(card_number):
    """
    Заменяет нужные цифры у номера карты на *
    :param card_number: Исходный номер карты
    :return: Маскированную строку
    """
    pass


def bluring_anumber(amount_number):
    """
    Заменяет нужные цифры у номера счета на *
    :param amount_number: Исходный номер счета
    :return: Маскированную строку
    """
    pass
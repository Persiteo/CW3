import datetime
import json


def read_json(file_path) -> list:
    """
    Читает файл json и возвращает его содержимое
    :param Абсолютный путь к файлу json
    :return: Данные в виде списка словарей
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        py_data = json.load(f)

    return py_data


def sort_data(array):
    """
    сортирует данные по дате и фильтрует по статусу операции EXECUTED
    :param array: исходные данныe для сортировки
    :return: Отсортированные данные
    """
    clean_data = []
    sorted_data = []

    for item in array:
        if "date" and "state" in item.keys():
            clean_data.append(item)
    clean_data.sort(key=lambda x: x["date"], reverse=True)

    for item in clean_data:
        if item["state"] == "EXECUTED":
            sorted_data.append(item)

    return sorted_data


def modified_date(array: dict):
    """
    Преобразует формат вывода даты операции
    :param array: Массив данных, cодержащий дату операции
    :return: Исправленный формат даты операции
    """
    return datetime.datetime.strptime(array['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")




def bluring_anumber(array: dict):
    """
    Заменяет нужные цифры номера карты на *
    :param array: Массив данных, cодержащий исходные номера карты
    :return: Маскированные строки
    """
    if 'to' in array.keys():
        blur_to = '**' + array['to'][-4::]
    else:
        blur_to = 'n/a'
    return blur_to


def bluring_cnumber(array: dict):
    """
    Заменяет нужные цифры номера cчёта на *
    :param array: Массив данных, cодержащий исходные номера счета
    :return: Маскированные строки
    """
    if 'from' in array.keys():
        if 'Счет' in array['from']:
            blur_from = f"{array['from'][:-16]}{'*' * 12}{array['from'][-4::]}"
        else:
            blur_from = f"{array['from'][:-12]} {array['from'][-12:-10]}** **** {array['from'][-4::]}"
    else:
        blur_from = 'n/a'
    return blur_from


def get_formated_info(array: dict) -> str:
    """
    Формируют по шаблону отчёт по операции
    :param array: Массив данных
    :return str: Отформатированные строки по шаблону
    """
    return f"{modified_date(array)} {array['description']} {bluring_cnumber(array)} -> {bluring_anumber(array)} {array['operationAmount']['amount']} {array['operationAmount']['currency']['name']}"


from src.utils import *


def test_read_json(path_to_test_json, expected_result_for_read_json_test):
    assert read_json(path_to_test_json) == expected_result_for_read_json_test


def test_sort_data(data_for_sort, expected_result_for_sort):
    assert sort_data(data_for_sort) == expected_result_for_sort


def test_modified_date():
    assert modified_date({"date": "2018-09-12T21:27:25.241689"}) == "12.09.2018"


def test_bluring_cnumber():
    assert bluring_cnumber({"from": "Visa Platinum 1246377376343588"}) == "Visa Platinum 1246 37** **** 3588"


def test_bluring_anumber():
    assert bluring_anumber({"to": "Счет 75651667383060284188"}) == "**4188"


def test_get_formated_info():
    pass
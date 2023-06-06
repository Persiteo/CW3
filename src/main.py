from src.utils import *
import os

sorted_list = sort_data(read_json(os.path.join(os.path.dirname(__file__), 'operations.json')))
for item in sorted_list[0:5]:
    print(get_formated_info(item))


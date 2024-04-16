#!/usr/bin/python3
"""write_file function definition module"""


import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file, using  JSON representation"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

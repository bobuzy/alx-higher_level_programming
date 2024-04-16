#!/usr/bin/python3
"""load_from_json_file function definition module"""

import json


def load_from_json_file(filename):
    """Create an Object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

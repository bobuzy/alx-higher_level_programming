#!/usr/bin/python3
"""write_file function definition module"""


def write_file(filename="", text=""):
    """Read file and print contents to standard output"""
    with open(filename, mode="w", encoding="utf-8") as file:
        length = file.write(text)
        return length

#!/usr/bin/python3
"""read_file function definition module"""


def read_file(filename=""):
    """Read file and print contents to standard output"""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")

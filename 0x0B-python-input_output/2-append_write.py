#!/usr/bin/python3
"""append_file function definition module"""


def append_write(filename="", text=""):
    """Append a string at the end of a file and
    return the number of characters added"""
    with open(filename, mode="a", encoding="utf-8") as file:
        length = file.write(text)
        return length

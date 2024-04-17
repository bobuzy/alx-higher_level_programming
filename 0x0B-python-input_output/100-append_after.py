#!/usr/bin/python3
"""append_after function definition module"""


def append_after(filename="", search_string="", new_string=""):
    """function definition
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

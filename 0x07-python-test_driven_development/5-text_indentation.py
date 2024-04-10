#!/usr/bin/python3
"""module for text_indentation"""


def text_indentation(text):

    """prints a text with 2 new lines after char: ., ? and :

    Args:
        text: String to be modified

    Raises:
        TypeError: if text is not string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    ind = 0

    while ind < len(text):
        if text[ind] in ".?:":
            print(text[ind] + "\n")
            if ind + 1 < len(text) and text[ind + 1] == " ":
                ind += 2
            else:
                ind += 1
        else:
            print(text[ind], end="")
            ind += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

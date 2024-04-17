#!/usr/bin/python3
"""pascal_traigle function definition module."""


def pascal_triangle(n):
    """ pascal traigle class body.
    """
    if n <= 0:
        return []

    pascal_list = [[1]]
    while len(pascal_list) != n:
        tri = pascal_list[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        pascal_list.append(tmp)
    return pascal_list

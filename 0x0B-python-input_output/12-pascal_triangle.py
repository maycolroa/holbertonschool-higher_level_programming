#!/usr/bin/python3
"""pascal"""


def pascal_triangle(n):
    """ Prints triangle """
    if n <= 0:
        return []
    triangle = []
    row = []
    for j in range(n):
        row = [1]
        if j > 0:
            for j in range(j):
                row.append(sum(triangle[-1][j:j+2]))
        triangle.append(row)
    return triangle

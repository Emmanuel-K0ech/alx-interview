#!/usr/bin/python3
"""
Pascal's Triangle Implementation
"""


def pascal_triangle(n):
    """ Function Definition of How the Algorithm works """
    result = []
    if n > 0:
        for i in range(1, n + 1):
            row = []
            c = 1
            for j in range(1, i + 1):
                row.append(c)
                c = c * (i - j) // j
            result.append(row)
    return result

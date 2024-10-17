#!/usr/bin/python3
""" Module 0-minoperations.py"""
import math
from typing import List


def minOperations(n: int) -> int:
    """
    This function returns the minimum number of operations needed
    to achieve [n H] e.g
    n = 9
    9 H = [ HHHHHHHHH ]
    Args:
        n (int): number of H to be achieved
    Return:
        int: minimum number of operations needed
    """
    # Deal with even factors if n an even number
    sum: int = 0
    while n % 2 == 0:
        sum += 2
        n = n // 2

    # After the above step the remainder is odd so you divide the number
    # with the possible factors which range from 3 to [sqrt(n) + 1 ]
    # with an interval of 2 since we are testing with odd numbers
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        sum += i
        n = n // i

    # The remeinder of the above will either be 1 or a prime number
    # So you print the remainder if its greater than 2
    if n > 2:
        sum += n

    return sum

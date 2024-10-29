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

    Function Logic
    - Deal with even factors if n an even number
    - After the above step the remainder is odd so you divide the number
    - with the possible factors which range from 3 to [sqrt(n) + 1 ]
    - with an interval of 2 since we are testing with odd numbers
    - The remeinder of the above will either be 1 or a prime number
    - So you print the remainder if its greater than 2

    Args:
        n (int): number of H to be achieved
    Return:
        int: minimum number of operations needed
    """
    if (n < 2):
        return 0
    opr, root = 0, 2
    while root <= n:
        if n % root == 0:
            opr += root
            n = n / root
            root -= 1
        root += 1
    return opr

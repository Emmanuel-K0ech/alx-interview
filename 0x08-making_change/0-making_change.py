#!/usr/bin/python3
""" 0-making_change.py Module"""


def makeChange(coins, total):
    """Finds the least amount of change possible from the coins given"""
    ans = 0

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    for denom in coins:
        count = total // denom
        ans += count
        total -= count * denom

        if total == 0:
            return ans

    return -1

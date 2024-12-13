#!/usr/bin/python3
"""Prime_game.py module"""


def sieve_of_eratosthenes(n):
    """
    Generates a list where prime indices are marked with 1 (True)
    and non-prime indices are marked with 0 (False).
    """
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, n + 1, i):
                primes[multiple] = 0
    return primes


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game
    Args:
        x (int): Number of rounds
        nums (list of int): List of numbers for the rounds
    Returns:
        str: Name of the winner ("Maria" or "Ben") or None
    """
    if not nums or x <= 0 or len(nums) != x:
        return None

    maria_score = 0
    ben_score = 0

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    for num in nums:
        prime_count = sum(primes[:num + 1])
        if prime_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None

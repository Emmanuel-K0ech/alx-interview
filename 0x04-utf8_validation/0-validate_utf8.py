#!/usr/bin/python3
""" Module 0-validate_utf8.py"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Returns True if a given valid UTF-8 encoding otherwise False"""
    bit_count = 0

    for byte in data:
        if not 0 <= byte <= 255:
            return False

        if bit_count == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                bit_count = 1
            elif byte >> 4 == 0b1110:
                bit_count = 2
            elif byte >> 3 == 0b11110:
                bit_count = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                bit_count -= 1
            else:
                return False

    return bit_count == 0

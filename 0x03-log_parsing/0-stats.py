#!/usr/bin/python3

import sys


def msg_print(sc_dict, file_size):
    """
    Messege printing method
    Args:
        sc_dict: dict of status codes
        file_size: total of the file
    """

    print("File size: {}".format(file_size))
    for key, val in sorted(sc_dict.items()):
        if val != 0:
            print("{}: {}".format(key, val))


file_size = 0
code = 0
counter = 0
sc_dict = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in sc_dict.keys()):
                    sc_dict[code] += 1

            if (counter == 10):
                msg_print(sc_dict, file_size)
                counter = 0

finally:
    msg_print(sc_dict, file_size)

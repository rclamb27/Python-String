#!/usr/bin/env python3
#
# Ryan Lamb
# CPSC 223P-03
#2020-09-10
#rclamb27@cus.fullerton.edu
""" Takes binary and returns it to a string and pring it out"""

import sys


def main():
    """Converts the argument from a binary representation to ascii then converts it to a string"""
    counter = 0
    for i in sys.argv:
        if counter != 0:
            ascii_values = int(i, 2)
            characters = chr(ascii_values)
            print(characters, end='')
        counter += 1
    print()

if __name__ == '__main__':
    main()

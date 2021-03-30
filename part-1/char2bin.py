#!/usr/bin/env python3
#
# Ryan Lamb
# CPSC 223P-03
#2020-09-08
#rclamb27@cus.fullerton.edu
""" Takes a string in the command line and converts it to binary"""

import sys
def conv_to_binary(number):
    """converts to binary and removes the 0b within and adds zeroes if there are not 8 digits in the binary"""
    answer = bin(number)[2:]
    if len(answer) != 8:
        answer = (8 - len(answer)) * '0' + answer
    return answer


def main():
    """Converts the argument into a character then an ascii value then binary"""
    counter = 1
    for i in sys.argv[1]:
        character = i
        value = ord(character)
        digits = conv_to_binary(value)
        if counter%7 != 0:
            print(digits, end=" ")
        else:
            print(digits)
        counter += 1
    print()

if __name__ == '__main__':
    main()

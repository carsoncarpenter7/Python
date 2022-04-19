#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-09-010
# carson.carpenter7@csu.fullerton.edu
#
"""
This is my program for converting and printing the string
representing the ASCII values of its binary representation
Character is inputed through the terminal
"""
import sys


def convert_from_binary():
    """ Converts binary to ASCII"""
    if len(sys.argv) > 1:
        character = sys.argv[1]
        for character in sys.argv[1:]:
            print(chr(int(character, 2)), end='')
        print()


if __name__ == '__main__':
    convert_from_binary()

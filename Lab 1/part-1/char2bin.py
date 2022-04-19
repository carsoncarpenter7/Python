#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-09-010
# carson.carpenter7@csu.fullerton.edu
#
"""
This is my program for converting and printing the string
to a binary representation of their ASCII values.
String is inputed through the terminal
"""
import sys


def convert_to_binary():
    """ Converts strings to binary numbers"""
    if len(sys.argv) > 1:
        # convert each char to
        # ASCII value
        character = sys.argv[1]
        # Convert ASCII value to binary
        size = len(character)
        range(size)
        for i in range(size):
            char = character[i]
            binary = str(bin(ord(char)))[2:]
            binary = ((8 - len(binary)) * '0') + binary
            print(binary, end=' ')
            if (i + 1) % 7 == 0:
                print()
        print()


if __name__ == '__main__':
    convert_to_binary()

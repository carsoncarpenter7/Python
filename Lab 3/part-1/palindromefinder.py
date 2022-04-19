#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-09-22
# carson.carpenter7@csu.fullerton.edu
#
"""
Find all the palindromes in a given file
"""

import sys


def is_palindrome(text):
    "Checks if text from file in reverse order is the same as original"
    return len(text) > 1 and text == text[::-1]


def main():
    """ This program reads the strings from the file
    and outputs the palindromes into a new file """
    if len(sys.argv) < 2:
        print('Not enough arguments. Please provide a file')
        sys.exit()
    file_name = sys.argv[1]
    outfile_name = sys.argv[2]
    with open(file_name, 'r') as file_handle:
        with open(outfile_name, 'w') as output_file_handle:
            for line in file_handle:
                line = line.strip()
                if is_palindrome(line.lower()):
                    output_file_handle.write(line.lower() + "\n")


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-09-15
# carson.carpenter7@csu.fullerton.edu
#
"""
This is my program for computing the sum of all the
multiples of 3 or 5 below 1000000
"""


def main():
    """ This Program seperates multiples of 3 and 5
    in 1000000 and gets the sum"""
    multiple = 0
    for i in range(1, 1000000):
        if not i % 5 or not i % 3:
            multiple = multiple + i

    print('The sum of all the multiples of 3 or 5 '
          'below 1000000 is {}'.format(multiple))


if __name__ == '__main__':
    main()

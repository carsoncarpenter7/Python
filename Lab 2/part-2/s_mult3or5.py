#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-09-15
# carson.carpenter7@csu.fullerton.edu
#
"""
This is my program for computing the sum of all the
multiples of 3 or 5 below 1000000 using set
"""


def main():
    """ This Program seperates multiples of 3 and 5
    in 1000000 using set() and range() and gets the sum"""
    three = set(range(0, 1000000, 3))
    five = set(range(0, 1000000, 5))
    multiples = three | five
    print(sum(multiples))


if __name__ == '__main__':
    main()

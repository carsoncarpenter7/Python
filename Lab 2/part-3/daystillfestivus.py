#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-09-17
# carson.carpenter7@csu.fullerton.edu
#
"""
This is my program that prints out the number of days from today
until the given Festivus. (Festivus is celebrated on December 23.)
"""

import sys
from datetime import datetime


def main():
    """ This program prints out the number of days from today
    until the given Festivus"""


CURRENT_DAY = datetime.now().day
CURRENT_MONTH = datetime.now().month
CURRENT_YEAR = datetime.now().year

YEAR = int(sys.argv[1])

# Days until festival
if YEAR >= CURRENT_YEAR:
    DAYSINMONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# If Festivus is Today
    if CURRENT_DAY == 23 and CURRENT_MONTH == 12 and YEAR == CURRENT_YEAR:
        print("Today is Festivus!")
# If Festivus is in the future
    else:
        USER_YEAR = CURRENT_YEAR + 1
        TOTAL_DAYS = 0
# years
        while USER_YEAR <= YEAR:
            TOTAL_DAYS += 365
            USER_YEAR += 1
        USER_MONTH = CURRENT_MONTH
# months convert to days
        while USER_MONTH < 11:
            TOTAL_DAYS += DAYSINMONTH[USER_MONTH]
            USER_MONTH += 1
        TOTAL_DAYS += (22 + DAYSINMONTH[CURRENT_MONTH-1] - CURRENT_DAY)
    print("There are", TOTAL_DAYS, "days untill Festivus", YEAR)
# Date has passed
elif YEAR < CURRENT_YEAR:
    print("Festivus", YEAR, "has passed.")


if __name__ == '__main__':
    main()

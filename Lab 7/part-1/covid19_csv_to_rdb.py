#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-11-10
# carson.carpenter7@csu.fullerton.edu
#
# Countyname (string)
# Statename (string)
# Date  (string or date object from SQL Alchemy)
# Confirmed (COVID-19 cases) (Integer)
# Deaths (Integer)
# Population (Integer)

""" This Program builds a relational database for
Covid Cases data in Orange County"""

# view database
# file covid_oc.sql3
# sqlite3 covid_oc.sql3
# select * from covid_cases;

import csv
import sys
from datetime import date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from CovidCase import *


def main():
    """ Create a ralational database using data from a CSV file in SQlite """
    if len(sys.argv) < 3:
        print("Error, please input file names again")
        sys.exit(1)
    engine = create_engine('sqlite:///' + sys.argv[2])
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    this_session = Session()

    with open(sys.argv[1], 'r') as file:
        reader = csv.reader(file)
        for i in reader:
            year, month, day = map(int, i[2].split('-'))
            data = CovidCase(i[0], i[1], date(year, month, day), int(i[3]),
                             int(i[4]), int(i[5]))
            this_session.add(data)
    this_session.commit()
    this_session.close()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-11-13
# carson.carpenter7@csu.fullerton.edu
#
""" Program to plot Covid cases and deaths per 10000 residents
from a relational database """

import sys
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import asc
import matplotlib.pyplot as plt
import numpy as np
from CovidCase import *


def main():
    """ Organize columns from the database and plot the data """
    size = 10000
    population_per_10k = 3175692 / float(size)

    engine = create_engine('sqlite:///covid_oc.sql3')
    session = sessionmaker(bind=engine)
    this_session = session()

    list_of_cases = [record.covid_cases for record in this_session
                     .query(CovidCase.covid_cases)
                     .order_by(asc(CovidCase.date))]
    # print (this_session.execute(confirmed_cases).fetchall())
    list_of_deaths = [record.deaths for record in this_session
                      .query(CovidCase.deaths)
                      .order_by(asc(CovidCase.date))]
    # print (this_session.execute(confirmed_deaths).fetchall())
    date_list = [record.date for record in this_session.query(CovidCase.date)]

    for i in list_of_cases:
        cases_per_10k = np.array([i // float(population_per_10k)
                                  for i in list_of_cases])
    for i in list_of_deaths:
        deaths_per_10k = np.array([i // float(population_per_10k)
                                   for i in list_of_deaths])
    print(cases_per_10k)
    print(deaths_per_10k)


    plt.plot(date_list, cases_per_10k, label='Covid Cases')
    plt.plot(date_list, deaths_per_10k, 'r', label='Covid Deaths')

    plt.xlabel('Date')
    plt.ylabel('Number of Covid Cases and Deaths Per 10,000 residents')
    plt.title("Monthly Covid Data for Orange County")
    plt.legend()

    plt.savefig(sys.argv[2])
    plt.show()
    plt.close()


if __name__ == "__main__":
    main()

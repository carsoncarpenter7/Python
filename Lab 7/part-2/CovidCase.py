#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-11-10
# carson.carpenter7@csu.fullerton.edu
#

#Define class
# For every row make an instance and write from database

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

""" This Program stores the six data fields found in each row of the CSV file """
Base = declarative_base()

class CovidCase(Base):
    """ Class to seperate data from file into tables """
    __tablename__ = 'covid_cases'
    id = Column(Integer, primary_key=True)
    county = Column(String)
    state = Column(String)
    date = Column(Date)
    covid_cases = Column(Integer)
    deaths = Column(Integer)
    population = Column(Integer)
    def __init__(self, county, state, date, covid_cases, deaths, population):
        self.county = county
        self.state = state
        self.date = date
        self.covid_cases = covid_cases
        self.deaths = deaths
        self.population = population
    def __repr__(self):
        return 'CovidCase({}, {}, {}, {}, {}, {})'.format(repr(self.county), repr(self.state),
                                                          repr(self.date), repr(self.covid_cases),
                                                          repr(self.deaths), repr(self.population))

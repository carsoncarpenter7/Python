#!/usr/bin/env python3

# 6 plots total 2000 - 2020 in big_mac_index_evaluation.pdf

# Next create a series of plots that describes how many hours a worker must work to purchase 4 Big Macs in the year 2017 using the minimum wage data and the Big Mac Index  data.
#To accomplish this, you must calculate some values before plotting. using mimum_wage.csv into hours)worked_to_feed_a_family.pdf


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
from time import sleep
import pandas as pd

# date - The date (year-month-day) that the data was collected
# local_price - The price of a Big Mac in that country in local currency.
# dollar_ex - The exchange rate, how much US$1 will buy of local currency
# dollar_price - The price of a Big Mac in that country in US dollars (local_price / dollar_ex)
# dollar_ppp - The implied purchasing power parity or in other words the implied exchange rate between the two currencies local_price / us_price
# dollar_valuation - The percent the local currency is over (+) or under (-) valued according when compared to a currency market exchange rate ((dollar_price / us_price ) / us_price) * 100 or ((dollar_ppp - dollar_ex) / dollar_ex) * 100
# dollar_adj_valuation - The percent the local currency is over (+) or under (-) valued adjusted for GDP per person (dollar_valuation + gdp_adjustement); gdp_adjustment is not given but can be derived from dollar_valuation and dollar_adj_valuation, gdp_adjustment = dollar_valuation - dollar_adj_valuation
# euro_adj_valuation - ignore this column
# sterling_adj_valuation - ignore this column
# yen_adj_valuation - ignore this column
# yuan_adj_valuation - ignore this column

def dollar_valuation():
    china_adj_valuation = []

    china = pd.read_csv('ECONOMIST-BIGMAC_CHN.csv')
    for i in china


    plt.xlabel('Dates')
    plt.ylabel('Floating Point Values')
    plt.title("Big Mac Index")
    #plt.legend()

    print('Writing plot to big_mac_index_plot.pdf')
    plt.savefig("big_mac_index_plot.pdf")
    plt.show()

    plt.close()


def main():
    """ Calling function to create graph """
    dollar_valuation()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-10-27
# carson.carpenter7@csu.fullerton.edu
#
"""Function to plot Misery Index, Unemployment Rate, and Inflation Rate """

import json
from datetime import datetime
import matplotlib.pyplot as plt


def misery_index():
    """Function to get data from .json file and plot Misery Index """
    date_list = []
    unemployment_list = []
    infaltiom_list = []
    misery_list = []

    file = 'USMISERY-INDEX.json'
    with open(file, 'r') as file_handle:
        dictionary = json.load(file_handle)
        # print(type(d))

        for i in dictionary['dataset_data']['data']:
            dates = i[0]
            unemployment = i[1]
            inflation = i[2]
            misery = i[3]
            date_list.append(dates)
            unemployment_list.append(unemployment)
            infaltiom_list.append(inflation)
            misery_list.append(misery)

        date_list = [datetime.strptime(d, "%Y-%m-%d") for d in date_list]

        plt.plot(date_list, misery_list, label='Misery Index')
        plt.plot(date_list, infaltiom_list, label='Inflation Rate')
        plt.plot(date_list, unemployment_list, label='Unemployment Rate')

        plt.xlabel('Dates')
        plt.ylabel('Floating Point Values')
        plt.title("US Misery Index Plot")
        plt.legend()

        print('Writing plot to us_misery_plot.pdf')
        plt.savefig("us_misery_plot.pdf")
        plt.show()

        plt.close()


def main():
    """ Calling function to create graph """
    misery_index()


if __name__ == "__main__":
    main()

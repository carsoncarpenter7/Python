# CPSC 223p
##  CSV File to Relational Database

Write a program named `covid19_csv_to_rdb.py` which takes two arguments. The first argument is an input CSV data file and the second argument is the output relational database file. The program reads in the input CSV data file and and coverts it to a relational database using Python's [CSV reader](https://docs.python.org/3/library/csv.html) and [SQLAlchemy](https://www.sqlalchemy.org/). The file is a CSV file of the COVID-19 data as reported by the [John Hopkins Coronavirus Resource Center](https://coronavirus.jhu.edu/) that has been edited to only include data for Orange County, California. The full data set can be found online at [https://github.com/govex/COVID-19](https://github.com/govex/COVID-19).

Using SQLAlchemy means that you will need to define a class that uses the same types as SQLAlchemy and inherits from SQLAlchemy's class hierarchy. Use the SQLAlchemy [reference library](https://www.sqlalchemy.org/library.html#reference) and [tutorials](https://www.sqlalchemy.org/library.html#tutorials) to help you get started with SQLAlchemy.

The data in the file, `simplified_orange_county.csv`, has six columns. The column names are given in `header.txt`. They are:

1. Countyname
1. Statename
1. Date
1. Confirmed (COVID-19 cases)
1. Deaths
1. Population

Remember that all the data in a CSV file is plain text and you will need to transform this data to match the types that you select for your class.

You will need to define one class that will map to rows in a relational database table. The class must be named `CovidCase` and store the six data fields found in each row of the CSV file. Defining `CovidCase` in a file on it's own, `CovidCase.py`, is recommended so that this class can be reused in part-2 of the exercise.

You will need to create a virtual environment for this project. Ensure that you capture whatever requirements your project needs in a `requirement.txt` file. You will need to use SQLAlchemy at a minimum. 

## Example Output
```
$ ./python covid19_csv_to_rdb.py  simplified_orange_county.csv covid_oc.sql3
$
```



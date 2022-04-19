# CPSC 223p
##  Plotting From a Relational Database

Write a program named `covid_case_load.py` which takes two arguments. The first argument is an input relational database file that you created in part-1 and the second argument is the output image file for the plot your program generates. In this exercise, you'll be using Matplotlib in conjunction with SQLAlchemy and your Object Relational Model to make a plot.

Using your database and class definition from part-1, to create and output the plot as a line plot. In a unique color, plot a line which represents the number of confirmed COVID-19 cases per 10,000 residents. In a unique color, plot a line which represents the number of deaths per 10,000 residents.

Clearly label the horizontal and vertical axis to make it easy to understand what is plotted. Provide a legend to clarify what each plot means.

You will need to create a virtual environment for this project. Ensure that you capture whatever requirements your project needs in a `requirement.txt` file. You will need to use SQLAlchemy at a minimum. 

## Example Output
```
$ ./python covid_case_load.py covid_oc.sql3 covid_oc_plot.pdf
$
```



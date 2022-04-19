# CPSC 223p
##  Days till Festivus!


Write a program named `daystillfestivus.py` which prints out the number of days from today until the given [Festivus](https://en.wikipedia.org/wiki/Festivus). ([Festivus](https://www.youtube.com/watch?v=HX55AzGku5Y) is celebrated on December 23.)

For example, if the input is 2020 and today's date is September 13, 2020, then the program will report that there are 100 days until Festivus.

The program that you submit must handle the following conditions:
* If today is Festivus it shall print 'Today is Festivus!'
* If the Festivus queried is in the past, then the program shall print 'Festivus XXXX has passed.' where XXXX is the year queried
* If the Festivus queried is in the future, then the program shall print 
'There are YY days until Festivus XXXX!' where YY are the number of days until Festivus and XXXX is the year queried

Please consider using the relevant Python Standard Library modules such as `sys`, `date`, and `timedelta` to complete this exercise.

## Example Output
'''
$ ./daystillfestivus.py
Please provide a year as an argument.
$ ./daystillfestivus.py 2019
Festivus 2019 has passed.
$ ./daystillfestivus.py 2020
There are 100 days until Festivus 2020!
$ ./daystillfestivus.py 2021
There are 465 days until Festivus 2021!
'''

Note that when no arguements are given the program fails gracefully.
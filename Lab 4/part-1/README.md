# CPSC 223p
##  Word Histogram

Write a program named `wordhistogram.py` which takes one file as an argument. The file is an plain text file which shall be analyzed by the program. Upon completing the analysis, the program shall output a report detailing the shortest word(s), the longest word(s), the most frequently used word(s), and a histogram of all the words used in the input file.

If there is a tie, then all words that are of the same length for that classification (longest, shortest, most frequent) are displayed as part of that class.

A word [histogram](https://en.wikipedia.org/wiki/Histogram) shows an approximate representation of the distribution of words used in the input file. An example text, `The_Jungle_Upton_Sinclair.txt`, is provided as a starting point for analyzing natural language. Draw your histogram by listing the word first and then print up to 65 `*` characters to represent the frequency of the word.

Since there is limited space on a terminal, ensure that your histogram does not wrap along the right edge of the terminal. Assume that the width of the histogram can not be wider than 65 characters. In calculating your histogram, map the highest frequency to 65 characters. For example, if the text has a word that appears 2000 times and it is the most frequently used word, then divide 2000 by 65 to approximate that each `*` character represents 30 occurrences of the word in question in the text. Thus if a word should appear less than 30 times, it receives zero `*` characters, a word that appeared 125 time would receive 4 `*` characters (0-30, 31-60, 61-90, 91-120, 120-150).

Print the order of the histogram from most frequent to least frequent.

The program must have a class named WordHistogram. This class must be the data structure that keeps track of the words that appear in the input text file and can return the histogram as a single string. The main function is responsible for opening and reading the the input text file.

Make sure your WordHistogram class has data members that are correctly named (use the underscore character!), has an initializer, and any necessary methods and data members.

In your main, use the given function to read from the filehandle.
```
def word_iterator(file_handle):
""" This iterates through all the words of a given file handle. """
  for line in file_handle:
    for word in line.split():
      yield word
```


If the histogram is computed or stored outside of an object named WordHistogram your submission will not receive credit. 


## Example Output
```
$ ./wordhistogram.py Candide_Voltaire.txt
Word Histogram Report
the (2179) ******************************************************************
of (1233) *************************************
to (1130) **********************************
and (1127) **********************************
a (863) **************************
in (623) ******************
i (446) *************
was (434) *************
that (414) ************
he (410) ************
with (395) ***********
is (348) **********
his (333) **********
you (317) *********
said (302) *********
not (276) ********
...
$
```


# CPSC 223p
##  Find all the palindromes in a file


Write a program named `palindromefinder.py` which takes two files as arguments. The first file is the input file which contains one word per line and the second file is the output file. The output file is created by finding and outputting all the palindromes in the input file.

A [palindrome](https://en.wikipedia.org/wiki/Palindrome) is a sequence of characters which reads the same backwards and forwards. For example, the word 'racecar' is a palindrome because if you read it from left to right or right to left the word is the same. Let us further limit our definition of a palindrome to a sequence of characters greater than length 1.

A sample input file is provided named `words_shuffled`. The file contains 235,885 words. You may want to create smaller sample input files before attempting to tackle the 235,885 word sample file.

Your program should not take longer than 5 seconds to calculate the output.


## Example Output
```
$ ./palindromefinder.py a_list_of_words palindromes_found
$
```

Let's imagine that the file `a_list_of_words` contained
```
racecar
A
lemon
```

Then after the program completes, the contents of the file `palindromes_found` shall be
```
racecar
```

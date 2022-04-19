#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-10-04
# carson.carpenter7@csu.fullerton.edu
#
"""
This is my program that outputs a report of amount of
words repeated in a file into a histogram."""
import sys
import math


def word_iterator(file_handle):
    """ This iterates through all the words of a given file handle. """
    for line in file_handle:
        for word in line.split():
            yield word


class WordHistogram:
    def __init__(self):
        """ Default """
        self.dictionary = {}

    def insert(self, word):
        """ Insert word to dictionary and remove punctuation """
        word = word.lower()
        for i in [',', '.', ':', ';', '\'', '!', '?', '(', ')', '\'']:
            word = word.replace(i, '')
        if word in self.dictionary:
            self.dictionary[word] = self.dictionary[word] + 1
        else:
            self.dictionary[word] = 1

    def report(self):
        """ Convert number to * (* = 30) """
        self.dictionary = sorted(self.dictionary.items(), key=lambda item: item[1], reverse=True)
        stars = ''
        for item in self.dictionary:
            if item[1] >= 30:
                stars += (item[0] + ' (' + str(item[1]) + ') '
                          + math.ceil(item[1] * 65 / self.dictionary[0][1]) * '*' + '\n')
        return stars


def main():
  if len(sys.argv) < 2:
    print("Provide an input file. Exiting")
    exit(1)
  wh = WordHistogram()
  with open(sys.argv[1], "r") as fh:
    for word in word_iterator(fh):
      wh.insert(word)
  print(wh.report())


if __name__ == '__main__':
  main()

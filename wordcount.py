#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import re

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

def word_counting(filename):
  file = open(filename, 'rt', encoding = 'utf-8')
  allwords = {}
  for line in file:
    splitline = line.split(sep = ' ')
    wordposition = 0

    ## remove newline from last word
    lastword = splitline[-1]
    lastword = lastword[0:-1]
    splitline[-1] = lastword

    ## make all words lowercase
    for word in splitline:
      word = word.lower()
      splitline[wordposition] = word
      wordposition += 1
    wordposition = 0

    for word in splitline:
      ## reset booleans
      inlist = False
      isaword = False

      ## remove punctuation from the word and check if word is just punctuation/spaces
      match = re.search(r'[a-zA-Z]+\b', word)
      if match:
        word = match.group()
        isaword = True
      
      ## checks if word is already in allwords dictionary and passed isaword match, if it is adds 1 to count, if not adds word to allwords
      for key in allwords:
        if key == word and isaword == True:
          allwords[key] += 1
          inlist = True
      if inlist == False and isaword == True:
          allwords[word] = 1
  file.close()
  return allwords


def print_words(filename):
  ## retrieve wordcount dictionary from word_counting function
  allwords = word_counting(filename)

  ## print out the word count sorted alphabetically
  for key in sorted(allwords.keys()):
    print(key, allwords[key])
  return



def print_top(filename):
  ## retrieve wordcount dictionary
  allwords = word_counting(filename)

  ## create sorted list of key tuples
  orderedwords = sorted(allwords.items(), key = lambda x: x[1], reverse = True)
  
  ## print out the key/value pairs of the 20 most common words
  for kvpair in orderedwords[:19]:
    print(kvpair[0], kvpair[1])

  return



# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()

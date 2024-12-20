#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  with open(filename, "r") as file:
    file_content = file.read()
    
    ## pull out the year
    year_match = re.search(r'Popularity in (\d\d\d\d)', file_content)
    if year_match:
      year = year_match.group(1)
    
    ## build dictionary with name|rank pairs
    names_with_ranks = {}
    ## regex to pull names out of html table format
    names_match = re.findall(r'(\d+)</td><td>(\w+)</td><td>(\w+)', file_content)
    if names_match:
      for item in names_match:
        ## add male name at this rank to dictionary
        name = names_match[int(item[0])-1][1]
        if name not in names_with_ranks:
          names_with_ranks[name] = names_match[int(item[0])-1][0]
        ## add female name at this rank to dictionary
        name = names_match[int(item[0])-1][2]
        if name not in names_with_ranks:
          names_with_ranks[name] = names_match[int(item[0])-1][0]
    
    ## build list starting with year then alphabetical name:rank pairs
    name_rank_list = [year]
    alphabetical_names_with_ranks = sorted(names_with_ranks)
    for item in alphabetical_names_with_ranks:
      name_rank_list.append(f'{item} {names_with_ranks[item]}')
  return name_rank_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.

  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # generate the list of names and their ranks for the declared file
  name_rank_list = extract_names(args[0])

  # print the names and ranks to a summary file if summary is chosen, print to console otherwise
  if summary:
    with open(f'{args[0]}_summary.txt', 'wt') as file:
      for item in name_rank_list:
        file.write(f'{item}\n')
  else:
    for item in name_rank_list:
      print(item)


if __name__ == '__main__':
  main()

#! usr/bin/python3

#Program finds common typos in a text
#Prints line number in which a typo occured
#Common typos: multiple spaces between words, repeated words.

import re
from os import path
from sys import argv

spaces_regex = re.compile(r"\w  +\w")
repeat_regex = re.compile(r"\b(\w+)\s+\1\b", re.I)

filename = argv[1]
file = open(filename, 'r')
result = open('result.txt', 'w')
for num, lines in enumerate(file, 1):
    search_spaces = spaces_regex.findall(lines)
    search_repeat = repeat_regex.findall(lines)
    """
    if search_spaces:
        print(search_spaces)
    if search_repeat:
        print(search_repeat)
    search_spaces, search_repeat = 0, 0
    """
    if search_spaces:
        result.write('Line ' + str(num) + ': multiple spaces\n')
    if search_repeat:
        result.write('Line ' + str(num) + ': repeating word:\n')
        for item in search_repeat:
            result.write('\t' + item + '\n')
result.close()
file.close()


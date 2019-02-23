#program to change static parts of many file names at one time
#user define a directory with files and a part in a name to be changed
#example: change filenames "skan001", "skan002", "skan003" etc.
#                       to "obraz001", "obraz002", "obraz003" etc.

from shutil import move
from os import path, listdir 
from re import compile, search

while True:
    print("Give files' directory: ")
    directory = input()
    if path.isdir(directory):
        break
    else:
        print("Directory does not exist or is not a folder")
print("Part of the filename to be changed: ")
name_old = input()
print("New part of the filename: ")
name_new = input()
name_regex = compile(r"^(.*?)(%s)(.*?)$" % name_old)
for filename in listdir(directory):
    regex = name_regex.search(filename)
    if regex == None:
        continue
    new_filename = regex.group(1) + name_new + regex.group(3)
    new_filename_path = path.join(directory, new_filename) 
    old_filename_path = path.join(directory, filename)
    print("Renaiming %s to %s" % (filename, new_filename))
    move(old_filename_path, new_filename_path)

#! usr/bin/python3

# Program copies the clipboard and split the text by the new line character.
# Bullet point is added to each line and the text is saved to seperate file.

import pyperclip
import os

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
        lines[i] = '*\t' + lines[i]
text = '\n'.join(lines)
"""cwd = os.getcwd()
iteration = 1
while True:
    result_file = 'bulletpoint_result%s.txt' % iteration
    if os.path.isfile(os.path.join(cwd, result_file)):
        iteration = iteration + 1
    else:
        file = open('bulletpoint_result%s.txt' % iteration, 'w')
        break
        """
file = open('bulletpoint_result.txt', 'w')
file.write(text.encode("utf-8"))
file.close()

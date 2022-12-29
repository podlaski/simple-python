# The program renames files specified by the user

import glob
import os

EXTENSION = '.bak'

example = input('Enter a filename or pattern: ')
filenames = glob.glob(example)

for filename in filenames:
    if '.' in filename:
        tokens = filename.rsplit('.', maxsplit=1)
        name = tokens[0]
        extension = tokens[1]
    else:
        name = filename
        extension = ''
        
    new_filename = name + EXTENSION
    os.rename(filename, new_filename)
    print(filename, '->', new_filename)

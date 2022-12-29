# Display the first line of files

import glob

example = input('Enter a filename or pattern: ')
filenames = glob.glob(example)

for filename in filenames:
    print(filename)

access = input('Are you sure to display? (y/n): ')

if access.lower() == 'y':
    for filename in filenames:
        with open(filename, 'r') as stream:
            text = stream.read()
            lines = text.split('\n')
            first_line = lines[0]
        print(filename, '|', first_line)
else:
    print("Access denied!")

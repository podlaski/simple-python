# Add in your console: python 030-sysargv-table.py example.txt example2.txt
# The system checks charackters, words and lines from the files specified via the console.

import sys

filenames = sys.argv[1:]

print('char word line filename')

for filename in filenames:
    with open(filename) as stream:
        content = stream.read()

        char = len(content)
        word = len(content.split())
        lines = len(content.split('\n'))
        
        print(f"{char:4} {word:4} {lines:4} {filename:20}")

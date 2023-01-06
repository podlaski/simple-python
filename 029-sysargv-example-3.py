# Add in your console: python 029-sysargv-example.py example.txt example2.txt
# The system checks charackters, words and lines from the files specified via the console.

import sys

filenames = sys.argv[1:]

for filename in filenames:
    with open(filename) as stream:
        content = stream.read()

        char = len(content)
        word = len(content.split())
        lines = len(content.split('\n'))
        
        print(f"Your file {filename} has {char} characters and {word} words and {lines} lines.\n")

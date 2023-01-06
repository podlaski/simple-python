# Add in your console: python 028-sysargv-example-2.py example.txt
# The system checks charackters, words and lines from the file specified via the console.
# This script is better option for big file than 027-sysargv-example.py

import sys

filename = sys.argv
char = 0
word = 0
lines = 0

with open(filename[1]) as stream:
    for line in stream:
        char += len(line)
        word += len(line.split())
        lines += 1

print(f"Your file has {char} characters and {word} words and {lines} lines.")

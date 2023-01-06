# Add in your console: python 027-sysargv-example.py example.txt
# The system checks charackters and words from the file specified via the console.

import sys

filename = sys.argv

with open(filename[1]) as stream:
    content = stream.read()

char = len(content)
word = len(content.split())

print(f"Your file has {char} characters and {word} words.")

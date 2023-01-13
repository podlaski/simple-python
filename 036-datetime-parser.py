# Convert your strong to data

from dateutil import parser

text = input('Add your date: ')
dt = parser.parse(text)
print(dt)

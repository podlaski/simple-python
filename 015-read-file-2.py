# Open and read file example.txt - version 2

path = r'example.txt'

with open(path) as stream:
  text = stream.read()

print(text)

# Write and read file example.txt

path = r'example.txt'
text = input('Add text: ')

with open(path, 'w') as stream:
  stream.write(text)

print(text)

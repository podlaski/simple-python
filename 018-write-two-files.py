# Write two files example.txt and example2.txt (with digit anonimization)

path = r'example.txt'
new_path = r'example2.txt'
text = input('Add text: ')

with open(path, 'w') as stream:
  stream.write(text)

for digit in '0123456789':
  text = text.replace(digit, '-')

with open(new_path, 'w') as stream:
  stream.write(text)

# digit anonymizer - if you use a digit we will change it to -

anonymous = ''

text = input('Add text: ')
for x in text:
  if x.isdigit():
    anonymous += '-'
  else:
    anonymous += x

print(f'Text with anonymized digits: {anonymous}')

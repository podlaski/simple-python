# digit anonymizer - if you use a digit we will change it to -

text = input('Add text: ')

for x in '0123456789':
  text = text.replace(x, '-')

print(f'Text with anonymized digits: {text}')

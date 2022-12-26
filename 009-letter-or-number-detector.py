# letter or number detector

text = input('Add letter or number: ')

if text.isalpha():
  print(f'{text} is the letter string')
elif text.isnumeric():
  print(f'{text} is the number')
elif text.isspace():
  print({f'{text} is a whitespace. Please use only letters or only digits.'})
else:
  print('Add correct value. You can use only letters or only digits.')

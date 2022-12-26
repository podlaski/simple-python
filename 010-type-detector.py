# type detector (letter, digit or whitespace)

text = input('Add any string of characters (letter, digit or whitespace): ')

for x in text:
  if x.isalpha():
    print(x, '- letter')
  elif x.isdigit():
    print(x, '- digit')
  elif x.isspace():
    print(x, '- whitespace')
  else:
    print(x, '- unknown')

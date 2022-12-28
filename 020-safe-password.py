# Safe password - add your password and the program will check if it is safe

password = input('Add your password: ')

lower = False
upper = False
space = False
special = False

length = len(password) >= 8

for char in password:
  if char.islower():
    lower = True
  elif char.isupper():
    upper = True
  elif char.isspace():
    space = True
  else:
    special = True

safe = lower and upper and not space and special and length

if safe:
  print('Your password is safe.')
else:
  print('Your password is not safe.')
  if not lower:
    print('- You must use a minimum of 1 lowercase letter.')
  if not upper:
    print('- You must use a minimum of 1 uppercase letter.')
  if not special:
    print('- You must use a minimum of 1 special character.')
  if not length:
    print('- You must use a minimum of 8 characters.')
  if space:
    print('- Do not use whitespace.')

# login generator

login = input("Add your name and surname: ")

# add 'user' at the beginning, use lowercase, delete spaces, replace s to $

new_login = ('user_' + login.lower().replace(' ', '_').replace('s','$'))

print(f'Your new login is: {new_login}')

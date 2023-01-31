from requests import get

r = get('https://wolnelektury.pl/api/genres')

print('Gatunki literackie:')

for genre in r.json():
    print(genre['name'], genre['href'])

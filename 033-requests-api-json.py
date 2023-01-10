import requests

URL = 'https://api.nbp.pl/api/exchangerates/tables/a/'
FILENAME = 'example.json'

rates = requests.get(URL)
rates = rates.text
print(rates)

with open(FILENAME, 'w') as save:
    save.write(rates)

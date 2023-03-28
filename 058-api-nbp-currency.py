from urllib.request import urlopen
from json import loads

# https://api.nbp.pl/en.html
# Add value and currency

with urlopen ('http://api.nbp.pl/api/exchangerates/tables/a/') as site:
    data = loads(site.read().decode('UTF-8'))
    rates = data[0]['rates']

    exchange = input("Jaka wartosc chcesz wymienic na zl? (Podaj wartość i walutę.)")
    value, code = exchange.split(" ")
    value = float(value)

    rate = list(filter(lambda x: x['code'] == code, rates))

    print(f'Otrzymujesz {value * rate[0]["mid"]} PLN')


import sys
import requests
from dateutil import parser

currency = input('Add currency (USD etc.): ')
dt = input("Add date: ")
dt = parser.parse(dt)
dt = dt.strftime('%Y-%m-%d')
print(f'Date: {dt}')
    
url =  f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{dt}/?format=json'

try:
    rate = requests.get(url)
    rate = rate.json()
    print(f'1 {currency} = ', rate['rates'][0]['mid'], 'PLN')

except:
    print('Wrong data.')

import requests

# check status code (add url)

url = input('ADD URL (use full address with https): ')
page = requests.head(url)
status = (f'{url} | {page.status_code}')

print(status)

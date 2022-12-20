import requests

# check status code

urls = [
    "https://arkadiuszpodlaski.pl",
    "http://arkadiuszpodlaski.pl",
    ]


for url in urls:
    page = requests.head(url)
    status = (f'{url} | {page.status_code}')
    print(status)

    

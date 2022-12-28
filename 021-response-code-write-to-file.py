import requests
import datetime

# check status code and write to file

today = datetime.datetime.now()
today = today.strftime("%d-%m-%Y, %H:%M")

url = ('https://arkadiuszpodlaski.pl')
page = requests.head(url)
status = (f'\n{url} | {page.status_code} | {today}')

print(status)

# write to file
path = 'example.txt'
stream = open(path, 'a')
stream.write(status)
stream.close()

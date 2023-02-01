# Start the browser and open the defined list of urls

import webbrowser

urls = [
    'https://www.bbc.co.uk/',
    'https://www.nytimes.com/',
    'https://www.onet.pl/',
    'https://www.wp.pl/',
    'https://www.interia.pl/'
]

for url in urls:
    webbrowser.open(url)

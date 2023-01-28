from lxml.html import fromstring
import requests

url = 'https://www.leroymerlin.pl/materialy-budowlane/materialy-budowlane-stan-surowy,a156.html'
page = requests.get(url)
html = page.text
path = '//*[@id="product-listing"]/div/a/h3'
content = fromstring(html)
products = content.xpath(path)

for product in products:
    print(product.text_content().strip())

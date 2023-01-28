from lxml.html import fromstring

html = '<html><body><p class="simple">This is <strong>green</strong> apple</p></body></html>'

x = fromstring(html)
path = x.xpath('//p[@class="simple"]/strong')
path = path[0]

print(path.text_content())

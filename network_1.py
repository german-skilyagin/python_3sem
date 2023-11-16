import requests
from lxml import etree

def get_wikipedia_links(url):
    response = requests.get(url)
    html = response.text

    tree = etree.HTML(html)
    links = tree.xpath('//a[contains(@href, "wikipedia.org")]/@href')

    return links

# Пример использования
url = 'https://ru.wikipedia.org/wiki/Python'
links = get_wikipedia_links(url)

for link in links:
    print(link)
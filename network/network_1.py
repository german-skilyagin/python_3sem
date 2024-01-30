import io
import requests
from lxml import etree

def get_links(link):
    data = requests.get(link).text
    parser = etree.HTMLParser()
    tree = etree.parse(io.StringIO(data), parser)
    for n in tree.xpath('//a'):
        print(n.get('href'))

def main():
    link = input("Enter the URL: ")
    get_links(link)

if __name__ == '__main__':
    main()
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://pythonscraping.com'
html = urlopen(url)
bsobj = BeautifulSoup(html, 'html.parser')

links = bsobj.find_all(src=True)
for link in links:
    print(link)


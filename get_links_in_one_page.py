from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

links = set()
def getLinks(tail):
    global links
    url = "https://www.marxists.org/chinese/maozedong/" + tail
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), 'html.parser')
    anchors = bs.find_all('a', href=re.compile('^(marxist)'))
    for link in anchors:
        if 'href' in link.attrs:
            if link['href'] not in links:
                links.add(link['href'])
    return links

for link in getLinks("index.htm#0"):
    print(link)